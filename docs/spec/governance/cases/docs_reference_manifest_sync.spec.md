# Governance Cases

## SRGOV-DOCS-QUAL-002

```yaml spec-test
id: SRGOV-DOCS-QUAL-002
title: reference index is generated from manifest
purpose: Ensures reference index markdown remains synchronized with the manifest source of truth.
type: governance.check
check: docs.reference_manifest_sync
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: docs/book/reference_index.md
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.reference_manifest_sync'
```
