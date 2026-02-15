# Governance Cases

## SRGOV-CONF-PORT-001

```yaml spec-test
id: SRGOV-CONF-PORT-001
title: conformance cases keep runner logic under harness
purpose: Ensures portable conformance fixtures do not place runner/setup keys at top level.
type: governance.check
check: conformance.no_runner_logic_outside_harness
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
      - conformance.no_runner_logic_outside_harness
```
