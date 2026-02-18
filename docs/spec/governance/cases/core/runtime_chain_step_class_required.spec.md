# Governance Cases

## SRGOV-CHAIN-007

```yaml contract-spec
id: SRGOV-CHAIN-007
title: chain steps declare must can cannot class
purpose: Ensures harness.chain.steps[*].class is explicit and valid for all chained
  cases.
type: governance.check
check: runtime.chain_step_class_required
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
