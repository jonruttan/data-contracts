# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml contract-spec
id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_decrease'
type: spec.export
contract:
- id: __export__policy.metric_non_decrease
  class: must
  asserts:
  - std.logic.gte:
    - std.math.add:
      - std.object.get:
        - var: subject
        - var: field
      - var: epsilon
    - std.object.get:
      - var: subject
      - var: baseline_field
harness:
  chain:
    exports:
    - as: policy.metric_non_decrease
      from: assert.function
      path: /__export__policy.metric_non_decrease
      params:
      - subject
      - field
      - baseline_field
      - epsilon
      required: true
```

```yaml contract-spec
id: LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_increase'
type: spec.export
contract:
- id: __export__policy.metric_non_increase
  class: must
  asserts:
  - std.logic.lte:
    - std.math.sub:
      - std.object.get:
        - var: subject
        - var: field
      - var: epsilon
    - std.object.get:
      - var: subject
      - var: baseline_field
harness:
  chain:
    exports:
    - as: policy.metric_non_increase
      from: assert.function
      path: /__export__policy.metric_non_increase
      params:
      - subject
      - field
      - baseline_field
      - epsilon
      required: true
```

```yaml contract-spec
id: LIB-POLICY-002-900-POLICY-METRIC-SMOKE
title: policy metric helpers execute as colocated executable checks
type: text.file
harness:
  chain:
    steps:
    - id: lib_non_decrease
      class: must
      ref: '#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE'
    - id: lib_non_increase
      class: must
      ref: '#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE'
    imports:
    - from: lib_non_decrease
      names:
      - policy.metric_non_decrease
    - from: lib_non_increase
      names:
      - policy.metric_non_increase
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - call:
      - var: policy.metric_non_decrease
      - lit:
          current: 10
          baseline: 9
      - current
      - baseline
      - 0
    - call:
      - var: policy.metric_non_increase
      - lit:
          current: 8
          baseline: 9
      - current
      - baseline
      - 0
  target: text
```
