# Governance Cases

## SRGOV-DOCS-GEN-022

```yaml spec-test
id: SRGOV-DOCS-GEN-022
title: stdlib symbols include examples
purpose: Ensures generated stdlib reference includes at least one complete example per symbol.
type: governance.check
check: docs.stdlib_examples_complete
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
      - docs.stdlib_examples_complete
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
