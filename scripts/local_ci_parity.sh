#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

./scripts/control_plane.sh governance
./scripts/control_plane.sh docs-generate-check
./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness

echo "[local-ci-parity] PASS"
