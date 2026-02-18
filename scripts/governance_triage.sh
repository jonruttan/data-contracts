#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

TRIAGE_ENABLED="${SPEC_GOV_TRIAGE_ENABLED:-1}"
TRIAGE_MAX_RETRIES="${SPEC_GOV_TRIAGE_MAX_RETRIES:-1}"
TRIAGE_FALLBACK_PREFIXES_RAW="${SPEC_GOV_TRIAGE_FALLBACK_PREFIXES:-docs.,normalization.,runtime.}"
TRIAGE_PROFILE_LEVEL="${SPEC_GOV_TRIAGE_PROFILE_LEVEL:-basic}"
BROAD_TIMEOUT_SECONDS="${SPEC_GOV_TRIAGE_STALL_TIMEOUT_SECONDS:-30}"
TRIAGE_LIVENESS_LEVEL="${SPEC_GOV_TRIAGE_LIVENESS_LEVEL:-strict}"
TRIAGE_LIVENESS_STALL_MS="${SPEC_GOV_TRIAGE_LIVENESS_STALL_MS:-5000}"
TRIAGE_LIVENESS_KILL_GRACE_MS="${SPEC_GOV_TRIAGE_LIVENESS_KILL_GRACE_MS:-1000}"
TARGETED_TIMEOUT_SECONDS="${SPEC_GOV_TRIAGE_TARGETED_TIMEOUT_SECONDS:-15}"
TIMEOUT_BIN="${SPEC_GOV_TRIAGE_TIMEOUT_BIN:-}"

MODE="auto"
IMPL="${SPEC_RUNNER_IMPL:-rust}"
FROM_FAILURES=""
PROFILE_LEVEL=""
declare -a CHECK_IDS=()
declare -a CHECK_PREFIXES=()

usage() {
  cat <<'USAGE'
Usage: scripts/governance_triage.sh [options]

Options:
  --mode auto|targeted
  --impl rust|python
  --check-id <id>            Repeatable (targeted mode)
  --check-prefix <prefix>    Repeatable (targeted mode)
  --from-failures <path>     Load failing check ids/prefixes from a prior triage JSON
  --profile-level <level>    off|basic|detailed|debug (passthrough to governance)
  --triage-enabled <0|1>
  --triage-max-retries <n>
  --triage-fallback-prefixes <csv>
  --triage-profile-level <level>
  --broad-timeout-seconds <n>
  --triage-liveness-level <level>
  --triage-liveness-stall-ms <n>
  --triage-liveness-kill-grace-ms <n>
USAGE
}

while [[ $# -gt 0 ]]; do
  case "${1:-}" in
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --impl)
      IMPL="${2:-}"
      shift 2
      ;;
    --check-id)
      CHECK_IDS+=("${2:-}")
      shift 2
      ;;
    --check-prefix)
      CHECK_PREFIXES+=("${2:-}")
      shift 2
      ;;
    --from-failures)
      FROM_FAILURES="${2:-}"
      shift 2
      ;;
    --profile-level)
      PROFILE_LEVEL="${2:-}"
      shift 2
      ;;
    --triage-enabled)
      TRIAGE_ENABLED="${2:-}"
      shift 2
      ;;
    --triage-max-retries)
      TRIAGE_MAX_RETRIES="${2:-}"
      shift 2
      ;;
    --triage-fallback-prefixes)
      TRIAGE_FALLBACK_PREFIXES_RAW="${2:-}"
      shift 2
      ;;
    --triage-profile-level)
      TRIAGE_PROFILE_LEVEL="${2:-}"
      shift 2
      ;;
    --broad-timeout-seconds)
      BROAD_TIMEOUT_SECONDS="${2:-}"
      shift 2
      ;;
    --triage-liveness-level)
      TRIAGE_LIVENESS_LEVEL="${2:-}"
      shift 2
      ;;
    --triage-liveness-stall-ms)
      TRIAGE_LIVENESS_STALL_MS="${2:-}"
      shift 2
      ;;
    --triage-liveness-kill-grace-ms)
      TRIAGE_LIVENESS_KILL_GRACE_MS="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unsupported governance-triage arg: ${1}" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "${PROFILE_LEVEL}" ]]; then
  PROFILE_LEVEL="${TRIAGE_PROFILE_LEVEL}"
fi

