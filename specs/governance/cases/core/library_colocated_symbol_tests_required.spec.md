# library.colocated_symbol_tests_required

```yaml contract-spec
id: SRGOV-LIB-SINGLE-002
title: library exports are referenced by executable tests
purpose: Ensures library exported symbols are exercised by colocated or downstream executable
  assertion/policy usage.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: library.colocated_symbol_tests_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
