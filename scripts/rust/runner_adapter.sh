#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

RUST_CLI_MANIFEST="${ROOT_DIR}/scripts/rust/spec_runner_cli/Cargo.toml"
RUST_CLI_BIN="${ROOT_DIR}/target/debug/spec_runner_cli"

subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi
shift

case "${subcommand}" in
  governance)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  style-check)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  normalize-check)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  normalize-fix)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  lint)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  typecheck)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  compilecheck)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  conformance-purpose-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  conformance-purpose-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-portability-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-portability-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-lang-adoption-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  spec-lang-adoption-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  runner-independence-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  runner-independence-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  python-dependency-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  python-dependency-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  docs-operability-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  docs-operability-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  contract-assertions-json)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  contract-assertions-md)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
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
  docs-build)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
    ;;
  docs-build-check)
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
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
    if [[ -x "${RUST_CLI_BIN}" ]]; then
      exec "${RUST_CLI_BIN}" "${subcommand}" "$@"
    fi
    exec cargo run --quiet --manifest-path "${RUST_CLI_MANIFEST}" -- "${subcommand}" "$@"
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