if [[ -z "${TIMEOUT_BIN}" ]]; then
  if command -v timeout >/dev/null 2>&1; then
    TIMEOUT_BIN="$(command -v timeout)"
  elif command -v gtimeout >/dev/null 2>&1; then
    TIMEOUT_BIN="$(command -v gtimeout)"
  else
    TIMEOUT_BIN=""
  fi
fi

case "${MODE}" in
  auto|targeted) ;;
  *)
    echo "ERROR: --mode must be auto|targeted (got '${MODE}')" >&2
    exit 2
    ;;
esac

declare -a FALLBACK_PREFIXES=()
IFS=',' read -r -a _fp <<< "${TRIAGE_FALLBACK_PREFIXES_RAW}"
for p in "${_fp[@]}"; do
  p="$(echo "${p}" | xargs)"
  [[ -n "${p}" ]] && FALLBACK_PREFIXES+=("${p}")
done

add_unique() {
  local needle="$1"
  shift
  local cur
  for cur in "$@"; do
    [[ "${cur}" == "${needle}" ]] && return 0
  done
  return 1
}

declare -a MAP_PATTERNS=()
declare -a MAP_PREFIXES=()
MAP_FILE="${ROOT_DIR}/docs/spec/governance/check_prefix_map_v1.yaml"
if [[ -f "${MAP_FILE}" ]]; then
  while IFS='=' read -r pattern prefix; do
    [[ -n "${pattern}" && -n "${prefix}" ]] || continue
    MAP_PATTERNS+=("${pattern}")
    MAP_PREFIXES+=("${prefix}")
  done < <(awk '
    BEGIN { in_rules=0 }
    /^rules:/ { in_rules=1; next }
    in_rules && /^[^[:space:]]/ { in_rules=0 }
    in_rules && /^[[:space:]]+[A-Za-z0-9._:-]+:[[:space:]]*[A-Za-z0-9._-]+/ {
      line=$0
      gsub(/^[[:space:]]+/, "", line)
      split(line, parts, ":")
      key=parts[1]
      val=parts[2]
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", val)
      print key "=" val
    }
  ' "${MAP_FILE}")
fi

if [[ -n "${FROM_FAILURES}" && -f "${FROM_FAILURES}" ]]; then
  while IFS= read -r line; do
    [[ -n "${line}" ]] || continue
    case "${line}" in
      ID:*) CHECK_IDS+=("${line#ID:}") ;;
      PREFIX:*) CHECK_PREFIXES+=("${line#PREFIX:}") ;;
    esac
  done < <(python3 - <<'PY' "${FROM_FAILURES}"
import json, sys
p = sys.argv[1]
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)
for k in data.get("failing_check_ids", []) or []:
    if isinstance(k, str) and k.strip():
        print("ID:" + k.strip())
for k in data.get("failing_check_prefixes", []) or []:
    if isinstance(k, str) and k.strip():
        print("PREFIX:" + k.strip())
PY
)
fi

mkdir -p .artifacts
TRIAGE_JSON=".artifacts/governance-triage.json"
TRIAGE_MD=".artifacts/governance-triage-summary.md"
TMP_OUT="$(mktemp -t governance-triage.XXXXXX)"
trap 'rm -f "${TMP_OUT}"' EXIT

build_prefixes_from_ids() {
  local id
  for id in "${CHECK_IDS[@]-}"; do
    [[ -n "${id}" ]] || continue
    local i
    local matched=0
    local best_pat=""
    local best_prefix=""
    for i in "${!MAP_PATTERNS[@]}"; do
      if [[ "${id}" == "${MAP_PATTERNS[$i]}"* ]]; then
        if [[ "${#MAP_PATTERNS[$i]}" -gt "${#best_pat}" ]]; then
          best_pat="${MAP_PATTERNS[$i]}"
          best_prefix="${MAP_PREFIXES[$i]}"
        fi
        matched=1
      fi
    done
    if [[ "${matched}" -eq 1 ]]; then
      if ! add_unique "${best_prefix}" "${CHECK_PREFIXES[@]-}"; then
        CHECK_PREFIXES+=("${best_prefix}")
      fi
    else
      if ! add_unique "${id}" "${CHECK_PREFIXES[@]-}"; then
        CHECK_PREFIXES+=("${id}")
      fi
    fi
  done
}

parse_error_ids_from_output() {
  local path="$1"
  local id
  while IFS= read -r id; do
    [[ -n "${id}" ]] || continue
    if ! add_unique "${id}" "${CHECK_IDS[@]-}"; then
      CHECK_IDS+=("${id}")
    fi
  done < <(rg -oN "^ERROR: ([A-Z0-9-]+):" "${path}" -r '$1' 2>/dev/null || true)
}

