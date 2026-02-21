# Governance Cases

## DCGOV-CONF-SPECLANG-002

```yaml contract-spec
id: DCGOV-CONF-SPECLANG-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: conformance evaluate-first ratio is non-regressing
purpose: Enforces ratchet-style non-regression for conformance evaluate coverage against the
  checked-in spec-lang adoption baseline.
type: contract.check
harness:
  root: .
  conformance_evaluate_first_non_regression:
    baseline_path: /specs/governance/metrics/spec_lang_adoption_baseline.json
    segment_fields:
      conformance:
        mean_logic_self_contained_ratio: non_decrease
    epsilon: 1.0e-12
    spec_lang_adoption:
      roots:
      - /specs/conformance/cases
      segment_rules:
      - prefix: specs/conformance/cases
        segment: conformance
      recursive: true
  check:
    profile: governance.scan
    config:
      check: conformance.evaluate_first_ratio_non_regression
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - conformance.evaluate_first_ratio_non_regression
    imports:
    - from: artifact
      names:
      - summary_json
```
