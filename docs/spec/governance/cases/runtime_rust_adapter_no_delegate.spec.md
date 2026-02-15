# Governance Cases

## SRGOV-RUNTIME-CONFIG-006

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-006
title: rust adapter does not delegate to python shell adapter
purpose: Ensures scripts/rust/runner_adapter.sh invokes the Rust CLI directly and does not call scripts/runner_adapter.sh.
type: governance.check
check: runtime.rust_adapter_no_delegate
harness:
  root: .
  rust_adapter:
    path: scripts/rust/runner_adapter.sh
    required_tokens:
      - "spec_runner_cli"
      - "cargo run --quiet"
    forbidden_tokens:
      - "scripts/runner_adapter.sh"
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.rust_adapter_no_delegate"]
```
