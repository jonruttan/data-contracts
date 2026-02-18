# Governance Cases

## SRGOV-RUNTIME-TRIAGE-015

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-015
title: ci gate default broad governance path is rust-native
purpose: Ensures ci-gate-summary defaults to governance-broad-native and does not route broad
  through Python governance scripts.
type: contract.check
harness:
  root: .
  ci_gate_default_no_python_governance:
    files:
    - /spec_runner/script_runtime_commands.py
    required_tokens:
    - governance-broad-native
    - governance_broad
    forbidden_tokens: []
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
      check: runtime.ci_gate_default_no_python_governance_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
