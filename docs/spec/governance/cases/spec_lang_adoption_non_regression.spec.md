# Governance Cases

## SRGOV-SPEC-LANG-002

```yaml spec-test
id: SRGOV-SPEC-LANG-002
title: spec-lang adoption metric is non-regressing
purpose: Enforces monotonic non-regression for spec-lang adoption metrics against checked-in baseline.
type: governance.check
check: spec.spec_lang_adoption_non_regression
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_adoption_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      overall_logic_self_contained_ratio: non_decrease
      native_logic_escape_case_ratio: non_increase
      governance_library_backed_policy_ratio: non_decrease
    segment_fields:
      conformance:
        mean_logic_self_contained_ratio: non_decrease
      governance:
        mean_logic_self_contained_ratio: non_decrease
        library_backed_policy_ratio: non_decrease
    epsilon: 1.0e-12
    spec_lang_adoption:
      roots:
      - /docs/spec/conformance/cases
      - /docs/spec/governance/cases
      - /docs/spec/impl
      segment_rules:
      - prefix: docs/spec/conformance/cases
        segment: conformance
      - prefix: docs/spec/governance/cases
        segment: governance
      - prefix: docs/spec/impl
        segment: impl
      recursive: true
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - spec.spec_lang_adoption_non_regression
```
