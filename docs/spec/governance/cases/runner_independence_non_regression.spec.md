# Governance Cases

## SRGOV-RUNTIME-INDEP-002

```yaml spec-test
id: SRGOV-RUNTIME-INDEP-002
title: runner independence metric is non-regressing
purpose: Enforces monotonic non-regression for runner independence metrics against checked-in baseline.
type: governance.check
check: runtime.runner_independence_non_regression
harness:
  root: .
  runner_independence_non_regression:
    baseline_path: docs/spec/metrics/runner_independence_baseline.json
    summary_fields:
      overall_runner_independence_ratio: non_decrease
      direct_runtime_invocation_count: non_increase
    segment_fields:
      gate_scripts:
        mean_runner_interface_usage_ratio: non_decrease
    epsilon: 1.0e-12
    runner_independence:
      segment_files:
        gate_scripts:
        - scripts/*.sh
        ci_workflows:
        - .github/workflows/*.yml
        adapter_interfaces:
        - scripts/runner_adapter.sh
        - scripts/rust/runner_adapter.sh
        - scripts/rust/spec_runner_cli/src/main.rs
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: runtime.runner_independence_non_regression'
```
