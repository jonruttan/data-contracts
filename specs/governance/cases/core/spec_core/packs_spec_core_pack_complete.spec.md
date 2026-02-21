```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PACK-003
    title: spec-core maintenance pack is complete
    purpose: Ensures spec-core pack includes schema and governance maintenance surfaces.
    harness:
      root: .
      pack:
        path: /specs/packs/spec_core_maintenance_pack_v1.yaml
        required_tokens:
          - pack_id: spec_core_maintenance_pack_v1
          - /specs/schema/schema_v2.md
          - /specs/schema/schema_catalog_v1.yaml
          - /specs/governance/cases/core/spec_core/runtime_schema_pin_pipeline_chain.spec.md
      check:
        profile: governance.scan
        config:
          check: packs.spec_core_pack_complete
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [violation_count]
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
