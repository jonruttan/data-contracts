# Governance Cases

## DCGOV-DOCS-GEN-022

```yaml contract-spec
id: DCGOV-DOCS-GEN-022
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: stdlib symbols include examples
purpose: Ensures generated stdlib reference includes at least one complete example per symbol.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.stdlib_examples_complete
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
      - docs.stdlib_examples_complete
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