run_governance() {
  local label="$1"
  shift
  local timeout_seconds="${1:-0}"
  shift || true
  local -a cmd=(./scripts/runner_adapter.sh --impl "${IMPL}" governance)
  if [[ "${PROFILE_LEVEL}" != "off" && -n "${PROFILE_LEVEL}" ]]; then
    cmd+=(--profile-level "${PROFILE_LEVEL}")
  fi
  if [[ -n "${TRIAGE_LIVENESS_LEVEL}" ]]; then
    cmd+=(--liveness-level "${TRIAGE_LIVENESS_LEVEL}")
  fi
  if [[ -n "${TRIAGE_LIVENESS_STALL_MS}" ]]; then
    cmd+=(--liveness-stall-ms "${TRIAGE_LIVENESS_STALL_MS}")
  fi
  if [[ -n "${TRIAGE_LIVENESS_KILL_GRACE_MS}" ]]; then
    cmd+=(--liveness-kill-grace-ms "${TRIAGE_LIVENESS_KILL_GRACE_MS}")
  fi
  cmd+=(--liveness-hard-cap-ms "$((BROAD_TIMEOUT_SECONDS * 1000))")
  cmd+=("$@")
  echo "[governance-triage] ${label}: ${cmd[*]}"
  if [[ "${timeout_seconds}" =~ ^[0-9]+$ ]] && [[ "${timeout_seconds}" -gt 0 ]]; then
    if [[ -n "${TIMEOUT_BIN}" ]]; then
      "${TIMEOUT_BIN}" "${timeout_seconds}" "${cmd[@]}" >"${TMP_OUT}" 2>&1 || return $?
    else
      "${cmd[@]}" >"${TMP_OUT}" 2>&1 || return $?
    fi
  else
    "${cmd[@]}" >"${TMP_OUT}" 2>&1 || return $?
  fi
}

triage_attempted=true
triage_mode="broad"
triage_result="not_run"
stall_detected=false
stall_phase=""
broad_exit_code=0
targeted_exit_code=0
final_exit=0
declare -a targeted_cmd_parts=()

if [[ "${TRIAGE_ENABLED}" != "1" && "${TRIAGE_ENABLED,,}" != "true" ]]; then
  triage_attempted=false
  triage_mode="broad"
  run_governance "broad-governance (triage disabled)" "${BROAD_TIMEOUT_SECONDS}" || broad_exit_code=$?
  cat "${TMP_OUT}"
  triage_result=$([[ "${broad_exit_code}" -eq 0 ]] && echo "pass" || echo "fail")
  final_exit="${broad_exit_code}"
else
  if [[ "${MODE}" == "targeted" ]]; then
    triage_mode="targeted"
    build_prefixes_from_ids
    if [[ "${#CHECK_PREFIXES[@]}" -eq 0 ]]; then
      CHECK_PREFIXES=("${FALLBACK_PREFIXES[@]}")
    fi
    local_args=()
    for p in "${CHECK_PREFIXES[@]}"; do
      local_args+=(--check-prefix "${p}")
    done
    run_governance "targeted-governance" "${TARGETED_TIMEOUT_SECONDS}" "${local_args[@]}" || targeted_exit_code=$?
    cat "${TMP_OUT}"
    triage_result=$([[ "${targeted_exit_code}" -eq 0 ]] && echo "pass" || echo "fail")
    final_exit="${targeted_exit_code}"
  else
    run_governance "broad-governance" "${BROAD_TIMEOUT_SECONDS}" || broad_exit_code=$?
    cat "${TMP_OUT}"
    parse_error_ids_from_output "${TMP_OUT}"
    build_prefixes_from_ids
    if [[ "${broad_exit_code}" -eq 124 ]]; then
      stall_detected=true
      stall_phase="governance.broad"
    fi
    if [[ "${broad_exit_code}" -eq 0 ]]; then
      triage_mode="broad"
      triage_result="pass"
      final_exit=0
    else
      triage_mode="both"
      if [[ "${#CHECK_PREFIXES[@]}" -eq 0 ]]; then
        CHECK_PREFIXES=("${FALLBACK_PREFIXES[@]}")
        if [[ "${stall_detected}" == "true" && "${#CHECK_PREFIXES[@]}" -gt 1 ]]; then
          CHECK_PREFIXES=("${CHECK_PREFIXES[0]}")
        fi
      fi
      retry=0
      while [[ "${retry}" -lt "${TRIAGE_MAX_RETRIES}" ]]; do
        retry=$((retry + 1))
        local_args=()
        for p in "${CHECK_PREFIXES[@]}"; do
          local_args+=(--check-prefix "${p}")
        done
        targeted_cmd_parts=("${local_args[@]}")
        run_governance "targeted-governance retry=${retry}" "${TARGETED_TIMEOUT_SECONDS}" "${local_args[@]}" || targeted_exit_code=$?
        cat "${TMP_OUT}"
        parse_error_ids_from_output "${TMP_OUT}"
        if [[ "${targeted_exit_code}" -eq 0 ]]; then
          break
        fi
      done
      if [[ "${targeted_exit_code}" -eq 0 ]]; then
        triage_result="pass"
        final_exit=0
      else
        triage_result=$([[ "${stall_detected}" == "true" ]] && echo "stalled" || echo "fail")
        final_exit="${targeted_exit_code:-1}"
      fi
    fi
  fi
