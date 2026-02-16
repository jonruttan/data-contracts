# Subject Profiles Conformance Cases

## SRCONF-PROFILE-001

```yaml spec-test
id: SRCONF-PROFILE-001
title: subject profile schema defines canonical envelope fields
purpose: Ensures subject profile schema defines JSON-core envelope and deterministic projection
  constraints.
type: text.file
path: /docs/spec/schema/subject_profiles_v1.yaml
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - profile_id
    - std.string.contains:
      - {var: subject}
      - profile_version
    - std.string.contains:
      - {var: subject}
      - json_core_only
    - std.string.contains:
      - {var: subject}
      - deterministic_projection
  target: text
```

## SRCONF-PROFILE-002

```yaml spec-test
id: SRCONF-PROFILE-002
title: text.file exposes context_json subject profile envelope
purpose: Ensures text.file harness provides context_json target with profile metadata and
  JSON value payload.
type: text.file
path: /docs/spec/contract/20_subject_profiles_v1.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - profile_id
      - text.file/v1
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - profile_version
      - 1
    - std.object.has_key:
      - {var: subject}
      - value
    - std.object.has_key:
      - {var: subject}
      - meta
  target: context_json
```
