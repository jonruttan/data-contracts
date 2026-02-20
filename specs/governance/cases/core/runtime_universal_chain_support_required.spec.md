# Governance Cases

## DCGOV-CHAIN-010

```yaml contract-spec
id: DCGOV-CHAIN-010
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: universal chain support is present in dispatcher
purpose: Ensures all executable task types execute through shared harness.chain orchestration
  in dispatcher.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.universal_chain_support_required
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
