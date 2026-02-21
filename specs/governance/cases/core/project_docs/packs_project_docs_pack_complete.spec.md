```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PACK-004
    title: project-docs maintenance pack is complete
    purpose: Ensures docs maintenance pack includes README/book coherence surfaces.
    harness:
      root: .
      pack:
        path: /specs/packs/project_docs_maintenance_pack_v1.yaml
        required_tokens:
          - pack_id: project_docs_maintenance_pack_v1
          - /specs/contract/10_docs_quality.md
          - /specs/governance/cases/core/project_docs/docs_readme_task_usage_paths_present.spec.md
      check:
        profile: governance.scan
        config:
          check: packs.project_docs_pack_complete
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
