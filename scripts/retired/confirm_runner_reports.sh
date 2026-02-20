#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

RUST_ROOT="${ROOT_DIR}/../dc-runner-rust"
RUST_REPORT="${RUST_ROOT}/.artifacts/runner-status-report-v1.json"
WORK_DIR="${ROOT_DIR}/.artifacts/confirm-runner-reports"
mkdir -p "${WORK_DIR}"

validate_report() {
  local path="$1"

  jq -e '
    (. | type == "object") and
    (.version == 1) and
    (.runner_id == "rust") and
    (.implementation_repo == "dc-runner-rust") and
    (.release_version | type == "string" and length > 0) and
    (.commit_sha | type == "string" and length > 0) and
    (.generated_at | type == "string" and length > 0) and
    (.lane_class == "required") and
    (.overall_status == "pass" or .overall_status == "fail" or .overall_status == "degraded" or .overall_status == "unknown") and
    (.fresh_until | type == "string" and length > 0) and
    (.command_results | type == "array" and length > 0) and
    (.artifact_refs | type == "array" and length > 0)
  ' "${path}" >/dev/null
}

if [[ ! -x "${RUST_ROOT}/scripts/emit_runner_status_report.sh" ]]; then
  echo "ERROR: missing rust producer command: ${RUST_ROOT}/scripts/emit_runner_status_report.sh" >&2
  exit 2
fi

"${RUST_ROOT}/scripts/emit_runner_status_report.sh" "${RUST_REPORT}"
validate_report "${RUST_REPORT}"

# Negative control: invalid version must fail validation.
jq '.version = 2' "${RUST_REPORT}" > "${WORK_DIR}/runner-status-report-v1.rust.invalid-version.json"
if validate_report "${WORK_DIR}/runner-status-report-v1.rust.invalid-version.json"; then
  echo "ERROR: expected invalid rust report version to fail validation" >&2
  exit 1
fi

SCENARIO_DIR="${WORK_DIR}/scenario"
mkdir -p "${SCENARIO_DIR}"
cp "${RUST_REPORT}" "${SCENARIO_DIR}/runner-status-report-v1.rust.json"
cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.python.json" "${SCENARIO_DIR}/runner-status-report-v1.python.json"
cp "${ROOT_DIR}/specs/conformance/cases/fixtures/status_exchange/runner-status-report-v1.php.json" "${SCENARIO_DIR}/runner-status-report-v1.php.json"

cat > "${SCENARIO_DIR}/local_release_rust.json" <<JSON
{
  "tag_name": "local-rust-report",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${SCENARIO_DIR}/runner-status-report-v1.rust.json"
    }
  ]
}
JSON
cat > "${SCENARIO_DIR}/local_release_python.json" <<JSON
{
  "tag_name": "local-python-fixture",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${SCENARIO_DIR}/runner-status-report-v1.python.json"
    }
  ]
}
JSON
cat > "${SCENARIO_DIR}/local_release_php.json" <<JSON
{
  "tag_name": "local-php-fixture",
  "assets": [
    {
      "name": "runner-status-report-v1.json",
      "browser_download_url": "file://${SCENARIO_DIR}/runner-status-report-v1.php.json"
    }
  ]
}
JSON

cat > "${SCENARIO_DIR}/registry.yaml" <<YAML
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
      release_api_url: file://${SCENARIO_DIR}/local_release_rust.json
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
      release_api_url: file://${SCENARIO_DIR}/local_release_python.json
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
      release_api_url: file://${SCENARIO_DIR}/local_release_php.json
      report_asset_name: runner-status-report-v1.json
      matrix_role: compatibility
      freshness_slo_hours: 72
YAML

./scripts/runner_status_ingest.sh \
  --registry "${SCENARIO_DIR#${ROOT_DIR}/}/registry.yaml" \
  --out-json ".artifacts/runner-status-matrix-rust-confirm.json" \
  --out-md ".artifacts/runner-status-matrix-rust-confirm.md" \
  --log-json ".artifacts/runner-status-ingest-log-rust-confirm.json" \
  --max-age-hours 72 \
  --enforce-freshness \
  --now-utc "2026-02-20T12:00:00Z"

jq -e '.matrix_rows[] | select(.runner_id == "rust") | .runner_status == "pass"' \
  .artifacts/runner-status-matrix-rust-confirm.json >/dev/null
jq -e '.matrix_rows[] | select(.runner_id == "rust") | .freshness_state == "fresh"' \
  .artifacts/runner-status-matrix-rust-confirm.json >/dev/null

echo "OK: runner report confirmation passed"
