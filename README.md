# mkdocs-treeblocks
_Revised on: 06-11-2026 by: Joshua Mullenberg_

`mkdocs-treeblocks` is a MkDocs plugin for rendering readable tree-style blocks in documentation.

The goal is to make directory structures, file trees, project layouts, and related hierarchy examples easier to write, read, and maintain in MkDocs documentation.

> [!NOTE]
> This project is currently in development. Syntax, behavior, and package interfaces are still subject to change.

## Initial purpose

This project grew from a need to create clean, text-based tree-style blocks directly in documentation using simple Markdown syntax.

The goal is to avoid switching to a separate app, copying output from a web tool, manually inserting Unicode tree characters, or wrestling with tree command filters just to produce a curated directory structure for documentation.

mkdocs-treeblocks provides a small, predictable syntax that renders tree structures consistently in MkDocs sites.

## Syntax

Tree blocks are written as fenced Markdown code blocks. Use three backticks to open and close the block, with tree as the language identifier.

The plugin transforms each fenced tree block into a fenced text block containing the rendered tree.

Indentation may use either four spaces or one tab per level, but each tree block must use one style consistently. Text and spacing after the structural indentation are preserved, allowing filenames, comments, and annotations to remain aligned.

<table>
    <tr>
        <th>Syntax by example</th>
        <th>Rendered output</th>
    </tr>
    <tr>
        <td>
            <pre><code>
```tree
mkdocs-project/
    docs/
        index.md
        ...
    mkdocs.yml        # mkdocs config
    README.md
    requirements.txt  # dependencies
    site/
        404.html
        assets/
        index.html
        ...
```
            </code></pre>
        </td>
        <td>
            <pre><code>
```text
mkdocs-project/
├── docs/
│   ├── index.md
│   └── ...
├── mkdocs.yml        # mkdocs config
├── README.md
├── requirements.txt  # dependencies
└── site/
    ├── 404.html
    ├── assets/
    ├── index.html
    └── ...
```
            </code></pre>
        </td>
    </tr>
</table>

---

## Installation, testing, and usage

Clone the repository, create and activate a virtual environment, then install the project in editable mode with its development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The editable install registers the treeblocks plugin with MkDocs and allows local source changes to take effect without reinstalling the package.

Run the test suite:

```bash
python -m pytest
```

Enable the plugin in mkdocs.yml:

```yaml
plugins:
  - treeblocks
```

Then write a fenced tree block in a Markdown page:

````
```tree
docs/
    index.md
    guides/
        install.md
```
````

During the MkDocs build, the plugin transforms the source into a fenced text block containing the rendered tree.

---
## Current implementation status

Implemented:

- Parse indented text into a tree structure with `parse_tree()`.
- Render a parsed tree as plain text with `render_tree()`.
- Use Unicode tree connectors such as `├──`, `└──`, and `│`.
- Preserve original node text, including aligned comments and annotations.
- Transform fenced Markdown `tree` blocks into rendered fenced `text` blocks with `transform_markdown()`.
- Leave non-`tree` fenced code blocks unchanged.
- Integrate with MkDocs through the `treeblocks` plugin.
- Raise MkDocs `PluginError` for invalid tree blocks.
- Test parser, renderer, Markdown transformer, and MkDocs plugin behavior with `pytest`.

Not implemented yet:

- Richer page, file, and line-aware error messages.

Potential future enhancements:

- Custom HTML rendering.
- Dedicated CSS styling.
- Optional automatic directory slash handling.

---
## Project Roadmap

#### <s>Phase 1: Scaffold and concept</s>
- <s>Create the project</s>
- <s>Set up the GitHub repository</s>
- <s>Document the purpose and syntax</s>
- <s>Add placeholder tests</s>
- <s>Create the initial README</s/
- <s>Make the first commit</s>
 
#### <s>Phase 2: Parser MVP</s>
- <s>Choose the first supported syntax</s>
- <s>Parse a small indented tree</s>
- <s>Add parser tests</s>
- <s>Add incremental documentation in /docs/</s>

#### <s>Phase 3: Renderer MVP</s>
- <s>Define renderer MVP behavior</s>
- <s>Add renderer tests</s>
- <s>Implement a plain Python renderer</s>
- <s>Document renderer behavior</s>
 
#### <s>Phase 4: Markdown transform MVP</s>
- <s>Choose fenced `tree` blocks as the first supported Markdown source syntax</s>
- <s>Detect and transform tree blocks in Markdown</s>
- <s>Replace transformed tree blocks with fenced `text` blocks</s>
- <s>Keep the transformer independent from MkDocs integration</s>

#### Phase 5: MkDocs plugin MVP
- <s>Add a minimal MkDocs plugin</s>
- <s>Register the plugin with MkDocs</s>
- <s>Add a minimal MkDocs fixture.</s>
- <s>Add MkDocs integration tests.</s>
- <s>Wrap parser failures as MkDocs `PluginError`</s>

#### Phase 6: Error handling & testing
- Add richer page/file/line-aware error messages.
- Test with Material for MkDocs.

#### Phase 7: Documentation Polish
- Update current documentation.
- Verify documentation includes installation, usage, and examples.
- Document limitations and troubleshooting notes.
- Set up GitHub issue and feature-request tracking.

#### Phase 8: Publish initial release
- Finalize package metadata in `pyproject.toml`.
- Install build tooling and create distribution packages.
- Test the built wheel in a clean virtual environment
- Publish the release to PyPI


