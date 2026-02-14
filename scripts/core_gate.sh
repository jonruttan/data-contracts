#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/python_bin.sh"
PYTHON_BIN="$(resolve_python_bin "${ROOT_DIR}")"

"${PYTHON_BIN}" scripts/run_governance_specs.py
"${PYTHON_BIN}" scripts/evaluate_style.py --check docs/spec
"${PYTHON_BIN}" -m pytest -q \
  tests/test_doc_parser_unit.py \
  tests/test_dispatcher_unit.py \
  tests/test_assertions_unit.py \
  tests/test_conformance_runner_unit.py

echo "OK: core gate checks passed"
