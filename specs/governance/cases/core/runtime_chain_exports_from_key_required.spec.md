# runtime.chain_exports_from_key_required

```yaml contract-spec
id: DCGOV-CHAIN-FROM-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain exports use canonical from key
purpose: Ensures harness.chain step exports declare the required from field and do not rely
  on non-canonical key forms.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_exports_from_key_required
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
