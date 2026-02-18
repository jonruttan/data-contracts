# Governance Cases

## SRGOV-REF-SYMBOLS-002

```yaml contract-spec
id: SRGOV-REF-SYMBOLS-002
title: governance policy symbols resolve through declared libraries
purpose: Ensures every dotted var reference used in policy_evaluate resolves from
  declared library symbols.
type: governance.check
check: reference.policy_symbols_resolve
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
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.policy_symbols_resolve
  target: summary_json
```
