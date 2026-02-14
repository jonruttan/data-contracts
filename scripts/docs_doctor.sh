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
"${PYTHON_BIN}" scripts/run_governance_specs.py
"${PYTHON_BIN}" scripts/evaluate_style.py --check docs/spec

echo "OK: docs doctor checks passed"
