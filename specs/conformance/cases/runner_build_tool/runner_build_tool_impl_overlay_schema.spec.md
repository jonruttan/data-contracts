```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/implementation_bundle_overlay_v1.yaml'}}}"
services:
- type: legacy.check_profile_text_file_config_path_specs_schema_implementation_bundle_overlay_v1_yaml
  operations:
  - id: svc.check_profile_text_file_config_path_specs_schema_implementation_bundle_overlay_v1_yaml.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCCONF-BTOOL-009
    title: implementation overlay schema defines patch overlay fields
    purpose: Implementation overlay schema must define add/replace/delete patch surfaces
      and output bundle metadata.
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
          - add_files
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - replace_files
      - id: assert_3
        assert:
          std.string.contains:
          - var: text
          - delete_paths
      - id: assert_4
        assert:
          std.string.contains:
          - var: text
          - output_bundle
```
