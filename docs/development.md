# Development notes
_Revised on: 06-09-2026 by: Joshua Mullenberg_

This page documents the current development workflow for `mkdocs-treeblocks`.

## Repository

GitHub repository:

```text
dontjoshme-sw/mkdocs-treeblocks
```

Python distribution name:

```text
mkdocs-treeblocks
```

Python import package name:

```text
mkdocs_treeblocks
```

The project uses a `src/` layout:

```text
src/mkdocs_treeblocks/
tests/
pyproject.toml
README.md
docs/
```

## Local development

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode with development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest
```

## Branch workflow

Keep `main` clean.

Use feature branches for task groups:

```bash
git switch -c feature/task-name
```

Run tests before committing:

```bash
python -m pytest
```

Check status before and after commits:

```bash
git status
```

## Current architecture

The project should keep the core logic independent from MkDocs.

Planned layers:

Current layers:

```text
Parser:
  Turns indented source text into a tree structure.

Renderer:
  Turns the tree structure into formatted tree output.

Markdown transformer:
  Finds fenced Markdown `tree` blocks and replaces them with rendered `text` blocks.

MkDocs integration:
  Planned later. Connects the plain Python transformer to MkDocs builds.
```

The current implementation includes the parser MVP, a plain-text renderer MVP, and a plain Python Markdown transformer MVP.

## Parser MVP

The parser lives in:

```text
src/mkdocs_treeblocks/parser.py
```

It currently provides:

```python
parse_tree(text: str)
TreeNode
TreeParseError
```

The parser supports:

- one root node
- four-space indentation
- tab indentation
- blank-line skipping
- preserving node text after leading indentation is removed

The parser rejects:

- empty tree blocks
- first node indented
- multiple root nodes
- skipped indentation levels
- mixed tabs and spaces
- partial-space indentation that is not a multiple of four

---
## Renderer MVP

The renderer lives in:

```text
src/mkdocs_treeblocks/renderer.py
```

It currently provides:

```python
render_tree(root: TreeNode, *, directory_slashes: bool = True) -> str
```

The renderer supports:

- plain-text tree output
- Unicode tree connectors
- nested guide lines
- display-only trailing slashes for nodes with children
- avoiding doubled slashes when a node already ends with `/`
- disabling inferred directory slashes with `directory_slashes=False`

Directory slash behavior belongs to rendering, not parsing. The parser preserves the original node text, and the renderer decides how to display parent nodes.

The renderer does not inspect the real filesystem. A node is displayed as a directory only when it has child nodes.

---
---

## Markdown transformer MVP

The Markdown transformer lives in: `src/mkdocs_treeblocks/transform.py`.

It currently provides:

```python
    transform_markdown(markdown: str) -> str
```

The transformer supports:

- finding fenced Markdown code blocks marked as tree
- parsing the inner tree source with parse_tree()
- rendering the parsed tree with render_tree()
- replacing the source block with a fenced text code block
- preserving Markdown outside transformed tree blocks
- leaving non-tree fenced code blocks unchanged

Invalid tree indentation raises TreeParseError from the parser. MkDocs-specific error wrapping with page and line context is planned for a later integration step

///


---
## Documentation approach

For now, project documentation should use GitHub-rendered Markdown files instead of a MkDocs site.

This keeps the project simple while the syntax and implementation are still changing.

Initial documentation structure:

```text
README.md
docs/syntax.md
docs/development.md
```

A MkDocs documentation site can be reconsidered later if the project grows enough to need navigation, search, richer examples, or published docs.
