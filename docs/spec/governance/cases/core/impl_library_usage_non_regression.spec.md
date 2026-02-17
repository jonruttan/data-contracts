# Governance Cases

## SRGOV-IMPL-SPECLANG-003

```yaml spec-test
id: SRGOV-IMPL-SPECLANG-003
title: impl library-backed assertion usage is non-regressing
purpose: Enforces monotonic non-regression for impl case wiring to shared spec-lang helper
  libraries.
type: governance.check
check: impl.library_usage_non_regression
harness:
  root: .
  impl_library_usage_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      impl_library_backed_case_ratio: non_decrease
    segment_fields:
      impl:
        library_backed_case_ratio: non_decrease
    epsilon: 1.0e-12
    spec_lang_adoption:
      roots:
      - /docs/spec/impl
      segment_rules:
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
      - impl.library_usage_non_regression
  target: summary_json
```
