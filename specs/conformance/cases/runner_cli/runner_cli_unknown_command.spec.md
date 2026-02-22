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
  actions:
  - id: svc.check_profile_text_file_config.default.1
    type: legacy.check_profile_text_file_config
    io: io
    profile: default
contracts:
- id: DCCONF-RCLI-004
  title: runner cli unknown commands fail non-zero
  purpose: Portable CLI contract requires unknown commands to fail with non-zero status.
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
        - unknown command
```
