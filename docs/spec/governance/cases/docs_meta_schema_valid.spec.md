# Governance Cases

## SRGOV-DOCS-V2-001

```yaml spec-test
id: SRGOV-DOCS-V2-001
title: docs metadata schema is valid for canonical reference chapters
purpose: Ensures each canonical reference chapter contains valid machine-checkable doc metadata.
type: governance.check
check: docs.meta_schema_valid
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.meta_schema_valid"]
```
