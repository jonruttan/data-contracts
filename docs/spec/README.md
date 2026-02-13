# Spec Docs

This folder contains the normative and working specification docs for
`spec_runner`.

## How To Navigate

- Start with design intent: `docs/design_philosophy.md`
- Start with guided authoring: `docs/book/README.md`
- Use stable schema shape: `docs/spec/schema/schema_v1.md`
- Use portable behavior contract: `docs/spec/contract/`
- Check open gaps: `docs/spec/backlog.md`

## Folder Layout

- `docs/spec/contract/`: versioned portable rules and policy files
- `docs/spec/schema/`: schema docs for executable `spec-test` case shape
- `docs/spec/conformance/`: cross-runtime conformance rules and fixtures
- `docs/spec/impl/`: implementation-specific notes (Python/PHP)
- `docs/spec/pending/`: draft proposals not yet adopted

## Authoring Rules

- Keep docs focused on `spec_runner` behavior and public contract semantics.
- Put runner-only setup under `harness:` in case examples (never as arbitrary
  top-level case keys).
- Keep examples executable when possible using fenced `yaml spec-test` blocks.
- Keep traceability current in `docs/spec/contract/traceability_v1.yaml`.
- `docs/spec/pending/` is draft-only: completed/resolved items MUST be removed
  from pending files instead of marked in place.
- Runtime config literals MUST be defined in `spec_runner/settings.py` and
  referenced from runtime Python code; duplicated literals in `spec_runner/`
  and `scripts/python/` fail governance checks.
