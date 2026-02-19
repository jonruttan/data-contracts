#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

TRIAGE_ENABLED="${SPEC_GOV_TRIAGE_ENABLED:-1}"
TRIAGE_MAX_RETRIES="${SPEC_GOV_TRIAGE_MAX_RETRIES:-1}"
TRIAGE_FALLBACK_PREFIXES_RAW="${SPEC_GOV_TRIAGE_FALLBACK_PREFIXES:-docs.,normalization.,runtime.}"
PROFILE_LEVEL="${SPEC_GOV_TRIAGE_PROFILE_LEVEL:-basic}"
MODE="${SPEC_GOV_TRIAGE_MODE_DEFAULT:-targeted-first}"
IMPL="${SPEC_RUNNER_IMPL:-rust}"

FROM_FAILURES=""
declare -a CHECK_IDS=()
declare -a CHECK_PREFIXES=()
declare -a CMD_ARR=()

auto_trim() {
  echo "${1:-}" | awk '{$1=$1;print}'
}

usage() {
  cat <<'USAGE'
Usage: scripts/governance_triage.sh [options]

Options:
  --mode auto|targeted|targeted-first|broad-first
  --impl rust
  --check-id <id>            Repeatable
  --check-prefix <prefix>    Repeatable
  --from-failures <path>     Read failing check ids/prefixes from triage JSON
  --profile-level <level>    off|basic|detailed|debug
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

if [[ "${IMPL}" != "rust" ]]; then
  echo "ERROR: --impl must be rust in data-contracts" >&2
  exit 2
fi

case "${MODE}" in
  auto|targeted|targeted-first|broad-first) ;;
  *)
    echo "ERROR: --mode must be auto|targeted|targeted-first|broad-first" >&2
    exit 2
    ;;
esac

if [[ -n "${FROM_FAILURES}" && -f "${FROM_FAILURES}" ]]; then
  if command -v jq >/dev/null 2>&1; then
    while IFS= read -r id; do
      [[ -n "${id}" ]] && CHECK_IDS+=("${id}")
    done < <(jq -r '.failing_check_ids[]? // empty' "${FROM_FAILURES}")
    while IFS= read -r prefix; do
      [[ -n "${prefix}" ]] && CHECK_PREFIXES+=("${prefix}")
    done < <(jq -r '.failing_check_prefixes[]? // empty' "${FROM_FAILURES}")
  else
    echo "ERROR: --from-failures requires jq" >&2
    exit 2
  fi
fi

if [[ "${#CHECK_PREFIXES[@]}" -eq 0 ]]; then
  IFS=',' read -r -a CHECK_PREFIXES <<< "${TRIAGE_FALLBACK_PREFIXES_RAW}"
fi

for i in "${!CHECK_PREFIXES[@]}"; do
  CHECK_PREFIXES[$i]="$(auto_trim "${CHECK_PREFIXES[$i]}")"
done

mkdir -p .artifacts
TRIAGE_JSON=".artifacts/governance-triage.json"
TRIAGE_MD=".artifacts/governance-triage-summary.md"
TMP_OUT="$(mktemp -t governance-triage.XXXXXX)"
trap 'rm -f "${TMP_OUT}"' EXIT

set_cmd() {
  local scope="$1"
  CMD_ARR=(./runners/public/runner_adapter.sh --impl rust governance)
  if [[ "${scope}" == "targeted" ]]; then
    local p
    for p in "${CHECK_PREFIXES[@]-}"; do
      [[ -n "${p}" ]] && CMD_ARR+=(--check-prefix "${p}")
    done
  fi
}

run_cmd_capture() {
  echo "[governance-triage] ${CMD_ARR[*]}"
  set +e
  "${CMD_ARR[@]}" 2>&1 | tee "${TMP_OUT}"
  local rc=$?
  set -e
  return "${rc}"
}

triage_attempted=true
triage_mode="${MODE}"
triage_result="fail"
broad_exit_code=0
targeted_exit_code=0
final_exit=1
selection_source="explicit"

if [[ "${TRIAGE_ENABLED}" != "1" && "${TRIAGE_ENABLED,,}" != "true" ]]; then
  triage_attempted=false
  triage_mode="broad"
  set_cmd broad
  run_cmd_capture || broad_exit_code=$?
  final_exit="${broad_exit_code}"
