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
liveness_level=""
liveness_stall_ms=""
liveness_min_events=""
liveness_hard_cap_ms=""
liveness_kill_grace_ms=""
fail_fast_setting=""
profile_on_fail=""
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
    --liveness-level)
      liveness_level="${2:-}"
      shift 2
      ;;
    --liveness-stall-ms)
      liveness_stall_ms="${2:-}"
      shift 2
      ;;
    --liveness-min-events)
      liveness_min_events="${2:-}"
      shift 2
      ;;
    --liveness-hard-cap-ms)
      liveness_hard_cap_ms="${2:-}"
      shift 2
      ;;
    --liveness-kill-grace-ms)
      liveness_kill_grace_ms="${2:-}"
      shift 2
      ;;
    --fail-fast)
      fail_fast_setting="1"
      shift
      ;;
    --continue-on-fail)
      fail_fast_setting="0"
      shift
      ;;
    --profile-on-fail)
      profile_on_fail="${2:-}"
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
if [[ -n "${liveness_level}" ]]; then
  export SPEC_RUNNER_LIVENESS_LEVEL="${liveness_level}"
fi
if [[ -n "${liveness_stall_ms}" ]]; then
  export SPEC_RUNNER_LIVENESS_STALL_MS="${liveness_stall_ms}"
fi
if [[ -n "${liveness_min_events}" ]]; then
  export SPEC_RUNNER_LIVENESS_MIN_EVENTS="${liveness_min_events}"
fi
if [[ -n "${liveness_hard_cap_ms}" ]]; then
  export SPEC_RUNNER_LIVENESS_HARD_CAP_MS="${liveness_hard_cap_ms}"
fi
if [[ -n "${liveness_kill_grace_ms}" ]]; then
  export SPEC_RUNNER_LIVENESS_KILL_GRACE_MS="${liveness_kill_grace_ms}"
fi
if [[ -n "${fail_fast_setting}" ]]; then
  export SPEC_RUNNER_FAIL_FAST="${fail_fast_setting}"
fi
if [[ -n "${profile_on_fail}" ]]; then
  export SPEC_RUNNER_PROFILE_ON_FAIL="${profile_on_fail}"
fi

case "${impl}" in
  rust)
    exec "${ROOT_DIR}/scripts/rust/runner_adapter.sh" "$@"
    ;;
  python)
    echo "ERROR: python runner impl is no longer supported on the runtime path (SRRUN-IMPL-001)." >&2
    echo "Use rust impl instead: ./scripts/runner_adapter.sh --impl rust ${subcommand}" >&2
    exit 2
    ;;
  *)
    echo "ERROR: unsupported runner implementation: ${impl} (expected rust only)" >&2
    exit 2
    ;;
esac
