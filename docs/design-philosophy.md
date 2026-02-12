# Design Philosophy

`spec_runner` exists to preserve intent as executable contract, not just to
run tests.

## Why Specs Exist

Specs capture:

- behavior requirements (`MUST`, `SHOULD`, `MUST_NOT`)
- rationale (why the rule exists)
- operational constraints (determinism, safety, portability)
- conformance evidence (how the rule is verified)

Without this, implementations can pass local tests while drifting in meaning.

## Document Layers

Use layered artifacts so humans, AI systems, and scripts can each consume what
they need:

- Design and rationale:
  `docs/spec/contract/*.md`
- Machine-readable normative policy:
  `docs/spec/contract/policy-v1.yaml`
- Schema and DSL shape:
  `docs/spec/schema/schema-v1.md`
- Evidence and traceability:
  `docs/spec/contract/traceability-v1.yaml`
- Conformance report shape:
  `docs/spec/conformance/report-format.md`

## Quality Bar

A contract rule is not complete until it has:

- stable rule id
- normative level (`MUST`/`SHOULD`/`MUST_NOT`)
- rationale and risk if violated
- clear scope and applicability
- traceable evidence path (fixtures/tests/implementation)

## Portability Principle

Portable behavior is what appears in contract + policy + conformance assets.
Implementation convenience behavior is allowed, but must be marked as
implementation-specific and must not be required for conformance.

## Change Control

When user-visible behavior changes, update in the same slice:

1. contract docs
2. policy metadata
3. schema docs
4. traceability mapping
5. tests/conformance assets
