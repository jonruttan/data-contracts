```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-BTOOL-003
    title: runner contract pack includes build tool contract surface
    purpose: Ensures runner contract pack includes build tool contract and conformance case coverage.
    harness:
      root: .
      pack:
        path: /specs/packs/runner_contract_pack_v1.yaml
        required_tokens:
          - /specs/contract/30_build_tool_command_set.md
          - /specs/contract/33_bundle_package_management.md
          - /specs/schema/runner_build_tool_contract_v1.yaml
          - /specs/schema/runner_bundle_lock_v1.yaml
          - /specs/schema/bundle_manifest_v1.yaml
          - /specs/schema/resolved_bundle_lock_v1.yaml
          - /specs/conformance/cases/runner_build_tool/runner_build_tool_required_core.spec.md
          - /specs/conformance/cases/runner_build_tool/runner_build_tool_required_sync.spec.md
          - /specs/conformance/cases/runner_build_tool/runner_build_tool_bundle_lock_schema.spec.md
          - /specs/conformance/cases/runner_build_tool/runner_build_tool_bundle_asset_naming.spec.md
      check:
        profile: governance.scan
        config:
          check: packs.runner_contract_pack_complete
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [violation_count]
      predicates:
        - id: assert_1
          required: false
          assert:
            call:
              - {var: policy.assert.no_violations}
              - std.object.assoc:
                - violation_count
                - {var: violation_count}
                - lit: {}
```
