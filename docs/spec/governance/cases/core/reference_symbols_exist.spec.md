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
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.symbols_exist
  target: summary_json
```
