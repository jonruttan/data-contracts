```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: LIB-POLICY-GOV-CATALOG-001
  type: contract.export
  title: governance catalog extractor predicates
  clauses:
    predicates:
    - id: __export__policy.catalog.duplicate_ids_zero
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - duplicate_case_id_count
        - 0
    - id: __export__policy.catalog.unmapped_checks_zero
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - unmapped_case_check_count
        - 0
    - id: __export__policy.catalog.multi_tier_collisions_zero
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - multi_tier_case_check_count
        - 0
    - id: __export__policy.catalog.check_field_presence_zero
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - missing_case_check_field_count
        - 0
  harness:
    exports:
    - as: policy.catalog.duplicate_ids_zero
      from: assert.function
      path: "/__export__policy.catalog.duplicate_ids_zero"
      params:
      - subject
      required: true
    - as: policy.catalog.unmapped_checks_zero
      from: assert.function
      path: "/__export__policy.catalog.unmapped_checks_zero"
      params:
      - subject
      required: true
    - as: policy.catalog.multi_tier_collisions_zero
      from: assert.function
      path: "/__export__policy.catalog.multi_tier_collisions_zero"
      params:
      - subject
      required: true
    - as: policy.catalog.check_field_presence_zero
      from: assert.function
      path: "/__export__policy.catalog.check_field_presence_zero"
      params:
      - subject
      required: true
  library:
    id: policy.governance.catalog
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
    - governance
- id: LIB-POLICY-GOV-CATALOG-900
  type: contract.check
  title: governance catalog policy library smoke
  harness:
    check:
      profile: text.file
      config: {}
    use:
    - ref: "#LIB-POLICY-GOV-CATALOG-001"
      as: lib_policy_gov_catalog
      symbols:
      - policy.catalog.duplicate_ids_zero
      - policy.catalog.unmapped_checks_zero
      - policy.catalog.multi_tier_collisions_zero
      - policy.catalog.check_field_presence_zero
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.catalog.duplicate_ids_zero
        - lit:
            duplicate_case_id_count: 0
      - call:
        - var: policy.catalog.unmapped_checks_zero
        - lit:
            unmapped_case_check_count: 0
      - call:
        - var: policy.catalog.multi_tier_collisions_zero
        - lit:
            multi_tier_case_check_count: 0
      - call:
        - var: policy.catalog.check_field_presence_zero
        - lit:
            missing_case_check_field_count: 0
```


