#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

impl="rust"
forward=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --impl)
      impl="${2:-}"
      shift 2
      ;;
    --impl=*)
      impl="${1#--impl=}"
      shift
      ;;
    *)
      forward+=("$1")
      shift
      ;;
  esac
done

if [[ "${impl}" != "rust" ]]; then
  echo "ERROR: unsupported runner adapter impl: ${impl}" >&2
  exit 2
fi

exec dc-runner "${forward[@]}"
