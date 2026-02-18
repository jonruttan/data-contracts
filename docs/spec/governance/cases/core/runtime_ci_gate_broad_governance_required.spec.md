# Governance Cases

## SRGOV-RUNTIME-TRIAGE-010

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-010
title: ci gate includes mandatory broad governance after critical phase
purpose: Ensures ci-gate-summary contains mandatory broad governance execution metadata.
type: governance.check
check: runtime.ci_gate_broad_governance_required
harness:
  root: .
  ci_gate_broad_required:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - governance_broad
    - triage_phase
    - broad_required
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
