# Tree block syntax

This page describes the planned author-facing syntax for `mkdocs-treeblocks`.

The current implementation includes only the parser MVP. Rendering and MkDocs integration are planned but not implemented yet.

## Basic idea

Authors write a simple indented tree:

```text
docs
. . . . index.md
. . . . guides
. . . . . . . . install.md
```

The parser reads the indentation and turns the text into a tree structure:

```text
docs
├── index.md
└── guides
    └── install.md
```

The rendered output layer is planned for a later task group.

## Indentation

The parser currently supports two indentation styles:

- four spaces per level
- one tab per level

Both of these are valid:

```text
docs
....index.md
....guides
........install.md
```

```text
docs
—>guides
—>—>install.md
```

## Do not mix tabs and spaces

A single tree block must use one indentation style consistently.

This is invalid:

```text
docs
....guides
—>—>install.md
```

Mixed indentation is rejected because it can look different in different editors and makes the tree structure ambiguous.

## Four spaces means one level

When using spaces, each indentation level must be exactly four spaces.

This is valid:

```text
docs
....guides
........install.md
```

This is invalid:

```text
docs
..guides
```

Two spaces is not a full indentation level.

## Blank lines

Blank lines are ignored.

These two examples are treated the same:

```text
docs

    index.md

    guides
        install.md
```

```text
docs
    index.md
    guides
        install.md
```

## Node text is preserved

After the leading tree indentation is removed, the rest of the line is preserved.

This allows aligned comments or annotations:

```text
docs
    index.md      # homepage
    guides        # user docs
```

The parser preserves the spacing in:

```text
index.md      # homepage
guides        # user docs
```

## One root node

A tree block should have one unindented root node.

Valid:

```text
project
    docs
    README.md
```

Invalid:

```text
project
other-project
```

Multiple root nodes are rejected by the current parser.

## Directory slashes

Directory slash behavior belongs to rendering, not parsing.

The parser does not change node names. It only identifies structure.

For example:

```text
docs
    guides
        install.md
```

The parser stores the names as written:

```text
docs
guides
install.md
```

A later renderer may choose to display parent nodes with trailing slashes:

```text
docs/
└── guides/
    └── install.md
```

That behavior is planned, but not implemented in the parser itself.

## Planned MkDocs syntax

The original project idea is to support a custom tree block in Markdown.

A possible future syntax is:

```markdown
/// tree
docs
    index.md
    guides
        install.md
///
```

A possible directory-aware version is:

```markdown
/// tree/
mkdocs-project
    docs
        index.md
    mkdocs.yml
    README.md
///
```

This syntax is not implemented yet.
