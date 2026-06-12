"""Markdown transformation helpers for mkdocs-treeblocks."""

from __future__ import annotations

import re

from mkdocs_treeblocks.parser import TreeParseError, parse_tree
from mkdocs_treeblocks.renderer import render_tree


_TREE_FENCE_RE = re.compile(
    r"(?P<opening>^```tree[ \t]*\n)"
    r"(?P<body>.*?)"
    r"(?P<closing>^```[ \t]*$)",
    re.MULTILINE | re.DOTALL,
)


def transform_markdown(markdown: str) -> str:
    """Transform fenced tree blocks into rendered fenced text blocks.

    The source block:

        ```tree
        docs
            index.md
        ```

    becomes:

        ```text
        docs/
        └── index.md
        ```

    Non-tree fenced code blocks are left unchanged.
    """

    def replace_tree_block(match: re.Match[str]) -> str:
        tree_source = match.group("body")
        block_line = markdown.count("\n", 0, match.start()) + 1

        try:
            root_nodes = parse_tree(tree_source)
        except TreeParseError as error:
            raise TreeParseError(
                f"tree block starting at line {block_line}: {error}"
            ) from error

        rendered_tree = render_tree(root_nodes)

        return f"```text\n{rendered_tree}\n```"

    return _TREE_FENCE_RE.sub(replace_tree_block, markdown)