# Governance Cases

## DCGOV-CONTRACT-002

```yaml contract-spec
id: DCGOV-CONTRACT-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: contract must-rule coverage stays complete
purpose: Ensures all MUST policy rules remain covered by traceability evidence and keeps overall
  contract coverage above a minimum baseline.
type: contract.check
harness:
  root: .
  contract_coverage:
    require_all_must_covered: true
    min_coverage_ratio: 0.5
  check:
    profile: governance.scan
    config:
      check: contract.coverage_threshold
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
      - contract.coverage_threshold
    imports:
    - from: artifact
      names:
      - summary_json
```
