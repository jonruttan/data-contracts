```yaml doc-meta
doc_id: DOC-REF-092
title: Appendix Harness Type Reference
status: active
audience: reviewer
owns_tokens:
- appendix_harness_type_reference
requires_tokens:
- core_case_model
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated harness type catalog is in sync.
examples:
- id: EX-APP-HARNESS-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

# Harness Type Reference

Machine-generated harness type catalog from schema registry profiles.

## Purpose

Provide generated reference for harness-specific type overlays and required fields.

## Inputs

- schema registry type overlay definitions

## Outputs

- deterministic type profile tables for harness case types

## Failure Modes

- stale generated block after registry edits
- missing generated markers
- type overlay mismatch

<!-- GENERATED:START harness_type_catalog -->

## Generated Harness Type Catalog

- type_profile_count: 8
- total_type_field_count: 30
- doc_quality_score: 1.0

| case_type | field_count | required_top_level | allowed_top_level_extra |
|---|---|---|---|
| `api.http` | 3 | - | - |
| `cli.run` | 2 | - | - |
| `contract.job` | 7 | `harness`, `contract` | - |
| `docs.generate` | 8 | - | - |
| `governance.check` | 1 | `check` | - |
| `orchestration.run` | 6 | - | - |
| `spec.export` | 2 | `contract`, `harness` | `imports` |
| `text.file` | 1 | - | - |


### Type Semantics

#### `api.http`

- Summary: Performs HTTP requests with deterministic mode and optional live mode.
- Defaults:
  - mode=deterministic
  - auth=none

- Failure Modes:
  - request transport failure
  - oauth config mismatch

- Examples:
  - `type: api.http`


#### `cli.run`

- Summary: Executes command processes and asserts over output/exit context.
- Defaults:
  - stdout/stderr capture enabled

- Failure Modes:
  - non-zero exit
  - timeout
  - entrypoint missing

- Examples:
  - `type: cli.run`


#### `contract.job`

- Summary: Harness type profile declared in schema registry.
- Defaults:
  - -

- Failure Modes:
  - schema validation failure

- Examples:
  - `type: contract.job`


#### `docs.generate`

- Summary: Generates docs surfaces from declared registry templates and data sources.
- Defaults:
  - strict template render
  - mode=write/check

- Failure Modes:
  - template key missing
  - generated drift in check mode

- Examples:
  - `type: docs.generate`


#### `governance.check`

- Summary: Runs governance scanner checks and exposes structured summary/violations.
- Defaults:
  - policy_evaluate required

- Failure Modes:
  - unknown check id
  - scanner mismatch

- Examples:
  - `type: governance.check`


#### `orchestration.run`

- Summary: Orchestrates implementation effect ops via ops.* registry dispatch.
- Defaults:
  - ops capability checks required

- Failure Modes:
  - undeclared ops symbol
  - capability denied

- Examples:
  - `type: orchestration.run`


#### `spec.export`

- Summary: Harness type profile declared in schema registry.
- Defaults:
  - -

- Failure Modes:
  - schema validation failure

- Examples:
  - `type: spec.export`


#### `text.file`

- Summary: Evaluates file text subjects using filesystem-backed harness extraction.
- Defaults:
  - path resolved from virtual-root model

- Failure Modes:
  - path missing
  - decode failure

- Examples:
  - `type: text.file`
<!-- GENERATED:END harness_type_catalog -->
