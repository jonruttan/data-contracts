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
- Contract-job metadata MUST use `harness.jobs[]` rows keyed by explicit `id`.

## Profile Types

- `core`
- `assertions`
- `harness`
- `path_model`
- `type`

## Type Profiles

Type profiles define per-`type` additions over common top-level keys:

- type-specific fields
- required keys
- optional extras

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable
for the same repository state.
