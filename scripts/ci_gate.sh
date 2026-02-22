#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

./scripts/control_plane.sh critical-gate
./scripts/control_plane.sh ci-gate-summary "$@"
