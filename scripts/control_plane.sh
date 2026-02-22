#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

ensure_artifacts_dir() {
  mkdir -p .artifacts
}

run_governance() {
  ensure_artifacts_dir
  ./scripts/governance_interface_validate.sh
  ./scripts/governance_boundary_validate.sh
  DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance --profile full "$@"
  ./scripts/governance_catalog_validate.sh
  ./scripts/spec_schema_pin_validate.sh
  ./scripts/governance_optional_report.sh
}

cmd="${1:-}"
[[ -n "${cmd}" ]] || {
  echo "usage: ./scripts/control_plane.sh <critical-gate|governance|docs-generate-check|style-check|governance-broad-native|ci-gate-summary>" >&2
  exit 2
}
shift || true

case "${cmd}" in
  governance)
    run_governance "$@"
    ;;
  governance-broad-native)
    ensure_artifacts_dir
    ./scripts/governance_interface_validate.sh
    ./scripts/governance_boundary_validate.sh
    DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh governance-broad-native "$@"
    ;;
  style-check)
    ensure_artifacts_dir
    DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh style-check "$@"
    ;;
  docs-generate-check)
    ensure_artifacts_dir
    DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh docs-generate-check "$@"
    ;;
  critical-gate)
    ensure_artifacts_dir
    ./scripts/governance_interface_validate.sh
    ./scripts/governance_boundary_validate.sh
    DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh critical-gate "$@"
    ;;
  ci-gate-summary)
    ensure_artifacts_dir
    DC_RUNNER_RUST_NATIVE_ONLY=1 ./scripts/runner_bin.sh ci-gate-summary "$@"
    ;;
  *)
    echo "unknown control-plane command: ${cmd}" >&2
    exit 2
    ;;
esac
