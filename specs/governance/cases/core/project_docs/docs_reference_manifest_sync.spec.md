# Governance Cases

## DCGOV-DOCS-QUAL-002

```yaml contract-spec
id: DCGOV-DOCS-QUAL-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: reference index is generated from manifest
purpose: Ensures reference index markdown remains synchronized with the manifest source of
  truth.
type: contract.check
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: /docs/book/reference_index.md
  check:
    profile: governance.scan
    config:
      check: docs.reference_manifest_sync
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
      - docs.reference_manifest_sync
    imports:
    - from: artifact
      names:
      - summary_json
```
