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
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: text
  steps:
  - id: assert_1
    assert:
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
harness:
  check:
    profile: text.file
    config:
      path: /specs/schema/subject_profiles_v1.yaml
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
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: context_json
  steps:
  - id: assert_1
    assert:
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
harness:
  check:
    profile: text.file
    config:
      path: /specs/contract/20_subject_profiles_v1.md
```
