```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: DCCONF-RCERT-001
  title: runner execution certificate v2 schema is declared
  purpose: Ensures the v2 runner execution certificate schema is present with core sections.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
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
    profile: text.file
    config:
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
- id: DCCONF-RCERT-002
  title: runner execution certificate v2 includes intent equivalence and proof
  purpose: Ensures v2 schema defines deterministic intent and payload proof fields.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
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
    profile: text.file
    config:
      use:
      - ref: "/specs/libraries/policy/policy_text.spec.md"
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
defaults:
  harness: check
```

