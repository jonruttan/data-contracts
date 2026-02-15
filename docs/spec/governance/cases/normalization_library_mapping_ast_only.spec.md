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
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - normalization.library_mapping_ast_only
```
