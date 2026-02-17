# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml spec-test
id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_decrease'
type: spec_lang.export
defines:
  public:
    policy.metric_non_decrease:
      fn:
      - [subject, field, baseline_field, epsilon]
      - std.logic.gte:
        - std.math.add:
          - std.object.get:
            - {var: subject}
            - {var: field}
          - {var: epsilon}
        - std.object.get:
          - {var: subject}
          - {var: baseline_field}
```

```yaml spec-test
id: LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_increase'
type: spec_lang.export
defines:
  public:
    policy.metric_non_increase:
      fn:
      - [subject, field, baseline_field, epsilon]
      - std.logic.lte:
        - std.math.sub:
          - std.object.get:
            - {var: subject}
            - {var: field}
          - {var: epsilon}
        - std.object.get:
          - {var: subject}
          - {var: baseline_field}
```

```yaml spec-test
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
assert:
- id: assert_1
  class: must
  checks:
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
