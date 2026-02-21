# Governance Cases

## DCGOV-DOCS-LIBSYM-003

```yaml contract-spec
id: DCGOV-DOCS-LIBSYM-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: library symbol docs include examples
purpose: Ensures each exported symbol has at least one structured documentation example.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.library_symbol_examples_present
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
      - docs.library_symbol_examples_present
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
