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
    - "{'root': '.', 'ci_ingest_job': {'path': '/.github/workflows/ci.yml', 'required_tokens':
      [{'runner-status-ingest': None}, './scripts/runner_status_ingest.sh --max-age-hours
      72 --enforce-freshness']}, 'check': {'profile': 'governance.scan', 'config':
      {'check': 'runtime.status_ingest_job_present'}}}"
services:
  actions:
  - id: svc.root_ci_ingest_job_path_github_workflows_ci_yml_required_tokens_runner_status_ingest_none_scripts_runner_status_ingest_sh_max_age_hours_72_enforce_freshness_check_profile_governance_scan_config_check_runtime_status_ingest_job_present.default.1
    type: legacy.root_ci_ingest_job_path_github_workflows_ci_yml_required_tokens_runner_status_ingest_none_scripts_runner_status_ingest_sh_max_age_hours_72_enforce_freshness_check_profile_governance_scan_config_check_runtime_status_ingest_job_present
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CI-002
  title: status ingest job present in ci
  purpose: Ensures CI includes a status-ingest control-plane job.
  clauses:
    imports:
    - artifact:
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
