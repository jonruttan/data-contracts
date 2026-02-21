# Governance Cases

## DCGOV-REF-PATHS-001

```yaml contract-spec
id: DCGOV-REF-PATHS-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: contract paths referenced by specs exist
purpose: Ensures referenced contract-root paths fail fast when missing.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: reference.contract_paths_exist
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
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - reference.contract_paths_exist
```
