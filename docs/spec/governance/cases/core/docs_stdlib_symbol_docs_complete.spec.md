# Governance Cases

## SRGOV-DOCS-GEN-021

```yaml spec-test
id: SRGOV-DOCS-GEN-021
title: stdlib symbols include semantic docs payload
purpose: Ensures every stdlib symbol has summary, params, returns, errors, and examples in
  generated catalogs.
type: governance.check
check: docs.stdlib_symbol_docs_complete
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
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.stdlib_symbol_docs_complete
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
