#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"
exec ./runners/public/runner_adapter.sh --impl rust migrate-case-doc-metadata-v1 "$@"
