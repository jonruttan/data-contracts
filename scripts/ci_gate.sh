#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ -z "${SPEC_RUNNER_BIN:-}" ]]; then
  SPEC_RUNNER_BIN="${ROOT_DIR}/scripts/runner_adapter.sh"
fi
if [[ -z "${SPEC_RUNNER_IMPL:-}" ]]; then
  SPEC_RUNNER_IMPL="rust"
fi

"${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" critical-gate

export SPEC_CI_GATE_SKIP_CRITICAL=1
"${SPEC_RUNNER_BIN}" ci-gate-summary \
  --runner-bin "${SPEC_RUNNER_BIN}" \
  --runner-impl "${SPEC_RUNNER_IMPL}" \
  --out .artifacts/gate-summary.json \
  --trace-out .artifacts/gate-exec-trace.json
