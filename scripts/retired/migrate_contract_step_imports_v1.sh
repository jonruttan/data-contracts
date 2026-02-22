#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

MODE=""
PATTERN=""
declare -a PATHS=()

while [[ $# -gt 0 ]]; do
  case "${1}" in
    --check)
      MODE="--check"
      shift
      ;;
    --write)
      MODE="--write"
      shift
      ;;
    --pattern)
      PATTERN="${2:-}"
      shift 2
      ;;
    --)
      shift
      while [[ $# -gt 0 ]]; do
        PATHS+=("$1")
        shift
      done
      ;;
    -*)
      echo "ERROR: unsupported arg: ${1}" >&2
      exit 2
      ;;
    *)
      PATHS+=("$1")
      shift
      ;;
  esac
done

if [[ -z "${MODE}" ]]; then
  echo "ERROR: choose either --check or --write" >&2
  exit 2
fi

ARGS=("${MODE}")
if [[ -n "${PATTERN}" ]]; then
  echo "WARN: --pattern is accepted for compatibility but ignored by Rust migrator" >&2
fi
if [[ "${#PATHS[@]}" -gt 0 ]]; then
  PATHS_CSV="$(IFS=,; echo "${PATHS[*]}")"
  ARGS+=("--paths" "${PATHS_CSV}")
fi

exec ./scripts/runner_bin.sh normalize-contract-step-imports-v1 "${ARGS[@]}"
