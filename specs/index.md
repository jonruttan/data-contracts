# Spec Index

Source of truth: spec.root.index

Canonical specification root for `data-contracts`.

## Canonical Inputs

- Active model snapshot: `/specs/00_core/current.md`
- Schema contracts: `/specs/01_schema/index.md`
- Normative contracts: `/specs/02_contracts/index.md`
- Governance checks: `/specs/04_governance/index.md`
- Reusable libraries: `/specs/05_libraries/index.md`
- Runner-ingestible packs: `/specs/00_core/packs/index.md`
- Bundle contracts/schemas: `/specs/02_contracts/33_bundle_package_management.md`,
  `/specs/02_contracts/34_runner_implementation_spec_bundles.md`,
  `/specs/01_schema/bundle_manifest_v1.yaml`,
  `/specs/01_schema/implementation_bundle_overlay_v1.yaml`

## Subdomains

- Governance support domains: `/specs/04_governance/metrics/`, `/specs/04_governance/tools/`, `/specs/04_governance/`

## Ownership Model

- `specs/**` is canonical.
- canonical bundle manifests/packages are sourced from
  `https://github.com/jonruttan/data-contracts-bundles`.
- `docs/book/**` is reader-facing and includes generated references.
- `docs/history/**` is archival and non-canonical.
