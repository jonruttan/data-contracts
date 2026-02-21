```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONTRACT-001
    title: contracts avoid rust-primary language
    purpose: Ensures active contracts remain implementation-agnostic.
    harness:
      root: .
      contract_language:
        files:
        - /specs/contract/10_docs_quality.md
        - /specs/contract/12_runner_interface.md
        - /specs/contract/25_compatibility_matrix.md
        forbidden_tokens:
        - implementation-agnostic
        - required lane
      check:
        profile: governance.scan
        config:
          check: runtime.contracts_no_rust_primary_language
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
```
