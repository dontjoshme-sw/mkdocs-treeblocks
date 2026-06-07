# mkdocs-treeblocks

`mkdocs-treeblocks` is an MkDocs extension for rendering readable tree-style blocks in documentation.

The goal is to make directory structures, file trees, project layouts, and related hierarchy examples easier to write, read, and maintain inside MkDocs documentation.

## Initial purpose

This project started from a documentation need of rendering clean text-based hierarchy trees from a simple markdown style syntax.  The idea is to avoid having to switch apps to copy paste from a web tool, manually insert unicode characters, or fight with the filtering options on a `tree` command to render the directory structure needed for the documentation.  

The initial goal is to support a small, predictable syntax that can render a tree structure consistently in MkDocs sites.

## Syntax

Each tree block will be rendered in a code block to preserve even spacing and alignment. The opening and closing of a tree block will be similar to a code block using three back-ticks followed by the `tree` keyword as the syntax.  When reformatted it will be inserted into a standard code block with the `text` syntax.  Indents can be either 4 spaces or a `tab`, but must be used consistently throughout the tree.  Appending the `tree` keyword with a `/`  as in `tree/` will direct the formatter to handle the tree as a directory, adding a `/` after directories in the tree will then be optional as the formatter will automatically add the trailing `/` if the next line is a child object.  Finally, tabs and spaces are preserved after the initial indentation which allows for properly aligned comments.

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

> [!Note]
> This project is currently experimental and in the planning / scaffolding stage.  Syntax is subject to change.

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

#### Phase 3: Minimal Renderer Behavior
- Define renderer MVP behavior
- Add basic tests
- Implement a plain Python renderer.
- Incremental documentation update in /docs/
 
#### Phase 4: MkDocs Integration
- Decide whether this should be a Markdown extension, MkDocs plugin or a MkDocs hook.
- Add a minimal MkDocs demo page
- Test with Material for MkDocs

#### Phase 5: Documentation and Polish
- Add usage documentation
- Add installation instructions
- Add examples
- Document limitations and troubleshooting notes


