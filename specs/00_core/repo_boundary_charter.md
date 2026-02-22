# Repository Boundary Charter

Source of truth: spec.repo_boundary_charter

This charter defines ownership boundaries between canonical schema contracts and
runner implementation behavior specs.

## Ownership

- `data-contracts` owns canonical schema, contract, conformance, governance, and
  policy semantics.
- `dc-runner-spec` owns runner-oriented implementation behavior specs,
  implementation contract sets, and runner runtime protocol contracts.

## Canonical Authority

- Canonical schema authority is `data-contracts` `/specs/01_schema/schema_v1.md`.
- Runner-owned executable cases in `dc-runner-spec` consume schema authority via
  `schema_ref: /specs/01_schema/schema_v1.md`.

## Forbidden Crossings in Canonical Trees

Canonical `data-contracts` trees must not contain internal runner tree surface
tokens.

Runner implementation references must use explicit external repository paths,
for example:

- `/dc-runner-spec/specs/impl/...`
- `/dc-runner-spec/specs/contract_sets/...`

## Enforcement

- Governance hard-fails when forbidden boundary tokens appear in canonical
  trees.
- Runner-specific behavior validation remains runner-owned and is not redefined
  inside canonical schema docs.
