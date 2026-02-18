# Governance Cases

## SRGOV-RUNTIME-TRIAGE-017

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-017
title: ci gate executes critical pass exactly once
purpose: Ensures ci_gate.sh runs critical-gate once and then invokes ci-gate-summary.
type: governance.check
check: runtime.ci_gate_single_pass_critical_required
harness:
  root: .
  ci_gate_single_pass_critical:
    path: /scripts/ci_gate.sh
    required_tokens:
    - critical-gate
    - ci-gate-summary
    ordered_tokens:
    - critical-gate
    - ci-gate-summary
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
