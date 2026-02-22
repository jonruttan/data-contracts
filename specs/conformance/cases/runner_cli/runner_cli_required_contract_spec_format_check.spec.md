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
  clauses:
  - id: DCCONF-RCLI-006
    title: runner cli exposes contract spec format check command
    purpose: Portable CLI contract requires the check mode for contract-spec key order formatting.
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
          - runner contract-spec-format --check
```
