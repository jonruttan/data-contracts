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
  dc-runner governance run "$@"
  ./scripts/governance_boundary_validate.sh
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
    dc-runner governance broad "$@"
    ;;
  style-check)
    ensure_artifacts_dir
    dc-runner quality style-check "$@"
    ;;
  docs-generate-check)
    ensure_artifacts_dir
    dc-runner docs generate-check "$@"
    ./scripts/docs_audience_generate.sh --check
    ;;
  critical-gate)
    ensure_artifacts_dir
    ./scripts/governance_interface_validate.sh
    dc-runner governance critical "$@"
    ;;
  ci-gate-summary)
    ensure_artifacts_dir
    dc-runner ci gate-summary "$@"
    ;;
  *)
    echo "unknown control-plane command: ${cmd}" >&2
    exit 2
    ;;
esac
