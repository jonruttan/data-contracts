# Governance Cases

## SRGOV-DOCS-QUAL-003

```yaml spec-test
id: SRGOV-DOCS-QUAL-003
title: doc token ownership is unique
purpose: Ensures canonical documentation tokens have a single owner page.
type: governance.check
check: docs.token_ownership_unique
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
    - 'PASS: docs.token_ownership_unique'
```
