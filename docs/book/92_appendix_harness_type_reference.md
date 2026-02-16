# Harness Type Reference

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

- type_profile_count: 7
- total_type_field_count: 7

| case_type | field_count | required_top_level | allowed_top_level_extra |
|---|---|---|---|
| `api.http` | 1 | `request` | - |
| `cli.run` | 2 | - | - |
| `docs.generate` | 0 | - | - |
| `governance.check` | 1 | `check` | - |
| `orchestration.run` | 0 | - | - |
| `spec_lang.library` | 2 | `definitions` | `imports` |
| `text.file` | 1 | - | - |
<!-- GENERATED:END harness_type_catalog -->
