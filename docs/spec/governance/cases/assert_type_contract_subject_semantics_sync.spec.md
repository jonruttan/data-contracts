# Governance Cases

## SRGOV-ASSERT-SUBJECT-001

```yaml spec-test
id: SRGOV-ASSERT-SUBJECT-001
title: type contracts define subject semantics
purpose: Ensures harness and type contracts define target subject semantics and avoid per-type operator allowlists.
type: governance.check
check: assert.type_contract_subject_semantics_sync
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
    - 'PASS: assert.type_contract_subject_semantics_sync'
```
