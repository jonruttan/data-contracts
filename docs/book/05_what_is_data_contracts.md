# What Is Data Contracts

## When to read this

Read this first if you need the operating model before writing or validating specs.

## What you will do

- Understand what this repository owns.
- Understand what runner repositories own.
- Understand how schema, contracts, and governance fit together.

## Step-by-step

1. Treat `data-contracts` as schema/contract/governance authority.
2. Treat runner repositories as execution implementations.
3. Author executable cases as markdown with `yaml contract-spec` blocks.
4. Use governance and critical-gate to enforce canonical behavior.

## Common failure signals

- Treating runner implementation behavior as schema authority.
- Mixing authoring guidance with runtime implementation internals.
- Documenting non-canonical forms in active guidance.

## Normative refs

- `specs/01_schema/schema_v1.md`
- `specs/02_contracts/12_runner_interface.md`
- `specs/02_contracts/21_schema_registry_contract.md`
