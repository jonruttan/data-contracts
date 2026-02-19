#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ -z "${SPEC_RUNNER_BIN:-}" ]]; then
  SPEC_RUNNER_BIN="${ROOT_DIR}/runners/public/runner_adapter.sh"
fi
if [[ -z "${SPEC_RUNNER_IMPL:-}" ]]; then
  SPEC_RUNNER_IMPL="rust"
fi
COMPAT_MATRIX_ENABLED="${SPEC_COMPAT_MATRIX_ENABLED:-0}"

MODE="${SPEC_PREPUSH_MODE:-critical}"
PARITY_T0="$(date +%s)"

run_step() {
  local name="$1"
  shift
  echo "[local-ci-parity] ${name}: $*"
  "$@"
}

collect_changed_paths() {
  local upstream=""
  local lines=()
  if upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null)"; then
    while IFS= read -r line; do
      [[ -n "${line}" ]] && lines+=("${line}")
    done < <(git diff --name-only "${upstream}...HEAD")
  fi
  while IFS= read -r line; do
    [[ -n "${line}" ]] && lines+=("${line}")
  done < <(git diff --name-only)
  while IFS= read -r line; do
    [[ -n "${line}" ]] && lines+=("${line}")
  done < <(git diff --name-only --cached)
  while IFS= read -r line; do
    [[ -n "${line}" ]] && lines+=("${line}")
  done < <(git ls-files --others --exclude-standard)
  if [[ "${#lines[@]}" -eq 0 ]]; then
    return 0
  fi
  printf '%s\n' "${lines[@]}" | awk '!seen[$0]++'
}

paths_match_prefixes() {
  local path
  while IFS= read -r path; do
    [[ -z "${path}" ]] && continue
    for prefix in "$@"; do
      if [[ "${path}" == "${prefix}"* ]]; then
        return 0
      fi
    done
  done <<< "${CHANGED_PATHS}"
  return 1
}

paths_all_in_list() {
  local path
  local seen=0
  while IFS= read -r path; do
    [[ -z "${path}" ]] && continue
    seen=1
    local allowed=0
    for exact in "$@"; do
      if [[ "${path}" == "${exact}" ]]; then
        allowed=1
        break
      fi
    done
    if [[ "${allowed}" -ne 1 ]]; then
      return 1
    fi
  done <<< "${CHANGED_PATHS}"
  [[ "${seen}" -eq 1 ]]
}

is_fast_path_script_only_change() {
  paths_all_in_list "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"
}

