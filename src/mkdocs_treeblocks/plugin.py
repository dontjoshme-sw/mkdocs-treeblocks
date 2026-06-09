"""MkDocs plugin integration for mkdocs-treeblocks."""

from __future__ import annotations

from mkdocs.plugins import BasePlugin

from mkdocs_treeblocks.transform import transform_markdown


class TreeblocksPlugin(BasePlugin):
    """MkDocs plugin that transforms fenced tree blocks before Markdown rendering."""

    def on_page_markdown(self, markdown: str, **kwargs: object) -> str:
        """Transform tree blocks in a page's Markdown source."""
        return transform_markdown(markdown)