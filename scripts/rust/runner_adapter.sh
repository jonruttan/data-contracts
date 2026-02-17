#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

RUST_CLI_MANIFEST="${ROOT_DIR}/scripts/rust/spec_runner_cli/Cargo.toml"
RUST_CLI_TARGET=""
RUST_CLI_BIN="${ROOT_DIR}/target/debug/spec_runner_cli"

# Prefer native Apple Silicon binaries when available to avoid Rosetta/runtime hangs.
if [[ "$(uname -s)" == "Darwin" && "$(uname -m)" == "arm64" ]]; then
  ARM_TARGET="aarch64-apple-darwin"
  ARM_BIN="${ROOT_DIR}/target/${ARM_TARGET}/debug/spec_runner_cli"
  RUST_CLI_TARGET="${ARM_TARGET}"
  RUST_CLI_BIN="${ARM_BIN}"
fi

run_rust_subcommand() {
  local cmd="$1"
  shift
  if [[ -x "${RUST_CLI_BIN}" ]]; then
    "${RUST_CLI_BIN}" "${cmd}" "$@"
    return
  fi
  if [[ -n "${RUST_CLI_TARGET}" ]] && ! rustup target list --installed 2>/dev/null | grep -qx "${RUST_CLI_TARGET}"; then
    echo "ERROR: missing Rust target '${RUST_CLI_TARGET}'. Install with: rustup target add ${RUST_CLI_TARGET}" >&2
    return 2
  fi
  if [[ -n "${RUST_CLI_TARGET}" ]]; then
    cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" --target "${RUST_CLI_TARGET}" -- "${cmd}" "$@"
  else
    cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${cmd}" "$@"
  fi
}

exec_rust_subcommand() {
  local cmd="$1"
  shift
  if [[ -x "${RUST_CLI_BIN}" ]]; then
    exec "${RUST_CLI_BIN}" "${cmd}" "$@"
  fi
  if [[ -n "${RUST_CLI_TARGET}" ]] && ! rustup target list --installed 2>/dev/null | grep -qx "${RUST_CLI_TARGET}"; then
    echo "ERROR: missing Rust target '${RUST_CLI_TARGET}'. Install with: rustup target add ${RUST_CLI_TARGET}" >&2
    exit 2
  fi
  if [[ -n "${RUST_CLI_TARGET}" ]]; then
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" --target "${RUST_CLI_TARGET}" -- "${cmd}" "$@"
  else
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${cmd}" "$@"
  fi
}

run_with_timeout() {
  local timeout_seconds="$1"
  local label="$2"
  local env_var_name="$3"
  shift 3

  if [[ ! "${timeout_seconds}" =~ ^[0-9]+$ ]] || [[ "${timeout_seconds}" -le 0 ]]; then
    echo "ERROR: invalid timeout '${timeout_seconds}' for ${env_var_name}; expected positive integer seconds" >&2
    return 2
  fi

  local timeout_flag
  timeout_flag="$(mktemp -t spec_runner_timeout.XXXXXX)"
  rm -f "${timeout_flag}"

  "$@" &
  local cmd_pid=$!
  (
    sleep "${timeout_seconds}"
    if kill -0 "${cmd_pid}" 2>/dev/null; then
      : > "${timeout_flag}"
      kill -TERM "${cmd_pid}" 2>/dev/null || true
      sleep 5
      kill -KILL "${cmd_pid}" 2>/dev/null || true
    fi
  ) &
  local watchdog_pid=$!

  local cmd_status=0
  if ! wait "${cmd_pid}"; then
    cmd_status=$?
  fi
  kill "${watchdog_pid}" 2>/dev/null || true
  wait "${watchdog_pid}" 2>/dev/null || true

  if [[ -f "${timeout_flag}" ]]; then
    rm -f "${timeout_flag}"
    echo "ERROR: '${label}' timed out after ${timeout_seconds}s. Override with ${env_var_name}=<seconds>." >&2
    return 124
  fi

  rm -f "${timeout_flag}"
  return "${cmd_status}"
}

run_with_timeout_env() {
  local env_var_name="$1"
  local default_seconds="$2"
  local label="$3"
  shift 3

  local timeout_seconds="${!env_var_name:-${default_seconds}}"
  run_with_timeout "${timeout_seconds}" "${label}" "${env_var_name}" "$@"
}

subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi
shift

case "${subcommand}" in
  spec-eval|spec-ref|validate-report|style-check|schema-registry-check|schema-registry-build|schema-docs-check|schema-docs-build|lint|typecheck|compilecheck|conformance-purpose-json|conformance-purpose-md|spec-portability-json|spec-portability-md|spec-lang-adoption-json|spec-lang-adoption-md|runner-independence-json|runner-independence-md|python-dependency-json|python-dependency-md|docs-operability-json|docs-operability-md|contract-assertions-json|contract-assertions-md|objective-scorecard-json|objective-scorecard-md|spec-lang-stdlib-json|spec-lang-stdlib-md|ci-gate-summary|ci-cleanroom|perf-smoke|docs-generate|docs-generate-check|docs-build|docs-build-check|docs-lint|docs-graph|conformance-parity|test-core|test-full)
    exec_rust_subcommand "${subcommand}" "$@"
    ;;
esac

case "${subcommand}" in
  governance)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_GOVERNANCE_SECONDS \
      120 \
      governance \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  governance-heavy)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_GOVERNANCE_HEAVY_SECONDS \
      180 \
      governance-heavy \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  normalize-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_NORMALIZE_SECONDS \
      120 \
      normalize-check \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  normalize-fix)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_NORMALIZE_SECONDS \
      120 \
      normalize-fix \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  objective-scorecard-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  objective-scorecard-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-lang-stdlib-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-lang-stdlib-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  ci-gate-summary)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  ci-cleanroom)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  perf-smoke)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  docs-generate)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-generate \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  docs-generate-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-generate-check \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  docs-build)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-build \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  docs-build-check)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_DOCS_SECONDS \
      180 \
      docs-build-check \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  docs-lint)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  docs-graph)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  conformance-parity)
    run_with_timeout_env \
      SPEC_RUNNER_TIMEOUT_CONFORMANCE_PARITY_SECONDS \
      240 \
      conformance-parity \
      run_rust_subcommand "${subcommand}" "$@"
    ;;
  test-core)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  test-full)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  *)
    echo "ERROR: unsupported runner adapter subcommand: ${subcommand}" >&2
    exit 2
    ;;
esac
