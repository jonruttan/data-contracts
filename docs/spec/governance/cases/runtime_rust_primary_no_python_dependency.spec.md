# Governance Cases

## SRGOV-RUST-PRIMARY-002

```yaml spec-test
id: SRGOV-RUST-PRIMARY-002
title: rust-primary gate scripts avoid direct python runner entrypoints
purpose: Ensures gate scripts stay runner-interface based and do not hardcode Python runner commands.
type: governance.check
check: runtime.runner_interface_gate_sync
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  runner_interface:
    required_paths:
    - scripts/runner_adapter.sh
    - scripts/rust/runner_adapter.sh
    files:
    - scripts/ci_gate.sh
    - scripts/docs_doctor.sh
    - scripts/core_gate.sh
    required_tokens:
    - SPEC_RUNNER_BIN
    - scripts/rust/runner_adapter.sh
    forbidden_tokens:
    - scripts/run_governance_specs.py
    - scripts/ci_gate_summary.py
    - scripts/evaluate_style.py --check docs/spec
    - scripts/conformance_purpose_report.py
    - scripts/compare_conformance_parity.py
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.runner_interface_gate_sync
```
