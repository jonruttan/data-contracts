```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-HARNESS-EXPORTS-004
    title: chain imports consumer surface remains unchanged
    purpose: Ensures consumer bindings continue to use harness.chain.imports semantics.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.chain_imports_consumer_surface_unchanged
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - summary_json
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
```
