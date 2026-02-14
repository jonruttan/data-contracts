# Governance Cases

## SRGOV-DOCS-V2-002

```yaml spec-test
id: SRGOV-DOCS-V2-002
title: reference index is generated from manifest
purpose: Ensures reference index markdown remains synchronized with the manifest source of truth.
type: governance.check
check: docs.reference_manifest_sync
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
    index_out: docs/book/reference_index.md
assert:
  - target: text
    must:
      - contain: ["PASS: docs.reference_manifest_sync"]
```
