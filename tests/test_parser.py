import pytest

from mkdocs_treeblocks.parser import TreeParseError, parse_tree


def test_parse_four_space_indented_tree():
    tree = parse_tree(
        """\
docs
    index.md
    guides
        install.md
"""
    )

    assert tree.text == "docs"
    assert [child.text for child in tree.children] == ["index.md", "guides"]
    assert tree.children[1].children[0].text == "install.md"


def test_parse_tab_indented_tree():
    tree = parse_tree(
        """\
docs
\tguides
\t\tinstall.md
"""
    )

    assert tree.text == "docs"
    assert tree.children[0].text == "guides"
    assert tree.children[0].children[0].text == "install.md"


def test_blank_lines_are_ignored():
    tree = parse_tree(
        """\
docs

    index.md

    guides
        install.md
"""
    )

    assert [child.text for child in tree.children] == ["index.md", "guides"]
    assert tree.children[1].children[0].text == "install.md"


def test_mixed_tabs_and_spaces_raise_error():
    with pytest.raises(TreeParseError):
        parse_tree(
            """\
docs
    guides
\t\tinstall.md
"""
        )


def test_invalid_space_indentation_raises_error():
    with pytest.raises(TreeParseError):
        parse_tree(
            """\
docs
  guides
"""
        )


def test_node_text_after_indentation_is_preserved():
    tree = parse_tree(
        """\
docs
    index.md      # homepage
    guides        # user docs
"""
    )

    assert tree.children[0].text == "index.md      # homepage"
    assert tree.children[1].text == "guides        # user docs"
