#!/usr/bin/env bash

emit_json_file() {
  local out_path="$1"
  local jq_program="$2"
  shift 2
  jq -n "$@" "${jq_program}" > "${out_path}"
}
