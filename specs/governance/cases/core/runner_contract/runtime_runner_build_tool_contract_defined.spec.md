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
- id: svc.check_profile_text_file_config.default.1
  type: legacy.check_profile_text_file_config
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-RUNTIME-BTOOL-001
  title: runner build tool contract document is defined
  purpose: Ensures tool-agnostic build tool contract document is present in the portable
    contract index.
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
        - "/specs/contract/30_build_tool_command_set.md"
```
