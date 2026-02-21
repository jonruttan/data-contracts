```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-BUNDLE-005
  title: implementation overlay bundle contract is defined
  purpose: Ensures implementation overlay bundle contract documents canonical base source, checksum requirements, and patch-based semantics.
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
        - data-contracts-bundles
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - checksum
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - add_files
    - id: assert_4
      assert:
        std.string.contains:
        - var: text
        - replace_files
    - id: assert_5
      assert:
        std.string.contains:
        - var: text
        - delete_paths
    - id: assert_6
      assert:
        std.string.contains:
        - var: text
        - Full copied canonical trees are not the normative model.
```
