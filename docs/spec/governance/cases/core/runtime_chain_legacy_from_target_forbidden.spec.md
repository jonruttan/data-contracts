# runtime.chain_legacy_from_forbidden

```yaml contract-spec
id: SRGOV-CHAIN-FROM-002
title: chain exports forbid legacy from_target key
purpose: Ensures harness.chain step exports reject from_target and require from.
type: governance.check
check: runtime.chain_legacy_from_forbidden
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
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```
