#!/usr/bin/env bash

fetch_release_json() {
  local release_api_url="$1"
  local release_json=""
  set +e
  release_json="$(curl --fail --location --silent --show-error "${release_api_url}")"
  local curl_code=$?
  set -e
  if [[ "${curl_code}" -ne 0 || -z "${release_json}" ]]; then
    return 1
  fi
  printf '%s\n' "${release_json}"
}

download_report_asset() {
  local source_url="$1"
  local out_file="$2"
  set +e
  curl --fail --location --silent --show-error "${source_url}" --output "${out_file}"
  local code=$?
  set -e
  return "${code}"
}

extract_release_asset_metadata() {
  local release_json="$1"
  local report_asset_name="$2"
  local release_version source_url sha256_reported

  release_version="$(jq -r '.tag_name // empty' <<<"${release_json}")"
  source_url="$(jq -r --arg name "${report_asset_name}" '.assets[]? | select(.name == $name) | .browser_download_url' <<<"${release_json}" | head -n1)"
  sha256_reported="$(jq -r --arg name "${report_asset_name}" '.assets[]? | select(.name == $name) | (.digest // "")' <<<"${release_json}" | head -n1)"
  sha256_reported="${sha256_reported#sha256:}"

  jq -cn \
    --arg release_version "${release_version}" \
    --arg source_url "${source_url}" \
    --arg sha256_reported "${sha256_reported}" \
    '{release_version:$release_version, source_url:$source_url, sha256_reported:$sha256_reported}'
}
