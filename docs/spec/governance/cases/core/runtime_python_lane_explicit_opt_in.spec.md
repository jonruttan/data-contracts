# Governance Cases

## SRGOV-RUNTIME-ENTRY-003

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-003
title: python lane is explicit opt-in
purpose: Ensures contributor docs require explicit impl selection when using the python runner
  lane.
type: governance.check
check: runtime.python_lane_explicit_opt_in
harness:
  root: .
  python_lane_opt_in:
    files:
    - docs/development.md
    - docs/spec/contract/12_runner_interface.md
    required_opt_in_tokens:
    - SPEC_RUNNER_IMPL=python
    - --impl python
    forbidden_default_tokens:
    - SPEC_RUNNER_IMPL="python"
    - SPEC_RUNNER_IMPL=python ./scripts/ci_gate.sh
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.python_lane_explicit_opt_in
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
  target: summary_json
```
