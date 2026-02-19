# Usage Guides

```yaml doc-meta
doc_id: DOC-GUIDE-200
title: Usage Guides Index
status: active
audience: author
owns_tokens:
- usage_guides_navigation_index
requires_tokens:
- usage_guides_entrypoint
commands:
- run: ./scripts/control_plane.sh docs-generate-check
  purpose: Ensure guide navigation remains synchronized.
examples:
- id: EX-GUIDE-INDEX-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a single navigation entry for all task-driven usage guides.

## Inputs

- guide files under `/docs/book/guides/`

## Outputs

- canonical guide discovery path for authors, maintainers, and reviewers

## Failure Modes

- missing required guide files
- guide filenames drifting from canonical numbered set

## Guide Set

1. `/docs/book/guides/guide_01_onboarding.md`
2. `/docs/book/guides/guide_02_first_spec_authoring.md`
3. `/docs/book/guides/guide_03_running_checks_and_gates.md`
4. `/docs/book/guides/guide_04_debugging_failures.md`
5. `/docs/book/guides/guide_05_release_and_change_control.md`
6. `/docs/book/guides/guide_06_governance_tuning.md`
7. `/docs/book/guides/guide_07_schema_extension_workflow.md`
8. `/docs/book/guides/guide_08_ci_integration.md`
9. `/docs/book/guides/guide_09_status_exchange_operations.md`
10. `/docs/book/guides/guide_10_reference_navigation_patterns.md`
