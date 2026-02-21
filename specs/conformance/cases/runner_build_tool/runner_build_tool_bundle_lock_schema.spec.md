```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-008
  title: project bundle lock schema defines canonical multi-bundle fields
  purpose: Project bundle lock schema must define bundles array, install directories, and source checksums.
  harness:
    check:
      profile: text.file
      config:
        path: "/specs/schema/project_bundle_lock_v1.yaml"
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
        - bundles
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - asset_url
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - sha256
    - id: assert_4
      assert:
        std.string.contains:
        - var: text
        - install_dir
```
