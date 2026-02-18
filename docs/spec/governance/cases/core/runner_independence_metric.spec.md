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
      - scripts/python/runner_adapter.sh
      - scripts/rust/runner_adapter.sh
      - scripts/rust/spec_runner_cli/src/main.rs
    direct_runtime_token_segments:
    - gate_scripts
    - ci_workflows
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - {var: subject}
        - segments
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - overall_runner_independence_ratio
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
      - runtime.runner_independence_metric
  target: summary_json
```
