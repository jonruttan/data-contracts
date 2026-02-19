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
    - /runners/python/spec_runner/script_runtime_commands.py
    - /runners/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - skipped_step_count
    - first_failure_step
    - aborted_after_step
    - blocked_by
    - skip_reason
  check:
    profile: governance.scan
    config:
      check: runtime.gate_skipped_steps_contract_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
