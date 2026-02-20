#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

summary=".artifacts/governance-summary.json"
cat_log=".artifacts/governance-catalog-validate.json"
schema_log=".artifacts/spec-schema-pin-validate.json"

for p in "${summary}" "${cat_log}" "${schema_log}"; do
  if [[ ! -f "${p}" ]]; then
    echo "ERROR: missing parity input artifact: ${p}" >&2
    exit 1
  fi
done

cat_total="$(jq -r '(.duplicate_case_id_count + .missing_case_check_field_count + .unmapped_case_check_count + .multi_tier_case_check_count)' "${cat_log}")"
schema_total="$(jq -r '(.missing_spec_version_count + .missing_schema_ref_count + .unknown_schema_ref_count + .mismatched_version_count)' "${schema_log}")"

# Associated governance checks that represent extractor policy surfaces.
check_fail_count="$(jq -r '[
  .checks[]
  | select(
      .check_id == "schema.spec_case_version_present" or
      .check_id == "schema.spec_case_schema_ref_present" or
      .check_id == "schema.spec_case_schema_ref_known" or
      .check_id == "schema.spec_case_version_matches_schema_ref"
    )
  | select(.status == "fail")
] | length' "${summary}")"

chain_fail_count="$(jq -r '[
  .checks[]
  | select(
      .check_id == "governance.catalog_pipeline_chain_valid" or
      .check_id == "schema.pin_pipeline_chain_valid"
    )
  | select(.status == "fail")
] | length' "${summary}")"

if [[ "${schema_total}" -gt 0 && "${check_fail_count}" -eq 0 ]]; then
  echo "ERROR: parity mismatch: schema extractor violations exist but governance checks did not fail" >&2
  exit 1
fi

if [[ "${schema_total}" -eq 0 && "${check_fail_count}" -gt 0 ]]; then
  echo "ERROR: parity mismatch: governance schema checks failed without extractor violations" >&2
  exit 1
fi

if [[ "${cat_total}" -gt 0 && "${chain_fail_count}" -eq 0 ]]; then
  echo "ERROR: parity mismatch: catalog extractor violations exist but pipeline chain checks did not fail" >&2
  exit 1
fi

jq -n \
  --argjson catalog_violation_count "${cat_total}" \
  --argjson schema_violation_count "${schema_total}" \
  --argjson governance_schema_check_fail_count "${check_fail_count}" \
  --argjson governance_pipeline_check_fail_count "${chain_fail_count}" \
  '{
    status: "pass",
    catalog_violation_count: $catalog_violation_count,
    schema_violation_count: $schema_violation_count,
    governance_schema_check_fail_count: $governance_schema_check_fail_count,
    governance_pipeline_check_fail_count: $governance_pipeline_check_fail_count
  }' > .artifacts/governance-policy-parity.json

echo "OK: governance policy parity passed"
