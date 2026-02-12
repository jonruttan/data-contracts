# Spec Docs

This folder contains the spec documentation for `spec_runner` itself.

Notes:

- Keep these docs focused on `spec_runner` behavior and its public schema.
- Canonical docs currently include:
  - `docs/design-philosophy.md`
  - `docs/spec/schema/schema-v1.md`
  - `docs/spec/contract/`
  - `docs/spec/backlog.md`
- Pending work specs go in `docs/spec/pending/`.
- Implementation-specific notes go in `docs/spec/impl/`.
- Cross-language parity docs go in `docs/spec/conformance/`.
- Contract traceability is maintained in:
  `docs/spec/contract/traceability-v1.yaml`.
- Specs can include executable cases as fenced blocks:
  ` ```yaml spec-test ... ``` `.
