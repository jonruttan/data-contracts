# Governance Cases

## DCGOV-DOCS-LIBSYM-002

```yaml contract-spec
id: DCGOV-DOCS-LIBSYM-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: library symbol doc params stay in sync
purpose: Ensures harness.exports params match doc.params names and order.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.library_symbol_params_sync
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
      - docs.library_symbol_params_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
