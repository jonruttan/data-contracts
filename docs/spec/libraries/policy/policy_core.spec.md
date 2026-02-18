# Spec-Lang Policy Core Library

## LIB-POLICY-001

```yaml contract-spec
id: LIB-POLICY-001
title: policy-core reusable governance predicates
type: spec.export
contract:
- id: __export__policy.pass_when_no_violations
  class: must
  asserts:
  - std.collection.is_empty:
    - std.object.get:
      - var: subject
      - violations
- id: __export__policy.fail_when_has_violations
  class: must
  asserts:
  - std.logic.not:
    - call:
      - var: policy.pass_when_no_violations
      - var: subject
- id: __export__policy.check_id_is
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - var: expected
- id: __export__policy.violation_count_is
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - violation_count
    - var: expected
harness:
  chain:
    exports:
    - as: policy.pass_when_no_violations
      from: assert.function
      path: /__export__policy.pass_when_no_violations
      params:
      - subject
      required: true
    - as: policy.fail_when_has_violations
      from: assert.function
      path: /__export__policy.fail_when_has_violations
      params:
      - subject
      required: true
    - as: policy.check_id_is
      from: assert.function
      path: /__export__policy.check_id_is
      params:
      - subject
      - expected
      required: true
    - as: policy.violation_count_is
      from: assert.function
      path: /__export__policy.violation_count_is
      params:
      - subject
      - expected
      required: true
```
