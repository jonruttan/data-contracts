```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-009
  title: implementation overlay schema defines patch overlay fields
  purpose: Implementation overlay schema must define add/replace/delete patch surfaces and output bundle metadata.
  harness:
    check:
      profile: text.file
      config:
        path: "/specs/schema/implementation_bundle_overlay_v1.yaml"
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
        - add_files
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - replace_files
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - delete_paths
    - id: assert_4
      assert:
        std.string.contains:
        - var: text
        - output_bundle
```
