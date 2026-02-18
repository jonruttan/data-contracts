# Governance Cases

## SRGOV-RUNTIME-FAILFAST-002

```yaml contract-spec
id: SRGOV-RUNTIME-FAILFAST-002
title: gate summary payload includes skipped step contract
purpose: Ensures gate summary output includes skipped-step and abort metadata fields.
type: contract.check
harness:
  root: .
  gate_skipped_contract:
    files:
    - /spec_runner/script_runtime_commands.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - skipped_step_count
    - first_failure_step
    - aborted_after_step
    - blocked_by
    - skip_reason
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.gate_skipped_steps_contract_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
