#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile optional \
  --out .artifacts/governance-optional-report.json \
  --trace-out .artifacts/governance-optional-report-trace.json \
  --summary-out .artifacts/governance-optional-report.md || true

echo "OK: governance optional report written"
