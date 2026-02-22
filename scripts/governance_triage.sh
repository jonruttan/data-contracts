#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
./scripts/control_plane.sh governance "$@"
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance --profile full \
  --out .artifacts/governance-triage.json \
  --trace-out .artifacts/governance-triage-trace.json \
  --summary-out .artifacts/governance-triage-summary.md

echo "governance triage: pass"
