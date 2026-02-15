# Governance Cases

## SRGOV-NORM-001

```yaml spec-test
id: SRGOV-NORM-001
title: normalization profile defines required source-of-truth fields
purpose: Ensures normalization profile exists and includes all required top-level keys and path scopes.
type: governance.check
check: normalization.profile_sync
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
    - 'PASS: normalization.profile_sync'
```
