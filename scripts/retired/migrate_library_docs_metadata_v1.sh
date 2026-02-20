#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"
exec ./scripts/runner_bin.sh migrate-library-docs-metadata-v1 "$@"
