#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --check-id runtime.repo_boundary_tokens_forbidden \
  --check-id runtime.repo_boundary_validator_tokens_configured \
  --out .artifacts/governance-boundary-validate.json \
  --trace-out .artifacts/governance-boundary-trace.json \
  --summary-out .artifacts/governance-boundary-summary.md

echo "OK: repository boundary tokens validated"
