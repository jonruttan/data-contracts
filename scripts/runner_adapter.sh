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
  normalize-check)
    exec "${PYTHON_BIN}" scripts/normalize_repo.py --check "$@"
    ;;
  normalize-fix)
    exec "${PYTHON_BIN}" scripts/normalize_repo.py --write "$@"
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
  spec-portability-json)
    exec "${PYTHON_BIN}" scripts/spec_portability_report.py --out .artifacts/spec-portability.json "$@"
    ;;
  spec-portability-md)
    exec "${PYTHON_BIN}" scripts/spec_portability_report.py --format md --out .artifacts/spec-portability-summary.md "$@"
    ;;
  spec-lang-adoption-json)
    exec "${PYTHON_BIN}" scripts/spec_lang_adoption_report.py --out .artifacts/spec-lang-adoption.json "$@"
    ;;
  spec-lang-adoption-md)
    exec "${PYTHON_BIN}" scripts/spec_lang_adoption_report.py --format md --out .artifacts/spec-lang-adoption-summary.md "$@"
    ;;
  runner-independence-json)
    exec "${PYTHON_BIN}" scripts/runner_independence_report.py --out .artifacts/runner-independence.json "$@"
    ;;
  runner-independence-md)
    exec "${PYTHON_BIN}" scripts/runner_independence_report.py --format md --out .artifacts/runner-independence-summary.md "$@"
    ;;
  python-dependency-json)
    exec "${PYTHON_BIN}" scripts/python_dependency_report.py --out .artifacts/python-dependency.json "$@"
    ;;
  python-dependency-md)
    exec "${PYTHON_BIN}" scripts/python_dependency_report.py --format md --out .artifacts/python-dependency-summary.md "$@"
    ;;
  docs-operability-json)
    exec "${PYTHON_BIN}" scripts/docs_operability_report.py --out .artifacts/docs-operability.json "$@"
    ;;
  docs-operability-md)
    exec "${PYTHON_BIN}" scripts/docs_operability_report.py --format md --out .artifacts/docs-operability-summary.md "$@"
    ;;
  contract-assertions-json)
    exec "${PYTHON_BIN}" scripts/contract_assertions_report.py --out .artifacts/contract-assertions.json "$@"
    ;;
  contract-assertions-md)
    exec "${PYTHON_BIN}" scripts/contract_assertions_report.py --format md --out .artifacts/contract-assertions-summary.md "$@"
    ;;
  objective-scorecard-json)
    exec "${PYTHON_BIN}" scripts/objective_scorecard_report.py --out .artifacts/objective-scorecard.json "$@"
    ;;
  objective-scorecard-md)
    exec "${PYTHON_BIN}" scripts/objective_scorecard_report.py --format md --out .artifacts/objective-scorecard-summary.md "$@"
    ;;
  ci-gate-summary)
    exec "${PYTHON_BIN}" scripts/ci_gate_summary.py "$@"
    ;;
  docs-build)
    exec "${PYTHON_BIN}" scripts/docs_build_reference.py "$@"
    ;;
  docs-build-check)
    exec "${PYTHON_BIN}" scripts/docs_build_reference.py --check "$@"
    ;;
  docs-lint)
    exec "${PYTHON_BIN}" scripts/docs_lint.py "$@"
    ;;
  docs-graph)
    exec "${PYTHON_BIN}" scripts/docs_graph_export.py "$@"
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
