#!/usr/bin/env bash

emit_matrix_json() {
  local updated_at="$1"
  local matrix_rows_json="$2"
  jq -cn --arg updated_at "${updated_at}" --argjson matrix_rows "${matrix_rows_json}" '{version:1, updated_at:$updated_at, matrix_rows:$matrix_rows}'
}

emit_matrix_markdown() {
  local out_json_file="$1"
  local out_md_file="$2"
  local now_utc="$3"
  local max_age_hours="$4"
  local compat_count="$5"

  {
    echo "# Runner Status Matrix"
    echo
    echo "- updated_at: \`${now_utc}\`"
    echo "- freshness_slo_hours: \`${max_age_hours}\`"
    echo "- compatibility_stale_or_missing_count: \`${compat_count}\`"
    echo
    echo "| runner_id | class | status | freshness | policy_effect |"
    echo "|---|---|---|---|---|"
    jq -r '.matrix_rows[] | "| \(.runner_id) | \(.lane_class) | \(.runner_status) | \(.freshness_state) | \(.policy_effect) |"' "${out_json_file}"
  } > "${out_md_file}"
}
