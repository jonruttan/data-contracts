# Governance Cases

## DCGOV-POLICY-REQ-003

```yaml contract-spec
id: DCGOV-POLICY-REQ-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: governance checks require structured assertion targets
purpose: Ensures governance cases validate deterministic structured result targets instead
  of relying on PASS text markers as primary contract truth.
type: contract.check
harness:
  root: .
  structured_assertions:
    cases_path: /specs/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.structured_assertions_required
  check:
    profile: governance.scan
    config:
      check: governance.structured_assertions_required
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
      - governance.structured_assertions_required
    imports:
    - from: artifact
      names:
      - summary_json
```
