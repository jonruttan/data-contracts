#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

WORK_DIR="${ROOT_DIR}/.artifacts/local-status-exchange"
mkdir -p "${WORK_DIR}"

seed_fixture_set() {
  local scenario_dir="$1"
  mkdir -p "${scenario_dir}"
  cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.rust.json" "${scenario_dir}/runner-status-report-v1.rust.json"
  cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.python.json" "${scenario_dir}/runner-status-report-v1.python.json"
  cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.php.json" "${scenario_dir}/runner-status-report-v1.php.json"
  cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.invalid.json" "${scenario_dir}/runner-status-report-v1.invalid.json"

  cat > "${scenario_dir}/local_release_rust.json" <<JSON
{
  "tag_name": "local-test",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${scenario_dir}/runner-status-report-v1.rust.json"
    }
  ]
}
JSON
  cat > "${scenario_dir}/local_release_python.json" <<JSON
{
  "tag_name": "local-test",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${scenario_dir}/runner-status-report-v1.python.json"
    }
  ]
}
JSON
  cat > "${scenario_dir}/local_release_php.json" <<JSON
{
  "tag_name": "local-test",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${scenario_dir}/runner-status-report-v1.php.json"
    }
  ]
}
JSON

  cat > "${scenario_dir}/registry.yaml" <<YAML
version: 1
runners:
  - runner_id: rust
    class: required
    status: active
    entrypoints:
      public_adapter: /scripts/runner_bin.sh
      implementation_repo: dc-runner-rust
    required_core_checks: []
    required_core_cases: []
    command_contract_subset: []
    artifact_contract:
      json_out: /.artifacts/runner-certification-{runner}.json
      md_out: /.artifacts/runner-certification-{runner}.md
    status_exchange:
      source_kind: release_asset
      release_api_url: file://${scenario_dir}/local_release_rust.json
      report_asset_name: runner-status-report-v1.json
      matrix_role: required
      freshness_slo_hours: 72

  - runner_id: python
    class: compatibility_non_blocking
    status: active
    entrypoints:
      public_adapter: /scripts/runner_bin.sh
      implementation_repo: dc-runner-python
    required_core_checks: []
    required_core_cases: []
    command_contract_subset: []
    artifact_contract:
      json_out: /.artifacts/runner-certification-{runner}.json
      md_out: /.artifacts/runner-certification-{runner}.md
    status_exchange:
      source_kind: release_asset
      release_api_url: file://${scenario_dir}/local_release_python.json
      report_asset_name: runner-status-report-v1.json
      matrix_role: compatibility
      freshness_slo_hours: 72

  - runner_id: php
    class: compatibility_non_blocking
    status: active
    entrypoints:
      public_adapter: /scripts/runner_bin.sh
      implementation_repo: dc-runner-php
    required_core_checks: []
    required_core_cases: []
    command_contract_subset: []
    artifact_contract:
      json_out: /.artifacts/runner-certification-{runner}.json
      md_out: /.artifacts/runner-certification-{runner}.md
    status_exchange:
      source_kind: release_asset
      release_api_url: file://${scenario_dir}/local_release_php.json
      report_asset_name: runner-status-report-v1.json
      matrix_role: compatibility
      freshness_slo_hours: 72
YAML
}

run_ingest() {
  local scenario="$1"
  local now_utc="$2"
  local enforce="$3"
  local expected_status="$4"

  local scenario_dir="${WORK_DIR}/${scenario}"
  seed_fixture_set "${scenario_dir}"

  case "${scenario}" in
    stale)
      # Move time beyond freshness SLO to force compatibility stale handling.
      ;;
    missing)
      # Break compatibility report source so ingest reports missing.
      jq '.assets[0].browser_download_url = "file:///does/not/exist/runner-status-report-v1.json"' \
        "${scenario_dir}/local_release_python.json" > "${scenario_dir}/local_release_python.tmp" \
        && mv "${scenario_dir}/local_release_python.tmp" "${scenario_dir}/local_release_python.json"
      ;;
    invalid)
      # Use invalid payload for php to validate error logging while matrix is still emitted.
      jq '.assets[0].browser_download_url = "file://'"${scenario_dir}"'/runner-status-report-v1.invalid.json"' \
        "${scenario_dir}/local_release_php.json" > "${scenario_dir}/local_release_php.tmp" \
        && mv "${scenario_dir}/local_release_php.tmp" "${scenario_dir}/local_release_php.json"
      ;;
  esac

  local out_json=".artifacts/runner-status-matrix-${scenario}.json"
  local out_md=".artifacts/runner-status-matrix-${scenario}.md"
  local out_log=".artifacts/runner-status-ingest-log-${scenario}.json"
  local rel_registry="${scenario_dir#${ROOT_DIR}/}/registry.yaml"

  set +e
  if [[ "${enforce}" == "enforce" ]]; then
    ./scripts/runner_status_ingest.sh \
      --registry "${rel_registry}" \
      --out-json "${out_json}" \
      --out-md "${out_md}" \
      --log-json "${out_log}" \
      --max-age-hours 72 \
      --enforce-freshness \
      --now-utc "${now_utc}"
    code=$?
  else
    ./scripts/runner_status_ingest.sh \
      --registry "${rel_registry}" \
      --out-json "${out_json}" \
      --out-md "${out_md}" \
      --log-json "${out_log}" \
      --max-age-hours 72 \
      --now-utc "${now_utc}"
    code=$?
  fi
  set -e

  if [[ "${expected_status}" == "pass" && "${code}" -ne 0 ]]; then
    echo "ERROR: scenario ${scenario} expected pass, got exit ${code}" >&2
    return 1
  fi
  if [[ "${expected_status}" == "fail" && "${code}" -eq 0 ]]; then
    echo "ERROR: scenario ${scenario} expected fail, got exit 0" >&2
    return 1
  fi

  test -f "${ROOT_DIR}/${out_json}"
  test -f "${ROOT_DIR}/${out_md}"
  test -f "${ROOT_DIR}/${out_log}"

  if [[ "${scenario}" == "invalid" ]]; then
    jq -e '.entries[] | select(.runner_id == "php") | .error | strings' "${ROOT_DIR}/${out_log}" >/dev/null
  fi
}

run_ingest fresh "2026-02-20T12:00:00Z" enforce pass
run_ingest stale "2026-02-24T12:00:00Z" enforce fail
run_ingest missing "2026-02-20T12:00:00Z" enforce fail
run_ingest invalid "2026-02-20T12:00:00Z" no_enforce pass

echo "OK: local status exchange scenarios passed"
