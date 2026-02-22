```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {}}}"
services:
- type: legacy.check_profile_text_file_config
  operations:
  - id: svc.check_profile_text_file_config.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCCONF-RCLI-002
    title: runner cli exposes governance command
    purpose: Portable CLI contract requires governance command.
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
          - runner governance
```
