#!/usr/bin/env bash

require_tool() {
  local tool="$1"
  if ! command -v "${tool}" >/dev/null 2>&1; then
    echo "ERROR: required tool not found: ${tool}" >&2
    exit 2
  fi
}

iso_to_epoch() {
  local iso="$1"
  jq -nr --arg iso "${iso}" '$iso | fromdateiso8601' 2>/dev/null || return 1
}

validate_report_shape() {
  local report_json="$1"
  jq -e '
    .version == 1 and
    (.runner_id | type == "string" and length > 0) and
    (.implementation_repo | type == "string" and length > 0) and
    (.release_version | type == "string" and length > 0) and
    (.commit_sha | type == "string" and length > 0) and
    (.generated_at | type == "string" and length > 0) and
    (.lane_class == "required" or .lane_class == "compatibility_non_blocking") and
    (.overall_status == "pass" or .overall_status == "fail" or .overall_status == "degraded" or .overall_status == "unknown") and
    (.fresh_until | type == "string" and length > 0) and
    (.command_results | type == "array") and
    (.artifact_refs | type == "array")
  ' >/dev/null <<<"${report_json}" 2>/dev/null
}

read_report_json() {
  local report_path="$1"
  jq -c . "${report_path}" 2>/dev/null || return 1
}
