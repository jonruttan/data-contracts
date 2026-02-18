# Governance Cases

## SRGOV-IMPL-SPECLANG-002

```yaml contract-spec
id: SRGOV-IMPL-SPECLANG-002
title: impl evaluate-first ratio is non-regressing
purpose: Enforces ratchet-style non-regression for impl evaluate coverage against
  the checked-in spec-lang adoption baseline.
type: governance.check
check: impl.evaluate_ratio_non_regression
harness:
  root: .
  impl_evaluate_first_non_regression:
    baseline_path: /docs/spec/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      overall_logic_self_contained_ratio: non_decrease
    segment_fields:
      impl:
        mean_logic_self_contained_ratio: non_decrease
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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - impl.evaluate_ratio_non_regression
  target: summary_json
```
