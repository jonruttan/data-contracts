```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-BTOOL-003
  title: runner contract pack includes build tool contract surface
  purpose: Ensures runner contract pack includes build tool contract and 
    conformance case coverage.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      required: false
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'pack': {'path': '/specs/packs/runner_contract_pack_v1.yaml',
      'required_tokens': ['/specs/contract/30_build_tool_command_set.md', '/specs/contract/33_bundle_package_management.md',
      '/specs/contract/34_runner_implementation_spec_bundles.md', '/specs/schema/runner_build_tool_contract_v1.yaml',
      '/specs/schema/project_bundle_lock_v1.yaml', '/specs/schema/bundle_manifest_v1.yaml',
      '/specs/schema/resolved_bundle_lock_v1.yaml', '/specs/schema/implementation_bundle_overlay_v1.yaml',
      '/specs/schema/implementation_bundle_build_lock_v1.yaml', '/specs/conformance/cases/runner_build_tool/runner_build_tool_required_core.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_required_sync.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_bundle_lock_schema.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_bundle_asset_naming.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_impl_overlay_schema.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_impl_bundle_commands.spec.md',
      '/specs/conformance/cases/runner_build_tool/runner_build_tool_project_lock_additional_role.spec.md']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'packs.runner_contract_pack_complete'}}}"
services:
  entries:
  - id: 
      svc.root_pack_path_specs_packs_runner_contract_pack_v1_yaml_required_tokens_specs_contract_30_build_tool_command_set_md_specs_contract_33_bundle_package_management_md_specs_contract_34_runner_implementation_spec_bundles_md_specs_schema_runner_build_tool_contract_v1_yaml_specs_schema_project_bundle_lock_v1_yaml_specs_schema_bundle_manifest_v1_yaml_specs_schema_resolved_bundle_lock_v1_yaml_specs_schema_implementation_bundle_overlay_v1_yaml_specs_schema_implementation_bundle_build_lock_v1_yaml_specs_conformance_cases_runner_build_tool_runner_build_tool_required_core_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_required_sync_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_bundle_lock_schema_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_bundle_asset_naming_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_impl_overlay_schema_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_impl_bundle_commands_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_project_lock_additional_role_spec_md_check_profile_governance_scan_config_check_packs_runner_contract_pack_complete.default.1
    type: 
      legacy.root_pack_path_specs_packs_runner_contract_pack_v1_yaml_required_tokens_specs_contract_30_build_tool_command_set_md_specs_contract_33_bundle_package_management_md_specs_contract_34_runner_implementation_spec_bundles_md_specs_schema_runner_build_tool_contract_v1_yaml_specs_schema_project_bundle_lock_v1_yaml_specs_schema_bundle_manifest_v1_yaml_specs_schema_resolved_bundle_lock_v1_yaml_specs_schema_implementation_bundle_overlay_v1_yaml_specs_schema_implementation_bundle_build_lock_v1_yaml_specs_conformance_cases_runner_build_tool_runner_build_tool_required_core_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_required_sync_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_bundle_lock_schema_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_bundle_asset_naming_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_impl_overlay_schema_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_impl_bundle_commands_spec_md_specs_conformance_cases_runner_build_tool_runner_build_tool_project_lock_additional_role_spec_md_check_profile_governance_scan_config_check_packs_runner_contract_pack_complete
    io: io
    profile: default
    config: {}
    default: true
```
