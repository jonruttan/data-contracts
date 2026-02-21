# Governance Cases

## DCGOV-DOCS-LAYOUT-004

```yaml contract-spec
id: DCGOV-DOCS-LAYOUT-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: active review assets live under docs/history/reviews
purpose: Enforces docs/history/reviews as canonical active review namespace while keeping historical review archives out of active workflow references.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.reviews_namespace_active
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
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - docs.reviews_namespace_active
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
