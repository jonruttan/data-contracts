#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance \
  --profile full \
  --check-id governance.catalog_pipeline_chain_valid \
  --check-id runtime.chain_entry_cases_present \
  --check-id runtime.shell_policy_branches_forbidden \
  --check-id runtime.infra_script_boundary_enforced \
  --out .artifacts/governance-catalog-validate.json \
  --trace-out .artifacts/governance-catalog-validate-trace.json \
  --summary-out .artifacts/governance-catalog-validate.md

echo "OK: governance catalog validation emitted from runner governance profile"
