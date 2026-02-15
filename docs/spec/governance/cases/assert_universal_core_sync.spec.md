# Governance Cases

## SRGOV-ASSERT-CORE-001

```yaml spec-test
id: SRGOV-ASSERT-CORE-001
title: assertion docs define universal evaluate core
purpose: Ensures schema and contract docs consistently define evaluate as the universal assertion core and classify other operators as authoring sugar.
type: governance.check
check: assert.universal_core_sync
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
      - assert.universal_core_sync
```
