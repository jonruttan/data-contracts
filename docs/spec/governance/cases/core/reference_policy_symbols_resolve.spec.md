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
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.policy_symbols_resolve
  target: summary_json
```
