#!/usr/bin/env bash

emit_check_set_id_profile_pairs() {
  local check_set_file="$1"
  awk '
  BEGIN { profile="" }
  /^  (critical|full|optional):[[:space:]]*$/ {
    profile=$1
    sub(/:$/, "", profile)
    next
  }
  /^      - id:[[:space:]]*/ {
    id=$0
    sub(/^      - id:[[:space:]]*/, "", id)
    if (profile != "") print id "|" profile
  }
  ' "${check_set_file}"
}

emit_optional_check_ids() {
  local check_set_file="$1"
  awk '
  BEGIN { profile="" }
  /^  (critical|full|optional):[[:space:]]*$/ {
    profile=$1
    sub(/:$/, "", profile)
    next
  }
  profile == "optional" && /^      - id:[[:space:]]*/ {
    id=$0
    sub(/^      - id:[[:space:]]*/, "", id)
    print id
  }
  ' "${check_set_file}" | sort -u
}
