```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-ENTRY-004
    title: public docs do not instruct direct rust adapter invocation
    purpose: Ensures public docs point to the canonical adapter entrypoint rather than internal
      rust adapter paths.
    harness:
      root: .
      public_docs:
        files:
        - /README.md
        - /docs/development.md
        - /specs/current.md
        - /specs/contract/12_runner_interface.md
        
        forbidden_tokens:
        - dc-runner-rust
        allowlist:
        - /specs/contract/12_runner_interface.md
        
      check:
        profile: governance.scan
        config:
          check: runtime.no_public_direct_rust_adapter_docs
      use:
      - ref: /specs/libraries/policy/policy_core.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.pass_when_no_violations
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          std.logic.eq:
          - {var: violation_count}
          - 0
      - id: assert_2
        assert:
        - std.logic.eq:
          - std.object.get:
            - {var: summary_json}
            - check_id
          - runtime.no_public_direct_rust_adapter_docs
        - std.logic.eq:
          - std.object.get:
            - {var: summary_json}
            - passed
          - true
        imports:
        - from: artifact
          names:
          - summary_json
```
