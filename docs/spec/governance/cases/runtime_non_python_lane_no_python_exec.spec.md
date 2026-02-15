# Governance Cases

## SRGOV-RUNTIME-PYDEP-003

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-003
title: non-python lanes avoid direct python execution tokens
purpose: Ensures default gate/orchestration and rust adapter lane files do not contain python execution tokens.
type: governance.check
check: runtime.non_python_lane_no_python_exec
harness:
  root: .
  python_dependency: {}
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
      - runtime.non_python_lane_no_python_exec
```
