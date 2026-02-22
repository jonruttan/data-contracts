```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-BUNDLE-004
  title: canonical bundle librarian repository is documented
  purpose: Ensures canonical bundle source points to data-contracts-bundles and 
    not local specs/bundles manifests.
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
        - data-contracts-bundles
    - id: assert_2
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - "/specs/bundles/index.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {'path': '/README.md'}}}"
services:
  entries:
  - id: svc.check_profile_text_file_config_path_readme_md.default.1
    type: legacy.check_profile_text_file_config_path_readme_md
    io: io
    profile: default
    config: {}
    default: true
```
