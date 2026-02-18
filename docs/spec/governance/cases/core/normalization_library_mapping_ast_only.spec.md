# Governance Cases

## SRGOV-NORM-005

```yaml contract-spec
id: SRGOV-NORM-005
title: library function expressions use mapping-ast authoring
purpose: Enforces spec-lang library function defines use canonical mapping-ast expression
  syntax only.
type: governance.check
check: normalization.library_mapping_ast_only
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
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - normalization.library_mapping_ast_only
  target: summary_json
```
