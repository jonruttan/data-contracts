# Governance Cases

## SRGOV-REF-SYMBOLS-001

```yaml contract-spec
id: SRGOV-REF-SYMBOLS-001
title: referenced library symbols resolve
purpose: Ensures harness.spec_lang exports and library symbols resolve deterministically.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: reference.symbols_exist
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - std.object.get:
            - {var: subject}
            - check_id
          - reference.symbols_exist
  target: summary_json
```
