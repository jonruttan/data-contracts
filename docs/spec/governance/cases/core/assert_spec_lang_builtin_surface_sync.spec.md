# Governance Cases

## SRGOV-ASSERT-SYNC-005

```yaml spec-test
id: SRGOV-ASSERT-SYNC-005
title: spec-lang builtin surface remains synced across contract and runners
purpose: Ensures builtin operators documented in the spec-lang contract are implemented in
  both Python and PHP runner evaluators.
type: governance.check
check: assert.spec_lang_builtin_surface_sync
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_builtin_sync:
    required_ops:
    - mul
    - div
    - mod
    - pow
    - abs
    - negate
    - inc
    - dec
    - clamp
    - round
    - floor
    - ceil
    - compare
    - between
    - xor
    - slice
    - reverse
    - zip
    - zip_with
    - range
    - repeat
    - keys
    - values
    - entries
    - merge
    - assoc
    - dissoc
    - pick
    - omit
    - prop_eq
    - where
    - compose
    - pipe
    - identity
    - always
    - replace
    - pad_left
    - pad_right
    - is_null
    - is_bool
    - is_number
    - is_string
    - is_list
    - is_dict
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - assert.spec_lang_builtin_surface_sync
```
