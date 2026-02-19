# Chapter 20: Case Model

```yaml doc-meta
doc_id: DOC-REF-120
title: Chapter 20 Case Model
status: active
audience: author
owns_tokens:
- case_topology_v1
requires_tokens:
- schema_v1_registry
commands:
- run: ./scripts/control_plane.sh governance --check-prefix schema
  purpose: Validate schema and case-shape governance contracts.
examples:
- id: EX-CASE-MODEL-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Define canonical executable case structure and responsibility boundaries.

## Inputs

- `specs/schema/schema_v1.md`
- `specs/contract/02_case_shape.md`
- `specs/contract/04_harness.md`

## Outputs

- consistent case topology
- explicit separation between extraction (`harness`) and decision logic (`contract`)

## Failure Modes

- runner-only config leaked outside `harness`
- implicit assertion state usage
- unknown top-level keys in executable case surfaces

## Canonical Top-Level Topology

Typical keys:

- `id`
- `type`
- `title`
- `domain` (optional)
- `doc` (required for `contract.export`, optional otherwise)
- `library` (for `contract.export`)
- `harness`
- `contract`
- `when` (optional)

## Responsibility Split

- `harness`: extraction/runtime setup and typed profile config.
- `contract`: assertion semantics and pass/fail authority.
- `when`: lifecycle hooks (`must`, `may`, `must_not`, `fail`, `complete`).

## Contract Form

`contract` is a mapping with:

- `defaults`
- `imports`
- `steps`

prior forms (`contract` list, `asserts`, `target`, `on`) are forbidden in canonical authoring.

## Normative References

- `specs/schema/schema_v1.md`
- `specs/contract/02_case_shape.md`
- `specs/contract/types/contract_check.md`
- `specs/contract/03_assertions.md`
