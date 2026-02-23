# Assertion Model

## When to read this

Read this when authoring checks, imports, and bindings.

## What you will do

- Use canonical `contracts.clauses[].asserts.checks[]` structure.
- Keep imports explicit and deterministic.
- Apply asset/artifact split correctly.

## Step-by-step

1. Define clause-level purpose and check list.
2. Declare imports from `asset`, `artifact`, or `service` as needed.
3. Bind inputs from `assets[].id` and outputs to `artifacts[].id`.
4. Keep advanced expression logic in spec-lang calls under `assert`.

## Common failure signals

- Input bound to produced artifact IDs.
- Output bound to consumed asset IDs.
- Check logic with unresolved import names.

## Normative refs

- `specs/02_contracts/03_assertions.md`
- `specs/02_contracts/21_schema_registry_contract.md`
- `specs/01_schema/schema_v1.md`
