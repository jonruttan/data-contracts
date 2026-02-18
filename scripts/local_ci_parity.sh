#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ -z "${SPEC_RUNNER_BIN:-}" ]]; then
  SPEC_RUNNER_BIN="${ROOT_DIR}/scripts/runner_adapter.sh"
fi
if [[ -z "${SPEC_RUNNER_IMPL:-}" ]]; then
  SPEC_RUNNER_IMPL="rust"
fi

MODE="${SPEC_PREPUSH_MODE:-parity}"

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

lane_rust_core() {
  run_step normalize-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" normalize-check
  run_step governance-triage ./scripts/governance_triage.sh --mode auto --impl "${SPEC_RUNNER_IMPL}"

  CHANGED_PATHS="$(collect_changed_paths || true)"
  if [[ -n "${CHANGED_PATHS}" ]]; then
    echo "[local-ci-parity] changed-paths detected:"
    while IFS= read -r path; do
      [[ -n "${path}" ]] && echo "[local-ci-parity]   - ${path}"
    done <<< "${CHANGED_PATHS}"
  else
    echo "[local-ci-parity] no changed paths detected"
  fi

  if paths_match_prefixes "docs/spec/" "spec_runner/" "scripts/run_governance_specs.py" "scripts/normalize_repo.py"; then
    run_step governance-heavy "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance-heavy
  else
    echo "[local-ci-parity] skip governance-heavy (no matching changes)"
  fi

  if paths_match_prefixes "docs/" "scripts/docs_" "scripts/generate_" "docs/spec/schema/" "docs/spec/metrics/" "spec_runner/docs_" "spec_runner/docs_generators.py"; then
    run_step docs-generate-check "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" docs-generate-check
  else
    echo "[local-ci-parity] skip docs-generate-check (no matching changes)"
  fi

  run_step perf-smoke "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" perf-smoke --mode strict --compare-only
}

lane_python_parity() {
  run_step python-governance-triage ./scripts/governance_triage.sh --mode auto --impl python
  run_step python-conformance-parity "${SPEC_RUNNER_BIN}" --impl python conformance-parity
}

case "${MODE}" in
  parity)
    lane_rust_core
    lane_python_parity
    ;;
  fast)
    lane_rust_core
    echo "[local-ci-parity] mode=fast: skip python parity lane"
    ;;
  *)
    echo "ERROR: unsupported SPEC_PREPUSH_MODE '${MODE}' (expected parity|fast)" >&2
    exit 2
    ;;
esac

echo "[local-ci-parity] PASS"
