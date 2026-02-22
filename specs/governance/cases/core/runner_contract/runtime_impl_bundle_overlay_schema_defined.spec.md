```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/implementation_bundle_build_lock_v1.yaml'}}}"
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/index.md'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-BUNDLE-006
    title: implementation overlay schemas are indexed and include integrity fields
    purpose: Ensures schema index and implementation build lock schema define deterministic integrity fields for overlay bundle builds.
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
          - "/specs/schema/implementation_bundle_overlay_v1.yaml"
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - "/specs/schema/implementation_bundle_build_lock_v1.yaml"
  - id: DCGOV-RUNTIME-BUNDLE-007
    title: implementation build lock schema defines deterministic integrity fields
    purpose: Ensures implementation build lock includes base/overlay/result hashes and resolved_files hash.
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
          - base_package_sha256
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - overlay_sha256
      - id: assert_3
        assert:
          std.string.contains:
          - var: text
          - result_package_sha256
      - id: assert_4
        assert:
          std.string.contains:
          - var: text
          - resolved_files_sha256
adapters:
- type: legacy.check_profile_text_file_config_path_specs_schema_index_md
  actions:
  - id: svc.check_profile_text_file_config_path_specs_schema_index_md.default.1
    profile: default
- type: legacy.check_profile_text_file_config_path_specs_schema_implementation_bundle_build_lock_v1_yaml
  actions:
  - id: svc.check_profile_text_file_config_path_specs_schema_implementation_bundle_build_lock_v1_yaml.default.1
    profile: default
services:
- id: svc.check_profile_text_file_config_path_specs_schema_index_md.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_schema_index_md.default.1
- id: svc.check_profile_text_file_config_path_specs_schema_implementation_bundle_build_lock_v1_yaml.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_schema_implementation_bundle_build_lock_v1_yaml.default.1
```
