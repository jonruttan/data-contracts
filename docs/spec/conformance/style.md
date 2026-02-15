# Conformance Case Authoring Style

Conformance case docs are authored as Markdown `*.spec.md` files with fenced
`yaml spec-test` blocks.

Style rules:

- one case per fenced `spec-test` block
- each block must be immediately preceded by `## <case-id>`
- case ids must be sorted ascending within each file
- each fenced block should stay small (120 lines max) for readability
- each case must include a non-empty `purpose` field describing the intent
- `purpose` should add context beyond `title` (not a copy)
- `purpose` should be at least 8 words and avoid placeholders (`todo`, `tbd`, `fixme`, `xxx`)
- prefer sugar assertion operators (`contain`, `regex`, `json_type`, `exists`)
  for new assertion authoring; use `evaluate` only when required by case intent

Purpose lint policy:

- defaults and runtime profiles are configured in `docs/spec/conformance/purpose_lint_v1.yaml`
- per-case override is optional via `purpose_lint` mapping:

## `evaluate` Expression Layout

Conformance cases using `evaluate` SHOULD keep spec-lang expressions in
operator-keyed mapping AST form for readability and deterministic review diffs.
Prefer condensed inline args for short expressions (for example
`eq: [{add: [1, 2]}, 3]`) while preserving mapping-AST semantics.

Use tooling to enforce/normalize:

- lint: `python scripts/evaluate_style.py --check docs/spec`
- format: `python scripts/evaluate_style.py --write docs/spec`
  - `runtime`: runtime profile name from policy (for example `php`)
  - `min_words`: integer override
  - `placeholders`: list override
  - `forbid_title_copy`: boolean override
  - `severity_by_code`: mapping override (code -> `info|warn|error`)
  - `enabled`: boolean override (when false, skips purpose quality checks; non-empty purpose is still required)

Warning code contract:

- canonical warning code definitions live in `docs/spec/conformance/purpose_warning_codes.md`

Rationale:

- keeps fixtures readable in code review
- keeps diffs small and localized
- keeps case discovery deterministic and predictable
