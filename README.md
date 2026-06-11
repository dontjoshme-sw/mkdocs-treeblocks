# mkdocs-treeblocks
_Revised on: 06-11-2026 by: Joshua Mullenberg_

`mkdocs-treeblocks` is a MkDocs plugin for rendering readable tree-style blocks in documentation.

The goal is to make directory structures, file trees, project layouts, and related hierarchy examples easier to write, read, and maintain in MkDocs documentation.

> [!NOTE]
> This project is currently in development. Syntax and public APIs are still subject to change.

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
- Integrate with MkDocs through the treeblocks plugin.
- Raise MkDocs PluginError for invalid tree blocks.
- Test parser and renderer, and Markdown transformer behavior with `pytest`.
- Test Mkdocs plugin behavior with `pytest`.

- MkDocs plugin integration.

Not implemented yet:

- Custom HTML rendering.
- CSS styling.
- Configuration through `mkdocs.yml`.
- Filesystem inspection.

Fix needed:
- When `directory_slashes = true` and there is a comment, the inferred directory slash is incorrectly placed after the comment.

---
## Project Roadmap

#### <s>Phase 1: Scaffold and concept</s>
- <s>Create the project</s>
- <s>Setup GitHub repository</s>
- <s>Document the purpose and syntax</s>
- <s>Add placeholder tests</s>
- <s>Initial README
- <s>Make the first commit</s>
 
#### <s>Phase 2: Minimal Rendering Experiment</s>
- <s>Choose the first supported syntax</s>
- <s>Parse a small tree block</s>
- <s>Add parser tests</s>
- <s>Incremental documentation in /docs/</s>

#### <s>Phase 3: Minimal Renderer Behavior</s>
- <s>Define renderer MVP behavior</s>
- <s>Add renderer tests</s>
- <s>Implement a plain Python renderer</s>
- <s>Document renderer behavior in README.md and docs/</s>
 
#### Phase 4: Markdown Transform MVP
- <s>Choose fenced `tree` blocks as the first supported Markdown source syntax</s>
- <s>Detect and transform tree blocks in Markdown</s>
- <s>Replace transformed tree blocks with fenced `text` blocks</s>
- <s>Keep the transformer independent from MkDocs integration</s>

#### Phase 5: MkDocs Integration
- <s>Decide whether this should be a Markdown extension, MkDocs plugin, or MkDocs hook.</s>
- <s>Add a minimal MkDocs plugin</s>
- <s>Add a minimal MkDocs fixture.</s>
- <s>Add MkDocs integration tests.</s>
- <s>Add page-aware build errors for invalid tree blocks.</s>
- <s>Wrap invalid tree blocks as MkDocs `PluginError`</s>
- Add richer page/file/line-aware error messages.
- Test with Material for MkDocs.

#### Phase 6: Documentation and Polish
- Add usage documentation
- Add installation instructions
- Add examples
- Document limitations and troubleshooting notes


