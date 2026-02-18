# Governance Cases

## SRGOV-RUNTIME-INDEP-002

```yaml spec-test
id: SRGOV-RUNTIME-INDEP-002
title: runner independence metric is non-regressing
purpose: Enforces monotonic non-regression for runner independence metrics against checked-in
  baseline.
type: governance.check
check: runtime.runner_independence_non_regression
harness:
  root: .
  runner_independence_non_regression:
    baseline_path: /docs/spec/metrics/runner_independence_baseline.json
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
        - scripts/ci_gate.sh
        - scripts/core_gate.sh
        - scripts/docs_doctor.sh
        ci_workflows:
        - .github/workflows/*.yml
        adapter_interfaces:
        - scripts/runner_adapter.sh
        - scripts/rust/runner_adapter.sh
        - scripts/rust/spec_runner_cli/src/main.rs
      direct_runtime_token_segments:
      - gate_scripts
      - ci_workflows
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
      - runtime.runner_independence_non_regression
  target: summary_json
```
