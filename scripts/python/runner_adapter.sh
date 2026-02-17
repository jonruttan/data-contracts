#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

source "${ROOT_DIR}/scripts/lib/python_bin.sh"
PYTHON_BIN="$(resolve_python_bin "${ROOT_DIR}")"

run_with_timeout() {
  local timeout_seconds="$1"
  local label="$2"
  local env_var_name="$3"
  shift 3

  if [[ ! "${timeout_seconds}" =~ ^[0-9]+$ ]] || [[ "${timeout_seconds}" -le 0 ]]; then
    echo "ERROR: invalid timeout '${timeout_seconds}' for ${env_var_name}; expected positive integer seconds" >&2
    return 2
  fi

  local timeout_flag
  timeout_flag="$(mktemp -t spec_runner_timeout.XXXXXX)"
  rm -f "${timeout_flag}"

  "$@" &
  local cmd_pid=$!
  (
    sleep "${timeout_seconds}"
    if kill -0 "${cmd_pid}" 2>/dev/null; then
      : > "${timeout_flag}"
      kill -TERM "${cmd_pid}" 2>/dev/null || true
      sleep 5
      kill -KILL "${cmd_pid}" 2>/dev/null || true
    fi
  ) &
  local watchdog_pid=$!

  local cmd_status=0
  if ! wait "${cmd_pid}"; then
    cmd_status=$?
  fi
  kill "${watchdog_pid}" 2>/dev/null || true
  wait "${watchdog_pid}" 2>/dev/null || true

  if [[ -f "${timeout_flag}" ]]; then
    rm -f "${timeout_flag}"
    echo "ERROR: '${label}' timed out after ${timeout_seconds}s. Override with ${env_var_name}=<seconds>." >&2
    return 124
  fi

  rm -f "${timeout_flag}"
  return "${cmd_status}"
}

run_with_timeout_env() {
  local env_var_name="$1"
  local default_seconds="$2"
  local label="$3"
  shift 3

  local timeout_seconds="${!env_var_name:-${default_seconds}}"
  run_with_timeout "${timeout_seconds}" "${label}" "${env_var_name}" "$@"
}

subcommand="${1:-}"
while [[ $# -gt 0 ]]; do
  case "${1:-}" in
    --verbose|-v)
      export SPEC_RUNNER_DEBUG=1
      export SPEC_RUNNER_DEBUG_LEVEL=1
      shift
      ;;
    -vv)
      export SPEC_RUNNER_DEBUG=1
      export SPEC_RUNNER_DEBUG_LEVEL=2
      shift
      ;;
    -vvv)
      export SPEC_RUNNER_DEBUG=1
      export SPEC_RUNNER_DEBUG_LEVEL=3
      shift
      ;;
    --profile-level)
      export SPEC_RUNNER_PROFILE_LEVEL="${2:-}"
      shift 2
      ;;
    --profile-out)
      export SPEC_RUNNER_PROFILE_OUT="${2:-}"
      shift 2
      ;;
    --profile-summary-out)
      export SPEC_RUNNER_PROFILE_SUMMARY_OUT="${2:-}"
      shift 2
      ;;
    --profile-heartbeat-ms)
      export SPEC_RUNNER_PROFILE_HEARTBEAT_MS="${2:-}"
      shift 2
      ;;
    --profile-stall-threshold-ms)
      export SPEC_RUNNER_PROFILE_STALL_THRESHOLD_MS="${2:-}"
      shift 2
      ;;
    --liveness-level)
      export SPEC_RUNNER_LIVENESS_LEVEL="${2:-}"
      shift 2
      ;;
    --liveness-stall-ms)
      export SPEC_RUNNER_LIVENESS_STALL_MS="${2:-}"
      shift 2
      ;;
    --liveness-min-events)
      export SPEC_RUNNER_LIVENESS_MIN_EVENTS="${2:-}"
      shift 2
      ;;
    --liveness-hard-cap-ms)
      export SPEC_RUNNER_LIVENESS_HARD_CAP_MS="${2:-}"
      shift 2
      ;;
    --liveness-kill-grace-ms)
      export SPEC_RUNNER_LIVENESS_KILL_GRACE_MS="${2:-}"
      shift 2
      ;;
    --fail-fast)
      export SPEC_RUNNER_FAIL_FAST=1
      shift
      ;;
    --continue-on-fail)
      export SPEC_RUNNER_FAIL_FAST=0
      shift
      ;;
    --profile-on-fail)
      export SPEC_RUNNER_PROFILE_ON_FAIL="${2:-}"
      shift 2
      ;;
    *)
      break
      ;;
  esac
