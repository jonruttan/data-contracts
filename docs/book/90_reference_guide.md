# Reference Guide

## When to read this

Read this when you need to jump from narrative guidance to authoritative source files quickly.

## What you will do

- Locate the owning schema/contract/governance source for each topic.
- Follow guide-to-contract mappings during implementation and review.

## Step-by-step

1. Identify the topic area (schema, assertions, governance, runner interface, bundles).
2. Jump to the mapped contract and schema paths.
3. Use governance case IDs to verify behavior.

## Common failure signals

- Following a narrative page without checking normative refs.
- Editing a derived/generated docs file instead of source-of-truth inputs.

## Normative refs

- `specs/01_schema/schema_v1.md`
- `specs/02_contracts/10_docs_quality.md`
- `specs/02_contracts/03_assertions.md`
- `specs/02_contracts/04_harness.md`
- `specs/02_contracts/21_schema_registry_contract.md`
- `specs/02_contracts/33_bundle_package_management.md`
- `specs/04_governance/check_sets_v1.yaml`

## Guide To Contract Map

- onboarding: `specs/02_contracts/12_runner_interface.md`
- first spec authoring: `specs/02_contracts/02_case_shape.md`, `specs/02_contracts/03_assertions.md`
- running checks and gates: `specs/02_contracts/12_runner_interface.md`, `specs/04_governance/check_sets_v1.yaml`
- debugging failures: `specs/02_contracts/15_governance_subject_model.md`
- release and change control: `specs/02_contracts/policy_v1.yaml`, `specs/02_contracts/traceability_v1.yaml`
- governance tuning: `specs/02_contracts/traceability_v1.yaml`
- schema extension workflow: `specs/01_schema/schema_v1.md`, `specs/02_contracts/21_schema_registry_contract.md`
- CI integration: `specs/02_contracts/25_compatibility_matrix.md`
- status exchange operations: `specs/02_contracts/27_runner_status_exchange.md`
- reference navigation patterns: `docs/book/reference_manifest.yaml`

## Generated References

- `docs/book/99_generated_reference_index.md`
