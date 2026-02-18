# Subject Profiles Conformance Cases

## SRCONF-PROFILE-001

```yaml contract-spec
id: SRCONF-PROFILE-001
title: subject profile schema defines canonical envelope fields
purpose: Ensures subject profile schema defines JSON-core envelope and deterministic projection
  constraints.
type: contract.check
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: MUST
  asserts:
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
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/schema/subject_profiles_v1.yaml
```

## SRCONF-PROFILE-002

```yaml contract-spec
id: SRCONF-PROFILE-002
title: text.file exposes context_json subject profile envelope
purpose: Ensures text.file harness provides context_json target with profile metadata and
  JSON value payload.
type: contract.check
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: MUST
  asserts:
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
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/contract/20_subject_profiles_v1.md
```
