#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ -z "${SPEC_RUNNER_BIN:-}" ]]; then
  SPEC_RUNNER_BIN="${ROOT_DIR}/scripts/runner_adapter.sh"
fi
if [[ -z "${SPEC_RUNNER_IMPL:-}" ]]; then
  SPEC_RUNNER_IMPL="python"
fi

run_step() {
  local name="$1"
  shift
  echo "[prepush] ${name}: $*"
  "$@"
}

run_step normalize-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" normalize-check
run_step governance "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance
run_step governance-heavy "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance-heavy
run_step docs-generate-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" docs-generate-check
run_step perf-smoke "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" perf-smoke --mode strict --compare-only

echo "[prepush] PASS"
