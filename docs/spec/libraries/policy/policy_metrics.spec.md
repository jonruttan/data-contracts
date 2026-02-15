# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml spec-test
id: LIB-POLICY-002
title: policy-metrics reusable non-regression predicates
type: spec_lang.library
functions:
  policy.metric_non_decrease:
    fn:
    - {lit: [subject, field, baseline_field, epsilon]}
    - gte:
      - add:
        - get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - get:
        - {var: subject}
        - {var: baseline_field}
  policy.metric_non_increase:
    fn:
    - {lit: [subject, field, baseline_field, epsilon]}
    - lte:
      - sub:
        - get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - get:
        - {var: subject}
        - {var: baseline_field}
exports:
- policy.metric_non_decrease
- policy.metric_non_increase
```
