# Metrics Reference

```yaml doc-meta
doc_id: DOC-REF-097
title: Appendix Metrics Reference
status: active
audience: reviewer
owns_tokens:
- appendix_metrics_reference
requires_tokens:
- quickstart_minimal_case
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated metrics field catalog remains synchronized.
examples:
- id: EX-APP-METRICS-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from metric baseline field surfaces.

## Purpose

Provide generated inventory of metric baseline fields used by objective/governance checks.

## Inputs

- metrics baselines and quality metrics field extraction

## Outputs

- deterministic field-count and baseline table output

## Failure Modes

- stale generated block after baseline updates
- missing generated markers
- field extraction drift

<!-- GENERATED:START metrics_field_catalog -->

## Generated Metrics Field Catalog

- baseline_count: 12
- unique_summary_field_count: 35
- unique_segment_field_count: 108

| baseline | summary_fields | segment_count |
|---|---|---|
| `/specs/governance/metrics/contract_assertions_baseline.json` | 5 | 4 |
| `/specs/governance/metrics/docs_generate_profile_baseline.json` | 0 | 0 |
| `/specs/governance/metrics/docs_generate_timing_baseline.json` | 0 | 0 |
| `/specs/governance/metrics/docs_operability_baseline.json` | 2 | 5 |
| `/specs/governance/metrics/governance_profile_baseline.json` | 0 | 0 |
| `/specs/governance/metrics/governance_timing_baseline.json` | 0 | 0 |
| `/specs/governance/metrics/objective_scorecard_baseline.json` | 6 | 0 |
| `/specs/governance/metrics/python_dependency_baseline.json` | 5 | 0 |
| `/specs/governance/metrics/runner_independence_baseline.json` | 3 | 3 |
| `/specs/governance/metrics/spec_lang_adoption_baseline.json` | 11 | 4 |
| `/specs/governance/metrics/spec_portability_baseline.json` | 7 | 4 |
| `/specs/governance/metrics/unit_test_opt_out_baseline.json` | 0 | 0 |
<!-- GENERATED:END metrics_field_catalog -->
