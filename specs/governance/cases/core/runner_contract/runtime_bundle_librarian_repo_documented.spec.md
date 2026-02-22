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
    - "{'check': {'profile': 'text.file', 'config': {'path': '/README.md'}}}"
services:
  actions:
  - id: svc.check_profile_text_file_config_path_readme_md.default.1
    type: legacy.check_profile_text_file_config_path_readme_md
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-BUNDLE-004
  title: canonical bundle librarian repository is documented
  purpose: Ensures canonical bundle source points to data-contracts-bundles and not
    local specs/bundles manifests.
  clauses:
    imports:
    - artifact:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - data-contracts-bundles
    - id: assert_2
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - "/specs/bundles/index.md"
```
