# Governance Cases

## SRGOV-DOCS-LAYOUT-001

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-001
title: docs layout canonical trees exist
purpose: Enforces canonical docs root namespaces.
type: governance.check
check: docs.layout_canonical_trees
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.layout_canonical_trees
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
