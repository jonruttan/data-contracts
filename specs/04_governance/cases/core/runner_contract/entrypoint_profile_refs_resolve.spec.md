```yaml contract-spec
spec_version: 1
schema_ref: /specs/01_schema/schema_v1.md
harness:
  type: unit.test
  profile: check
  config:
    check:
      profile: text.file
      config: {}
contracts:
  clauses:
  - id: DCGOV-ENTRY-002
    title: entrypoint profiles resolve to check sets
    purpose: Ensures command entrypoints map to declared governance profiles.
    asserts:
      imports:
      - from: asset
        names:
        - text
      checks:
      - id: assert_1
        assert:
          std.string.contains:
          - var: text
          - profile: full
      - id: assert_2
        assert:
          std.string.contains:
          - var: text
          - profile: critical
      - id: assert_3
        assert:
          std.string.contains:
          - var: text
          - id: docs-generate
      - id: assert_4
        assert:
          std.string.contains:
          - var: text
          - id: docs-generate-check
      - id: assert_5
        assert:
          std.string.contains:
          - var: text
          - id: docs-build
      - id: assert_6
        assert:
          std.string.contains:
          - var: text
          - id: docs-build-check
      - id: assert_7
        assert:
          std.string.contains:
          - var: text
          - id: docs-lint
      - id: assert_8
        assert:
          std.string.contains:
          - var: text
          - id: docs-graph
adapters:
- type: beta.check_profile_text_file_config
  actions:
  - id: svc.gov.entry.profile.resolve.1
    direction: bidirectional
    profile: default
services:
- id: svc.gov.entry.profile.resolve.1
  consumes:
  - svc.gov.entry.profile.resolve.1
```
