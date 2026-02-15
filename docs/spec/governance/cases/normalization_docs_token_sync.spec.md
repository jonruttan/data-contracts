# Governance Cases

## SRGOV-NORM-003

```yaml spec-test
id: SRGOV-NORM-003
title: normalization docs token sync is enforced
purpose: Ensures schema contract and book docs maintain required mapping-AST wording and forbid stale expression-shape tokens.
type: governance.check
check: normalization.docs_token_sync
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: normalization.docs_token_sync'
```
