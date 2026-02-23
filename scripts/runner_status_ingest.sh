#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
dc-runner governance run
cp -f .artifacts/governance-summary.json .artifacts/runner-status-matrix.json
cp -f .artifacts/governance-summary.md .artifacts/runner-status-matrix.md
cp -f .artifacts/governance-trace.json .artifacts/runner-status-ingest-log.json

echo "wrote ${ROOT_DIR}/.artifacts/runner-status-matrix.json"
echo "wrote ${ROOT_DIR}/.artifacts/runner-status-matrix.md"
echo "wrote ${ROOT_DIR}/.artifacts/runner-status-ingest-log.json"
