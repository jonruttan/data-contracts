#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/artifact_paths.sh"
source "${ROOT_DIR}/scripts/lib/yaml_to_json.sh"
source "${ROOT_DIR}/scripts/ingest/parse_args.sh"
source "${ROOT_DIR}/scripts/ingest/resolve_registry.sh"
source "${ROOT_DIR}/scripts/ingest/fetch_release_asset.sh"
source "${ROOT_DIR}/scripts/ingest/emit_matrix_artifacts.sh"
source "${ROOT_DIR}/scripts/ingest/emit_ingest_log.sh"

REGISTRY_PATH="/specs/schema/runner_certification_registry_v1.yaml"
OUT_JSON="/.artifacts/runner-status-matrix.json"
OUT_MD="/.artifacts/runner-status-matrix.md"
OUT_LOG_JSON="/.artifacts/runner-status-ingest-log.json"
MAX_AGE_HOURS="${RUNNER_STATUS_MAX_AGE_HOURS:-72}"
ENFORCE_FRESHNESS=0
NOW_UTC="${RUNNER_STATUS_NOW_UTC:-$(date -u +%Y-%m-%dT%H:%M:%SZ)}"

parse_ingest_args "$@"

require_tool php
require_tool jq
require_tool curl
require_tool shasum

REGISTRY_FILE="$(resolve_artifact_path "${ROOT_DIR}" "${REGISTRY_PATH}")"
OUT_JSON_FILE="$(resolve_artifact_path "${ROOT_DIR}" "${OUT_JSON}")"
OUT_MD_FILE="$(resolve_artifact_path "${ROOT_DIR}" "${OUT_MD}")"
OUT_LOG_FILE="$(resolve_artifact_path "${ROOT_DIR}" "${OUT_LOG_JSON}")"

ensure_parent_dir "${OUT_JSON_FILE}"
ensure_parent_dir "${OUT_MD_FILE}"
ensure_parent_dir "${OUT_LOG_FILE}"

if [[ ! -f "${REGISTRY_FILE}" ]]; then
  echo "ERROR: registry file not found: ${REGISTRY_FILE}" >&2
  exit 2
fi

if ! NOW_EPOCH="$(iso_to_epoch "${NOW_UTC}")"; then
  echo "ERROR: --now-utc must be RFC3339 UTC, got '${NOW_UTC}'" >&2
  exit 2
fi

REGISTRY_JSON="$(parse_yaml_file_to_json "${REGISTRY_FILE}")"

RUNNER_ROWS='[]'
LOG_ROWS='[]'
COMPAT_STALE_OR_MISSING=0

while IFS= read -r runner; do
  runner_id="$(jq -r '.runner_id' <<<"${runner}")"
  runner_class="$(jq -r '.class' <<<"${runner}")"
  runner_declared_status="$(jq -r '.status' <<<"${runner}")"
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

  if [[ "${runner_declared_status}" == "planned" ]]; then
    freshness_state="missing"
    policy_effect="non_blocking_warn"
    error="planned lane (no active status exchange required)"
  elif [[ -z "${release_api_url}" ]]; then
    error="status_exchange.release_api_url missing"
  else
    if ! release_json="$(fetch_release_json "${release_api_url}")"; then
      error="failed fetching release metadata"
    else
      meta_json="$(extract_release_asset_metadata "${release_json}" "${report_asset_name}")"
      release_version="$(jq -r '.release_version' <<<"${meta_json}")"
      source_url="$(jq -r '.source_url' <<<"${meta_json}")"
      sha256_reported="$(jq -r '.sha256_reported' <<<"${meta_json}")"

      if [[ -z "${source_url}" ]]; then
        error="missing report asset '${report_asset_name}'"
      else
        tmp_report="$(mktemp)"
        if ! download_report_asset "${source_url}" "${tmp_report}"; then
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
              if validate_report_shape "${report_json}"; then
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
                error="report schema validation failed"
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

  # Transport layer computes observable status fields for artifacts;
  # blocking policy is enforced in governance spec checks.
  if [[ "${runner_class}" == "required" ]]; then
    if [[ "${overall_status}" == "fail" || "${overall_status}" == "degraded" || "${overall_status}" == "unknown" || "${freshness_state}" == "missing" ]]; then
      policy_effect="blocking_fail"
    else
      policy_effect="non_blocking_warn"
    fi
  else
    if [[ "${freshness_state}" == "stale" || "${freshness_state}" == "missing" ]]; then
      policy_effect="non_blocking_fail"
      if [[ "${runner_declared_status}" == "active" ]]; then
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

MATRIX_JSON="$(emit_matrix_json "${NOW_UTC}" "${RUNNER_ROWS}")"
LOG_JSON="$(emit_ingest_log_json "${NOW_UTC}" "${MAX_AGE_HOURS}" "${COMPAT_STALE_OR_MISSING}" "${LOG_ROWS}")"

printf '%s\n' "${MATRIX_JSON}" > "${OUT_JSON_FILE}"
printf '%s\n' "${LOG_JSON}" > "${OUT_LOG_FILE}"
emit_matrix_markdown "${OUT_JSON_FILE}" "${OUT_MD_FILE}" "${NOW_UTC}" "${MAX_AGE_HOURS}" "${COMPAT_STALE_OR_MISSING}"

if [[ "${ENFORCE_FRESHNESS}" == "1" ]]; then
  echo "INFO: --enforce-freshness accepted for compatibility; policy decided by governance checks"
fi

echo "wrote ${OUT_JSON_FILE}"
echo "wrote ${OUT_MD_FILE}"
echo "wrote ${OUT_LOG_FILE}"
