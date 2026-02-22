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
- id: DCCONF-BTOOL-004
  title: runner build tool contract defines optional task catalog
  purpose: Portable build tool contract should declare the MAY task catalog for optional capabilities.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      required: false
      assert:
        std.string.contains:
        - var: text
        - smoke
    - id: assert_2
      required: false
      assert:
        std.string.contains:
        - var: text
        - package-check
    - id: assert_3
      required: false
      assert:
        std.string.contains:
        - var: text
        - release-verify
    - id: assert_4
      required: false
      assert:
        std.string.contains:
        - var: text
        - docs-check
    - id: assert_5
      required: false
      assert:
        std.string.contains:
        - var: text
        - lint
    - id: assert_6
      required: false
      assert:
        std.string.contains:
        - var: text
        - typecheck
```
