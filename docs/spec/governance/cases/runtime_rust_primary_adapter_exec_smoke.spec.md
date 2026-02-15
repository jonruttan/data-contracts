# Governance Cases

## SRGOV-RUST-PRIMARY-005

```yaml spec-test
id: SRGOV-RUST-PRIMARY-005
title: rust-primary adapter executes and returns deterministic smoke output
purpose: Ensures the Rust adapter is executable in governance and emits deterministic output/exit-code behavior for a smoke command.
type: governance.check
check: runtime.rust_adapter_exec_smoke
harness:
  root: .
  rust_adapter_exec_smoke:
    command:
      - scripts/rust/runner_adapter.sh
      - lint
    expected_exit_codes: [0]
    required_output_tokens: []
    forbidden_output_tokens:
      - "scripts/runner_adapter.sh"
    timeout_seconds: 180
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.rust_adapter_exec_smoke"]
```
