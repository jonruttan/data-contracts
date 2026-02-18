# Governance Cases

## SRGOV-REF-SYMBOLS-003

```yaml contract-spec
id: SRGOV-REF-SYMBOLS-003
title: library exports are referenced
purpose: Ensures exported library symbols are referenced by case policies/expressions or harness
  exports.
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
      check: reference.library_exports_used
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
          - reference.library_exports_used
  target: summary_json
```
