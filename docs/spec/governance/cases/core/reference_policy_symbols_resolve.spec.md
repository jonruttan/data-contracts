# Governance Cases

## SRGOV-REF-SYMBOLS-002

```yaml spec-test
id: SRGOV-REF-SYMBOLS-002
title: governance policy symbols resolve through declared libraries
purpose: Ensures every dotted var reference used in policy_evaluate resolves from declared
  library symbols.
type: governance.check
check: reference.policy_symbols_resolve
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
      - reference.policy_symbols_resolve
```
