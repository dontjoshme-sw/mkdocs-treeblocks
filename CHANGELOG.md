# mkdocs-treeblocks 0.1.0

## Initial alpha release of mkdocs-treeblocks.

mkdocs-treeblocks is a MkDocs extension for rendering simple tree-style code blocks as directory/file tree output during a MkDocs build.

Added

* Added support for fenced ` ```tree` code blocks in Markdown.
* Added parser support for indentation-based tree input.
* Added Unicode tree rendering using branch characters such as ├── and └──.
* Added Markdown transformation that converts source tree fences into rendered text fences.
* Added MkDocs plugin integration through the treeblocks plugin entry point.
* Added build-time diagnostics for invalid tree indentation.
* Added diagnostics that report the source Markdown file and starting line of the failing tree block.
* Added compatibility test coverage for both basic MkDocs and Material for MkDocs projects.
* Added package metadata for local wheel and source distribution builds.
---

### Example Usage

_Source Markdown:_

```tree
docs
    index.md
    guides
        install.md
```

_Rendered output:_

```text
docs
├── index.md
└── guides
    └── install.md
```
---

## Installation

`pip install mkdocs-treeblocks`

Enable the plugin in mkdocs.yml:

```yaml
plugins:
  - search
  - treeblocks
```
---

### Current limitations

* Tree blocks currently use four-space or single tab indentation levels.
* Error diagnostics report the source file and tree-block starting line, but not yet the exact malformed line inside the tree block.
* This is an early alpha release, so syntax and behavior may still change before a stable 1.0.0 release.