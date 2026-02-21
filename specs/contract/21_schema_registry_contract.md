# Schema Registry Contract (v2)

## Purpose

The schema registry under `specs/schema/registry/v2/` is the machine source of truth for executable case-shape constraints.

## Normative Rules

- Runtime schema validation MUST be driven from compiled registry data.
- Unknown top-level case keys MUST fail with `schema`.
- Suite top-level validation MUST enforce `spec_version`, `schema_ref`, and non-empty `contracts`.
- Contract-item validation MUST enforce per-item `id` and `clauses` shape.
- Registry profiles MUST use `specs/schema/registry_schema_v1.yaml` shape.
- `specs/schema/schema_v2.md` MUST contain generated registry snapshot
  content and stay synchronized.
- Runtime expectation overrides MUST use `expect.overrides[]` (no `expect.impl.*` wildcard keys).
- Contract-job metadata MUST use `clauses.config.jobs[]` rows keyed by explicit `id`.
- `contracts[].harness` MUST resolve to a catalog entry in
  `/specs/schema/harness_contract_catalog_v1.yaml`; unknown harness names are
  hard-fail schema errors.
- Suite artifact references MUST be declared only under
  `artifact.imports[]`/`artifact.exports[]`.
- Root `exports[]` MUST be function-only declarations using
  `as` + `from: assert.function` + `path`.
- Suite defaults and clause defaults are optional compression surfaces; empty
  defaults mappings are non-canonical.

## Profile Types

- `core`
- `assertions`
- `harness`
- `path_model`
- `deprecated type overlays` (migration-only; non-normative)

## Harness Catalog

Harness catalog entries define per-harness additions over common case keys:

- required top-level companion keys
- required and allowed clause keys
- allowed export mode (`function`)

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable
for the same repository state.
