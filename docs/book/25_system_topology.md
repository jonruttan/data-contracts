# System Topology

## When to read this

Read this when you need repository ownership and boundary clarity.

## What you will do

- Map spec authority to `data-contracts`.
- Map execution authority to runner repositories.
- Keep cross-repo contracts explicit and minimal.

## Step-by-step

1. Treat `/specs/01_schema` and `/specs/02_contracts` as normative core.
2. Treat `/specs/03_conformance` and `/specs/04_governance` as executable policy surfaces.
3. Keep docs/book narrative aligned to those sources.
4. Keep runner behavior references interface-only.

## Common failure signals

- Specs redefining runner implementation internals.
- Runner docs redefining schema semantics.
- Bundle metadata treated as semantic authority.

## Normative refs

- `specs/00_core/repo_boundary_charter.md`
- `specs/02_contracts/12_runner_interface.md`
- `specs/02_contracts/34_runner_implementation_spec_bundles.md`
