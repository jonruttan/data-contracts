#!/usr/bin/env bash

emit_ingest_log_json() {
  local generated_at="$1"
  local max_age_hours="$2"
  local compat_stale_or_missing="$3"
  local entries_json="$4"

  jq -cn \
    --arg generated_at "${generated_at}" \
    --argjson max_age_hours "${max_age_hours}" \
    --argjson compat_stale_or_missing "${compat_stale_or_missing}" \
    --argjson entries "${entries_json}" \
    '{
      version: 1,
      generated_at: $generated_at,
      max_age_hours: $max_age_hours,
      compatibility_stale_or_missing_count: $compat_stale_or_missing,
      entries: $entries
    }'
}
