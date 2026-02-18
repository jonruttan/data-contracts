# Governance Cases

## SRGOV-CHAIN-004

```yaml contract-spec
id: SRGOV-CHAIN-004
title: chain fail_fast defaults stay canonical
purpose: Ensures harness.chain fail_fast and allow_continue fields preserve bool/default
  contracts.
type: governance.check
check: runtime.chain_fail_fast_default
harness:
  root: .
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
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
