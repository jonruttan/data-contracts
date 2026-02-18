# Governance Cases

## SRGOV-ASSERT-CORE-001

```yaml contract-spec
id: SRGOV-ASSERT-CORE-001
title: assertion docs define universal evaluate core
purpose: Ensures schema and contract docs consistently define evaluate as the universal
  assertion core and classify other operators as authoring sugar.
type: governance.check
check: assert.universal_core_sync
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
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - assert.universal_core_sync
  target: summary_json
```
