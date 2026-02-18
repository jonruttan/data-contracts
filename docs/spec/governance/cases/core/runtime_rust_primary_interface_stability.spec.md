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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_subcommands
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
