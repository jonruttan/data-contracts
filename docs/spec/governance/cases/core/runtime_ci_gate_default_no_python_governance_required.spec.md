# Governance Cases

## SRGOV-RUNTIME-TRIAGE-015

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-015
title: ci gate default broad governance path is rust-native
purpose: Ensures ci-gate-summary defaults to governance-broad-native and does not route broad
  through Python governance scripts.
type: governance.check
check: runtime.ci_gate_default_no_python_governance_required
harness:
  root: .
  ci_gate_default_no_python_governance:
    files:
    - /scripts/ci_gate_summary.py
    required_tokens:
    - governance-broad-native
    - governance_broad
    forbidden_tokens:
    - run_governance_specs.py
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
