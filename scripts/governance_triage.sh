#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
./scripts/control_plane.sh governance "$@"
dc-runner governance run
cp -f .artifacts/governance-summary.json .artifacts/governance-triage.json
cp -f .artifacts/governance-trace.json .artifacts/governance-triage-trace.json
cp -f .artifacts/governance-summary.md .artifacts/governance-triage-summary.md

echo "governance triage: pass"
