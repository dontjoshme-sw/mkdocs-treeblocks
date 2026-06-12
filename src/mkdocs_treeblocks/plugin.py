"""MkDocs plugin integration for mkdocs-treeblocks."""

from __future__ import annotations

from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin

from mkdocs_treeblocks.parser import TreeParseError
from mkdocs_treeblocks.transform import transform_markdown


class TreeblocksPlugin(BasePlugin):
    """MkDocs plugin that transforms fenced tree blocks before Markdown rendering."""

    def on_page_markdown(self, markdown: str, **kwargs: object) -> str:
        """Transform tree blocks in a page's Markdown source."""
        try:
            return transform_markdown(markdown)
        except TreeParseError as error:
            raise PluginError(
                f"treeblocks failed to parse a tree block: {error}"
            ) from error
            