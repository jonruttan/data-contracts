```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-010
  title: implementation bundle contract defines build and package command surface
  purpose: Runner implementation spec bundle contract must expose build-impl, package-impl, and package-check command vocabulary.
  harness:
    check:
      profile: text.file
      config:
        path: "/specs/contract/34_runner_implementation_spec_bundles.md"
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
