# Governance Cases

## SRGOV-RUNTIME-CONFIG-004

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-004
title: rust runner adapter declares required interface subcommands
purpose: Ensures the Rust runner adapter exposes the required runner interface subcommand labels.
type: governance.check
check: runtime.runner_interface_subcommands
harness:
  root: .
  runner_interface_subcommands:
    path: scripts/rust/runner_adapter.sh
    required_subcommands:
    - governance
    - style-check
    - lint
    - typecheck
    - compilecheck
    - conformance-purpose-json
    - conformance-purpose-md
    - spec-portability-json
    - spec-portability-md
    - docs-build
    - docs-build-check
    - docs-lint
    - docs-graph
    - conformance-parity
    - test-core
    - test-full
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: runtime.runner_interface_subcommands'
```
