```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/02_contracts/29_runner_cli_interface.md'}}}"
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/01_schema/runner_cli_contract_v1.yaml'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-RCLI-006
    title: contract spec formatter command contract is synchronized
    purpose: Ensures runner CLI contract docs and schema include the contract-spec-format command surface and mode metadata.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
        - std.string.contains:
          - var: text
          - contract-spec-format
        - std.string.contains:
          - var: text
          - "--check"
        - std.string.contains:
          - var: text
          - "--write"
adapters:
- type: legacy.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md
  actions:
  - id: svc.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md.default.1
    profile: default
- type: legacy.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml
  actions:
  - id: svc.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml.default.1
    profile: default
services:
- id: svc.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md.default.1
- id: svc.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml.default.1
```
