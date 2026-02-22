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
    - "{'root': '.', 'status_ingestion': {'files': ['/scripts/runner_status_ingest.sh', '/specs/schema/runner_certification_registry_v2.yaml'], 'required_tokens': ['release_api_url', 'report_asset_name', 'runner-status-matrix.json', 'runner-status-ingest-log.json']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.compatibility_status_ingestion_configured'}}}"
services:
  entries:
  - id: svc.root_status_ingestion_files_scripts_runner_status_ingest_sh_specs_schema_runner_certification_registry_v2_yaml_required_tokens_release_api_url_report_asset_name_runner_status_matrix_json_runner_status_ingest_log_json_check_profile_governance_scan_config_check_runtime_compatibility_status_ingestion_configured.default.1
    type: legacy.root_status_ingestion_files_scripts_runner_status_ingest_sh_specs_schema_runner_certification_registry_v2_yaml_required_tokens_release_api_url_report_asset_name_runner_status_matrix_json_runner_status_ingest_log_json_check_profile_governance_scan_config_check_runtime_compatibility_status_ingestion_configured
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-STATUS-003
  title: compatibility status ingestion is configured
  purpose: Ensures status exchange ingestion is wired to release assets and matrix artifacts.
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

