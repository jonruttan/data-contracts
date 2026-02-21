# Governance Cases

## DCGOV-SPEC-MD-002

```yaml contract-spec
id: DCGOV-SPEC-MD-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: canonical executable trees forbid yaml and json case files
purpose: Ensures no runnable .spec.yaml, .spec.yml, or .spec.json files exist under canonical
  executable case roots.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.no_executable_yaml_json_in_case_trees
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
      - spec.no_executable_yaml_json_in_case_trees
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
