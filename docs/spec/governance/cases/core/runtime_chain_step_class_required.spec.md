# Governance Cases

## SRGOV-CHAIN-007

```yaml spec-test
id: SRGOV-CHAIN-007
title: chain steps declare must can cannot class
purpose: Ensures harness.chain.steps[*].class is explicit and valid for all chained cases.
type: governance.check
check: runtime.chain_step_class_required
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
