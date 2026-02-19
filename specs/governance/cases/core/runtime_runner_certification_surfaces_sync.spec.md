# Governance Cases

## DCGOV-RUNTIME-CERT-002

```yaml contract-spec
id: DCGOV-RUNTIME-CERT-002
title: runner certification command surfaces stay in sync
purpose: Ensures runner-certify command exists across canonical runtime surfaces.
type: contract.check
harness:
  root: .
  runner_certification_surfaces:
    files:
    - /dc-runner-rust/runner_adapter.sh
    - /dc-runner-rust/spec_runner_cli/src/main.rs
    - /specs/governance/cases/core/runtime_runner_interface_subcommands.spec.md
    required_tokens:
    - runner-certify
  check:
    profile: governance.scan
    config:
      check: runtime.runner_certification_surfaces_sync
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
```
