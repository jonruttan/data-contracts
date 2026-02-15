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
      - runtime.runner_independence_metric
```
