# Governance Cases

## SRGOV-RUST-PRIMARY-001

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-001
title: rust-primary ci lane runs core gate via runner interface
purpose: Ensures CI includes a Rust-primary lane that executes core gate through SPEC_RUNNER_BIN.
type: contract.check
harness:
  root: .
  runner_interface_ci_lane:
    workflow: .github/workflows/ci.yml
    required_tokens:
    - 'core-gate-rust-adapter:'
    - 'SPEC_RUNNER_BIN: ./runners/public/runner_adapter.sh'
    - 'SPEC_RUNNER_IMPL: rust'
    - 'run: ./scripts/core_gate.sh'
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_ci_lane
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
