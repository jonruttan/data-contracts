# Governance Cases

## SRGOV-DOCS-OPER-002

```yaml spec-test
id: SRGOV-DOCS-OPER-002
title: docs operability metric is non-regressing
purpose: Enforces monotonic non-regression for docs operability metrics against checked-in baseline.
type: governance.check
check: docs.operability_non_regression
harness:
  root: .
  docs_operability_non_regression:
    baseline_path: docs/spec/metrics/docs_operability_baseline.json
    summary_fields:
      overall_docs_operability_ratio: non_decrease
    segment_fields:
      book:
        mean_runnable_example_coverage_ratio: non_decrease
      contract:
        mean_token_sync_compliance_ratio: non_decrease
    epsilon: 1.0e-12
    docs_operability:
      reference_manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - docs.operability_non_regression
```
