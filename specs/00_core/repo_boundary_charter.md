# Repository Boundary Charter

Source of truth: spec.repo_boundary_charter

This charter defines ownership boundaries between canonical schema contracts and reusable runner-oriented spec contracts.

## Ownership

- `data-contracts` owns canonical schema, contract, conformance, governance, and policy semantics.
- `data-contracts-runner` owns reusable shared runner-oriented behavior specs and shared runner contracts.
- `data-contracts-library` owns reusable runner overlays and shared reusable libraries.

## Canonical Authority

- Canonical schema authority is `data-contracts` `/specs/01_schema/schema_v1.md`.
- Reusable shared runner executable cases in `data-contracts-runner` consume schema authority via `schema_ref: /specs/01_schema/schema_v1.md`.

## Forbidden Crossings in Canonical Trees

Canonical `data-contracts` trees must not contain internal reusable-runner tree surface tokens.

Reusable runner implementation references must use explicit external repository paths, for example:

- `/data-contracts-runner/specs/07_runner_behavior/runner/...`
- `/data-contracts-runner/specs/07_runner_behavior/contract_sets/shared/...`
- `/dc-runner-rust/specs/impl/rust/...`
- `/dc-runner-python/specs/impl/python/...`
- `/dc-runner-php/specs/impl/php/...`

## Enforcement

- Governance hard-fails when forbidden boundary tokens appear in canonical trees.
- Runner-specific behavior validation remains runner-owned and is not redefined inside canonical schema docs.
- Canonical shared runner behavior manifests must reference `data-contracts-runner`.
- Canonical shared libraries and overlays must reference `data-contracts-library`.
