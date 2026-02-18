# Governance Cases

## SRGOV-RUNTIME-TRIAGE-003

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-003
title: ci gate summary uses governance triage and emits triage metadata
purpose: Ensures both Python and Rust ci-gate-summary paths reference governance triage flow.
type: contract.check
harness:
  root: .
  cigate_governance_triage:
    files:
    - /runners/python/spec_runner/script_runtime_commands.py
    - /runners/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - governance_broad
    - triage_attempted
    - triage_mode
    - triage_result
    - failing_check_ids
    - failing_check_prefixes
    - stall_detected
    - stall_phase
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
      check: runtime.cigate_uses_governance_triage_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
