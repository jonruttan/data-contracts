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
    - "{'check': {'profile': 'text.file', 'config': {'path': '/scripts/bundle'}}}"
services:
- id: svc.check_profile_text_file_config_path_scripts_bundle.default.1
  type: legacy.check_profile_text_file_config_path_scripts_bundle
  mode: default
  direction: bidirectional
contracts:
- id: DCCONF-BTOOL-007
  title: bundle tooling exposes install command surface
  purpose: Bundle CLI must expose install and install-check commands for multi-bundle
    project workflows.
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
        - scripts/bundle install --project-lock
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - scripts/bundle install-check --project-lock
```
