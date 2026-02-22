```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/contract/33_bundle_package_management.md'}}}"
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/runner_build_tool_contract_v1.yaml'}}}"
services:
  defaults:
    profile: default
  actions:
  - id: svc.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md.default.1
    type: legacy.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md
  - id: svc.check_profile_text_file_config_path_specs_schema_runner_build_tool_contract_v1_yaml.default.1
    type: legacy.check_profile_text_file_config_path_specs_schema_runner_build_tool_contract_v1_yaml
contracts:
- id: DCGOV-RUNTIME-BUNDLE-001
  title: runner bundle package management contract is defined
  purpose: Ensures bundle package management contract describes release-asset and
    checksum requirements.
  clauses:
    imports:
    - artifact:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - bundle-sync
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - bundle-sync-check
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - release-asset
    - id: assert_4
      assert:
        std.string.contains:
        - var: text
        - checksum
    - id: assert_5
      assert:
        std.string.contains:
        - var: text
        - bundles.lock.yaml
    - id: assert_6
      assert:
        std.string.contains:
        - var: text
        - data-contracts-bundles
    - id: assert_7
      assert:
        std.string.contains:
        - var: text
        - dc-runner-rust-specs
- id: DCGOV-RUNTIME-BUNDLE-003
  title: runner build tool schema declares bundle sync tasks
  purpose: Ensures runner build tool schema uses bundle-sync task ids and does not
    include legacy spec-sync task ids.
  clauses:
    imports:
    - artifact:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - bundle-sync
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - bundle-sync-check
    - id: assert_3
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - spec-sync
```
