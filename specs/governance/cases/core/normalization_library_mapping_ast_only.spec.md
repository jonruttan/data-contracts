# Governance Cases

## SRGOV-NORM-005

```yaml contract-spec
id: SRGOV-NORM-005
title: library function expressions use mapping-ast authoring
purpose: Enforces spec-lang library function defines use canonical mapping-ast expression
  syntax only.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.library_mapping_ast_only
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - normalization.library_mapping_ast_only
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```
