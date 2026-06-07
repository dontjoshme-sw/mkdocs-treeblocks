# Development notes

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
git switch -c parser-mvp
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

```text
Parser:
  Turns indented source text into a tree structure.

Renderer:
  Turns the tree structure into formatted tree output.

MkDocs integration:
  Finds tree blocks during a MkDocs build and replaces them.
```

The current implementation includes the parser MVP only.

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
