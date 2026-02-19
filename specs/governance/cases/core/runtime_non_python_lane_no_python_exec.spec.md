# Governance Cases

## SRGOV-RUNTIME-PYDEP-003

```yaml contract-spec
id: SRGOV-RUNTIME-PYDEP-003
title: non-python lanes avoid direct python execution tokens
purpose: Ensures default gate/orchestration and rust adapter lane files do not contain python
  execution tokens.
type: contract.check
harness:
  root: .
  python_dependency: {}
  check:
    profile: governance.scan
    config:
      check: runtime.non_python_lane_no_python_exec
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
