# Governance Cases

## DCGOV-DOCS-GEN-006

```yaml contract-spec
id: DCGOV-DOCS-GEN-006
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: spec lang builtin catalog artifacts are synchronized
purpose: Ensures generated spec-lang builtin JSON and markdown artifacts are up-to-date.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.spec_lang_builtin_catalog_sync
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
      - docs.spec_lang_builtin_catalog_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
