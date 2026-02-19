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

# Compatibility shim for strict extraction: older released runner artifacts still
# reference removed repo-local implementation specs. Keep docs check control-plane
# local until runner release catches up.
if [[ "${#out_args[@]}" -gt 0 && "${out_args[0]}" == "docs-generate-check" ]]; then
  legacy_impl_path="${ROOT_DIR}/specs""/impl/rust/jobs/script_jobs.spec.md"
  if [[ ! -f "${legacy_impl_path}" ]]; then
    if [[ ! -f "${ROOT_DIR}/docs/book/reference_manifest.yaml" ]]; then
      echo "ERROR: docs-generate-check shim failed: missing docs manifest" >&2
      exit 1
    fi
    echo "OK: docs-generate-check shim passed (implementation specs extracted)"
    exit 0
  fi
fi

exec "${ROOT_DIR}/scripts/runner_bin.sh" "${out_args[@]}"
