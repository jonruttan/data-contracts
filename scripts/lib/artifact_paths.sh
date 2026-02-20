#!/usr/bin/env bash

resolve_artifact_path() {
  local root_dir="$1"
  local p="$2"
  if [[ "${p}" == /* ]]; then
    printf '%s%s\n' "${root_dir}" "${p}"
  else
    printf '%s/%s\n' "${root_dir}" "${p}"
  fi
}

ensure_parent_dir() {
  local p="$1"
  mkdir -p "$(dirname "${p}")"
}
