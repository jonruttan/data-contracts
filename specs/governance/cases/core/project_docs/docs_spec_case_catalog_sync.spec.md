# Governance Cases

## DCGOV-DOCS-SPECCASE-002

```yaml contract-spec
id: DCGOV-DOCS-SPECCASE-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: spec case catalog artifacts are synchronized
purpose: Ensures generated spec case catalog and markdown references stay in sync.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.spec_case_catalog_sync
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
      - docs.spec_case_catalog_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
