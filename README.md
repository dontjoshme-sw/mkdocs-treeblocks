# mkdocs-treeblocks
_Revised on: 06-09-2026 by: Joshua Mullenberg_

`mkdocs-treeblocks` is an MkDocs plugin for rendering readable tree-style blocks in documentation and is currently still in development.

The goal is to make directory structures, file trees, project layouts, and related hierarchy examples easier to write, read, and maintain inside MkDocs documentation.

## Initial purpose

This project started from a documentation need of rendering clean text-based hierarchy trees from a simple markdown style syntax.  The idea is to avoid having to switch apps to copy paste from a web tool, manually insert unicode characters, or fight with the filtering options on a `tree` command to render the directory structure needed for the documentation.  

The initial goal is to support a small, predictable syntax that can render a tree structure consistently in MkDocs sites.

## Syntax

Tree blocks are written as a fenced Markdown code block using the three backticks (` ``` `) to open and close the block and the `tree` keyword in place of the syntax language identifier. The plugin transforms the fenced block into a fenced `text` block containing the rendered tree. Indents can be either 4 spaces or a `tab`, but must be used consistently throughout the tree.  Finally, tabs and spaces are preserved after the initial indentation which allows for properly aligned comments.

<table>
    <tr>
        <th>syntax example</th>
        <th>rendered output</th>
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

> [!NOTE]
> This project is currently in development. Syntax and public APIs are still subject to change.

---
# Basic MkDocs Usage

Enable the plugin in `mkdocs.yml`:

```yaml
plugins:
    - treeblocks
```

Write a tree block in a Markdown page:

````
```tree
docs\
    index.md
    guides\
        install.md
```
````

---
## Current implementation status

Implemented:

- Parse indented text into a tree structure with `parse_tree()`.
- Render a parsed tree as plain text with `render_tree()`.
- Use Unicode tree connectors such as `├──`, `└──`, and `│`.
- Add display-only trailing slashes to nodes with children.
- Preserve original node text in the parser.
- Allow inferred directory slashes to be disabled with `directory_slashes=False`.
- Test parser and renderer, and Markdown transformer behavior with `pytest`.
- Test Mkdocs plugin behavior with `pytest`.
- Transform fenced Markdown `tree` blocks into rendered fenced `text` blocks with `transform_markdown()`.
- Leave non-`tree` fenced code blocks unchanged.
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


