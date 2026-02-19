#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

REGISTRY_PATH="/specs/schema/runner_certification_registry_v1.yaml"
OUT_JSON="/.artifacts/runner-status-matrix.json"
OUT_MD="/.artifacts/runner-status-matrix.md"
OUT_LOG_JSON="/.artifacts/runner-status-ingest-log.json"
MAX_AGE_HOURS="${RUNNER_STATUS_MAX_AGE_HOURS:-72}"
ENFORCE_FRESHNESS=0
NOW_UTC="${RUNNER_STATUS_NOW_UTC:-$(date -u +%Y-%m-%dT%H:%M:%SZ)}"

usage() {
  cat <<'EOF'
Usage: ./scripts/runner_status_ingest.sh [options]

Options:
  --registry <path>        Runner certification registry path (default: /specs/schema/runner_certification_registry_v1.yaml)
  --out-json <path>        Matrix JSON output path (default: /.artifacts/runner-status-matrix.json)
  --out-md <path>          Matrix Markdown output path (default: /.artifacts/runner-status-matrix.md)
  --log-json <path>        Ingest log output path (default: /.artifacts/runner-status-ingest-log.json)
  --max-age-hours <int>    Freshness SLO in hours (default: 72)
  --enforce-freshness      Exit non-zero when active compatibility telemetry is stale or missing
  --now-utc <rfc3339>      Override current UTC time (test support)
EOF
}

