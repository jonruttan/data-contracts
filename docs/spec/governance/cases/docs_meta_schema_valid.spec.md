# Governance Cases

## SRGOV-DOCS-QUAL-001

```yaml spec-test
id: SRGOV-DOCS-QUAL-001
title: docs metadata schema is valid for canonical reference chapters
purpose: Ensures each canonical reference chapter contains valid machine-checkable doc metadata.
type: governance.check
check: docs.meta_schema_valid
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
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
      - docs.meta_schema_valid
```
