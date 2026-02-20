# Governance Cases

## DCGOV-DOCS-REF-013

```yaml contract-spec
id: DCGOV-DOCS-REF-013
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: review snapshot template matches canonical contract
purpose: Ensures docs/history/reviews template enforces canonical section order, table headers, and candidate schema scaffolding.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.review_snapshot_template_contract_sync
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
      - docs.review_snapshot_template_contract_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
