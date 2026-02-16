# Governance Cases

## SRGOV-RUNTIME-CONFIG-005

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-005
title: ci workflow exercises rust runner interface lane
purpose: Ensures CI runs core gate through the public runner interface in explicit rust mode.
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
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
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
      - runtime.runner_interface_ci_lane
```
