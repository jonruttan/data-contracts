# runtime.chain_library_symbol_exports_valid

```yaml contract-spec
id: DCGOV-CHAIN-FROM-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain assert function imports are valid
purpose: Ensures from=assert.function step imports include valid symbol path and contract
  shape.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_library_symbol_exports_valid
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
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
