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

- type_profile_count: 3
- total_type_field_count: 15
- doc_quality_score: 1.0

| case_type | field_count | required_top_level | allowed_top_level_extra |
|---|---|---|---|
| `contract.check` | 5 | `harness`, `contract` | - |
| `contract.export` | 3 | `contract`, `harness` | `imports` |
| `contract.job` | 7 | `harness`, `contract` | - |


### Type Semantics

#### `contract.check`

- Summary: Runs canonical contract checks using harness.check profiles.
- Defaults:
  - evaluate-only assertions
  - MUST/MAY/MUST_NOT class semantics

- Failure Modes:
  - unknown check profile
  - invalid check config

- Examples:
  - `type: contract.check`


#### `contract.export`

- Summary: Declares reusable contract symbol exports for chain imports.
- Defaults:
  - harness.exports with from=assert.function

- Failure Modes:
  - invalid export shape
  - unresolvable export path

- Examples:
  - `type: contract.export`


#### `contract.job`

- Summary: Executes harness.jobs metadata through contract-driven ops.job.dispatch.
- Defaults:
  - dispatch from contract assertions
  - summary_json output target

- Failure Modes:
  - missing job metadata
  - dispatch helper error

- Examples:
  - `type: contract.job`
<!-- GENERATED:END harness_type_catalog -->
