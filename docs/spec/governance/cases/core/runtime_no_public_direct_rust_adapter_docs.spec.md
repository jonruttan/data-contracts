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
    - /docs/spec/current.md
    - /docs/spec/contract/12_runner_interface.md
    - /docs/spec/contract/16_rust_primary_transition.md
    forbidden_tokens:
    - scripts/rust/runner_adapter.sh
    allowlist:
    - /docs/spec/contract/12_runner_interface.md
    - /docs/spec/contract/16_rust_primary_transition.md
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
      check: runtime.no_public_direct_rust_adapter_docs
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
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
    - lit:
        lit:
          lit:
            MUST:
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
  target: summary_json
```
