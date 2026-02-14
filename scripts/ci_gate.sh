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

"${PYTHON_BIN}" scripts/ci_gate_summary.py --python-bin "${PYTHON_BIN}" --out .artifacts/gate-summary.json
