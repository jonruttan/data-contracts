# Governance Cases

## DCGOV-CHAIN-012

```yaml contract-spec
id: DCGOV-CHAIN-012
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain state sharing uses explicit exports only
purpose: Ensures chain state propagation is declared through explicit target-derived exports.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_exports_explicit_only
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
