# Guide 07: Schema Extension Workflow

## When to read this

Read this before modifying schema fields, constraints, or requiredness semantics.

## What you will do

- update schema and registry contracts consistently
- update executable cases and docs

## Step-by-step

1. Update schema/registry definitions.
2. Update normative contracts that describe the behavior.
3. Update conformance/governance cases.
4. Update docs/book references and examples.

## Common failure signals

- schema changed without contract updates
- cases still validating old shape
- docs examples using stale fields

## Normative refs

- `specs/01_schema/schema_v1.md`
- `specs/02_contracts/21_schema_registry_contract.md`
- `specs/04_governance/cases/core/spec_core/`
