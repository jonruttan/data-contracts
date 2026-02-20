# Governance Cases

## DCGOV-DOCS-GEN-002

```yaml contract-spec
id: DCGOV-DOCS-GEN-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docs generator outputs are synchronized
purpose: Ensures all registry-backed docs generator outputs are up-to-date in check mode.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.generator_outputs_sync
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
      - docs.generator_outputs_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
