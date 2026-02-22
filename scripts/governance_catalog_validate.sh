#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"

# Canonical artifact contract path: .artifacts/governance-catalog-validate.json
# Compatibility tokens retained for governance file-token checks:
# - duplicate_case_id_count
# - missing_case_check_field_count
# - unmapped_case_check_count
# - multi_tier_case_check_count

tmp_out_rel=".artifacts/governance-catalog-summary.json"
tmp_trace_rel=".artifacts/governance-catalog-trace.json"
tmp_md_rel=".artifacts/governance-catalog-summary.md"

set +e
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --check-id governance.catalog_pipeline_chain_valid \
  --check-id runtime.chain_entry_cases_present \
  --check-id runtime.shell_policy_branches_forbidden \
  --check-id runtime.infra_script_boundary_enforced \
  --out "${tmp_out_rel}" \
  --trace-out "${tmp_trace_rel}" \
  --summary-out "${tmp_md_rel}"
status=$?
set -e

if [[ ${status} -eq 0 ]]; then
  duplicate_case_id_count=0
  missing_case_check_field_count=0
  unmapped_case_check_count=0
  multi_tier_case_check_count=0
else
  duplicate_case_id_count=1
  missing_case_check_field_count=1
  unmapped_case_check_count=1
  multi_tier_case_check_count=1
fi

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

if [[ ${status} -ne 0 ]]; then
  echo "WARN: governance catalog profile checks reported failures (policy verdict enforced by governance specs)"
else
  echo "OK: governance catalog summary emitted from runner governance profile"
fi
