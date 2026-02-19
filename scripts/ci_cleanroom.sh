#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF="${1:-HEAD}"
SOURCE_MODE="${SPEC_CLEANROOM_SOURCE_MODE:-working-tree}"

TMP_PARENT="$(mktemp -d "${TMPDIR:-/tmp}/data-contracts-cleanroom.XXXXXX")"
WORKTREE_DIR="${TMP_PARENT}/repo"

cleanup() {
  if [[ "${SOURCE_MODE}" == "head" ]]; then
    git -C "${ROOT_DIR}" worktree remove --force "${WORKTREE_DIR}" >/dev/null 2>&1 || true
  fi
  rm -rf "${TMP_PARENT}"
}
trap cleanup EXIT

if [[ "${SOURCE_MODE}" == "head" ]]; then
  echo "[cleanroom] creating git worktree at ${WORKTREE_DIR} (${REF})"
  git -C "${ROOT_DIR}" worktree add --detach "${WORKTREE_DIR}" "${REF}" >/dev/null
else
  echo "[cleanroom] creating working-tree snapshot at ${WORKTREE_DIR}"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude=".git/" \
      --exclude=".artifacts/" \
      --exclude="target/" \
      "${ROOT_DIR}/" "${WORKTREE_DIR}/"
  else
    (
      cd "${ROOT_DIR}" && \
      tar --exclude=".git" --exclude=".artifacts" --exclude="target" -cf - .
    ) | (cd "${WORKTREE_DIR}" && tar -xf -)
  fi
  printf "gitdir: /dev/null\n" > "${WORKTREE_DIR}/.git"
fi

cd "${WORKTREE_DIR}"

echo "[cleanroom] running ci gate"
./scripts/ci_gate.sh

echo "[cleanroom] PASS"
