```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-SCHEMA-PIN-005
    title: schema catalog includes active contract-spec v1
    purpose: Ensures active schema catalog includes canonical contract-spec v1 entry.
    harness:
      root: .
      schema_catalog:
        path: /specs/schema/schema_catalog_v1.yaml
        required_tokens:
        - schema_id: contract_spec
        - major: 1
        - path: /specs/schema/schema_v1.md
        - status: active
      check:
        profile: governance.scan
        config:
          check: schema.catalog_contains_active_schema_v1
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
