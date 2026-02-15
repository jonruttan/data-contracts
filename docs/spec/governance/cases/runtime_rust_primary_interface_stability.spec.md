# Governance Cases

## SRGOV-RUST-PRIMARY-003

```yaml spec-test
id: SRGOV-RUST-PRIMARY-003
title: rust-primary adapter keeps required runner-interface subcommands
purpose: Ensures Rust-primary operation preserves required runner-interface subcommand compatibility.
type: governance.check
check: runtime.runner_interface_subcommands
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
    - runner-independence-json
    - runner-independence-md
    - python-dependency-json
    - python-dependency-md
    - ci-gate-summary
    - docs-build
    - docs-build-check
    - docs-lint
    - docs-graph
    - conformance-parity
    - test-core
    - test-full
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
      - runtime.runner_interface_subcommands
```
