# Governance Cases

## SRGOV-DOCS-V2-004

```yaml spec-test
id: SRGOV-DOCS-V2-004
title: doc token dependencies resolve to owner docs
purpose: Ensures required tokens in doc metadata are owned and present in owner docs.
type: governance.check
check: docs.token_dependency_resolved
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.token_dependency_resolved"]
```
