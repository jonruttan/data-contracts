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
  runner_interface_subcommands:
    path: /scripts/rust/runner_adapter.sh
    required_subcommands:
    - governance
    - style-check
    - normalize-check
    - normalize-fix
    - schema-registry-check
    - schema-registry-build
    - schema-docs-check
    - schema-docs-build
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
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.runner_interface_subcommands
```
