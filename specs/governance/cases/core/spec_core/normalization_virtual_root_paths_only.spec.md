# Governance Cases

## DCGOV-NORM-PATHS-001

```yaml contract-spec
id: DCGOV-NORM-PATHS-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: scoped spec paths use canonical virtual-root form
purpose: Ensures path-bearing spec fields use canonical virtual-root `/...` form.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.virtual_root_paths_only
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
      - normalization.virtual_root_paths_only
```
