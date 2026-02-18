# Spec Case Shape Reference

```yaml doc-meta
doc_id: DOC-REF-098
title: Appendix Spec Case Shape Reference
status: active
audience: reviewer
owns_tokens:
- appendix_spec_case_shape_reference
requires_tokens:
- core_case_model
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated schema field catalog remains synchronized.
examples:
- id: EX-APP-SCHEMA-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from the schema registry type and field profiles.

## Purpose

Provide generated case-shape field reference derived from schema registry profiles.

## Inputs

- schema registry overlays and compiled field model

## Outputs

- deterministic top-level field and type-profile tables

## Failure Modes

- stale generated block after schema changes
- missing generated markers
- schema/catalog drift

<!-- GENERATED:START spec_schema_field_catalog -->

## Generated Spec Schema Field Catalog

- top_level_field_count: 16
- type_profile_count: 8
- total_type_field_count: 30

### Top-Level Fields

| key | type | required | since |
|---|---|---|---|
| `assert_health` | `mapping` | false | `v1` |
| `contract` | `list` | false | `v1` |
| `expect` | `mapping` | false | `v1` |
| `harness` | `mapping` | false | `v1` |
| `id` | `string` | true | `v1` |
| `path` | `string` | false | `v1` |
| `purpose` | `string` | false | `v1` |
| `requires` | `mapping` | false | `v1` |
| `title` | `string` | false | `v1` |
| `type` | `string` | true | `v1` |
| `when` | `mapping` | false | `v1` |
| `when.complete` | `list` | false | `v1` |
| `when.fail` | `list` | false | `v1` |
| `when.may` | `list` | false | `v1` |
| `when.must` | `list` | false | `v1` |
| `when.must_not` | `list` | false | `v1` |

### Type Profiles

| case_type | field_count | required_top_level |
|---|---|---|
| `api.http` | 3 | - |
| `cli.run` | 2 | - |
| `contract.job` | 7 | `harness`, `contract` |
| `docs.generate` | 8 | - |
| `governance.check` | 1 | `check` |
| `orchestration.run` | 6 | - |
| `spec.export` | 2 | `contract`, `harness` |
| `text.file` | 1 | - |
<!-- GENERATED:END spec_schema_field_catalog -->
