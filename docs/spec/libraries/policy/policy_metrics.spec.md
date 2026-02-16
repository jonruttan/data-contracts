# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml spec-test
id: LIB-POLICY-002
title: policy-metrics reusable non-regression predicates
type: spec_lang.library
defines:
  private:
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
