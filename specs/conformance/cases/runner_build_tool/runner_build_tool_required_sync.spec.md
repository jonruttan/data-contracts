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
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/contract/30_build_tool_command_set.md'}}}"
services:
- id: svc.check_profile_text_file_config_path_specs_contract_30_build_tool_command_set_md.default.1
  type: legacy.check_profile_text_file_config_path_specs_contract_30_build_tool_command_set_md
  mode: default
  direction: bidirectional
contracts:
- id: DCCONF-BTOOL-002
  title: runner build tool contract defines required bundle sync tasks
  purpose: Portable build tool contract must define bundle-sync and bundle-sync-check
    required tasks.
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
          - "`spec-sync`"
    - id: assert_4
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - "`spec-sync-check`"
```
