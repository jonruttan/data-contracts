```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-BTOOL-005
    title: runner bundle lock schema defines canonical lock fields
    purpose: Runner bundle lock schema must define source asset URL, sha256, and resolved lock hash fields.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/runner_bundle_lock_v1.yaml
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
              - root_bundle_id
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - asset_url
        - id: assert_3
          assert:
            std.string.contains:
              - {var: text}
              - sha256
        - id: assert_4
          assert:
            std.string.contains:
              - {var: text}
              - resolved_bundle_lock_sha256
```
