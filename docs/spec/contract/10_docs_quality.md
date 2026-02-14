# Docs Quality Contract (v1)

Documentation is a tested product surface.

## Reference Surface

The canonical reference manual surface for v1 is:

- `docs/book/*`
- `docs/spec/contract/*`
- `docs/spec/schema/schema_v1.md`

MUST:

- reference-surface files required by governance MUST exist.
- the machine-checked book index (`docs/book/reference_index.md`) MUST match
  the actual reference-manual chapter set and order.

## Required Section Coverage

MUST:

- core reference chapters MUST include required section tokens defined by
  governance policy.
- missing required section tokens MUST fail governance checks.

## Executable Example Policy

MUST:

- `yaml spec-test` fenced examples in reference docs MUST parse as YAML.
- shell/python code examples in the reference surface MUST pass lightweight
  static validation.
- invalid examples MUST fail unless explicitly opted out.

Opt-out format:

- `DOCS-EXAMPLE-OPT-OUT: <reason>`

Rules:

- reason text MUST be specific and non-empty.
- opt-out applies only to nearby example blocks and SHOULD be temporary.

## CLI Docs Completeness

MUST:

- public CLI flags extracted from runner scripts MUST be documented in the
  required implementation/development docs.
- docs MUST include default behavior, opt-in behavior, and failure-mode notes
  for each public runner interface.

## Contract/Schema/Book Synchronization

MUST:

- core assertion tokens used by authors and implementers MUST remain synchronized
  across:
  - `docs/book/03_assertions.md`
  - `docs/spec/contract/03_assertions.md`
  - `docs/spec/schema/schema_v1.md`

## Enforcement

These requirements are enforced by governance checks and are hard CI gates.
