# Governance Cases

## DCGOV-CHAIN-004

```yaml contract-spec
id: DCGOV-CHAIN-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain fail_fast defaults stay canonical
purpose: Ensures harness.chain fail_fast and allow_continue fields preserve bool/default contracts.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_fail_fast_default
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
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```
