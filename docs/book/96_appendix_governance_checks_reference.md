# Governance Checks Reference

```yaml doc-meta
doc_id: DOC-REF-096
title: Appendix Governance Checks Reference
status: active
audience: reviewer
owns_tokens:
- appendix_governance_checks_reference
requires_tokens:
- governance_workflow_quickpath
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated governance check catalog remains synchronized.
examples:
- id: EX-APP-GOVCHECK-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from governance check registrations and case mappings.

## Purpose

Provide generated inventory of governance check IDs and case coverage.

## Inputs

- governance check registry and governance case files

## Outputs

- deterministic check-id coverage table

## Failure Modes

- stale generated block after check/case changes
- missing generated markers
- check-to-case mapping drift

<!-- GENERATED:START governance_check_catalog -->

## Generated Governance Check Catalog

- check_count: 0
- checks_with_cases: 0
- checks_without_cases: 0

| check_id | case_count | has_case |
|---|---|---|
<!-- GENERATED:END governance_check_catalog -->
