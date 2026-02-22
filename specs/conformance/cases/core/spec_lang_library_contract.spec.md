```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: DCCONF-LIB-CONTRACT-001
  title: policy library uses producer harness exports
  purpose: Ensures policy library authoring uses producer-owned root exports 
    mode=function with assert.function source mappings.
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
          - 'type: spec.export'
          - 'harness:'
          - 'exports:'
          - 'from: assert.function'
      - call:
        - var: policy.text.contains_none
        - var: text
        - lit:
          - 'defines:'
- id: DCCONF-LIB-CONTRACT-002
  title: path library uses producer harness exports
  purpose: Ensures path library authoring uses producer-owned root exports 
    mode=function with assert.function source mappings.
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
          - 'type: spec.export'
          - 'harness:'
          - 'exports:'
          - 'from: assert.function'
      - call:
        - var: policy.text.contains_none
        - var: text
        - lit:
          - 'defines:'
- id: DCCONF-LIB-CONTRACT-003
  title: policy library index tracks canonical files
  purpose: Ensures generated policy library index includes canonical file 
    references.
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
          - "/specs/libraries/policy/policy_core.spec.md"
          - "/specs/libraries/policy/policy_metrics.spec.md"
defaults:
  harness: check
harness:
  type: unit.test
  profile: check
services:
  defaults:
    type: assert.check
    io: input
    profile: text.file
  entries:
  - id: svc.assert_check.text_file.1
    config:
      path: "/specs/libraries/policy/policy_core.spec.md"
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
        - policy.text.contains_none
  - id: svc.assert_check.text_file.2
    config:
      path: "/specs/libraries/path/path_core.spec.md"
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
        - policy.text.contains_none
  - id: svc.assert_check.text_file.3
    config:
      path: "/specs/libraries/policy/index.md"
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
```



