#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

impl="${SPEC_RUNNER_IMPL:-rust}"
if [[ "${1:-}" == "--impl" ]]; then
  if [[ $# -lt 3 ]]; then
    echo "ERROR: --impl requires a value and subcommand" >&2
    exit 2
  fi
  impl="$2"
  shift 2
fi

subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi

case "${impl}" in
  rust)
    exec "${ROOT_DIR}/scripts/rust/runner_adapter.sh" "$@"
    ;;
  python)
    exec "${ROOT_DIR}/scripts/python/runner_adapter.sh" "$@"
    ;;
  *)
    echo "ERROR: unsupported runner implementation: ${impl} (expected rust|python)" >&2
    exit 2
    ;;
esac
