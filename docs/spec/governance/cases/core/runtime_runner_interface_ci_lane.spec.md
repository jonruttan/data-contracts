# Governance Cases

## SRGOV-RUNTIME-CONFIG-005

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-005
title: ci workflow exercises rust runner interface and python parity lanes
purpose: Ensures CI runs core gate through the public runner interface in explicit rust mode
  and keeps a dedicated python parity lane runnable.
type: governance.check
check: runtime.runner_interface_ci_lane
harness:
  root: .
  runner_interface_ci_lane:
    workflow: .github/workflows/ci.yml
    required_tokens:
    - 'core-gate-rust-adapter:'
    - 'SPEC_RUNNER_BIN: ./scripts/runner_adapter.sh'
    - 'SPEC_RUNNER_IMPL: rust'
    - 'run: ./scripts/core_gate.sh'
    - 'python-parity-lane:'
    - ./scripts/runner_adapter.sh --impl python governance
    - ./scripts/runner_adapter.sh --impl python conformance-parity
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
      - runtime.runner_interface_ci_lane
  target: summary_json
```
