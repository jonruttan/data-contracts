```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-BUNDLE-006
    title: implementation overlay schemas are indexed and include integrity fields
    purpose: Ensures schema index and implementation build lock schema define deterministic integrity fields for overlay bundle builds.
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
              - /specs/schema/implementation_bundle_overlay_v1.yaml
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - /specs/schema/implementation_bundle_build_lock_v1.yaml
  - id: DCGOV-RUNTIME-BUNDLE-007
    title: implementation build lock schema defines deterministic integrity fields
    purpose: Ensures implementation build lock includes base/overlay/result hashes and resolved_files hash.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/implementation_bundle_build_lock_v1.yaml
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
              - base_package_sha256
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - overlay_sha256
        - id: assert_3
          assert:
            std.string.contains:
              - {var: text}
              - result_package_sha256
        - id: assert_4
          assert:
            std.string.contains:
              - {var: text}
              - resolved_files_sha256
```