done
subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi
shift

case "${subcommand}" in
  validate-report)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands validate-report "$@"
    ;;
  governance)
    exec "${PYTHON_BIN}" scripts/run_governance_specs.py "$@"
    ;;
  governance-heavy)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_GOVERNANCE_HEAVY_SECONDS \
      180 \
      governance-heavy \
      "${PYTHON_BIN}" scripts/run_governance_specs.py \
      --check-prefix runtime.chain \
      --check-prefix library. \
      --check-prefix normalization.mapping_ast_only \
      --check-prefix normalization.virtual_root_paths_only \
      "$@"
    ;;
  style-check)
    exec "${PYTHON_BIN}" scripts/evaluate_style.py --check docs/spec "$@"
    ;;
  normalize-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_NORMALIZE_SECONDS \
      120 \
      normalize-check \
      "${PYTHON_BIN}" scripts/normalize_repo.py --check "$@"
    ;;
  normalize-fix)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_NORMALIZE_SECONDS \
      120 \
      normalize-fix \
      "${PYTHON_BIN}" scripts/normalize_repo.py --write "$@"
    ;;
  schema-registry-check)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands schema-registry-report --format json --out .artifacts/schema_registry_report.json --check "$@"
    ;;
  schema-registry-build)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands schema-registry-report --format json --out .artifacts/schema_registry_report.json "$@"
    ;;
  schema-docs-check)
    exec "${PYTHON_BIN}" scripts/generate_schema_docs.py --check "$@"
    ;;
  schema-docs-build)
    exec "${PYTHON_BIN}" scripts/generate_schema_docs.py "$@"
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
  spec-lang-stdlib-json)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands spec-lang-stdlib-report --out .artifacts/spec-lang-stdlib.json "$@"
    ;;
  spec-lang-stdlib-md)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands spec-lang-stdlib-report --format md --out .artifacts/spec-lang-stdlib-summary.md "$@"
    ;;
  ci-gate-summary)
    exec "${PYTHON_BIN}" scripts/ci_gate_summary.py "$@"
    ;;
  ci-cleanroom)
    exec "${ROOT_DIR}/scripts/ci_cleanroom.sh" "$@"
    ;;
  perf-smoke)
    exec "${PYTHON_BIN}" scripts/perf_smoke.py "$@"
    ;;
  docs-generate)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-generate \
      "${PYTHON_BIN}" scripts/docs_generate_all.py --build "$@"
    ;;
  docs-generate-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-generate-check \
      "${PYTHON_BIN}" scripts/docs_generate_all.py --check "$@"
    ;;
  docs-build)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-build \
      "${PYTHON_BIN}" scripts/docs_generate_all.py --build --surface reference_book "$@"
    ;;
  docs-build-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-build-check \
      "${PYTHON_BIN}" scripts/docs_generate_all.py --check --surface reference_book "$@"
    ;;
  docs-lint)
    exec "${PYTHON_BIN}" -m spec_runner.spec_lang_commands docs-lint "$@"
    ;;
  docs-graph)
    exec "${PYTHON_BIN}" scripts/docs_generate_all.py --build --surface docs_graph "$@"
    ;;
  conformance-parity)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_CONFORMANCE_PARITY_SECONDS \
      240 \
      conformance-parity \
      "${PYTHON_BIN}" scripts/compare_conformance_parity.py \
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
