# library.colocated_symbol_tests_required

```yaml contract-spec
id: SRGOV-LIB-SINGLE-002
title: library exports are referenced by executable tests
purpose: Ensures library exported symbols are exercised by colocated or downstream
  executable assertion/policy usage.
type: governance.check
check: library.colocated_symbol_tests_required
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
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
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```
