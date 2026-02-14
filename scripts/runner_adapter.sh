#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/python_bin.sh"
PYTHON_BIN="$(resolve_python_bin "${ROOT_DIR}")"

subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi
shift

case "${subcommand}" in
  governance)
    exec "${PYTHON_BIN}" scripts/run_governance_specs.py "$@"
    ;;
  style-check)
    exec "${PYTHON_BIN}" scripts/evaluate_style.py --check docs/spec "$@"
    ;;
  lint)
    exec "${PYTHON_BIN}" -m ruff check . "$@"
    ;;
  typecheck)
    exec "${PYTHON_BIN}" -m mypy spec_runner "$@"
    ;;
  compilecheck)
    exec "${PYTHON_BIN}" -m compileall -q spec_runner scripts tests "$@"
    ;;
  conformance-purpose-json)
    exec "${PYTHON_BIN}" scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json "$@"
    ;;
  conformance-purpose-md)
    exec "${PYTHON_BIN}" scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md "$@"
    ;;
  conformance-parity)
    exec "${PYTHON_BIN}" scripts/compare_conformance_parity.py \
      --cases docs/spec/conformance/cases \
      --php-runner scripts/php/conformance_runner.php \
      --out .artifacts/conformance-parity.json \
      "$@"
    ;;
  test-core)
    exec "${PYTHON_BIN}" -m pytest -q \
      tests/test_doc_parser_unit.py \
      tests/test_dispatcher_unit.py \
      tests/test_assertions_unit.py \
      tests/test_conformance_runner_unit.py \
      "$@"
    ;;
  test-full)
    exec "${PYTHON_BIN}" -m pytest "$@"
    ;;
  *)
    echo "ERROR: unsupported runner adapter subcommand: ${subcommand}" >&2
    exit 2
    ;;
esac
