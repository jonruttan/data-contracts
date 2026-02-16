# Governance Cases

## SRGOV-POLICY-LIB-001

```yaml spec-test
id: SRGOV-POLICY-LIB-001
title: governance library-backed policy usage is non-regressing
purpose: Enforces monotonic non-regression for governance policy expressions that use shared
  spec-lang libraries.
type: governance.check
check: governance.policy_library_usage_non_regression
harness:
  root: .
  policy_library_usage_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      governance_library_backed_policy_ratio: non_decrease
    segment_fields:
      governance:
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
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - governance.policy_library_usage_non_regression
```
