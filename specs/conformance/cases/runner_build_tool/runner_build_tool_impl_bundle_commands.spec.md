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
    - "{'check': {'profile': 'text.file', 'config': {'path': '/specs/contract/34_runner_implementation_spec_bundles.md'}}}"
services:
  entries:
  - id: svc.check_profile_text_file_config_path_specs_contract_34_runner_implementation_spec_bundles_md.default.1
    type: legacy.check_profile_text_file_config_path_specs_contract_34_runner_implementation_spec_bundles_md
    io: io
    profile: default
    config: {}
contracts:
- id: DCCONF-BTOOL-010
  title: implementation bundle contract defines build and package command surface
  purpose: Runner implementation spec bundle contract must expose build-impl, package-impl, and package-check command vocabulary.
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
        - build-impl
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - package-impl
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - package-check
    - id: assert_4
      assert:
        std.string.contains:
        - var: text
        - data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz
```
