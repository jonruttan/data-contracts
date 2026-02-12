# Conformance Case Authoring Style

Conformance case docs are authored as Markdown `*.spec.md` files with fenced
`yaml spec-test` blocks.

Style rules:

- one case per fenced `spec-test` block
- each block must be immediately preceded by `## <case-id>`
- case ids must be sorted ascending within each file
- each fenced block should stay small (50 lines max) for readability
- each case must include a non-empty `purpose` field describing the intent
- `purpose` should add context beyond `title` (not a copy)
- `purpose` should be at least 8 words and avoid placeholders (`todo`, `tbd`, `fixme`, `xxx`)

Purpose lint policy:

- defaults and runtime profiles are configured in `docs/spec/conformance/purpose-lint-v1.yaml`
- per-case override is optional via `purpose_lint` mapping:
  - `runtime`: runtime profile name from policy (for example `php`)
  - `min_words`: integer override
  - `placeholders`: list override
  - `forbid_title_copy`: boolean override
  - `enabled`: boolean override (when false, skips purpose quality checks; non-empty purpose is still required)

Warning code contract:

- canonical warning code definitions live in `docs/spec/conformance/purpose-warning-codes.md`

Rationale:

- keeps fixtures readable in code review
- keeps diffs small and localized
- keeps case discovery deterministic and predictable