fi

python3 - <<'PY' \
  "${TRIAGE_JSON}" "${triage_attempted}" "${triage_mode}" "${triage_result}" \
  "${stall_detected}" "${stall_phase}" "${broad_exit_code}" "${targeted_exit_code}" \
  "${final_exit}" "${TRIAGE_MD}" "${MODE}" "${IMPL}" \
  "$(printf '%s\n' "${CHECK_IDS[@]-}")" "$(printf '%s\n' "${CHECK_PREFIXES[@]-}")" \
  "$(printf '%s\n' "${targeted_cmd_parts[@]-}")"
import json, sys
from pathlib import Path

out = Path(sys.argv[1])
triage_attempted = sys.argv[2].lower() == "true"
triage_mode = sys.argv[3]
triage_result = sys.argv[4]
stall_detected = sys.argv[5].lower() == "true"
stall_phase = sys.argv[6]
broad_exit_code = int(sys.argv[7] or "0")
targeted_exit_code = int(sys.argv[8] or "0")
final_exit = int(sys.argv[9] or "0")
md_path = Path(sys.argv[10])
mode = sys.argv[11]
impl = sys.argv[12]
ids = [x for x in (sys.argv[13] or "").splitlines() if x.strip()]
prefixes = [x for x in (sys.argv[14] or "").splitlines() if x.strip()]
targeted_parts = [x for x in (sys.argv[15] or "").splitlines() if x.strip()]

payload = {
    "version": 1,
    "status": "pass" if final_exit == 0 else "fail",
    "triage_attempted": triage_attempted,
    "triage_mode": triage_mode,
    "triage_result": triage_result,
    "failing_check_ids": ids,
    "failing_check_prefixes": prefixes,
    "stall_detected": stall_detected,
    "stall_phase": stall_phase or None,
    "broad_exit_code": broad_exit_code,
    "targeted_exit_code": targeted_exit_code,
    "final_exit_code": final_exit,
    "impl": impl,
    "requested_mode": mode,
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

summary = [
    "# Governance Triage Summary",
    "",
    f"- status: `{payload['status']}`",
    f"- triage_mode: `{triage_mode}`",
    f"- triage_result: `{triage_result}`",
    f"- stall_detected: `{str(stall_detected).lower()}`",
    f"- stall_phase: `{stall_phase or ''}`",
    "",
    "## Failing Check IDs",
    "",
]
if ids:
    summary.extend([f"- `{x}`" for x in ids])
else:
    summary.append("- none")
summary += ["", "## Failing Check Prefixes", ""]
if prefixes:
    summary.extend([f"- `{x}`" for x in prefixes])
else:
    summary.append("- none")
summary += ["", "## Suggested Targeted Re-run", ""]
if targeted_parts:
    cmd = "./scripts/runner_adapter.sh --impl " + impl + " governance " + " ".join(targeted_parts)
    summary.append(f"- `{cmd}`")
else:
    summary.append("- `./scripts/runner_adapter.sh --impl " + impl + " governance`")
md_path.parent.mkdir(parents=True, exist_ok=True)
md_path.write_text("\n".join(summary) + "\n", encoding="utf-8")
PY

echo "[governance-triage] wrote ${TRIAGE_JSON}"
echo "[governance-triage] wrote ${TRIAGE_MD}"
exit "${final_exit}"
