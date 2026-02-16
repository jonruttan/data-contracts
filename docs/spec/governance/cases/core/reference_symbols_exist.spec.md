# Governance Cases

## SRGOV-REF-SYMBOLS-001

```yaml spec-test
id: SRGOV-REF-SYMBOLS-001
title: referenced library symbols resolve
purpose: Ensures harness.spec_lang exports and library symbols resolve deterministically.
type: governance.check
check: reference.symbols_exist
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
      - reference.symbols_exist
```
