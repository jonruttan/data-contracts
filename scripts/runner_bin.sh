#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_FILE="${ROOT_DIR}/specs/01_schema/dc_runner_rust_lock_v1.yaml"
CACHE_ROOT="${ROOT_DIR}/.artifacts/tools/dc-runner-rust"

detect_platform() {
  local os arch
  os="$(uname -s)"
  arch="$(uname -m)"
  case "${os}:${arch}" in
    Darwin:arm64) echo "darwin-arm64" ;;
    Darwin:x86_64) echo "darwin-x86_64" ;;
    Linux:x86_64) echo "linux-x86_64" ;;
    *)
      echo "ERROR: unsupported platform ${os}/${arch} for dc-runner-rust release artifact." >&2
      return 2
      ;;
  esac
}

require_tool() {
  local tool="$1"
  if ! command -v "${tool}" >/dev/null 2>&1; then
    echo "ERROR: required tool not found: ${tool}" >&2
    return 2
  fi
}

read_lock_value() {
  local key="$1"
  awk -v k="${key}" '
    $1 == k ":" {
      val=$2
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", val)
      print val
      exit
    }
  ' "${LOCK_FILE}"
}

read_artifact_value() {
  local platform="$1"
  local key="$2"
  awk -v p="${platform}" -v k="${key}" '
    $0 ~ "^  " p ":" {
      in_platform=1
      next
    }
    in_platform && $0 ~ "^  [A-Za-z0-9._-]+:$" {
      in_platform=0
      next
    }
    in_platform && $0 ~ "^    " k ":" {
      val=$0
      sub("^    " k ":[[:space:]]*", "", val)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", val)
      print val
      exit
    }
  ' "${LOCK_FILE}"
}

resolve_runner_bin() {
  if [[ -n "${DC_RUNNER_RUST_BIN:-}" ]]; then
    if [[ ! -x "${DC_RUNNER_RUST_BIN}" ]]; then
      echo "ERROR: DC_RUNNER_RUST_BIN is set but not executable: ${DC_RUNNER_RUST_BIN}" >&2
      return 2
    fi
    echo "${DC_RUNNER_RUST_BIN}"
    return 0
  fi

  require_tool curl
  require_tool shasum

  if [[ ! -f "${LOCK_FILE}" ]]; then
    echo "ERROR: missing runner lock file: ${LOCK_FILE}" >&2
    return 2
  fi

  local platform version url sha expected bin_dir bin_path tmp_path
  platform="$(detect_platform)"
  version="$(read_lock_value "release_version")"
  url="$(read_artifact_value "${platform}" "url")"
  sha="$(read_artifact_value "${platform}" "sha256")"

  if [[ -z "${version}" || -z "${url}" || -z "${sha}" ]]; then
    echo "ERROR: lock file is incomplete for platform '${platform}' in ${LOCK_FILE}" >&2
    return 2
  fi
  if [[ "${sha}" == REPLACE_WITH_REAL_SHA256* ]]; then
    echo "ERROR: lock file contains placeholder checksum for '${platform}'. Set real SHA256 before use." >&2
    return 2
  fi

  bin_dir="${CACHE_ROOT}/${version}/${platform}"
  bin_path="${bin_dir}/dc-runner-rust"
  mkdir -p "${bin_dir}"

  if [[ ! -x "${bin_path}" ]]; then
    tmp_path="${bin_path}.download"
    rm -f "${tmp_path}"
    curl --fail --location --silent --show-error "${url}" --output "${tmp_path}"
    expected="$(shasum -a 256 "${tmp_path}" | awk '{print $1}')"
    if [[ "${expected}" != "${sha}" ]]; then
      rm -f "${tmp_path}"
      echo "ERROR: checksum mismatch for ${url}. Expected ${sha}, got ${expected}" >&2
      return 2
    fi
    mv "${tmp_path}" "${bin_path}"
    chmod +x "${bin_path}"
  fi

  echo "${bin_path}"
}

main() {
  local bin
  bin="$(resolve_runner_bin)"
  exec "${bin}" "$@"
}

main "$@"
