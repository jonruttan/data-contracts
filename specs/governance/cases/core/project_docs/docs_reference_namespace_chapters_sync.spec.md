# Governance Cases

## DCGOV-DOCS-GEN-025

```yaml contract-spec
id: DCGOV-DOCS-GEN-025
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: spec lang namespace chapters are present and manifest-synced
purpose: Ensures generated namespace chapter files exist and are listed in the book manifest.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.reference_namespace_chapters_sync
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
      - docs.reference_namespace_chapters_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
