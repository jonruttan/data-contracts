# Governance Cases

## SRGOV-RUNTIME-CONFIG-005

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-005
title: ci workflow exercises rust runner interface lane
purpose: Ensures CI runs core gate with SPEC_RUNNER_BIN set to the Rust adapter path.
type: governance.check
check: runtime.runner_interface_ci_lane
harness:
  root: .
  runner_interface_ci_lane:
    workflow: .github/workflows/ci.yml
    required_tokens:
      - "core-gate-rust-adapter:"
      - "SPEC_RUNNER_BIN: ./scripts/rust/runner_adapter.sh"
      - "run: ./scripts/core_gate.sh"
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.runner_interface_ci_lane"]
```
