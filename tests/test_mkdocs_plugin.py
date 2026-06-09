from __future__ import annotations

from pathlib import Path

import pytest
from mkdocs.commands.build import build
from mkdocs.config import load_config
from mkdocs.exceptions import PluginError


def test_mkdocs_plugin_transforms_tree_blocks(tmp_path: Path) -> None:
    fixture_dir = Path(__file__).parent / "fixtures" / "mkdocs_basic"
    site_dir = tmp_path / "site"

    config = load_config(
        str(fixture_dir / "mkdocs.yml"),
        site_dir=str(site_dir),
        strict=True,
    )

    build(config)

    html = (site_dir / "index.html").read_text()

    assert "Before the tree block." in html
    assert "docs/" in html
    assert "├── index.md" in html
    assert "└── guides/" in html
    assert "└── install.md" in html
    assert "After the tree block." in html


def test_mkdocs_plugin_wraps_tree_parse_errors() -> None:
    from mkdocs_treeblocks.plugin import TreeblocksPlugin

    plugin = TreeblocksPlugin()

    markdown = """```tree
docs
   bad-indent.md
```
"""

    with pytest.raises(PluginError, match="treeblocks failed to parse a tree block"):
        plugin.on_page_markdown(markdown)
