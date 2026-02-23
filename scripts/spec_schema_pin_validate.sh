#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
dc-runner governance run
cp -f .artifacts/governance-summary.json .artifacts/spec-schema-pin-validate.json
cp -f .artifacts/governance-trace.json .artifacts/spec-schema-pin-validate-trace.json
cp -f .artifacts/governance-summary.md .artifacts/spec-schema-pin-validate.md

echo "OK: schema pin validation emitted from runner governance profile"
