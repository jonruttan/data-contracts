# Governance Cases

## SRGOV-SPEC-LANG-002

```yaml spec-test
id: SRGOV-SPEC-LANG-002
title: spec-lang adoption metric is non-regressing
purpose: Enforces monotonic non-regression for spec-lang adoption metrics against checked-in
  baseline.
type: governance.check
check: spec.spec_lang_adoption_non_regression
harness:
  root: .
  spec_lang_adoption_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      overall_logic_self_contained_ratio: non_decrease
      native_logic_escape_case_ratio: non_increase
      governance_library_backed_policy_ratio: non_decrease
      governance_symbol_resolution_ratio: non_decrease
      library_public_surface_ratio: non_decrease
    segment_fields:
      conformance:
        mean_logic_self_contained_ratio: non_decrease
      governance:
        mean_logic_self_contained_ratio: non_decrease
        library_backed_policy_ratio: non_decrease
        governance_symbol_resolution_ratio: non_decrease
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
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - spec.spec_lang_adoption_non_regression
  target: summary_json
```
