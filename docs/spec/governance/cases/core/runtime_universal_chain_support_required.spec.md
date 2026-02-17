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
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
