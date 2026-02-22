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
    - "{'check': {'profile': 'text.file', 'config': {}}}"
services:
  entries:
  - id: svc.check_profile_text_file_config.default.1
    type: legacy.check_profile_text_file_config
    io: io
    profile: default
contracts:
- id: DCCONF-BTOOL-005
  title: runner build tool contract declares manifest path requirement
  purpose: Build tool command contract must require each runner repository to publish a task map manifest path.
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
        - "/specs/impl/<runner>/runner_build_tool_contract_v1.yaml"
```
