```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-BTOOL-011
    title: project bundle lock schema supports additional role entries
    purpose: Project lock schema must allow role additional for implementation-specific bundles.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/project_bundle_lock_v1.yaml
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [text]
      predicates:
        - id: assert_1
          assert:
            std.string.contains:
              - {var: text}
              - role
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - primary
        - id: assert_3
          assert:
            std.string.contains:
              - {var: text}
              - additional
```
