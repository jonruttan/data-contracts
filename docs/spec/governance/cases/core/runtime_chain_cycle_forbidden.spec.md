# Governance Cases

## SRGOV-CHAIN-002

```yaml contract-spec
id: SRGOV-CHAIN-002
title: chain cycles are forbidden
purpose: Ensures direct and indirect harness.chain dependency cycles are rejected.
type: governance.check
check: runtime.chain_cycle_forbidden
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
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
