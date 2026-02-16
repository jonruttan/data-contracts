# Governance Cases

## SRGOV-CHAIN-010

```yaml spec-test
id: SRGOV-CHAIN-010
title: universal chain support is present in dispatcher
purpose: Ensures all executable task types execute through shared harness.chain orchestration
  in dispatcher.
type: governance.check
check: runtime.universal_chain_support_required
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
