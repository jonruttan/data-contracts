# Governance Cases

## SRGOV-SPEC-MD-002

```yaml contract-spec
id: SRGOV-SPEC-MD-002
title: canonical executable trees forbid yaml and json case files
purpose: Ensures no runnable .spec.yaml, .spec.yml, or .spec.json files exist under canonical
  executable case roots.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: spec.no_executable_yaml_json_in_case_trees
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - spec.no_executable_yaml_json_in_case_trees
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
