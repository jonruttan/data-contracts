```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-001
  title: runner build tool contract defines required core tasks
  purpose: Portable build tool contract must define build, test, and verify 
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
        - build
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - test
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - verify
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
    config: {}
```
