# Governance Cases

## SRGOV-NORM-002

```yaml spec-test
id: SRGOV-NORM-002
title: normalization enforces mapping-ast-only expression authoring
purpose: Ensures expression-bearing YAML fields remain mapping-AST only and normalized through the unified normalize check.
type: governance.check
check: normalization.mapping_ast_only
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: normalization.mapping_ast_only'
```
