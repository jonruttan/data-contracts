#!/usr/bin/env bash
set -euo pipefail

manifest="${1:-specs/04_governance/runner_entrypoints_v1.yaml}"
runner_bin="${2:-dc-runner}"

mkdir -p .artifacts
out=".artifacts/runner-entrypoints.json"

"${runner_bin}" entrypoints list --format json > "$out"
expected_ids="$(sed -n 's/^  - id: //p' "$manifest")"
if [ -z "$expected_ids" ]; then
  echo "ERROR: no expected entrypoint IDs found in $manifest"
  exit 1
fi

missing=0
while IFS= read -r id; do
  [ -z "$id" ] && continue
  if ! grep -q "\"id\": \"${id}\"" "$out"; then
    echo "ERROR: installed ${runner_bin} missing required entrypoint id: ${id}"
    missing=1
  fi
done <<EOF_IDS
${expected_ids}
EOF_IDS

if [ "$missing" -ne 0 ]; then
  echo "ERROR: installed ${runner_bin} is not compatible with current specs. Publish/update dc-runner-cli before running this CI."
  exit 1
fi
