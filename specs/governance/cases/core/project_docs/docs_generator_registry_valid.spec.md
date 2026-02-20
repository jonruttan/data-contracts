# Governance Cases

## DCGOV-DOCS-GEN-001

```yaml contract-spec
id: DCGOV-DOCS-GEN-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docs generator registry is valid and complete
purpose: Ensures docs generator registry exists, validates, and includes required surfaces.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.generator_registry_valid
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
      - docs.generator_registry_valid
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
