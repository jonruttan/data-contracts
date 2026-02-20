# Governance Cases

## DCGOV-CHAIN-006

```yaml contract-spec
id: DCGOV-CHAIN-006
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain refs use canonical scalar format
purpose: Ensures harness.chain step refs are scalar [path][#case_id] values and reject non-canonical
  mapping form.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_ref_scalar_required
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
