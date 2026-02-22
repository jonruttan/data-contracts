```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
- type: io.fs
  operations:
  - id: svc.assert_check.text_file.1
    config:
      use:
      - as: lib_policy_text
        symbols:
        - policy.text.contains_pair
        artifact_id: art.svc.assert_check.text_file.1.use_1.1
    mode: read.text
    direction: input
contracts:
  asserts:
  - id: DCCONF-RCERT-001
    title: runner execution certificate v2 schema is declared
    purpose: Ensures the v2 runner execution certificate schema is present with core sections.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
        - call:
          - var: policy.text.contains_pair
          - var: text
          - type
          - runtime.runner_execution_certificate
        - call:
          - var: policy.text.contains_pair
          - var: text
          - version
          - '2'
  - id: DCCONF-RCERT-002
    title: runner execution certificate v2 includes intent equivalence and proof
    purpose: Ensures v2 schema defines deterministic intent and payload proof fields.
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
        - call:
          - var: policy.text.contains_pair
          - var: text
          - execution_intent
          - registry_ref
        - call:
          - var: policy.text.contains_pair
          - var: text
          - equivalence
          - intent_hash
        - call:
          - var: policy.text.contains_pair
          - var: text
          - proof
          - payload_sha256
artifacts:
- id: art.svc.assert_check.text_file.1.use_1.1
  ref: "/specs/libraries/policy/policy_text.spec.md"
  direction: input
```

