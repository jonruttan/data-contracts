# Governance Cases

## SRGOV-CHAIN-002

```yaml spec-test
id: SRGOV-CHAIN-002
title: chain cycles are forbidden
purpose: Ensures direct and indirect harness.chain dependency cycles are rejected.
type: governance.check
check: runtime.chain_cycle_forbidden
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```
