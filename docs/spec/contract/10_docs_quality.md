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
- the machine-readable reference manifest (`docs/book/reference_manifest.yaml`)
  MUST remain synchronized with generated reference artifacts.

## Required Section Coverage

MUST:

- core reference chapters MUST include required section tokens defined by
  governance policy.
- missing required section tokens MUST fail governance checks.

## Metadata Schema

MUST:

- canonical reference chapters MUST include valid `doc-meta` metadata in front
  matter or `yaml doc-meta` fenced form.
- metadata MUST conform to `docs/spec/schema/docs_schema_v1.md`.
- each metadata `owns_tokens` entry MUST have unique ownership across the
  canonical reference surface.
- each metadata `requires_tokens` entry MUST resolve to an owner doc and appear
  in owner text.

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

Reference generation and graph artifacts:

- `scripts/docs_build_reference.py` renders:
  - `docs/book/reference_index.md`
  - `docs/book/reference_coverage.md`
  - `docs/book/docs_graph.json`
- `scripts/docs_build_reference.py --check` enforces freshness.

These requirements are enforced by governance checks and CI gates as hard
failures.
