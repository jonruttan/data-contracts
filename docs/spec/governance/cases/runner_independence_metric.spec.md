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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
      - {has_key: [{ref: subject}, summary]}
      - {has_key: [{ref: subject}, segments]}
      - has_key:
        - {get: [{ref: subject}, summary]}
        - overall_runner_independence_ratio
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - runtime.runner_independence_metric
```
