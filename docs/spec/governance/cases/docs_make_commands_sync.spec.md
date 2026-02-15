# Governance Cases

## SRGOV-DOCS-REF-007

```yaml spec-test
id: SRGOV-DOCS-REF-007
title: docs use canonical make command entrypoints
purpose: Keeps contributor docs aligned on the canonical make-based command entrypoints for verification and gate execution.
type: governance.check
check: docs.make_commands_sync
harness:
  root: .
  make_commands:
    files:
    - README.md
    - docs/development.md
    required_tokens:
    - make verify-docs
    - make core-check
    - make check
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - docs.make_commands_sync
```