else
  case "${MODE}" in
    targeted)
      set_cmd targeted
      run_cmd_capture || targeted_exit_code=$?
      final_exit="${targeted_exit_code}"
      ;;
    broad-first)
      set_cmd broad
      run_cmd_capture || broad_exit_code=$?
      if [[ "${broad_exit_code}" -eq 0 ]]; then
        final_exit=0
      else
        set_cmd targeted
        run_cmd_capture || targeted_exit_code=$?
        final_exit="${targeted_exit_code}"
      fi
      ;;
    auto|targeted-first)
      retry=0
      while [[ "${retry}" -lt "${TRIAGE_MAX_RETRIES}" ]]; do
        retry=$((retry + 1))
        set_cmd targeted
        run_cmd_capture || targeted_exit_code=$?
        if [[ "${targeted_exit_code}" -eq 0 ]]; then
          final_exit=0
          break
        fi
      done
      if [[ "${final_exit}" -ne 0 ]]; then
        set_cmd broad
        run_cmd_capture || broad_exit_code=$?
        final_exit="${broad_exit_code}"
      fi
      ;;
  esac
fi

if [[ "${final_exit}" -eq 0 ]]; then
  triage_result="pass"
else
  triage_result="fail"
fi

if command -v jq >/dev/null 2>&1; then
  FAIL_IDS_JSON="$(printf '%s\n' "${CHECK_IDS[@]-}" | jq -R -s -c 'split("\n")|map(select(length>0))')"
  FAIL_PREFIX_JSON="$(printf '%s\n' "${CHECK_PREFIXES[@]-}" | jq -R -s -c 'split("\n")|map(select(length>0))')"
  jq -n \
    --arg status "$( [[ "${final_exit}" -eq 0 ]] && echo pass || echo fail )" \
    --argjson triage_attempted "$( [[ "${triage_attempted}" == true ]] && echo true || echo false )" \
    --arg triage_mode "${triage_mode}" \
    --arg triage_result "${triage_result}" \
    --argjson broad_exit_code "${broad_exit_code}" \
    --argjson targeted_exit_code "${targeted_exit_code}" \
    --argjson final_exit_code "${final_exit}" \
    --arg impl rust \
    --arg requested_mode "${MODE}" \
    --arg selection_source "${selection_source}" \
    --argjson failing_check_ids "${FAIL_IDS_JSON}" \
    --argjson failing_check_prefixes "${FAIL_PREFIX_JSON}" \
    '{version:1,status:$status,triage_attempted:$triage_attempted,triage_mode:$triage_mode,triage_result:$triage_result,failing_check_ids:$failing_check_ids,failing_check_prefixes:$failing_check_prefixes,stall_detected:false,stall_phase:null,broad_exit_code:$broad_exit_code,targeted_exit_code:$targeted_exit_code,final_exit_code:$final_exit_code,impl:$impl,requested_mode:$requested_mode,selection_source:$selection_source,broad_required:false}' > "${TRIAGE_JSON}"
else
  echo '{"version":1,"status":"fail","error":"jq is required"}' > "${TRIAGE_JSON}"
fi

{
  echo "# Governance Triage Summary"
  echo
  echo "- status: \`$( [[ "${final_exit}" -eq 0 ]] && echo pass || echo fail )\`"
  echo "- triage_mode: \`${triage_mode}\`"
  echo "- triage_result: \`${triage_result}\`"
  echo
  echo "## Failing Check IDs"
  echo
  if [[ "${#CHECK_IDS[@]}" -eq 0 ]]; then
    echo "- none"
  else
    for id in "${CHECK_IDS[@]-}"; do
      echo "- \`${id}\`"
    done
  fi
  echo
  echo "## Failing Check Prefixes"
  echo
  if [[ "${#CHECK_PREFIXES[@]}" -eq 0 ]]; then
    echo "- none"
  else
    for prefix in "${CHECK_PREFIXES[@]-}"; do
      echo "- \`${prefix}\`"
    done
  fi
  echo
  echo "## Suggested Targeted Re-run"
  echo
  printf -- '- `./runners/public/runner_adapter.sh --impl rust governance'
  local_has_prefix=false
  for prefix in "${CHECK_PREFIXES[@]-}"; do
    [[ -z "${prefix}" ]] && continue
    printf -- ' --check-prefix %q' "${prefix}"
    local_has_prefix=true
  done
  echo '`'
} > "${TRIAGE_MD}"

echo "[governance-triage] wrote ${TRIAGE_JSON}"
echo "[governance-triage] wrote ${TRIAGE_MD}"
exit "${final_exit}"
