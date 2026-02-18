# Governance Cases

## SRGOV-DOCS-LAYOUT-001

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-001
title: docs layout canonical trees exist
purpose: Enforces canonical docs root namespaces.
type: governance.check
check: docs.layout_canonical_trees
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
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.layout_canonical_trees
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
