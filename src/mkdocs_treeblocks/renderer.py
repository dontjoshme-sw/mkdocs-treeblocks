from mkdocs_treeblocks.parser import TreeNode


def render_tree(root: TreeNode, *, directory_slashes: bool = False) -> str:
    """Render a parsed tree as plain text using Unicode tree connectors."""
    lines = [_display_text(root, directory_slashes=directory_slashes)]

    for index, child in enumerate(root.children):
        is_last = index == len(root.children) - 1
        _render_child(
            child,
            lines,
            prefix="",
            is_last=is_last,
            directory_slashes=directory_slashes,
        )

    return "\n".join(lines)


def _render_child(
    node: TreeNode,
    lines: list[str],
    *,
    prefix: str,
    is_last: bool,
    directory_slashes: bool,
) -> None:
    connector = "└── " if is_last else "├── "
    lines.append(f"{prefix}{connector}{_display_text(node, directory_slashes=directory_slashes)}")

    child_prefix = f"{prefix}{'    ' if is_last else '│   '}"

    for index, child in enumerate(node.children):
        child_is_last = index == len(node.children) - 1
        _render_child(
            child,
            lines,
            prefix=child_prefix,
            is_last=child_is_last,
            directory_slashes=directory_slashes,
        )


def _display_text(node: TreeNode, *, directory_slashes: bool) -> str:
    if directory_slashes and node.children and not node.text.endswith("/"):
        return f"{node.text}/"

    return node.text