# Governance Cases

## SRGOV-SPEC-PORT-002

```yaml spec-test
id: SRGOV-SPEC-PORT-002
title: spec-lang self-containment metric is non-regressing
purpose: Enforces a monotonic ratchet so configured spec-lang self-containment metrics cannot decrease from baseline.
type: governance.check
check: spec.portability_non_regression
harness:
  root: .
  portability_non_regression:
    baseline_path: docs/spec/metrics/spec_portability_baseline.json
    summary_fields:
    - overall_logic_self_contained_ratio
    segment_fields:
      conformance:
      - mean_logic_self_contained_ratio
      governance:
      - mean_logic_self_contained_ratio
      impl:
      - mean_logic_self_contained_ratio
    epsilon: 1.0e-12
    portability_metric:
      roots:
      - docs/spec/conformance/cases
      - docs/spec/governance/cases
      - docs/spec/impl
      core_types:
      - text.file
      - cli.run
      segment_rules:
      - prefix: docs/spec/conformance/cases
        segment: conformance
      - prefix: docs/spec/governance/cases
        segment: governance
      - prefix: docs/spec/impl
        segment: impl
      runtime_capability_tokens:
      - api.http
      - governance.check
      runtime_capability_prefixes:
      - runtime.
      - php.
      - python.
      weights:
        non_evaluate_leaf_share: 0.45
        expect_impl_overlay: 0.25
        runtime_specific_capability: 0.15
        non_core_type: 0.15
      report:
        top_n: 10
      enforce: false
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - spec.portability_non_regression
```
