# Governance Cases

## SRGOV-RUNTIME-INDEP-001

```yaml spec-test
id: SRGOV-RUNTIME-INDEP-001
title: runner independence metric report generation is valid
purpose: Ensures runtime runner-independence report generation and shape are valid.
type: governance.check
check: runtime.runner_independence_metric
harness:
  root: .
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
    - and:
      - has_key:
        - subject: []
        - summary
      - has_key:
        - subject: []
        - segments
      - has_key:
        - get:
          - subject: []
          - summary
        - overall_runner_independence_ratio
assert:
- target: text
  must:
  - contain:
    - 'PASS: runtime.runner_independence_metric'
```
