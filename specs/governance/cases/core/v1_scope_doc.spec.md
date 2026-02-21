# Governance Cases

## DCGOV-DOC-V1-001

```yaml contract-spec
id: DCGOV-DOC-V1-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: v1 scope contract doc exists and includes required sections
purpose: Ensures v1 scope and compatibility commitments remain explicit and discoverable.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.v1_scope_contract
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
      - docs.v1_scope_contract
    imports:
    - from: artifact
      names:
      - summary_json
```
