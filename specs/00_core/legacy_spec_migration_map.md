# Legacy Spec Migration Map

## Path Migrations

- `/specs/schema/` -> `/specs/01_schema/`
- `/specs/contract/` -> `/specs/02_contracts/`
- `/specs/conformance/` -> `/specs/03_conformance/`
- `/specs/libraries/` -> `/specs/05_libraries/`
- `registry/v2` -> `registry/v1`

## Identifier Migrations

- `schema_v2` -> `schema_v1`
- `schema.catalog_contains_active_schema_v2` -> `schema.catalog_contains_active_schema_v1`
- `normalization.contract_spec_key_order_v2` -> `normalization.contract_spec_key_order_v1`
- `runner_execution_certificate_v2` -> `runner_execution_certificate_v1`
- `runner_certification_registry_v2` -> `runner_certification_registry_v1`
- `runner_certification_registry_local_v2` -> `runner_certification_registry_local_v1`

## Removal Policy

- Legacy specs and references are removed after all references are rewritten to canonical v1 surfaces.
- No compatibility aliases are retained in canonical authoring references.
