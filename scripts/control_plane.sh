#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

ensure_artifacts_dir() {
  mkdir -p .artifacts
}

check_required_files() {
  local required=(
    "README.md"
    "docs/book/index.md"
    "docs/book/reference_manifest.yaml"
    "specs/contract/10_docs_quality.md"
    "specs/contract/12_runner_interface.md"
    "specs/contract/25_compatibility_matrix.md"
    "specs/contract/27_runner_status_exchange.md"
    "specs/schema/runner_status_report_v1.yaml"
    "specs/schema/runner_status_matrix_v1.yaml"
    "specs/schema/runner_certification_registry_v1.yaml"
    "specs/governance/check_sets_v1.yaml"
    "specs/governance/check_prefix_map_v1.yaml"
    ".github/workflows/ci.yml"
  )

  local missing=0
  for file in "${required[@]}"; do
    if [[ ! -f "${file}" ]]; then
      echo "missing required file: ${file}" >&2
      missing=1
    fi
  done
  return "${missing}"
}

check_no_runtime_runner_execution() {
  local pattern='runners/public/runner_adapter\.sh --impl'
  if rg -n "${pattern}" .github/workflows/ci.yml scripts/ci_gate.sh scripts/core_gate.sh scripts/local_ci_parity.sh Makefile >/dev/null; then
    echo "runtime runner execution references are forbidden in control-plane CI surfaces" >&2
    rg -n "${pattern}" .github/workflows/ci.yml scripts/ci_gate.sh scripts/core_gate.sh scripts/local_ci_parity.sh Makefile || true
    return 1
  fi
}

check_control_plane_language() {
  rg -n --fixed-strings "implementation-agnostic control plane" README.md >/dev/null
  rg -n "does .*execute runtime lanes" README.md >/dev/null
  rg -n --fixed-strings "implementation-agnostic boundary" specs/contract/12_runner_interface.md >/dev/null
  rg -n --fixed-strings "telemetry and governance evaluator" specs/contract/25_compatibility_matrix.md >/dev/null
}

check_readme_usage_paths() {
  local need=(
    "How Users Use This Project"
    "Author a spec change"
    "Validate docs and contract coherence"
    "Read compatibility and status telemetry"
    "Debug governance or documentation drift"
  )

  local token
  for token in "${need[@]}"; do
    if ! rg -n --fixed-strings "${token}" README.md >/dev/null; then
      echo "README missing required task path token: ${token}" >&2
      return 1
    fi
  done

  if rg -n "make (setup|prepush)|hooks-install" README.md >/dev/null; then
    echo "README contains forbidden Makefile onboarding cookbook tokens" >&2
    return 1
  fi
}

run_governance() {
  ensure_artifacts_dir
  check_required_files
  check_no_runtime_runner_execution
  check_control_plane_language
  check_readme_usage_paths

  cat > .artifacts/control-plane-governance-summary.md <<'MD'
# Control-Plane Governance Summary

- status: pass
- checks:
  - required files present
  - CI/runtime execution forbidden in this repository
  - control-plane language present in docs/contracts
  - README task-based usage paths present
MD

  jq -n '{status:"pass", checks:["required_files","control_plane_ci_runner_execution_forbidden","control_plane_language_present","readme_task_usage_paths_present"]}' > .artifacts/control-plane-governance-summary.json
  echo "OK: governance checks passed"
}

run_docs_generate_check() {
  ensure_artifacts_dir
  local required=(
    "docs/book/reference_manifest.yaml"
    "docs/book/reference_index.md"
    "docs/book/reference_coverage.md"
    "docs/book/99_generated_reference_index.md"
  )
  local missing=0
  local file
  for file in "${required[@]}"; do
    if [[ ! -f "${file}" ]]; then
      echo "missing docs reference surface: ${file}" >&2
      missing=1
    fi
  done
  if [[ "${missing}" -ne 0 ]]; then
    return 1
  fi
  echo "OK: docs reference surfaces present"
}

run_critical_gate() {
  run_governance
  run_docs_generate_check
  ./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness

  jq -n '{status:"pass", mode:"critical", steps:["governance","docs-generate-check","runner-status-ingest"]}' > .artifacts/critical-gate-summary.json
  echo "OK: critical gate checks passed"
}

run_ci_gate_summary() {
  ensure_artifacts_dir
  local out=".artifacts/gate-summary.json"
  local trace_out=".artifacts/gate-exec-trace.json"

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --out)
        out="$2"
        shift 2
        ;;
      --trace-out)
        trace_out="$2"
        shift 2
        ;;
      --runner-bin|--runner-impl)
        shift 2
        ;;
      *)
        shift
        ;;
    esac
  done

  jq -n '{status:"pass", control_plane_only:true, timestamp:now|todate}' > "${out}"
  jq -n '{events:[{"step":"ci-gate-summary","status":"pass"}]}' > "${trace_out}"
  echo "OK: ci gate summary written"
}

cmd="${1:-}"
[[ -n "${cmd}" ]] || {
  echo "usage: ./scripts/control_plane.sh <critical-gate|governance|docs-generate-check|style-check|governance-broad-native|ci-gate-summary>" >&2
  exit 2
}
shift || true

case "${cmd}" in
  critical-gate)
    run_critical_gate
    ;;
  governance|governance-broad-native|style-check)
    run_governance
    ;;
  docs-generate-check)
    run_docs_generate_check
    ;;
  ci-gate-summary)
    run_ci_gate_summary "$@"
    ;;
  *)
    echo "unknown control-plane command: ${cmd}" >&2
    exit 2
    ;;
esac
