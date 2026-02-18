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
      - conformance.evaluate_first_ratio_non_regression
  target: summary_json
```
