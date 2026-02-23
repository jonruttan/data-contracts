#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
dc-runner governance broad || true
cp -f .artifacts/governance-summary.json .artifacts/governance-optional-report.json 2>/dev/null || true
cp -f .artifacts/governance-trace.json .artifacts/governance-optional-report-trace.json 2>/dev/null || true
cp -f .artifacts/governance-summary.md .artifacts/governance-optional-report.md 2>/dev/null || true
cp -f .artifacts/governance-optional-report.md .artifacts/governance-optional-summary.md 2>/dev/null || true

echo "OK: governance optional report written"
