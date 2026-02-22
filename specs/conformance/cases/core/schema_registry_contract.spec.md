```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - check
services:
  actions:
  - id: svc.check.text_file.1
    type: assert.check
    io: input
    profile: text.file
    config:
      use:
      - as: lib_policy_text
        symbols:
        - policy.text.contains_all
        artifact_id: art.svc.check.text_file.1.use_1.1
      source_artifact_id: art.svc.check.text_file.1.source.1
contracts:
- id: DCCONF-SCHEMA-REG-001
  title: schema docs include generated registry snapshot markers
  purpose: Ensures generated schema registry snapshot markers and section header are present in schema_v1 documentation.
  expect:
    portable:
      status: pass
      category:
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
          - 'BEGIN GENERATED: SCHEMA_REGISTRY_V1'
          - 'END GENERATED: SCHEMA_REGISTRY_V1'
          - Generated Registry Snapshot
artifacts:
- id: art.svc.check.text_file.1.source.1
  ref: "/specs/schema/schema_v2.md"
  io: input
- id: art.svc.check.text_file.1.use_1.1
  ref: "/specs/libraries/policy/policy_text.spec.md"
  io: input
```
