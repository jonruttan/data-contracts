# Contract Bundle Taxonomy Contract (v1)

Defines canonical bundle terminology for project-scoped validation and artifact generation.

## Canonical Hierarchy

Canonical hierarchy is:

- `Bundle -> Domain -> Module -> Contract`

Hierarchy rules:

- `Bundle` is the top-level canonical unit.
- `Domain` is a functional partition within a bundle (for example `tooling`, `docs`, `source`).
- `Module` is a cohesive capability inside a domain.
- `Contract` is the executable spec unit.

## Bundle Terms

- `Artifact`: output boundary declared or validated by bundle modules (file, directory, report, manifest, lock).
- `Bundle Package`: downloadable immutable materialization of a bundle version.
- `Bundle Manifest`: machine-readable descriptor of bundle structure and metadata.
- `Bundle Lock`: resolved immutable record that captures selected content and integrity hashes.

Trigger semantics are out of scope for this taxonomy version.

## Canonical Metadata Vocabulary

Bundle metadata uses:

- `bundle_id` (string)
- `bundle_version` (SemVer string)
- `maintainers[]` (owner list)

`bundle_version` and `maintainers` are canonical names for new bundle metadata.

## Legacy Alias Policy

Legacy terms remain migration aliases and are not co-equal canonical terms:

- `contract_set` is a legacy alias for bundle selection/resolution surfaces.
- `pack` is a legacy alias for curated bundle views.
- `author` is a deprecated alias for ownership metadata; use `maintainers`.
- bare `version` is ambiguous for bundle metadata; use `bundle_version`.

## Compatibility Intent

- Existing contract-set and pack surfaces may remain for compatibility during migration.
- New bundle-oriented schema and docs must prefer canonical bundle vocabulary.
