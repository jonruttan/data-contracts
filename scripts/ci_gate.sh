#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ -z "${PYTHON_BIN:-}" ]]; then
  if [[ -x "${ROOT_DIR}/.venv/bin/python" ]]; then
    PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"
  elif [[ -x "${ROOT_DIR}/../../.venv/bin/python" ]]; then
    PYTHON_BIN="${ROOT_DIR}/../../.venv/bin/python"
  else
    PYTHON_BIN="python3"
  fi
fi

"${PYTHON_BIN}" scripts/check_contract_governance.py
"${PYTHON_BIN}" -m ruff check .
"${PYTHON_BIN}" -m compileall -q spec_runner scripts tests
"${PYTHON_BIN}" scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
"${PYTHON_BIN}" scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
"${PYTHON_BIN}" scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md
"${PYTHON_BIN}" scripts/compare_conformance_parity.py \
  --cases docs/spec/conformance/cases \
  --php-runner scripts/php/conformance_runner.php \
  --out .artifacts/conformance-parity.json
"${PYTHON_BIN}" -m pytest
