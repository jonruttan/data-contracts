# Governance Cases

## SRGOV-SPEC-MD-002

```yaml spec-test
id: SRGOV-SPEC-MD-002
title: canonical executable trees forbid yaml and json case files
purpose: Ensures no runnable .spec.yaml, .spec.yml, or .spec.json files exist under canonical
  executable case roots.
type: governance.check
check: spec.no_executable_yaml_json_in_case_trees
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - spec.no_executable_yaml_json_in_case_trees
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
