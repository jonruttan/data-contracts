#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
dc-runner governance run
cp -f .artifacts/governance-summary.json .artifacts/governance-catalog-validate.json
cp -f .artifacts/governance-trace.json .artifacts/governance-catalog-validate-trace.json
cp -f .artifacts/governance-summary.md .artifacts/governance-catalog-validate.md

echo "OK: governance catalog validation emitted from runner governance profile"
