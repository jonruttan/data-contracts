# Governance Cases

## SRGOV-DOCS-OPER-002

```yaml contract-spec
id: SRGOV-DOCS-OPER-002
title: docs operability metric is non-regressing
purpose: Enforces monotonic non-regression for docs operability metrics against checked-in
  baseline.
type: contract.check
harness:
  root: .
  docs_operability_non_regression:
    baseline_path: /docs/spec/metrics/docs_operability_baseline.json
    summary_fields:
      overall_docs_operability_ratio: non_decrease
    segment_fields:
      book:
        mean_runnable_example_coverage_ratio: non_decrease
      contract:
        mean_token_sync_compliance_ratio: non_decrease
    epsilon: 1.0e-12
    docs_operability:
      reference_manifest: /docs/book/reference_manifest.yaml
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.operability_non_regression
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - docs.operability_non_regression
  target: summary_json
```
