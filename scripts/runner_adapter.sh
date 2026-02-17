#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

impl="${SPEC_RUNNER_IMPL:-rust}"
verbose_level=0
profile_level=""
profile_out=""
profile_summary_out=""
profile_heartbeat_ms=""
profile_stall_threshold_ms=""
while [[ $# -gt 0 ]]; do
  case "${1:-}" in
    --verbose|-v)
      verbose_level=1
      shift
      ;;
    -vv)
      verbose_level=2
      shift
      ;;
    -vvv)
      verbose_level=3
      shift
      ;;
    --profile-level)
      profile_level="${2:-}"
      shift 2
      ;;
    --profile-out)
      profile_out="${2:-}"
      shift 2
      ;;
    --profile-summary-out)
      profile_summary_out="${2:-}"
      shift 2
      ;;
    --profile-heartbeat-ms)
      profile_heartbeat_ms="${2:-}"
      shift 2
      ;;
    --profile-stall-threshold-ms)
      profile_stall_threshold_ms="${2:-}"
      shift 2
      ;;
    *)
      break
      ;;
  esac
done

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

if [[ "${verbose_level}" -gt 0 ]]; then
  export SPEC_RUNNER_DEBUG=1
  export SPEC_RUNNER_DEBUG_LEVEL="${verbose_level}"
fi
if [[ -n "${profile_level}" ]]; then
  export SPEC_RUNNER_PROFILE_LEVEL="${profile_level}"
fi
if [[ -n "${profile_out}" ]]; then
  export SPEC_RUNNER_PROFILE_OUT="${profile_out}"
fi
if [[ -n "${profile_summary_out}" ]]; then
  export SPEC_RUNNER_PROFILE_SUMMARY_OUT="${profile_summary_out}"
fi
if [[ -n "${profile_heartbeat_ms}" ]]; then
  export SPEC_RUNNER_PROFILE_HEARTBEAT_MS="${profile_heartbeat_ms}"
fi
if [[ -n "${profile_stall_threshold_ms}" ]]; then
  export SPEC_RUNNER_PROFILE_STALL_THRESHOLD_MS="${profile_stall_threshold_ms}"
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
