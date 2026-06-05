from __future__ import annotations

from dataclasses import dataclass, field


class TreeParseError(ValueError):
    """Raised when tree block text cannot be parsed."""


@dataclass
class TreeNode:
    text: str
    children: list["TreeNode"] = field(default_factory=list)


def parse_tree(text: str) -> TreeNode:
    """Parse indented tree block text into a TreeNode hierarchy."""
    parsed_lines = _parse_lines(text)

    if not parsed_lines:
        raise TreeParseError("Tree block is empty.")

    root_depth, root_text = parsed_lines[0]

    if root_depth != 0:
        raise TreeParseError("The first tree node must not be indented.")

    root = TreeNode(root_text)
    stack: list[tuple[int, TreeNode]] = [(root_depth, root)]

    for depth, node_text in parsed_lines[1:]:
        if depth > stack[-1][0] + 1:
            raise TreeParseError("Tree indentation cannot skip levels.")

        while stack and stack[-1][0] >= depth:
            stack.pop()

        if not stack:
            raise TreeParseError("Tree contains more than one root node.")

        node = TreeNode(node_text)
        stack[-1][1].children.append(node)
        stack.append((depth, node))

    return root


def _parse_lines(text: str) -> list[tuple[int, str]]:
    indent_style: str | None = None
    parsed_lines: list[tuple[int, str]] = []

    for line in text.splitlines():
        if not line.strip():
            continue

        indent, node_text = _split_indent(line)

        if indent:
            line_indent_style = _detect_indent_style(indent)

            if indent_style is None:
                indent_style = line_indent_style
            elif indent_style != line_indent_style:
                raise TreeParseError("Tree block cannot mix tabs and spaces for indentation.")

            depth = _indent_depth(indent, line_indent_style)
        else:
            depth = 0

        parsed_lines.append((depth, node_text))

    return parsed_lines


def _split_indent(line: str) -> tuple[str, str]:
    stripped = line.lstrip(" \t")
    indent_length = len(line) - len(stripped)
    return line[:indent_length], stripped


def _detect_indent_style(indent: str) -> str:
    has_spaces = " " in indent
    has_tabs = "\t" in indent

    if has_spaces and has_tabs:
        raise TreeParseError("Tree block cannot mix tabs and spaces for indentation.")

    if has_tabs:
        return "tabs"

    return "spaces"


def _indent_depth(indent: str, indent_style: str) -> int:
    if indent_style == "tabs":
        return len(indent)

    if len(indent) % 4 != 0:
        raise TreeParseError("Space indentation must use multiples of four spaces.")

    return len(indent) // 4
