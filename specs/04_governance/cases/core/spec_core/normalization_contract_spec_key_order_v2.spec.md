```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/01_schema/schema_v2.md'}}}"
contracts:
  clauses:
  - id: DCGOV-NORM-007
    title: v2 contract spec key order contract is documented
    purpose: Ensures schema v2 documents canonical suite-root and contract-item key ordering for formatter enforcement.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
        - std.string.contains:
          - var: text
          - "## v2 Canonical Key Order (Formatter Scope)"
        - std.string.contains:
          - var: text
          - Suite root canonical order
        - std.string.contains:
          - var: text
          - contracts[] canonical order
        - std.string.contains:
          - var: text
          - "`spec_version`"
        - std.string.contains:
          - var: text
          - "`contracts`"
        - std.string.contains:
          - var: text
          - list item order is preserved as-authored
adapters:
- type: legacy.check_profile_text_file_config_path_specs_schema_schema_v2_md
  actions:
  - id: svc.check_profile_text_file_config_path_specs_schema_schema_v2_md.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.check_profile_text_file_config_path_specs_schema_schema_v2_md.default.1
  consumes:
  - svc.check_profile_text_file_config_path_specs_schema_schema_v2_md.default.1
```
