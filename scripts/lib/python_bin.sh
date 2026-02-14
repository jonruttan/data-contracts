#!/usr/bin/env bash

resolve_python_bin() {
  local root_dir="$1"
  if [[ -n "${PYTHON_BIN:-}" ]]; then
    printf '%s\n' "${PYTHON_BIN}"
    return 0
  fi
  if [[ -x "${root_dir}/.venv/bin/python" ]]; then
    printf '%s\n' "${root_dir}/.venv/bin/python"
    return 0
  fi
  if [[ -x "${root_dir}/../../.venv/bin/python" ]]; then
    printf '%s\n' "${root_dir}/../../.venv/bin/python"
    return 0
  fi
  printf '%s\n' "python3"
}
