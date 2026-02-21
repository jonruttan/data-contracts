```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PACK-005
    title: pack paths resolve in repository
    purpose: Ensures all pack manifests and referenced case paths exist.
    harness:
      root: .
      required_paths:
        - /specs/packs/runner_contract_pack_v1.yaml
        - /specs/packs/spec_core_maintenance_pack_v1.yaml
        - /specs/packs/project_docs_maintenance_pack_v1.yaml
        - /specs/conformance/cases/runner_cli/runner_cli_required_help.spec.md
        - /specs/conformance/cases/runner_cli/runner_cli_required_governance.spec.md
        - /specs/conformance/cases/runner_cli/runner_cli_required_conformance.spec.md
        - /specs/conformance/cases/runner_cli/runner_cli_unknown_command.spec.md
        - /specs/conformance/cases/runner_cli/runner_cli_optional_capability_negotiation.spec.md
      check:
        profile: governance.scan
        config:
          check: packs.pack_paths_resolve
    clauses:
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
