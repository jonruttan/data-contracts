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
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.stdlib_symbol_docs_complete
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
