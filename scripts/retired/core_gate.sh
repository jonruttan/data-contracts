#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

./scripts/control_plane.sh governance
./scripts/control_plane.sh docs-generate-check

echo "OK: core gate checks passed"
