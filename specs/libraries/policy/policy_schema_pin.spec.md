```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
contracts:
  - id: LIB-POLICY-SCHEMA-PIN-001
    type: contract.export
    title: schema pin extractor predicates
    clauses:
      defaults: {}
      predicates:
        - id: __export__policy.schema_pin.missing_spec_version_zero
          assert:
            std.logic.eq:
              - std.object.get:
                  - {var: subject}
                  - missing_spec_version_count
              - 0
        - id: __export__policy.schema_pin.missing_schema_ref_zero
          assert:
            std.logic.eq:
              - std.object.get:
                  - {var: subject}
                  - missing_schema_ref_count
              - 0
        - id: __export__policy.schema_pin.unknown_schema_ref_zero
          assert:
            std.logic.eq:
              - std.object.get:
                  - {var: subject}
                  - unknown_schema_ref_count
              - 0
        - id: __export__policy.schema_pin.version_match_zero
          assert:
            std.logic.eq:
              - std.object.get:
                  - {var: subject}
                  - mismatched_version_count
              - 0
    harness:
      exports:
        - as: policy.schema_pin.missing_spec_version_zero
          from: assert.function
          path: /__export__policy.schema_pin.missing_spec_version_zero
          params: [subject]
          required: true
        - as: policy.schema_pin.missing_schema_ref_zero
          from: assert.function
          path: /__export__policy.schema_pin.missing_schema_ref_zero
          params: [subject]
          required: true
        - as: policy.schema_pin.unknown_schema_ref_zero
          from: assert.function
          path: /__export__policy.schema_pin.unknown_schema_ref_zero
          params: [subject]
          required: true
        - as: policy.schema_pin.version_match_zero
          from: assert.function
          path: /__export__policy.schema_pin.version_match_zero
          params: [subject]
          required: true
    library:
      id: policy.schema.pin
      module: policy
      stability: alpha
      owner: data-contracts
      tags: [policy, schema]
  - id: LIB-POLICY-SCHEMA-PIN-900
    type: contract.check
    title: schema pin policy library smoke
    harness:
      check:
        profile: text.file
        config: {}
      use:
        - ref: '#LIB-POLICY-SCHEMA-PIN-001'
          as: lib_policy_schema_pin
          symbols:
            - policy.schema_pin.missing_spec_version_zero
            - policy.schema_pin.missing_schema_ref_zero
            - policy.schema_pin.unknown_schema_ref_zero
            - policy.schema_pin.version_match_zero
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [text]
      predicates:
        - id: assert_1
          assert:
            - call:
                - {var: policy.schema_pin.missing_spec_version_zero}
                - lit: {missing_spec_version_count: 0}
            - call:
                - {var: policy.schema_pin.missing_schema_ref_zero}
                - lit: {missing_schema_ref_count: 0}
            - call:
                - {var: policy.schema_pin.unknown_schema_ref_zero}
                - lit: {unknown_schema_ref_count: 0}
            - call:
                - {var: policy.schema_pin.version_match_zero}
                - lit: {mismatched_version_count: 0}
```


