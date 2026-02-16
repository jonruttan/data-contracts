# Governance Cases

## SRGOV-CHAIN-009

```yaml spec-test
id: SRGOV-CHAIN-009
title: chain contract uses harness.chain only
purpose: Ensures chain declarations appear only at harness.chain and not in alternate top-level
  or type-specific locations.
type: governance.check
check: runtime.chain_contract_single_location
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
