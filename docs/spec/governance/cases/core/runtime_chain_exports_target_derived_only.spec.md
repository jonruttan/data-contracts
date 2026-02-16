# Governance Cases

## SRGOV-CHAIN-003

```yaml spec-test
id: SRGOV-CHAIN-003
title: chain exports remain target-derived only
purpose: Ensures harness.chain step exports declare only explicit target-derived extraction
  keys.
type: governance.check
check: runtime.chain_exports_target_derived_only
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
