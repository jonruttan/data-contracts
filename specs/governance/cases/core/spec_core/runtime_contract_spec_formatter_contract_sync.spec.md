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
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/contract/29_runner_cli_interface.md'}}}"
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/schema/runner_cli_contract_v1.yaml'}}}"
services:
- id: svc.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md.default.1
  type: legacy.check_profile_text_file_config_path_specs_contract_29_runner_cli_interface_md
  mode: default
- id: svc.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml.default.1
  type: legacy.check_profile_text_file_config_path_specs_schema_runner_cli_contract_v1_yaml
  mode: default
contracts:
- id: DCGOV-RUNTIME-RCLI-006
  title: contract spec formatter command contract is synchronized
  purpose: Ensures runner CLI contract docs and schema include the contract-spec-format
    command surface and mode metadata.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
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
```
