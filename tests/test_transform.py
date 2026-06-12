import pytest

from mkdocs_treeblocks.parser import TreeParseError
from mkdocs_treeblocks.transform import transform_markdown


def test_transform_single_tree_block():
    markdown = """Before.

```tree
docs/
    index.md
    guides/
        install.md
```

After.
"""

    expected = """Before.

```text
docs/
├── index.md
└── guides/
    └── install.md
```

After.
"""

    assert transform_markdown(markdown) == expected


def test_transform_multiple_tree_blocks():
    markdown = """First:

```tree
docs/
    index.md
```

Second:

```tree
src/
    mkdocs_treeblocks/
        parser.py
```
"""

    expected = """First:

```text
docs/
└── index.md
```

Second:

```text
src/
└── mkdocs_treeblocks/
    └── parser.py
```
"""

    assert transform_markdown(markdown) == expected


def test_transform_markdown_without_tree_blocks_is_unchanged():
    markdown = """# Heading

This is ordinary Markdown.

```python
print("hello")
```
"""

    assert transform_markdown(markdown) == markdown


def test_transform_preserves_non_tree_fenced_blocks():
    markdown = """```text
already rendered
```

```python
print("hello")
```
"""

    assert transform_markdown(markdown) == markdown


def test_transform_invalid_tree_block_raises_tree_parse_error():
    markdown = """```tree
docs
  bad-indent.md
```
"""

    with pytest.raises(TreeParseError):
        transform_markdown(markdown)