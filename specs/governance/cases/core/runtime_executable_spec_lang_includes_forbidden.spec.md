# runtime.executable_spec_lang_includes_forbidden

```yaml contract-spec
id: DCGOV-CHAIN-FROM-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: executable cases forbid spec_lang includes
purpose: Ensures executable case types do not use harness.spec_lang.includes and load symbols
  through harness.chain.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.executable_spec_lang_includes_forbidden
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
