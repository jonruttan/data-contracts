#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/scan_case_ids.sh"
source "${ROOT_DIR}/scripts/lib/scan_check_sets.sh"
source "${ROOT_DIR}/scripts/lib/artifact_paths.sh"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"
# Canonical artifact contract path: .artifacts/governance-catalog-validate.json

core_checks_tmp="$(mktemp)"
set_ids_tmp="$(mktemp)"
trap 'rm -f "${core_checks_tmp}" "${set_ids_tmp}"' EXIT

duplicate_case_id_count="$(count_duplicate_case_ids "${ROOT_DIR}")"

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
    printf '%s|%s\n' "${f}" "${check_id}" >> "${core_checks_tmp}"
  else
    printf '%s|\n' "${f}" >> "${core_checks_tmp}"
  fi
done < <(find specs/governance/cases/core -type f -name '*.spec.md' | sort)

emit_check_set_id_profile_pairs "specs/governance/check_sets_v1.yaml" > "${set_ids_tmp}"

missing_case_check_field_count=0
unmapped_case_check_count=0
multi_tier_case_check_count=0

while IFS='|' read -r path check; do
  if [[ -z "${check}" ]]; then
    missing_case_check_field_count=$((missing_case_check_field_count + 1))
    continue
  fi
  matches="$(awk -F'|' -v c="${check}" '$1==c {print $2}' "${set_ids_tmp}" | wc -l | tr -d ' ')"
  if [[ "${matches}" -eq 0 ]]; then
    unmapped_case_check_count=$((unmapped_case_check_count + 1))
  fi
  if [[ "${matches}" -ne 1 ]]; then
    multi_tier_case_check_count=$((multi_tier_case_check_count + 1))
  fi
done < "${core_checks_tmp}"

jq -n \
  --argjson duplicate_case_id_count "${duplicate_case_id_count}" \
  --argjson missing_case_check_field_count "${missing_case_check_field_count}" \
  --argjson unmapped_case_check_count "${unmapped_case_check_count}" \
  --argjson multi_tier_case_check_count "${multi_tier_case_check_count}" \
  '{
    duplicate_case_id_count: $duplicate_case_id_count,
    missing_case_check_field_count: $missing_case_check_field_count,
    unmapped_case_check_count: $unmapped_case_check_count,
    multi_tier_case_check_count: $multi_tier_case_check_count
  }' > "${OUT_DIR}/governance-catalog-validate.json"

cat > "${OUT_DIR}/governance-catalog-validate.md" <<MD
# Governance Catalog Validation

- duplicate_case_id_count: ${duplicate_case_id_count}
- missing_case_check_field_count: ${missing_case_check_field_count}
- unmapped_case_check_count: ${unmapped_case_check_count}
- multi_tier_case_check_count: ${multi_tier_case_check_count}
MD

if [[ "${duplicate_case_id_count}" -gt 0 || "${missing_case_check_field_count}" -gt 0 || "${unmapped_case_check_count}" -gt 0 || "${multi_tier_case_check_count}" -gt 0 ]]; then
  echo "WARN: governance catalog extractor found violations (policy verdict is enforced in governance spec checks)"
else
  echo "OK: governance catalog extractor generated clean summary"
fi
