# Governance Cases

## SRGOV-POLICY-LIB-001

```yaml contract-spec
id: SRGOV-POLICY-LIB-001
title: governance library-backed policy usage is non-regressing
purpose: Enforces monotonic non-regression for governance policy expressions that use shared
  spec-lang libraries.
type: contract.check
harness:
  root: .
  policy_library_usage_non_regression:
    baseline_path: /specs/metrics/spec_lang_adoption_baseline.json
    summary_fields:
      governance_library_backed_policy_ratio: non_decrease
    segment_fields:
      governance:
        library_backed_policy_ratio: non_decrease
    epsilon: 1.0e-12
    spec_lang_adoption:
      roots:
      - /specs/conformance/cases
      - /specs/governance/cases
      - /specs/impl
      segment_rules:
      - prefix: specs/conformance/cases
        segment: conformance
      - prefix: specs/governance/cases
        segment: governance
      - prefix: specs/impl
        segment: impl
      recursive: true
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: governance.policy_library_usage_non_regression
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
