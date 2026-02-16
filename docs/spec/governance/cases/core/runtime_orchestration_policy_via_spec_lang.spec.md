# Governance Cases

## SRGOV-RUNTIME-ORCH-001

```yaml spec-test
id: SRGOV-RUNTIME-ORCH-001
title: gate orchestration verdict is policy-driven via spec-lang
purpose: Ensures CI gate summary determines final verdict using a spec-lang policy expression
  from governance config.
type: governance.check
check: runtime.orchestration_policy_via_spec_lang
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  orchestration_policy:
    files:
    - path: /scripts/ci_gate_summary.py
      required_tokens:
      - _load_gate_policy_expr(
      - eval_predicate(
      - policy_verdict
    - path: /docs/spec/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md
      required_tokens:
      - gate_policy
      - policy_evaluate
    forbidden_tokens: []
    policy_evaluate:
    - eq:
      - count:
        - filter:
          - fn:
            - [step]
            - neq:
              - get:
                - {var: step}
                - status
              - pass
          - {var: subject}
      - 0
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - runtime.orchestration_policy_via_spec_lang
```
