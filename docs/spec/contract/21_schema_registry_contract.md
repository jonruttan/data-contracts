# Schema Registry Contract (v1)

## Purpose

The schema registry under `docs/spec/schema/registry/v1/` is the machine source
of truth for executable case-shape constraints.

## Normative Rules

- Runtime schema validation MUST be driven from compiled registry data.
- Unknown top-level case keys MUST fail with `schema`.
- Registry profiles MUST use `docs/spec/schema/registry_schema_v1.yaml` shape.
- `docs/spec/schema/schema_v1.md` MUST contain generated registry snapshot
  content and stay synchronized.

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
