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
      - runtime.runner_interface_subcommands
```
