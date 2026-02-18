# Governance Cases

## SRGOV-RUNTIME-TRIAGE-011

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-011
title: ci gate runs governance critical step before broad governance
purpose: Ensures ci-gate-summary defines governance_critical before governance_broad.
type: governance.check
check: runtime.ci_gate_critical_first_required
harness:
  root: .
  ci_gate_critical_first:
    files:
    - /scripts/ci_gate_summary.py
    ordered_tokens:
    - governance_critical
    - governance_broad
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
