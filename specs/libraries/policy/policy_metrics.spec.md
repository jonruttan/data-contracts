# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml contract-spec
id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_decrease'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__policy.metric_non_decrease
    assert:
      std.logic.gte:
      - std.math.add:
        - std.object.get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - std.object.get:
        - {var: subject}
        - {var: baseline_field}
harness:
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
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__policy.metric_non_increase
    assert:
      std.logic.lte:
      - std.math.sub:
        - std.object.get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - std.object.get:
        - {var: subject}
        - {var: baseline_field}
harness:
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
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: '#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE'
    as: lib_non_decrease
    symbols:
    - policy.metric_non_decrease
  - ref: '#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE'
    as: lib_non_increase
    symbols:
    - policy.metric_non_increase
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': text
    assert:
    - call:
      - {var: policy.metric_non_decrease}
      - lit:
          current: 10
          baseline: 9
      - current
      - baseline
      - 0
    - call:
      - {var: policy.metric_non_increase}
      - lit:
          current: 8
          baseline: 9
      - current
      - baseline
      - 0
```
