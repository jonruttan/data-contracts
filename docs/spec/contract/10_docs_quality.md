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

- `scripts/docs_generate_all.py --build` is the canonical generator orchestrator.
- `scripts/docs_generate_all.py --check` is the canonical hard-fail freshness check.
- `scripts/docs_build_reference.py` remains a surface-specific wrapper and renders:
  - `docs/book/reference_index.md`
  - `docs/book/reference_coverage.md`
  - `docs/book/docs_graph.json`
- API catalog generators produce:
  - `docs/book/runner_api_reference.md`
  - `docs/book/harness_type_reference.md`
  - `docs/book/spec_lang_builtin_catalog.md`
  - `docs/book/contract_policy_reference.md`
  - `docs/book/traceability_reference.md`
  - `docs/book/governance_checks_reference.md`
  - `docs/book/metrics_reference.md`
  - `docs/book/spec_case_shape_reference.md`
  - `.artifacts/runner-api-catalog.json`
  - `.artifacts/harness-type-catalog.json`
  - `.artifacts/spec-lang-builtin-catalog.json`
  - `.artifacts/policy-rule-catalog.json`
  - `.artifacts/traceability-catalog.json`
  - `.artifacts/governance-check-catalog.json`
  - `.artifacts/metrics-field-catalog.json`
  - `.artifacts/spec-schema-field-catalog.json`
- generated sections are read-only and delimited by
  `<!-- GENERATED:START ... -->` / `<!-- GENERATED:END ... -->` markers.
- docs generator report artifacts are required:
  - `.artifacts/docs-generator-report.json`
  - `.artifacts/docs-generator-summary.md`

These requirements are enforced by governance checks and CI gates as hard
failures.

## Release Guidance Policy

MUST:

- release guidance MUST point to executable gate entrypoints.
- sequential manual "do X, then inspect Y" checklist choreography is an
  anti-pattern for this repo and MUST NOT be documented as normative process.
