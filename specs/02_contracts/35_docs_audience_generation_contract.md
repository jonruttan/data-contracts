# Docs Audience Generation Contract (v1)

Defines deterministic generation of audience-targeted documentation surfaces from
spec-declared docs metadata.

## Canonical Audience Enum

- `operator`
- `integrator`
- `implementer`
- `maintainer`
- `governance`
- `reviewer`
- `auditor`

## Source Inputs

Generator MUST collect docs metadata from:

1. executable spec surfaces (`*.spec.md`)
2. structured docs metadata fields (`docs[]`, `harness.docs[]`, and equivalent)
3. `yaml doc-meta` fences where present

Non-canonical audience tokens are invalid for active v1 surfaces.

## Outputs

For each audience, generator MUST emit:

- `/docs/audience/<audience>/index.md`
- `/docs/audience/<audience>/reference_manifest.yaml`
- `/docs/audience/<audience>/reference_index.md`
- `/docs/audience/<audience>/reference_coverage.md`

Output structure schema:

- `/specs/01_schema/docs_audience_surface_v1.yaml`

## Deterministic Rules

1. Normalize metadata and reject unknown audience tokens.
2. Build audience-specific source path set from declared metadata only.
3. Sort source paths lexicographically.
4. Render manifest/index/coverage in stable order.
5. `--check` mode MUST hard-fail on drift from generated result.
6. Output artifacts are generated per audience from executable spec metadata and are
   deterministic regardless of runtime language.

## Runtime and Policy

- `dc-runner docs generate` and `dc-runner docs generate-check` are spec-native
  command entrypoints and must not execute project Python scripts.
- Generator CLI contracts are:
  - `dc-runner docs generate --build`
  - `dc-runner docs generate --check`
  - `dc-runner docs generate --build --surface <audience>`
- Supported operational flags are `--summary-out`, `--timing-out`, `--report-out`,
  and `--jobs`.
- Shell scripts remain wrappers only.
- Audience docs generation/check semantics are governed by executable specs and
  policy contracts.
