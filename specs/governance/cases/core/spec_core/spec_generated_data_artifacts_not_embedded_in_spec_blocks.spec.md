# Governance Cases

## DCGOV-SPEC-MD-004

```yaml contract-spec
id: DCGOV-SPEC-MD-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: generated data artifacts do not embed executable spec blocks
purpose: Ensures machine-native yaml and json data artifact surfaces remain non-executable
  and do not contain yaml contract-spec fences.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.generated_data_artifacts_not_embedded_in_spec_blocks
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
      - spec.generated_data_artifacts_not_embedded_in_spec_blocks
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
