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
  - id: DCGOV-RUNTIME-BTOOL-002
    title: runner build tool contract schema is defined
    purpose: Ensures tool-agnostic build tool schema is present in schema index.
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
          - "/specs/schema/runner_build_tool_contract_v1.yaml"
```
