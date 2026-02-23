# Guide 02: First Spec Authoring

## When to read this

Read this before creating your first executable `yaml contract-spec` block.

## What you will do

- author minimal canonical suite shape
- validate with governance checks

## Step-by-step

1. Add `spec_version: 1` and canonical `schema_ref`.
2. Declare `harness` with all runner inputs under `harness.config`.
3. Add one clause and one check under `contracts.clauses[].asserts.checks[]`.
4. Run required checks.

## Common failure signals

- missing clause/check IDs
- top-level keys outside schema contract
- unresolved imports/bindings

## Normative refs

- `specs/01_schema/schema_v1.md`
- `specs/02_contracts/02_case_shape.md`
- `specs/02_contracts/03_assertions.md`
