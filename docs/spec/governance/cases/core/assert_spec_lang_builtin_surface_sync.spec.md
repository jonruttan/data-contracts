# Governance Cases

## SRGOV-ASSERT-SYNC-005

```yaml contract-spec
id: SRGOV-ASSERT-SYNC-005
title: spec-lang builtin surface remains synced across contract and runners
purpose: Ensures builtin operators documented in the spec-lang contract are implemented in
  both Python and PHP runner evaluators.
type: contract.check
harness:
  root: .
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
      check: assert.spec_lang_builtin_surface_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
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
  target: summary_json
```
