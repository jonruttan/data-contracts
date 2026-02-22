```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/scripts/bundle'}}}"
contracts:
  clauses:
  - id: DCCONF-BTOOL-007
    title: bundle tooling exposes install command surface
    purpose: Bundle CLI must expose install and install-check commands for multi-bundle project workflows.
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
          - scripts/bundle install --project-lock
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - scripts/bundle install-check --project-lock
adapters:
- type: legacy.check_profile_text_file_config_path_scripts_bundle
  actions:
  - id: svc.check_profile_text_file_config_path_scripts_bundle.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.check_profile_text_file_config_path_scripts_bundle.default.1
  consumes:
  - svc.check_profile_text_file_config_path_scripts_bundle.default.1
```
