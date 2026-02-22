```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/02_contracts/33_bundle_package_management.md'}}}"
contracts:
  clauses:
  - id: DCCONF-BTOOL-006
    title: bundle package contract defines canonical data-contract-bundle asset naming
    purpose: Ensures bundle package contract uses the canonical data-contract-bundle prefix and version token format.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
          std.string.contains:
          - var: text
          - data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.sha256
      - id: assert_3
        assert:
          std.string.contains:
          - var: text
          - data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.intoto.json
      - id: assert_4
        assert:
          std.logic.not:
            std.string.contains:
            - var: text
            - bundle-{bundle_id}-{bundle_version}.tar.gz
adapters:
- type: legacy.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md
  actions:
  - id: svc.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md.default.1
```
