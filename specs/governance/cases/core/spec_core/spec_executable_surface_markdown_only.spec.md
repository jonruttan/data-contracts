# Governance Cases

## DCGOV-SPEC-MD-001

```yaml contract-spec
id: DCGOV-SPEC-MD-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: executable spec surfaces are markdown only
purpose: Ensures all canonical executable case trees are authored as .spec.md and do not use
  runnable yaml/json case files.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.executable_surface_markdown_only
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
      - spec.executable_surface_markdown_only
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
