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
    - std.math.mul
    - std.math.div
    - std.math.mod
    - std.math.pow
    - std.math.abs
    - std.math.negate
    - std.math.inc
    - std.math.dec
    - std.math.clamp
    - std.math.round
    - std.math.floor
    - std.math.ceil
    - std.logic.compare
    - std.logic.between
    - std.logic.xor
    - std.collection.slice
    - std.collection.reverse
    - std.collection.zip
    - std.collection.zip_with
    - std.math.range
    - std.collection.repeat
    - std.object.keys
    - std.object.values
    - std.object.entries
    - std.object.merge
    - std.object.assoc
    - std.object.dissoc
    - std.object.pick
    - std.object.omit
    - std.object.prop_eq
    - std.object.where
    - std.fn.compose
    - std.fn.pipe
    - std.fn.identity
    - std.fn.always
    - std.string.replace
    - std.string.pad_left
    - std.string.pad_right
    - std.type.is_null
    - std.type.is_bool
    - std.type.is_number
    - std.type.is_string
    - std.type.is_list
    - std.type.is_dict
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - assert.spec_lang_builtin_surface_sync
```
