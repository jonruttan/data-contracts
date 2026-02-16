# Governance Cases

## SRGOV-RUST-PRIMARY-001

```yaml spec-test
id: SRGOV-RUST-PRIMARY-001
title: rust-primary ci lane runs core gate via runner interface
purpose: Ensures CI includes a Rust-primary lane that executes core gate through SPEC_RUNNER_BIN.
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
