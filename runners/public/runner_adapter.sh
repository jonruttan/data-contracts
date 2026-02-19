#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

impl="${SPEC_RUNNER_IMPL:-rust}"
out_args=()

while [[ $# -gt 0 ]]; do
  case "${1}" in
    --impl)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --impl requires a value" >&2
        exit 2
      fi
      impl="${2}"
      shift 2
      ;;
    *)
      out_args+=("${1}")
      shift
      ;;
  esac
done

if [[ "${impl}" != "rust" ]]; then
  echo "ERROR: unsupported runner implementation: ${impl} (expected rust only)" >&2
  exit 2
fi

exec "${ROOT_DIR}/scripts/runner_bin.sh" "${out_args[@]}"
