from mkdocs_treeblocks.parser import TreeNode


def render_tree(root: TreeNode) -> str:
    """Render a parsed tree as plain text using Unicode tree connectors."""
    lines = [root.text]

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
) -> None:
    connector = "└── " if is_last else "├── "
    lines.append(f"{prefix}{connector}{node.text}")

    child_prefix = f"{prefix}{'    ' if is_last else '│   '}"

    for index, child in enumerate(node.children):
        _render_child(
            child,
            lines,
            prefix=child_prefix,
            is_last=index == len(node.children) - 1,
        )