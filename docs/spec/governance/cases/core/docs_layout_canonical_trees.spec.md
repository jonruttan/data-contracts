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
  spec_lang:
    includes:
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
      - docs.layout_canonical_trees
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
