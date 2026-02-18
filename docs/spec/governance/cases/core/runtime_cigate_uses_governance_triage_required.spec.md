# Governance Cases

## SRGOV-RUNTIME-TRIAGE-003

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-003
title: ci gate summary uses governance triage and emits triage metadata
purpose: Ensures both Python and Rust ci-gate-summary paths reference governance triage flow.
type: governance.check
check: runtime.cigate_uses_governance_triage_required
harness:
  root: .
  cigate_governance_triage:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - governance_triage.sh
    - triage_attempted
    - triage_mode
    - triage_result
    - failing_check_ids
    - failing_check_prefixes
    - stall_detected
    - stall_phase
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
```
