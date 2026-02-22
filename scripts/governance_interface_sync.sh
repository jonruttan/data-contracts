#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_ROOT="${ROOT_DIR}/specs/04_governance"
DST_ROOT="${ROOT_DIR}/specs/governance"

ALLOWED_REL=(
  "index.md"
  "check_sets_v1.yaml"
  "check_prefix_map_v1.yaml"
  "cases/core/index.md"
  "metrics/index.md"
)

mode="--write"
if [[ $# -gt 1 ]]; then
  echo "usage: ./scripts/governance_interface_sync.sh [--write|--check]" >&2
  exit 2
fi
if [[ $# -eq 1 ]]; then
  mode="$1"
fi
case "${mode}" in
  --write|--check)
    ;;
  *)
    echo "usage: ./scripts/governance_interface_sync.sh [--write|--check]" >&2
    exit 2
    ;;
esac

for rel in "${ALLOWED_REL[@]}"; do
  src="${SRC_ROOT}/${rel}"
  if [[ ! -f "${src}" ]]; then
    echo "ERROR: missing canonical governance source file: ${src}" >&2
    exit 1
  fi
done

check_only() {
  if [[ ! -d "${DST_ROOT}" ]]; then
    echo "ERROR: governance interface directory is missing: ${DST_ROOT}" >&2
    exit 1
  fi

  local actual_sorted expected_sorted
  actual_sorted="$(mktemp)"
  expected_sorted="$(mktemp)"

  (
    cd "${DST_ROOT}"
    find . -type f | sed 's#^\./##' | sort
  ) > "${actual_sorted}"
  printf '%s\n' "${ALLOWED_REL[@]}" | sort > "${expected_sorted}"

  if ! diff -u "${expected_sorted}" "${actual_sorted}" >/dev/null; then
    echo "ERROR: governance interface surface has drift or extra files under specs/governance" >&2
    diff -u "${expected_sorted}" "${actual_sorted}" || true
    rm -f "${actual_sorted}" "${expected_sorted}"
    exit 1
  fi

  local rel
  for rel in "${ALLOWED_REL[@]}"; do
    src="${SRC_ROOT}/${rel}"
    dst="${DST_ROOT}/${rel}"
    if [[ ! -f "${dst}" ]]; then
      echo "ERROR: missing generated interface file: ${dst}" >&2
      rm -f "${actual_sorted}" "${expected_sorted}"
      exit 1
    fi
    if ! cmp -s "${src}" "${dst}"; then
      echo "ERROR: interface file out of sync: specs/governance/${rel}" >&2
      rm -f "${actual_sorted}" "${expected_sorted}"
      exit 1
    fi
  done

  rm -f "${actual_sorted}" "${expected_sorted}"
  echo "OK: governance interface is synced with specs/04_governance"
}

write_all() {
  rm -rf "${DST_ROOT}"
  mkdir -p "${DST_ROOT}/cases/core" "${DST_ROOT}/metrics"

  local rel
  for rel in "${ALLOWED_REL[@]}"; do
    src="${SRC_ROOT}/${rel}"
    dst="${DST_ROOT}/${rel}"
    mkdir -p "$(dirname "${dst}")"
    cp "${src}" "${dst}"
    echo "synced: specs/governance/${rel}"
  done

  check_only
}

if [[ "${mode}" == "--check" ]]; then
  check_only
else
  write_all
fi
