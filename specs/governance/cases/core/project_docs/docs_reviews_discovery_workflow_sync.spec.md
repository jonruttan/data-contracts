# Governance Cases

## DCGOV-DOCS-REF-027

```yaml contract-spec
id: DCGOV-DOCS-REF-027
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: discovery review workflow is documented and synced
purpose: Ensures docs/history/reviews README documents scaffold, validate, and pending-conversion flow for the discovery prompt.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.reviews_discovery_workflow_sync
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
      - docs.reviews_discovery_workflow_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