print_critical_summary() {
  local summary_file="${ROOT_DIR}/.artifacts/critical-gate-summary.json"
  if [[ ! -f "${summary_file}" ]]; then
    echo "[local-ci-parity] critical summary missing: ${summary_file}"
    return 0
  fi
  local total_ms
  total_ms="$(grep -E '"total_duration_ms"' "${summary_file}" | head -1 | sed -E 's/[^0-9]*([0-9]+).*/\1/')"
  local first_failure
  first_failure="$(grep -E '"first_failure_check_id"' "${summary_file}" | head -1 | sed -E 's/.*: (null|"([^"]*)").*/\2/')"
  echo "[local-ci-parity] critical-gate total_duration_ms=${total_ms:-unknown}"
  if [[ -n "${first_failure}" ]]; then
    echo "[local-ci-parity] critical-gate first_failure_check_id=${first_failure}"
  fi
}

run_critical_gate() {
  local code=0
  set +e
  run_step critical-gate "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" critical-gate
  code=$?
  set -e
  print_critical_summary
  if [[ "${code}" -ne 0 ]]; then
    return "${code}"
  fi
}

lane_rust_core() {
  run_critical_gate

  CHANGED_PATHS="$(collect_changed_paths || true)"
  if [[ -n "${CHANGED_PATHS}" ]]; then
    echo "[local-ci-parity] changed-paths detected:"
    while IFS= read -r path; do
      [[ -n "${path}" ]] && echo "[local-ci-parity]   - ${path}"
    done <<< "${CHANGED_PATHS}"
  else
    echo "[local-ci-parity] no changed paths detected"
  fi

  if [[ "${SPEC_PREPUSH_REQUIRE_BROAD:-0}" == "1" ]]; then
    run_step governance-triage ./scripts/governance_triage.sh --mode broad-first --impl "${SPEC_RUNNER_IMPL}"
  else
    echo "[local-ci-parity] skip broad governance (set SPEC_PREPUSH_REQUIRE_BROAD=1 to enable)"
  fi

  if paths_match_prefixes "specs/" "runners/python/spec_runner/" "runners/python/spec_runner/normalize_repo_runtime.py" "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"; then
    if paths_all_in_list "specs/governance/check_sets_v1.yaml"; then
      echo "[local-ci-parity] skip normalize-check (check_sets-only change)"
    elif is_fast_path_script_only_change; then
      echo "[local-ci-parity] skip normalize-check (gate-script-only change)"
    else
      run_step normalize-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" normalize-check --changed-only
    fi
  else
    echo "[local-ci-parity] skip normalize-check (no matching changes)"
  fi

  if paths_match_prefixes "specs/" "runners/python/spec_runner/spec_lang_lint.py" "runners/python/spec_runner/spec_lang_hygiene.py" "runners/python/spec_runner/spec_lang_format.py" "runners/python/spec_runner/spec_lang_commands.py" "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"; then
    if paths_all_in_list "specs/governance/check_sets_v1.yaml"; then
      echo "[local-ci-parity] skip style-check (check_sets-only change)"
    elif is_fast_path_script_only_change; then
      echo "[local-ci-parity] skip style-check (gate-script-only change)"
    else
      run_step style-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" style-check
    fi
  else
    echo "[local-ci-parity] skip style-check (no matching changes)"
  fi

  if paths_match_prefixes "docs/" "scripts/docs_" "scripts/generate_" "specs/schema/" "specs/governance/metrics/" "runners/python/spec_runner/docs_" "runners/python/spec_runner/docs_generators.py" "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"; then
    if paths_all_in_list "specs/governance/check_sets_v1.yaml"; then
      echo "[local-ci-parity] skip docs-generate-check (check_sets-only change)"
    elif is_fast_path_script_only_change; then
      echo "[local-ci-parity] skip docs-generate-check (gate-script-only change)"
    else
      run_step docs-generate-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" docs-generate-check
    fi
  else
    echo "[local-ci-parity] skip docs-generate-check (no matching changes)"
  fi

  if paths_match_prefixes "docs/" "runners/python/spec_runner/script_runtime_commands.py" "runners/python/spec_runner/docs_inventory.py" "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"; then
    if paths_all_in_list "specs/governance/check_sets_v1.yaml"; then
      echo "[local-ci-parity] skip docs-lint (check_sets-only change)"
    elif is_fast_path_script_only_change; then
      echo "[local-ci-parity] skip docs-lint (gate-script-only change)"
    else
      run_step docs-lint "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" docs-lint
    fi
  else
    echo "[local-ci-parity] skip docs-lint (no matching changes)"
  fi

  if [[ "${SPEC_PREPUSH_REQUIRE_BROAD:-0}" == "1" ]]; then
    run_step perf-smoke "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" perf-smoke --mode strict --compare-only
  else
    echo "[local-ci-parity] skip perf-smoke (broad mode disabled)"
  fi
}

lane_compatibility_matrix() {
  if [[ "${COMPAT_MATRIX_ENABLED}" != "1" ]]; then
    echo "[local-ci-parity] compatibility matrix disabled (set SPEC_COMPAT_MATRIX_ENABLED=1 to enable)"
    return 0
  fi
  echo "[local-ci-parity] compatibility matrix enabled (non-blocking)"
  local py_cmd=""
  if [[ -n "${VIRTUAL_ENV:-}" && -x "${VIRTUAL_ENV}/bin/python" ]]; then
    py_cmd="${VIRTUAL_ENV}/bin/python"
  elif [[ -x "${ROOT_DIR}/.venv/bin/python" ]]; then
    py_cmd="${ROOT_DIR}/.venv/bin/python"
  elif command -v python3 >/dev/null 2>&1; then
    py_cmd="python3"
  fi
  if [[ -n "${py_cmd}" ]]; then
    set +e
    PYTHONPATH="${ROOT_DIR}/runners/python" run_step compat-python-governance "${py_cmd}" -m spec_runner.spec_lang_commands run-governance-specs --liveness-level basic
    PYTHONPATH="${ROOT_DIR}/runners/python" run_step compat-python-parity "${py_cmd}" -m spec_runner.spec_lang_commands compare-conformance-parity --python-only --cases specs/conformance/cases --out .artifacts/conformance-parity-python.json
    set -e
  else
    echo "[local-ci-parity] skip python compatibility lane (python interpreter unavailable)"
  fi
  if command -v php >/dev/null 2>&1; then
    set +e
    run_step compat-php-conformance php runners/php/conformance_runner.php --cases specs/conformance/cases --case-formats md --out .artifacts/php-conformance-report.json
    set -e
  else
    echo "[local-ci-parity] skip php compatibility lane (php interpreter unavailable)"
  fi
}

case "${MODE}" in
  critical)
    lane_rust_core
    lane_compatibility_matrix
    echo "[local-ci-parity] mode=critical: rust-only critical path"
    ;;
  fast)
    lane_rust_core
    lane_compatibility_matrix
    echo "[local-ci-parity] mode=fast: rust-only critical path"
    ;;
  *)
    echo "ERROR: unsupported SPEC_PREPUSH_MODE '${MODE}' (expected critical|fast)" >&2
    exit 2
    ;;
esac

PARITY_T1="$(date +%s)"
PARITY_ELAPSED="$((PARITY_T1 - PARITY_T0))"
echo "[local-ci-parity] elapsed_seconds=${PARITY_ELAPSED}"
if [[ "${PARITY_ELAPSED}" -gt 120 ]]; then
  echo "[local-ci-parity] WARNING: exceeded target SLO (120s)"
fi
echo "[local-ci-parity] PASS"
