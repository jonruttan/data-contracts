# Governance Cases

## DCGOV-CONF-TYPE-001

```yaml contract-spec
id: DCGOV-CONF-TYPE-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: conformance case types have matching type contract docs
purpose: Ensures each type used by portable conformance fixtures is documented under the type-contract
  index.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.type_contract_docs
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
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - conformance.type_contract_docs
    imports:
    - from: artifact
      names:
      - summary_json
```
