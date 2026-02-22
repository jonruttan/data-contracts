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
    - "{'root': '.', 'ci_matrix_artifacts': {'path': '/.github/workflows/ci.yml',
      'required_tokens': ['.artifacts/runner-status-matrix.json', '.artifacts/runner-status-matrix.md',
      '.artifacts/runner-status-ingest-log.json']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'runtime.matrix_artifacts_emitted'}}}"
services:
- id: svc.root_ci_matrix_artifacts_path_github_workflows_ci_yml_required_tokens_artifacts_runner_status_matrix_json_artifacts_runner_status_matrix_md_artifacts_runner_status_ingest_log_json_check_profile_governance_scan_config_check_runtime_matrix_artifacts_emitted.default.1
  type: legacy.root_ci_matrix_artifacts_path_github_workflows_ci_yml_required_tokens_artifacts_runner_status_matrix_json_artifacts_runner_status_matrix_md_artifacts_runner_status_ingest_log_json_check_profile_governance_scan_config_check_runtime_matrix_artifacts_emitted
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-RUNTIME-CI-003
  title: matrix artifacts are emitted in ci
  purpose: Ensures CI publishes canonical status matrix artifacts.
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
