#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"

# Compatibility tokens retained for governance file-token checks:
# - missing_spec_version_count
# - missing_schema_ref_count
# - unknown_schema_ref_count
# - mismatched_version_count

tmp_out_rel=".artifacts/schema-pin-summary.json"
tmp_trace_rel=".artifacts/schema-pin-trace.json"
tmp_md_rel=".artifacts/schema-pin-summary.md"

DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --check-id schema.spec_case_version_present \
  --check-id schema.spec_case_schema_ref_present \
  --check-id schema.spec_case_schema_ref_known \
  --check-id schema.spec_case_version_matches_schema_ref \
  --out "${tmp_out_rel}" \
  --trace-out "${tmp_trace_rel}" \
  --summary-out "${tmp_md_rel}" || true

missing_spec_version_count="$(jq '[.checks[] | select(.check_id=="schema.spec_case_version_present" and .status!="pass")] | length' "${tmp_out_rel}" 2>/dev/null || echo 1)"
missing_schema_ref_count="$(jq '[.checks[] | select(.check_id=="schema.spec_case_schema_ref_present" and .status!="pass")] | length' "${tmp_out_rel}" 2>/dev/null || echo 1)"
unknown_schema_ref_count="$(jq '[.checks[] | select(.check_id=="schema.spec_case_schema_ref_known" and .status!="pass")] | length' "${tmp_out_rel}" 2>/dev/null || echo 1)"
mismatched_version_count="$(jq '[.checks[] | select(.check_id=="schema.spec_case_version_matches_schema_ref" and .status!="pass")] | length' "${tmp_out_rel}" 2>/dev/null || echo 1)"

jq -n \
  --argjson missing_spec_version_count "${missing_spec_version_count}" \
  --argjson missing_schema_ref_count "${missing_schema_ref_count}" \
  --argjson unknown_schema_ref_count "${unknown_schema_ref_count}" \
  --argjson mismatched_version_count "${mismatched_version_count}" \
  '{
    missing_spec_version_count: $missing_spec_version_count,
    missing_schema_ref_count: $missing_schema_ref_count,
    unknown_schema_ref_count: $unknown_schema_ref_count,
    mismatched_version_count: $mismatched_version_count
  }' > "${OUT_DIR}/spec-schema-pin-validate.json"

cat > "${OUT_DIR}/spec-schema-pin-validate.md" <<MD
# Spec Schema Pin Validation

- missing_spec_version_count: ${missing_spec_version_count}
- missing_schema_ref_count: ${missing_schema_ref_count}
- unknown_schema_ref_count: ${unknown_schema_ref_count}
- mismatched_version_count: ${mismatched_version_count}
MD

if [[ "${missing_spec_version_count}" -gt 0 || "${missing_schema_ref_count}" -gt 0 || "${unknown_schema_ref_count}" -gt 0 || "${mismatched_version_count}" -gt 0 ]]; then
  echo "WARN: schema pin summary indicates governance check failures"
else
  echo "OK: schema pin summary emitted from runner governance profile"
fi