to_abs_path() {
  local p="$1"
  if [[ "${p}" == /* ]]; then
    echo "${ROOT_DIR}${p}"
  else
    echo "${ROOT_DIR}/${p}"
  fi
}

iso_to_epoch() {
  local iso="$1"
  jq -nr --arg iso "${iso}" '$iso | fromdateiso8601' 2>/dev/null || return 1
}

read_report_json() {
  local report_path="$1"
  jq -c . "${report_path}" 2>/dev/null || return 1
}

require_tool() {
  local tool="$1"
  if ! command -v "${tool}" >/dev/null 2>&1; then
    echo "ERROR: required tool not found: ${tool}" >&2
    exit 2
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --registry)
      REGISTRY_PATH="$2"
      shift 2
      ;;
    --out-json)
      OUT_JSON="$2"
      shift 2
      ;;
    --out-md)
      OUT_MD="$2"
      shift 2
      ;;
    --log-json)
      OUT_LOG_JSON="$2"
      shift 2
      ;;
    --max-age-hours)
      MAX_AGE_HOURS="$2"
      shift 2
      ;;
    --enforce-freshness)
      ENFORCE_FRESHNESS=1
      shift
      ;;
    --now-utc)
      NOW_UTC="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

require_tool php
require_tool jq
require_tool curl
require_tool shasum

REGISTRY_FILE="$(to_abs_path "${REGISTRY_PATH}")"
OUT_JSON_FILE="$(to_abs_path "${OUT_JSON}")"
OUT_MD_FILE="$(to_abs_path "${OUT_MD}")"
OUT_LOG_FILE="$(to_abs_path "${OUT_LOG_JSON}")"

mkdir -p "$(dirname "${OUT_JSON_FILE}")"
mkdir -p "$(dirname "${OUT_MD_FILE}")"
mkdir -p "$(dirname "${OUT_LOG_FILE}")"

if [[ ! -f "${REGISTRY_FILE}" ]]; then
  echo "ERROR: registry file not found: ${REGISTRY_FILE}" >&2
  exit 2
fi

if ! NOW_EPOCH="$(iso_to_epoch "${NOW_UTC}")"; then
  echo "ERROR: --now-utc must be RFC3339 UTC, got '${NOW_UTC}'" >&2
  exit 2
fi

REGISTRY_JSON="$(php -r '
$data = yaml_parse_file($argv[1]);
if ($data === false) {
  fwrite(STDERR, "ERROR: failed parsing YAML registry\n");
  exit(2);
}
echo json_encode($data, JSON_UNESCAPED_SLASHES);
' "${REGISTRY_FILE}")"

RUNNER_ROWS='[]'
LOG_ROWS='[]'
COMPAT_STALE_OR_MISSING=0

while IFS= read -r runner; do
  runner_id="$(jq -r '.runner_id' <<<"${runner}")"
  runner_class="$(jq -r '.class' <<<"${runner}")"
  runner_status="$(jq -r '.status' <<<"${runner}")"
  impl_repo="$(jq -r '.entrypoints.implementation_repo // "unknown"' <<<"${runner}")"
  release_api_url="$(jq -r '.status_exchange.release_api_url // empty' <<<"${runner}")"
  report_asset_name="$(jq -r '.status_exchange.report_asset_name // "runner-status-report-v1.json"' <<<"${runner}")"
  runner_slo="$(jq -r '.status_exchange.freshness_slo_hours // empty' <<<"${runner}")"
  if [[ -z "${runner_slo}" || "${runner_slo}" == "null" ]]; then
    runner_slo="${MAX_AGE_HOURS}"
  fi

  freshness_state="missing"
  policy_effect="non_blocking_warn"
  overall_status="unknown"
  release_version=""
  report_generated_at=""
  source_url=""
  sha256_reported=""
  error=""
  age_hours=""

  if [[ "${runner_status}" == "planned" ]]; then
    freshness_state="missing"
    policy_effect="non_blocking_warn"
    error="planned lane (no active status exchange required)"
  elif [[ -z "${release_api_url}" ]]; then
    error="status_exchange.release_api_url missing"
  else
    release_json=""
    set +e
    release_json="$(curl --fail --location --silent --show-error "${release_api_url}")"
    curl_code=$?
    set -e
    if [[ "${curl_code}" -ne 0 || -z "${release_json}" ]]; then
      error="failed fetching release metadata"
    else
      release_version="$(jq -r '.tag_name // empty' <<<"${release_json}")"
      source_url="$(jq -r --arg name "${report_asset_name}" '.assets[]? | select(.name == $name) | .browser_download_url' <<<"${release_json}" | head -n1)"
      sha256_reported="$(jq -r --arg name "${report_asset_name}" '.assets[]? | select(.name == $name) | (.digest // "")' <<<"${release_json}" | head -n1)"
      sha256_reported="${sha256_reported#sha256:}"

      if [[ -z "${source_url}" ]]; then
        error="missing report asset '${report_asset_name}'"
      else
        tmp_report="$(mktemp)"
        set +e
        curl --fail --location --silent --show-error "${source_url}" --output "${tmp_report}"
        fetch_code=$?
        set -e
        if [[ "${fetch_code}" -ne 0 ]]; then
          error="failed downloading report asset"
        else
          if [[ -n "${sha256_reported}" ]]; then
            downloaded_sha="$(shasum -a 256 "${tmp_report}" | awk '{print $1}')"
            if [[ "${downloaded_sha}" != "${sha256_reported}" ]]; then
              error="checksum mismatch for report asset"
            fi
          fi
          if [[ -z "${error}" ]]; then
            if report_json="$(read_report_json "${tmp_report}")"; then
              overall_status="$(jq -r '.overall_status // "unknown"' <<<"${report_json}")"
              report_generated_at="$(jq -r '.generated_at // empty' <<<"${report_json}")"
              if [[ -n "${report_generated_at}" ]] && report_epoch="$(iso_to_epoch "${report_generated_at}")"; then
                age_hours="$(( (NOW_EPOCH - report_epoch) / 3600 ))"
                if [[ "${age_hours}" -le "${runner_slo}" ]]; then
                  freshness_state="fresh"
                else
                  freshness_state="stale"
                fi
              else
                freshness_state="missing"
                error="report missing valid generated_at"
              fi
            else
              error="invalid report JSON"
            fi
          fi
        fi
        rm -f "${tmp_report}"
      fi
    fi
  fi

  if [[ "${runner_class}" == "required" ]]; then
    if [[ "${overall_status}" == "fail" || "${overall_status}" == "degraded" || "${overall_status}" == "unknown" || "${freshness_state}" == "missing" ]]; then
      policy_effect="blocking_fail"
    else
      policy_effect="non_blocking_warn"
    fi
  else
    if [[ "${freshness_state}" == "stale" || "${freshness_state}" == "missing" ]]; then
      policy_effect="non_blocking_fail"
      if [[ "${runner_status}" == "active" ]]; then
        COMPAT_STALE_OR_MISSING=$((COMPAT_STALE_OR_MISSING + 1))
      fi
    else
      policy_effect="non_blocking_warn"
    fi
  fi

  row="$(jq -cn \
    --arg runner_id "${runner_id}" \
    --arg implementation_repo "${impl_repo}" \
    --arg lane_class "${runner_class}" \
    --arg runner_status "${overall_status}" \
    --arg freshness_state "${freshness_state}" \
    --arg policy_effect "${policy_effect}" \
    --arg release_version "${release_version}" \
    --arg generated_at "${report_generated_at}" \
    --arg source_url "${source_url}" \
    --arg age_hours "${age_hours}" \
    '{
      runner_id: $runner_id,
      implementation_repo: $implementation_repo,
      lane_class: $lane_class,
      runner_status: $runner_status,
      freshness_state: $freshness_state,
      policy_effect: $policy_effect,
      status_source: {
        release_version: $release_version,
        report_url: $source_url
      },
      status_report: {
        generated_at: $generated_at,
        age_hours: (if $age_hours == "" then null else ($age_hours|tonumber) end)
      }
    }')"
  RUNNER_ROWS="$(jq -c --argjson row "${row}" '. + [$row]' <<<"${RUNNER_ROWS}")"

  log_row="$(jq -cn \
    --arg runner_id "${runner_id}" \
    --arg implementation_repo "${impl_repo}" \
    --arg release_api_url "${release_api_url}" \
    --arg report_asset_name "${report_asset_name}" \
    --arg source_url "${source_url}" \
    --arg freshness_state "${freshness_state}" \
    --arg policy_effect "${policy_effect}" \
    --arg error "${error}" \
    '{
      runner_id: $runner_id,
      implementation_repo: $implementation_repo,
      release_api_url: $release_api_url,
      report_asset_name: $report_asset_name,
      report_url: $source_url,
      freshness_state: $freshness_state,
      policy_effect: $policy_effect,
      error: (if $error == "" then null else $error end)
    }')"
  LOG_ROWS="$(jq -c --argjson row "${log_row}" '. + [$row]' <<<"${LOG_ROWS}")"
done < <(jq -c '.runners[]' <<<"${REGISTRY_JSON}")

MATRIX_JSON="$(jq -cn \
  --arg updated_at "${NOW_UTC}" \
  --argjson matrix_rows "${RUNNER_ROWS}" \
  '{version: 1, updated_at: $updated_at, matrix_rows: $matrix_rows}')"

LOG_JSON="$(jq -cn \
  --arg generated_at "${NOW_UTC}" \
  --argjson max_age_hours "${MAX_AGE_HOURS}" \
  --argjson compat_stale_or_missing "${COMPAT_STALE_OR_MISSING}" \
  --argjson entries "${LOG_ROWS}" \
  '{
    version: 1,
    generated_at: $generated_at,
    max_age_hours: $max_age_hours,
    compatibility_stale_or_missing_count: $compat_stale_or_missing,
    entries: $entries
  }')"

printf '%s\n' "${MATRIX_JSON}" > "${OUT_JSON_FILE}"
printf '%s\n' "${LOG_JSON}" > "${OUT_LOG_FILE}"

{
  echo "# Runner Status Matrix"
  echo
  echo "- updated_at: \`${NOW_UTC}\`"
  echo "- freshness_slo_hours: \`${MAX_AGE_HOURS}\`"
  echo "- compatibility_stale_or_missing_count: \`${COMPAT_STALE_OR_MISSING}\`"
  echo
  echo "| runner_id | class | status | freshness | policy_effect |"
  echo "|---|---|---|---|---|"
  jq -r '.matrix_rows[] | "| \(.runner_id) | \(.lane_class) | \(.runner_status) | \(.freshness_state) | \(.policy_effect) |"' "${OUT_JSON_FILE}"
} > "${OUT_MD_FILE}"

if [[ "${ENFORCE_FRESHNESS}" == "1" && "${COMPAT_STALE_OR_MISSING}" -gt 0 ]]; then
  echo "ERROR: compatibility status freshness policy violation count=${COMPAT_STALE_OR_MISSING}" >&2
  exit 1
fi

echo "wrote ${OUT_JSON_FILE}"
echo "wrote ${OUT_MD_FILE}"
echo "wrote ${OUT_LOG_FILE}"

