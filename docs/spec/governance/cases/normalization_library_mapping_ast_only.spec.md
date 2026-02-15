# Governance Cases

## SRGOV-NORM-005

```yaml spec-test
id: SRGOV-NORM-005
title: library function expressions use mapping-ast authoring
purpose: Enforces spec-lang library function definitions use canonical mapping-ast expression syntax only.
type: governance.check
check: normalization.library_mapping_ast_only
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - normalization.library_mapping_ast_only
```
