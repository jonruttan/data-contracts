# Governance Cases

## SRGOV-RUNTIME-PYDEP-003

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-003
title: non-python lanes avoid direct python execution tokens
purpose: Ensures default gate/orchestration and rust adapter lane files do not contain python
  execution tokens.
type: governance.check
check: runtime.non_python_lane_no_python_exec
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  python_dependency: {}
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.non_python_lane_no_python_exec
```
