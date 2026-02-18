# Governance Cases

## SRGOV-RUNTIME-TRIAGE-016

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-016
title: default ci gate excludes report-generation commands
purpose: Ensures ci-gate-summary default step list does not include report-generation command
  invocations.
type: governance.check
check: runtime.ci_gate_default_report_commands_forbidden
harness:
  root: .
  ci_gate_default_reports_forbidden:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
    - spec_portability_json
    - spec_portability_md
    - spec_lang_adoption_json
    - spec_lang_adoption_md
    - runner_independence_json
    - runner_independence_md
    - python_dependency_json
    - python_dependency_md
    - docs_operability_json
    - docs_operability_md
    - contract_assertions_json
    - contract_assertions_md
    - objective_scorecard_json
    - objective_scorecard_md
    - spec_lang_stdlib_json
    - spec_lang_stdlib_md
    - conformance_purpose_json
    - conformance_purpose_md
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
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
```
