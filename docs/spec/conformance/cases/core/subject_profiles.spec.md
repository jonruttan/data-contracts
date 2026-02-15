# Subject Profiles Conformance Cases

## SRCONF-PROFILE-001

```yaml spec-test
id: SRCONF-PROFILE-001
title: subject profile schema defines canonical envelope fields
purpose: Ensures subject profile schema defines JSON-core envelope and deterministic projection constraints.
type: text.file
path: /docs/spec/schema/subject_profiles_v1.yaml
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - {contains: [{var: subject}, profile_id]}
    - {contains: [{var: subject}, profile_version]}
    - {contains: [{var: subject}, json_core_only]}
    - {contains: [{var: subject}, deterministic_projection]}
```

## SRCONF-PROFILE-002

```yaml spec-test
id: SRCONF-PROFILE-002
title: text.file exposes context_json subject profile envelope
purpose: Ensures text.file harness provides context_json target with profile metadata and JSON value payload.
type: text.file
path: /docs/spec/contract/20_subject_profiles_v1.md
expect:
  portable:
    status: pass
assert:
- target: context_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, profile_id]}
      - text.file/v1
    - eq:
      - {get: [{var: subject}, profile_version]}
      - 1
    - {has_key: [{var: subject}, value]}
    - {has_key: [{var: subject}, meta]}
```
