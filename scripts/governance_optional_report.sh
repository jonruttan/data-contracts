#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/scan_check_sets.sh"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"

optional_ids_tmp="$(mktemp)"
case_checks_tmp="$(mktemp)"
trap 'rm -f "${optional_ids_tmp}" "${case_checks_tmp}"' EXIT

emit_optional_check_ids "specs/governance/check_sets_v1.yaml" > "${optional_ids_tmp}"

while IFS= read -r f; do
  check_id="$(awk '
    BEGIN { in_config=0 }
    /^[[:space:]]*config:[[:space:]]*$/ { in_config=1; next }
    in_config && /^[[:space:]]*check:[[:space:]]*/ {
      sub(/^[[:space:]]*check:[[:space:]]*/, "", $0)
      print $0
      exit
    }
  ' "${f}")"
  if [[ -n "${check_id}" ]]; then
    printf '%s|%s\n' "${check_id}" "${f}" >> "${case_checks_tmp}"
  fi
done < <(find specs/governance/cases/core -type f -name '*.spec.md' | sort)

optional_check_count="$(wc -l < "${optional_ids_tmp}" | tr -d ' ')"
optional_case_bound_count=0
optional_missing_case_count=0

summary_file="${OUT_DIR}/governance-optional-summary.md"
{
  echo "# Governance Optional Summary"
  echo
} > "${summary_file}"

while IFS= read -r id; do
  count="$(awk -F'|' -v c="${id}" '$1==c {n++} END {print n+0}' "${case_checks_tmp}")"
  if [[ "${count}" -gt 0 ]]; then
    optional_case_bound_count=$((optional_case_bound_count + 1))
  else
    optional_missing_case_count=$((optional_missing_case_count + 1))
  fi
done < "${optional_ids_tmp}"

{
  echo "- optional_check_count: \`${optional_check_count}\`"
  echo "- optional_case_bound_count: \`${optional_case_bound_count}\`"
  echo "- optional_missing_case_count: \`${optional_missing_case_count}\`"
  while IFS= read -r id; do
    count="$(awk -F'|' -v c="${id}" '$1==c {n++} END {print n+0}' "${case_checks_tmp}")"
    echo "- \`${id}\` cases: \`${count}\`"
  done < "${optional_ids_tmp}"
} >> "${summary_file}"

jq -n \
  --arg status "report-only" \
  --argjson optional_check_count "${optional_check_count}" \
  --argjson optional_case_bound_count "${optional_case_bound_count}" \
  --argjson optional_missing_case_count "${optional_missing_case_count}" \
  '{
    status: $status,
    optional_check_count: $optional_check_count,
    optional_case_bound_count: $optional_case_bound_count,
    optional_missing_case_count: $optional_missing_case_count
  }' > "${OUT_DIR}/governance-optional-report.json"

echo "OK: governance optional report written"
