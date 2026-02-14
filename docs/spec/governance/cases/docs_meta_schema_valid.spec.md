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
assert:
  - target: text
    must:
      - contain: ["PASS: docs.meta_schema_valid"]
```
