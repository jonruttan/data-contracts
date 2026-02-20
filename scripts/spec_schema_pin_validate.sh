#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/yaml_to_json.sh"

OUT_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${OUT_DIR}"

catalog="${ROOT_DIR}/specs/schema/schema_catalog_v1.yaml"
if [[ ! -f "${catalog}" ]]; then
  echo "ERROR: missing schema catalog: ${catalog}" >&2
  exit 2
fi

# Probe YAML parser as an infra check and keep the richer awk scanner below.
parse_yaml_file_to_json "${catalog}" >/dev/null

read -r missing_spec_version_count missing_schema_ref_count unknown_schema_ref_count mismatched_version_count < <(
  awk '
    BEGIN {
      missing_spec=0; missing_ref=0; unknown_ref=0; mismatch=0

      while ((getline line < "specs/schema/schema_catalog_v1.yaml") > 0) {
        if (line ~ /^[[:space:]]*-[[:space:]]schema_id:[[:space:]]/) {
          if (path != "" && status == "active" && major != "") active[path]=major
          path=""; status=""; major=""
          continue
        }
        if (line ~ /^[[:space:]]*major:[[:space:]]*[0-9]+/) {
          major=line
          sub(/^[[:space:]]*major:[[:space:]]*/, "", major)
          continue
        }
        if (line ~ /^[[:space:]]*path:[[:space:]]*/) {
          path=line
          sub(/^[[:space:]]*path:[[:space:]]*/, "", path)
          gsub(/^"|"$/, "", path)
          continue
        }
        if (line ~ /^[[:space:]]*status:[[:space:]]*/) {
          status=line
          sub(/^[[:space:]]*status:[[:space:]]*/, "", status)
          gsub(/^"|"$/, "", status)
          continue
        }
      }
      if (path != "" && status == "active" && major != "") active[path]=major

      cmd="find specs/conformance/cases specs/governance/cases specs/libraries -name \"*.spec.md\" -type f | sort"
      while ((cmd | getline file) > 0) {
        in_block=0
        spec=""
        ref=""
        while ((getline l < file) > 0) {
          if (l ~ /^(```+|~~~+)yaml contract-spec[[:space:]]*$/) {
            in_block=1
            spec=""
            ref=""
            continue
          }
          if (in_block && l ~ /^(```+|~~~+)[[:space:]]*$/) {
            if (spec == "") missing_spec++
            if (ref == "") missing_ref++
            if (ref != "") {
              if (!(ref in active)) {
                unknown_ref++
              } else if (spec == "" || spec !~ /^[0-9]+$/ || spec != active[ref]) {
                mismatch++
              }
            }
            in_block=0
            continue
          }
          if (in_block && l ~ /^spec_version:[[:space:]]*/) {
            spec=l
            sub(/^spec_version:[[:space:]]*/, "", spec)
            gsub(/^"|"$/, "", spec)
            continue
          }
          if (in_block && l ~ /^schema_ref:[[:space:]]*/) {
            ref=l
            sub(/^schema_ref:[[:space:]]*/, "", ref)
            gsub(/^"|"$/, "", ref)
            continue
          }
        }
        close(file)
      }
      close(cmd)

      print missing_spec, missing_ref, unknown_ref, mismatch
    }
  '
)

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
  echo "WARN: schema pin extractor found violations (policy verdict is enforced in governance spec checks)"
else
  echo "OK: schema pin extractor generated clean summary"
fi
