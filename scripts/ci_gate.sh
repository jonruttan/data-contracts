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
if [[ -z "${SPEC_CI_PYTHON:-}" ]]; then
  if [[ -n "${VIRTUAL_ENV:-}" && -x "${VIRTUAL_ENV}/bin/python" ]]; then
    SPEC_CI_PYTHON="${VIRTUAL_ENV}/bin/python"
  elif [[ -x "${ROOT_DIR}/.venv/bin/python" ]]; then
    SPEC_CI_PYTHON="${ROOT_DIR}/.venv/bin/python"
  else
    SPEC_CI_PYTHON="python3"
  fi
fi

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

only_check_sets_changes() {
  local changed path
  changed="$(collect_changed_paths || true)"
  [[ -n "${changed}" ]] || return 1
  while IFS= read -r path; do
    [[ -z "${path}" ]] && continue
    if [[ "${path}" != "docs/spec/governance/check_sets_v1.yaml" ]]; then
      return 1
    fi
  done <<< "${changed}"
  return 0
}

only_gate_script_changes() {
  local changed path
  changed="$(collect_changed_paths || true)"
  [[ -n "${changed}" ]] || return 1
  while IFS= read -r path; do
    [[ -z "${path}" ]] && continue
    if [[ "${path}" != "scripts/local_ci_parity.sh" && "${path}" != "scripts/ci_gate.sh" ]]; then
      return 1
    fi
  done <<< "${changed}"
  return 0
}

if [[ "${CI:-}" != "true" ]] && [[ "${SPEC_CI_GATE_LOCAL_FAST_PATH:-1}" != "0" ]]; then
  if only_check_sets_changes; then
    echo "[ci-gate] local fast path: check_sets-only change; delegating to local_ci_parity.sh"
    exec "${ROOT_DIR}/scripts/local_ci_parity.sh"
  fi
  if only_gate_script_changes; then
    echo "[ci-gate] local fast path: gate-script-only change; delegating to local_ci_parity.sh"
    exec "${ROOT_DIR}/scripts/local_ci_parity.sh"
  fi
fi

"${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" critical-gate

"${SPEC_CI_PYTHON}" -m spec_runner.spec_lang_commands check-docs-freshness --strict

"${SPEC_RUNNER_BIN}" ci-gate-summary \
  --runner-bin "${SPEC_RUNNER_BIN}" \
  --runner-impl "${SPEC_RUNNER_IMPL}" \
  --out .artifacts/gate-summary.json \
  --trace-out .artifacts/gate-exec-trace.json
