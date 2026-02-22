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
  - id: DCCONF-RCLI-005
    title: runner cli supports optional capability negotiation
    purpose: Portable CLI contract allows optional capability flags such as structured output mode.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        required: false
        assert:
          std.string.contains:
          - var: text
          - "--json"
```
