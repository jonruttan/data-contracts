#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

DELEGATE="${ROOT_DIR}/scripts/runner_adapter.sh"

subcommand="${1:-}"
if [[ -z "${subcommand}" ]]; then
  echo "ERROR: missing runner adapter subcommand" >&2
  exit 2
fi
shift

case "${subcommand}" in
  governance)
    exec "${DELEGATE}" governance "$@"
    ;;
  style-check)
    exec "${DELEGATE}" style-check "$@"
    ;;
  lint)
    exec "${DELEGATE}" lint "$@"
    ;;
  typecheck)
    exec "${DELEGATE}" typecheck "$@"
    ;;
  compilecheck)
    exec "${DELEGATE}" compilecheck "$@"
    ;;
  conformance-purpose-json)
    exec "${DELEGATE}" conformance-purpose-json "$@"
    ;;
  conformance-purpose-md)
    exec "${DELEGATE}" conformance-purpose-md "$@"
    ;;
  spec-portability-json)
    exec "${DELEGATE}" spec-portability-json "$@"
    ;;
  spec-portability-md)
    exec "${DELEGATE}" spec-portability-md "$@"
    ;;
  docs-build)
    exec "${DELEGATE}" docs-build "$@"
    ;;
  docs-build-check)
    exec "${DELEGATE}" docs-build-check "$@"
    ;;
  docs-lint)
    exec "${DELEGATE}" docs-lint "$@"
    ;;
  docs-graph)
    exec "${DELEGATE}" docs-graph "$@"
    ;;
  conformance-parity)
    exec "${DELEGATE}" conformance-parity "$@"
    ;;
  test-core)
    exec "${DELEGATE}" test-core "$@"
    ;;
  test-full)
    exec "${DELEGATE}" test-full "$@"
    ;;
  *)
    echo "ERROR: unsupported runner adapter subcommand: ${subcommand}" >&2
    exit 2
    ;;
esac
