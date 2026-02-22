#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --check-id runtime.status_ingest_pipeline_chain_valid \
  --check-id runtime.compatibility_status_ingestion_configured \
  --check-id runtime.compatibility_status_freshness_within_slo \
  --check-id runtime.compatibility_missing_status_visibility_required \
  --out .artifacts/runner-status-matrix.json \
  --trace-out .artifacts/runner-status-ingest-log.json \
  --summary-out .artifacts/runner-status-matrix.md

echo "wrote ${ROOT_DIR}/.artifacts/runner-status-matrix.json"
echo "wrote ${ROOT_DIR}/.artifacts/runner-status-matrix.md"
echo "wrote ${ROOT_DIR}/.artifacts/runner-status-ingest-log.json"
