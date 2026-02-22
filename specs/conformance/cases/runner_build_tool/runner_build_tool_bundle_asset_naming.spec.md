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
services:
- id: svc.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md.default.1
  type: legacy.check_profile_text_file_config_path_specs_contract_33_bundle_package_management_md
  mode: default
  direction: bidirectional
contracts:
- id: DCCONF-BTOOL-006
  title: bundle package contract defines canonical data-contract-bundle asset naming
  purpose: Ensures bundle package contract uses the canonical data-contract-bundle
    prefix and version token format.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
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
```
