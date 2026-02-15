# Governance Cases

## SRGOV-DOCS-QUAL-004

```yaml spec-test
id: SRGOV-DOCS-QUAL-004
title: doc token dependencies resolve to owner docs
purpose: Ensures required tokens in doc metadata are owned and present in owner docs.
type: governance.check
check: docs.token_dependency_resolved
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - docs.token_dependency_resolved
```
