# Case Model

## When to read this

Read this before authoring or reviewing executable `.spec.md` cases.

## What you will do

- Apply canonical contract-spec shape.
- Keep harness config under `harness`.
- Keep assertion behavior in `contracts.clauses[].asserts.checks[]`.

## Step-by-step

1. Start each executable block with `spec_version: 1` and `schema_ref`.
2. Define harness inputs under `harness.config` only.
3. Define assertions under `contracts.clauses[].asserts`.
4. Use bindings for explicit symbol wiring.

## Common failure signals

- Top-level runner config keys outside `harness`.
- Missing clause/check IDs.
- Non-deterministic imports or unresolved symbols.

## Normative refs

- `specs/01_schema/schema_v1.md`
- `specs/02_contracts/02_case_shape.md`
- `specs/02_contracts/04_harness.md`
