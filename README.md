# mkdocs-treeblocks
_Revised on: 06-09-2026 by: Joshua Mullenberg_

`mkdocs-treeblocks` is an MkDocs extension for rendering readable tree-style blocks in documentation.

The goal is to make directory structures, file trees, project layouts, and related hierarchy examples easier to write, read, and maintain inside MkDocs documentation.

## Initial purpose

This project started from a documentation need of rendering clean text-based hierarchy trees from a simple markdown style syntax.  The idea is to avoid having to switch apps to copy paste from a web tool, manually insert unicode characters, or fight with the filtering options on a `tree` command to render the directory structure needed for the documentation.  

The initial goal is to support a small, predictable syntax that can render a tree structure consistently in MkDocs sites.

## Syntax

Each tree block will be rendered in a code block to preserve even spacing and alignment. The opening and closing of a tree block will be similar to a code block using three back-ticks followed by the `tree` keyword as the syntax.  When reformatted it will be inserted into a standard code block with the `text` syntax.  Indents can be either 4 spaces or a `tab`, but must be used consistently throughout the tree.  Appending the `tree` keyword with a `/`  as in `tree/` will direct the formatter to handle the tree as a directory, adding a `/` after directories in the tree will then be optional as the formatter will automatically add the trailing `/` if the next line is a child object.  Finally, tabs and spaces are preserved after the initial indentation which allows for properly aligned comments.

The current transformer MVP recognizes fenced blocks marked as `tree` and replaces them with fenced `text` blocks. A separate `tree/` fence mode is not implemented yet; directory slashes are currently inferred by the renderer when a node has children.

<table>
    <tr>
        <th>pre-formatted syntax</th>
        <th>after formatting</th>
    </tr>
    <tr>
        <td>
            <pre><code>
```tree/
mkdocs-project
    docs
        index.md
        ...
    mkdocs.yml        # mkdocs config
    README.md
    requirements.txt  # dependencies  
    site
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
> This project is currently experimental. The parser, plain-text renderer, and plain Python Markdown transformer MVP are implemented and tested, but MkDocs integration has not been added yet. Syntax and public APIs are still subject to change.

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
- Transform fenced Markdown `tree` blocks into rendered fenced `text` blocks with `transform_markdown()`.
- Leave non-`tree` fenced code blocks unchanged.
 
Not implemented yet:

- MkDocs hook, plugin, or Markdown extension integration.
- HTML rendering.
- CSS styling.
- Configuration through `mkdocs.yml`.
- Filesystem inspection.

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
- Decide whether this should be a Markdown extension, MkDocs plugin, or MkDocs hook.
- Add a minimal MkDocs demo page.
- Test with Material for MkDocs.
- Add page-aware build errors for invalid tree blocks.

#### Phase 6: Documentation and Polish
- Add usage documentation
- Add installation instructions
- Add examples
- Document limitations and troubleshooting notes


