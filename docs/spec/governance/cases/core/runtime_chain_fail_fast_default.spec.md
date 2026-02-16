# Governance Cases

## SRGOV-CHAIN-004

```yaml spec-test
id: SRGOV-CHAIN-004
title: chain fail_fast defaults stay canonical
purpose: Ensures harness.chain fail_fast and allow_continue fields preserve bool/default contracts.
type: governance.check
check: runtime.chain_fail_fast_default
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
