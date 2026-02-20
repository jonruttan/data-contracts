# library.colocated_symbol_tests_required

```yaml contract-spec
id: DCGOV-LIB-SINGLE-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
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
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
