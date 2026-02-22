```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: DCCONF-PROFILE-001
  title: subject profile schema defines canonical envelope fields
  purpose: Ensures subject profile schema defines JSON-core envelope and 
    deterministic projection constraints.
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
      - call:
        - var: policy.text.contains_all
        - var: text
        - lit:
          - profile_id
          - profile_version
          - json_core_only
          - deterministic_projection
- id: DCCONF-PROFILE-002
  title: text.file exposes context_json subject profile envelope
  purpose: Ensures text.file harness provides context_json target with profile 
    metadata and JSON value payload.
  expect:
    portable:
      status: pass
  clauses:
    imports:
    - from: artifact
      names:
      - context_json
    predicates:
    - id: assert_1
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: context_json
          - profile_id
        - text.file/v1
      - std.logic.eq:
        - std.object.get:
          - var: context_json
          - profile_version
        - 1
      - std.object.has_key:
        - var: context_json
        - value
      - std.object.has_key:
        - var: context_json
        - meta
defaults:
  harness: check
harness:
  type: unit.test
  profile: check
  config: {}
services:
  defaults:
    type: assert.check
    io: input
    profile: text.file
  entries:
  - id: svc.assert_check.text_file.1
    config:
      path: "/specs/schema/subject_profiles_v1.yaml"
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
    default: true
  - id: svc.assert_check.text_file.2
    config:
      path: "/specs/contract/20_subject_profiles_v1.md"
```


