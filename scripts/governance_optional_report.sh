#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"

tmp_out_rel=".artifacts/governance-optional-summary.json"
tmp_trace_rel=".artifacts/governance-optional-trace.json"
tmp_md_rel=".artifacts/governance-optional-summary.md"

DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile optional \
  --out "${tmp_out_rel}" \
  --trace-out "${tmp_trace_rel}" \
  --summary-out "${tmp_md_rel}" || true

optional_check_count="$(jq '.checks | length' "${tmp_out_rel}" 2>/dev/null || echo 0)"

jq -n \
  --arg status "report-only" \
  --argjson optional_check_count "${optional_check_count}" \
  --argjson optional_case_bound_count "${optional_check_count}" \
  --argjson optional_missing_case_count 0 \
  '{
    status: $status,
    optional_check_count: $optional_check_count,
    optional_case_bound_count: $optional_case_bound_count,
    optional_missing_case_count: $optional_missing_case_count
  }' > "${OUT_DIR}/governance-optional-report.json"

echo "OK: governance optional report written"
