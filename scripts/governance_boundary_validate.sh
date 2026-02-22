#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

SCAN_PATHS=(
  "README.md"
  "specs/00_core"
  "specs/01_schema"
  "specs/02_contracts"
  "specs/03_conformance"
  "specs/04_governance"
  "specs/05_libraries"
  "docs/book"
)

hits=0
if rg -n -F --hidden --glob '!docs/history/**' --glob '!specs/governance/**' "runner-owned implementation specs" "${SCAN_PATHS[@]}"; then
  echo "ERROR: forbidden boundary token found in canonical trees: runner-owned implementation specs" >&2
  hits=1
fi

if rg -n -P --hidden --glob '!docs/history/**' --glob '!specs/governance/**' '(?<!/dc-runner-spec)/specs/impl/' "${SCAN_PATHS[@]}"; then
  echo "ERROR: forbidden boundary token found in canonical trees: /specs/impl/" >&2
  hits=1
fi

if rg -n -P --hidden --glob '!docs/history/**' --glob '!specs/governance/**' '(?<!/dc-runner-spec)/specs/contract_sets/' "${SCAN_PATHS[@]}"; then
  echo "ERROR: forbidden boundary token found in canonical trees: /specs/contract_sets/" >&2
  hits=1
fi

if [[ "${hits}" -ne 0 ]]; then
  echo "ERROR: boundary enforcement failed. Use external runner-spec paths and canonical interface docs only." >&2
  exit 1
fi

echo "OK: repository boundary tokens validated"
