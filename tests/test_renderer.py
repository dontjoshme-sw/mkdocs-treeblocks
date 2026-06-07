from mkdocs_treeblocks.parser import parse_tree
from mkdocs_treeblocks.renderer import render_tree


def test_renders_single_root_node():
    root = parse_tree("docs")

    assert render_tree(root) == "docs"

def test_renders_root_with_one_child():
    root = parse_tree(
        """\
docs
    index.md
"""
    )

    assert render_tree(root) == """\
docs/
└── index.md"""

def test_renders_root_with_multiple_children():
    root = parse_tree(
        """\
docs
    index.md
    about.md
"""
    )

    assert render_tree(root) == """\
docs/
├── index.md
└── about.md"""

def test_renders_nested_children_with_guide_lines():
    root = parse_tree(
        """\
docs
    index.md
    guides
        install.md
        config.md
    reference
        api.md
"""
    )

    assert render_tree(root) == """\
docs/
├── index.md
├── guides/
│   ├── install.md
│   └── config.md
└── reference/
    └── api.md"""

def test_adds_trailing_slash_to_nodes_with_children():
    root = parse_tree(
        """\
docs
    guides
        install.md
"""
    )

    assert render_tree(root) == """\
docs/
└── guides/
    └── install.md"""

def test_does_not_double_existing_trailing_slash():
    root = parse_tree(
        """\
docs/
    guides/
        install.md
"""
    )

    assert render_tree(root) == """\
docs/
└── guides/
    └── install.md"""

def test_can_disable_directory_slashes():
    root = parse_tree(
        """\
docs
    guides
        install.md
"""
    )

    assert render_tree(root, directory_slashes=False) == """\
docs
└── guides
    └── install.md"""