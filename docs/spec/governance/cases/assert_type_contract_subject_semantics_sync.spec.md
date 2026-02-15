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
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - assert.type_contract_subject_semantics_sync
```
