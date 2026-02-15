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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - check_id
      - spec.no_executable_yaml_json_in_case_trees
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
