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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
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
      - normalization.mapping_ast_only
```
