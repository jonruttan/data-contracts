```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: DCCONF-SCHEMA-STDLIB-003
  title: json parsing and type predicates stay deterministic
  purpose: Ensures parsed JSON shapes can be validated with deterministic type 
    predicates.
  expect:
    portable:
      status: pass
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - std.logic.eq:
        - std.type.json_type:
          - std.json.parse:
            - '{"id":1,"tags":["alpha","beta"]}'
          - dict
        - true
      - std.logic.eq:
        - std.type.json_type:
          - std.object.get:
            - std.json.parse:
              - '{"id":1,"tags":["alpha","beta"]}'
            - tags
          - list
        - true
- id: DCCONF-SCHEMA-STDLIB-004
  title: parsed payload predicates support deterministic error-shape checks
  purpose: Ensures JSON payload predicate composition remains deterministic for 
    invalid-value checks.
  expect:
    portable:
      status: pass
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.logic.and:
        - std.logic.eq:
          - std.type.json_type:
            - std.object.get:
              - std.json.parse:
                - '{"id":"x"}'
              - id
            - string
          - true
        - std.logic.not:
          - std.logic.eq:
            - std.object.get:
              - std.json.parse:
                - '{"id":"x"}'
              - id
            - 1
defaults:
  harness: check
harness:
  type: unit.test
  profile: check
services:
  entries:
  - id: svc.assert_check.text_file.1
    type: assert.check
    io: input
    profile: text.file
    config:
      path: "/specs/conformance/cases/core/spec_lang_schema.spec.md"
```


