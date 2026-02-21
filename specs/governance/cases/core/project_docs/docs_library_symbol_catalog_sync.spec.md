# Governance Cases

## DCGOV-DOCS-LIBSYM-004

```yaml contract-spec
id: DCGOV-DOCS-LIBSYM-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: library symbol catalog artifacts are synchronized
purpose: Ensures generated library symbol catalog and markdown references are up-to-date.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.library_symbol_catalog_sync
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
      - docs.library_symbol_catalog_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
