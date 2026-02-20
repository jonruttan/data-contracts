#!/usr/bin/env bash

scan_case_ids() {
  local root_dir="$1"
  rg -n '^id:\s*' "${root_dir}/specs" -g '*.spec.md' | sed -E 's/.*id:\s*//'
}

count_duplicate_case_ids() {
  local root_dir="$1"
  scan_case_ids "${root_dir}" | sort | uniq -d | sed '/^$/d' | wc -l | tr -d ' '
}
