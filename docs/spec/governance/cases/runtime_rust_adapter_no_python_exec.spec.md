# Governance Cases

## SRGOV-RUST-PRIMARY-008

```yaml spec-test
id: SRGOV-RUST-PRIMARY-008
title: rust runner interface avoids direct python execution tokens
purpose: Ensures the Rust runner interface implementation does not hardcode direct python executable invocation.
type: governance.check
check: runtime.rust_adapter_no_python_exec
harness:
  root: .
  rust_no_python_exec:
    path: scripts/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
      - "python3"
      - "PYTHON_BIN"
      - "resolve_python_bin"
      - "scripts/run_governance_specs.py"
  policy_evaluate:
    - ["eq", true, true]
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.rust_adapter_no_python_exec"]
```
