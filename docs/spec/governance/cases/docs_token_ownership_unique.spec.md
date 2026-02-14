# Governance Cases

## SRGOV-DOCS-V2-003

```yaml spec-test
id: SRGOV-DOCS-V2-003
title: doc token ownership is unique
purpose: Ensures canonical documentation tokens have a single owner page.
type: governance.check
check: docs.token_ownership_unique
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.token_ownership_unique"]
```
