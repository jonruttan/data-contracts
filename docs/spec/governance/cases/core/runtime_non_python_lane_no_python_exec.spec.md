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
  python_dependency: {}
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.non_python_lane_no_python_exec
  target: summary_json
```
