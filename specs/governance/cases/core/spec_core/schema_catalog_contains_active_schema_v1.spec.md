```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'schema_catalog': {'path': '/specs/schema/schema_catalog_v1.yaml', 'required_tokens': [{'schema_id': 'contract_spec'}, {'major': 2}, {'path': '/specs/schema/schema_v2.md'}, {'status': 'active'}]}, 'check': {'profile': 'governance.scan', 'config': {'check': 'schema.catalog_contains_active_schema_v2'}}}"
services:
  entries:
  - id: svc.root_schema_catalog_path_specs_schema_schema_catalog_v1_yaml_required_tokens_schema_id_contract_spec_major_2_path_specs_schema_schema_v2_md_status_active_check_profile_governance_scan_config_check_schema_catalog_contains_active_schema_v2.default.1
    type: legacy.root_schema_catalog_path_specs_schema_schema_catalog_v1_yaml_required_tokens_schema_id_contract_spec_major_2_path_specs_schema_schema_v2_md_status_active_check_profile_governance_scan_config_check_schema_catalog_contains_active_schema_v2
    io: io
    profile: default
contracts:
- id: DCGOV-SCHEMA-PIN-005
  title: schema catalog includes active contract-spec v2
  purpose: Ensures active schema catalog includes canonical contract-spec v2 entry.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```
