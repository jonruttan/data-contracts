# Governance Cases

## SRGOV-DOCS-QUAL-007

```yaml spec-test
id: SRGOV-DOCS-QUAL-007
title: docs example ids are unique
purpose: Ensures example identifiers are unique across canonical docs metadata.
type: governance.check
check: docs.example_id_uniqueness
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
- target: text
  must:
  - contain:
    - 'PASS: docs.example_id_uniqueness'
```
