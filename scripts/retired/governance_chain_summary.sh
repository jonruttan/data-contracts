#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

SUMMARY_FILE=".artifacts/governance-summary.json"
OUT_JSON=".artifacts/governance-chain-summary.json"
OUT_MD=".artifacts/governance-chain-summary.md"

if [[ ! -f "${SUMMARY_FILE}" ]]; then
  echo "ERROR: missing governance summary artifact: ${SUMMARY_FILE}" >&2
  exit 1
fi

jq -n \
  --arg generated_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --argjson checks "$(jq '[.checks[] | select(.check_id | test("pipeline_chain|chain_entry_cases_present|policy_library_exports_resolve"))]' "${SUMMARY_FILE}")" \
  '{generated_at:$generated_at, checks:$checks}' > "${OUT_JSON}"

{
  echo "# Governance Chain Summary"
  echo
  jq -r '.checks[] | "- \(.check_id): \(.status)"' "${OUT_JSON}"
} > "${OUT_MD}"

echo "wrote ${OUT_JSON}"
echo "wrote ${OUT_MD}"
