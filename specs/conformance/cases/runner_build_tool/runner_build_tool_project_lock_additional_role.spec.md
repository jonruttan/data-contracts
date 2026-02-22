```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/project_bundle_lock_v1.yaml'}}}"
services:
- type: legacy.check_profile_text_file_config_path_specs_schema_project_bundle_lock_v1_yaml
  operations:
  - id: svc.check_profile_text_file_config_path_specs_schema_project_bundle_lock_v1_yaml.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCCONF-BTOOL-011
    title: project bundle lock schema supports additional role entries
    purpose: Project lock schema must allow role additional for implementation-specific bundles.
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
          - role
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - primary
      - id: assert_3
        assert:
          std.string.contains:
          - var: text
          - additional
```
