# Governance Catalog Policy Library

## LIB-POLICY-GOV-CATALOG-001

```yaml contract-spec
id: LIB-POLICY-GOV-CATALOG-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
title: governance catalog extractor predicates
contract:
  defaults: {}
  steps:
    - id: __export__policy.catalog.duplicate_ids_zero
      assert:
        std.logic.eq:
          - std.object.get:
              - {var: subject}
              - duplicate_case_id_count
          - 0
    - id: __export__policy.catalog.unmapped_checks_zero
      assert:
        std.logic.eq:
          - std.object.get:
              - {var: subject}
              - unmapped_case_check_count
          - 0
    - id: __export__policy.catalog.multi_tier_collisions_zero
      assert:
        std.logic.eq:
          - std.object.get:
              - {var: subject}
              - multi_tier_case_check_count
          - 0
    - id: __export__policy.catalog.check_field_presence_zero
      assert:
        std.logic.eq:
          - std.object.get:
              - {var: subject}
              - missing_case_check_field_count
          - 0
harness:
  exports:
    - as: policy.catalog.duplicate_ids_zero
      from: assert.function
      path: /__export__policy.catalog.duplicate_ids_zero
      params: [subject]
      required: true
    - as: policy.catalog.unmapped_checks_zero
      from: assert.function
      path: /__export__policy.catalog.unmapped_checks_zero
      params: [subject]
      required: true
    - as: policy.catalog.multi_tier_collisions_zero
      from: assert.function
      path: /__export__policy.catalog.multi_tier_collisions_zero
      params: [subject]
      required: true
    - as: policy.catalog.check_field_presence_zero
      from: assert.function
      path: /__export__policy.catalog.check_field_presence_zero
      params: [subject]
      required: true
library:
  id: policy.governance.catalog
  module: policy
  stability: alpha
  owner: data-contracts
  tags: [policy, governance]
```

## LIB-POLICY-GOV-CATALOG-900

```yaml contract-spec
id: LIB-POLICY-GOV-CATALOG-900
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: governance catalog policy library smoke
harness:
  check:
    profile: text.file
    config: {}
  use:
    - ref: '#LIB-POLICY-GOV-CATALOG-001'
      as: lib_policy_gov_catalog
      symbols:
        - policy.catalog.duplicate_ids_zero
        - policy.catalog.unmapped_checks_zero
        - policy.catalog.multi_tier_collisions_zero
        - policy.catalog.check_field_presence_zero
contract:
  defaults: {}
  imports:
    - from: artifact
      names: [text]
  steps:
    - id: assert_1
      assert:
        - call:
            - {var: policy.catalog.duplicate_ids_zero}
            - lit: {duplicate_case_id_count: 0}
        - call:
            - {var: policy.catalog.unmapped_checks_zero}
            - lit: {unmapped_case_check_count: 0}
        - call:
            - {var: policy.catalog.multi_tier_collisions_zero}
            - lit: {multi_tier_case_check_count: 0}
        - call:
            - {var: policy.catalog.check_field_presence_zero}
            - lit: {missing_case_check_field_count: 0}
```
