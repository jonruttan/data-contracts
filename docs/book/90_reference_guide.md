# Chapter 90: Reference Guide

```yaml doc-meta
doc_id: DOC-REF-190
title: Chapter 90 Reference Guide
status: active
audience: reviewer
owns_tokens:
- normative_reference_map
requires_tokens:
- deterministic_failure_triage
commands:
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Verify generated reference surfaces are synchronized.
examples:
- id: EX-REFERENCE-GUIDE-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a concise map from narrative and guide workflows to normative schema/contract references.

## Inputs

- schema docs under `specs/schema`
- contract docs under `specs/contract`
- generated reference outputs under `docs/book`

## Outputs

- authoritative lookup path for reviewers and maintainers

## Failure Modes

- using narrative docs where normative contract text is required
- stale generated refs interpreted as source of truth

## Normative Sources

- `specs/schema/schema_v1.md`
- `specs/schema/runner_status_report_v1.yaml`
- `specs/schema/runner_status_matrix_v1.yaml`
- `specs/contract/02_case_shape.md`
- `specs/contract/03_assertions.md`
- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/10_docs_quality.md`
- `specs/contract/12_runner_interface.md`
- `specs/contract/22_docs_information_architecture.md`
- `specs/contract/25_compatibility_matrix.md`
- `specs/contract/27_runner_status_exchange.md`

## Guide To Contract Map

| Guide | Primary normative sources |
| --- | --- |
| `guide_01_onboarding.md` | `specs/contract/10_docs_quality.md`, `specs/contract/12_runner_interface.md` |
| `guide_02_first_spec_authoring.md` | `specs/contract/02_case_shape.md`, `specs/contract/03_assertions.md` |
| `guide_03_running_checks_and_gates.md` | `specs/contract/12_runner_interface.md`, `specs/contract/15_governance_subject_model.md` |
| `guide_04_debugging_failures.md` | `specs/contract/10_docs_quality.md`, `specs/contract/15_governance_subject_model.md` |
| `guide_05_release_and_change_control.md` | `specs/contract/10_docs_quality.md`, `specs/contract/policy_v1.yaml` |
| `guide_06_governance_tuning.md` | `specs/contract/15_governance_subject_model.md`, `specs/contract/traceability_v1.yaml` |
| `guide_07_schema_extension_workflow.md` | `specs/schema/schema_v1.md`, `specs/contract/21_schema_registry_contract.md` |
| `guide_08_ci_integration.md` | `specs/contract/12_runner_interface.md`, `specs/contract/25_compatibility_matrix.md` |
| `guide_09_status_exchange_operations.md` | `specs/contract/27_runner_status_exchange.md`, `specs/schema/runner_status_matrix_v1.yaml` |
| `guide_10_reference_navigation_patterns.md` | `specs/contract/10_docs_quality.md`, `docs/book/reference_manifest.yaml` |

## Generated References

Use `docs/book/99_generated_reference_index.md` as the canonical entrypoint.
For canonical full case templates, see `docs/book/93n_spec_case_templates_reference.md`.
