# Governance Cases

## SRGOV-RUNTIME-ENTRY-004

```yaml contract-spec
id: SRGOV-RUNTIME-ENTRY-004
title: public docs do not instruct direct rust adapter invocation
purpose: Ensures public docs point to the canonical adapter entrypoint rather than internal
  rust adapter paths.
type: contract.check
harness:
  root: .
  public_docs:
    files:
    - /README.md
    - /docs/development.md
    - /specs/current.md
    - /specs/contract/12_runner_interface.md
    - /specs/contract/16_rust_primary_transition.md
    forbidden_tokens:
    - runners/rust/runner_adapter.sh
    allowlist:
    - /specs/contract/12_runner_interface.md
    - /specs/contract/16_rust_primary_transition.md
  check:
    profile: governance.scan
    config:
      check: runtime.no_public_direct_rust_adapter_docs
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
        - check_id
      - runtime.no_public_direct_rust_adapter_docs
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    imports:
      subject:
        from: artifact
        key: summary_json
```
