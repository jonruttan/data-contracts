# Chapter 35: Usage Guides

```yaml doc-meta
doc_id: DOC-REF-135
title: Chapter 35 Usage Guides
status: active
audience: author
owns_tokens:
- usage_guides_entrypoint
requires_tokens:
- system_topology_view
commands:
- run: ./scripts/control_plane.sh docs-generate-check
  purpose: Ensure guide-linked reference surfaces stay synchronized.
examples:
- id: EX-USAGE-INDEX-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide task-driven entrypoints for common and advanced workflows.

## Inputs

- guide pages under `/docs/book/guides/`

## Outputs

- practical paths for onboarding, authoring, operations, and extension

## Failure Modes

- using advanced workflows before completing core setup
- skipping validation steps and trusting partial results

## Guide Paths

- `/docs/book/guides/index.md`
- `/docs/book/guides/guide_01_onboarding.md`
- `/docs/book/guides/guide_02_first_spec_authoring.md`
- `/docs/book/guides/guide_03_running_checks_and_gates.md`
- `/docs/book/guides/guide_04_debugging_failures.md`
- `/docs/book/guides/guide_05_release_and_change_control.md`
- `/docs/book/guides/guide_06_governance_tuning.md`
- `/docs/book/guides/guide_07_schema_extension_workflow.md`
- `/docs/book/guides/guide_08_ci_integration.md`
- `/docs/book/guides/guide_09_status_exchange_operations.md`
- `/docs/book/guides/guide_10_reference_navigation_patterns.md`
