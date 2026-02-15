# Governance Cases

## SRGOV-CONF-SPECLANG-002

```yaml spec-test
id: SRGOV-CONF-SPECLANG-002
title: conformance evaluate-first ratio is non-regressing
purpose: Enforces ratchet-style non-regression for conformance evaluate coverage against the
  checked-in spec-lang adoption baseline.
type: governance.check
check: conformance.evaluate_first_ratio_non_regression
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  conformance_evaluate_first_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    segment_fields:
      conformance:
        mean_logic_self_contained_ratio: non_decrease
    epsilon: 1.0e-12
    spec_lang_adoption:
      roots:
      - /docs/spec/conformance/cases
      segment_rules:
      - prefix: docs/spec/conformance/cases
        segment: conformance
      recursive: true
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - conformance.evaluate_first_ratio_non_regression
```
