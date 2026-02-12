# Conformance Case Authoring Style

Conformance case docs are authored as Markdown `*.spec.md` files with fenced
`yaml spec-test` blocks.

Style rules:

- one case per fenced `spec-test` block
- each block must be immediately preceded by `## <case-id>`
- case ids must be sorted ascending within each file
- each fenced block should stay small (50 lines max) for readability
- each case must include a non-empty `why` field describing the intent

Rationale:

- keeps fixtures readable in code review
- keeps diffs small and localized
- keeps case discovery deterministic and predictable
