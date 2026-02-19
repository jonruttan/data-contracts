# Governance Cases

## SRGOV-RUST-PRIMARY-003

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-003
title: rust-primary adapter keeps required runner-interface subcommands
purpose: Ensures Rust-primary operation preserves required runner-interface subcommand compatibility.
type: contract.check
harness:
  root: .
  runner_interface_subcommands:
    path: /runners/rust/runner_adapter.sh
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
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_subcommands
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
