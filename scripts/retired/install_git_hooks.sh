#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ ! -x ".githooks/pre-push" ]]; then
  echo "ERROR: missing executable .githooks/pre-push" >&2
  exit 1
fi

git config --local core.hooksPath .githooks

echo "[hooks] core.hooksPath set to .githooks"
echo "[hooks] pre-push hook installed"
