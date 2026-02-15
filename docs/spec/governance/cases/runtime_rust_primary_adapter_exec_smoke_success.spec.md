# Governance Cases

## SRGOV-RUST-PRIMARY-006

```yaml spec-test
id: SRGOV-RUST-PRIMARY-006
title: rust-primary adapter executes success-path smoke command deterministically
purpose: Ensures the Rust adapter can execute a supported success-path command with deterministic success output and exit-code behavior.
type: governance.check
check: runtime.rust_adapter_exec_smoke
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  rust_adapter_exec_smoke:
    command:
    - scripts/rust/runner_adapter.sh
    - style-check
    expected_exit_codes:
    - 0
    required_output_tokens:
    - 'OK: evaluate style formatting is canonical'
    forbidden_output_tokens:
    - unsupported runner adapter subcommand
    - rust runner adapter subcommand not yet implemented
    timeout_seconds: 180
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
      - runtime.rust_adapter_exec_smoke
```
