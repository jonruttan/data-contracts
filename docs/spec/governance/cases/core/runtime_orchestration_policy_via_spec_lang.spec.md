# Governance Cases

## SRGOV-RUNTIME-ORCH-001

```yaml contract-spec
id: SRGOV-RUNTIME-ORCH-001
title: gate orchestration verdict is policy-driven via spec-lang
purpose: Ensures CI gate summary determines final verdict from assert-derived
  step statuses without policy_evaluate expressions.
type: governance.check
check: runtime.orchestration_policy_via_spec_lang
harness:
  root: .
  orchestration_policy:
    files:
    - path: /scripts/ci_gate_summary.py
      required_tokens:
      - _evaluate_gate_policy(
      - all(str(row.get("status", "")) == "pass"
      - policy_verdict
    - path: /docs/spec/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md
      required_tokens:
      - runtime.orchestration_policy_via_spec_lang
      - _evaluate_gate_policy(
    forbidden_tokens: []
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.orchestration_policy_via_spec_lang
  target: summary_json
```
