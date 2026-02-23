#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --out .artifacts/spec-schema-pin-validate.json \
  --trace-out .artifacts/spec-schema-pin-validate-trace.json \
  --summary-out .artifacts/spec-schema-pin-validate.md

echo "OK: schema pin validation emitted from runner governance profile"
