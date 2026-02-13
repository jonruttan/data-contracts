# Spec Docs

This folder contains the normative and working specification docs for
`spec_runner`.

## How To Navigate

- Start with design intent: `docs/design-philosophy.md`
- Use stable schema shape: `docs/spec/schema/schema-v1.md`
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
- Keep traceability current in `docs/spec/contract/traceability-v1.yaml`.
