# runtime.chain_legacy_from_target_forbidden

```yaml spec-test
id: SRGOV-CHAIN-FROM-002
title: chain exports forbid legacy from_target key
purpose: Ensures harness.chain step exports reject from_target and require from.
type: governance.check
check: runtime.chain_legacy_from_target_forbidden
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
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
  target: summary_json
```
