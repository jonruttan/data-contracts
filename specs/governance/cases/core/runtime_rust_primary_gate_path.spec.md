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
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_ci_lane
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
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
      - runtime.runner_interface_ci_lane
```
