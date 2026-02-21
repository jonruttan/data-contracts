```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-BUNDLE-002
    title: runner bundle lock schema is indexed
    purpose: Ensures schema index includes bundle manifest and lock schemas for runner consumers.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/index.md
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
              - /specs/schema/bundle_manifest_v1.yaml
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - /specs/schema/resolved_bundle_lock_v1.yaml
        - id: assert_3
          assert:
            std.string.contains:
              - {var: text}
              - /specs/schema/runner_bundle_lock_v1.yaml
```
