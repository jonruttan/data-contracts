#!/usr/bin/env bash

ingest_usage() {
  cat <<'USAGE'
Usage: ./scripts/runner_status_ingest.sh [options]

Options:
  --registry <path>        Runner certification registry path (default: /specs/schema/runner_certification_registry_v1.yaml)
  --out-json <path>        Matrix JSON output path (default: /.artifacts/runner-status-matrix.json)
  --out-md <path>          Matrix Markdown output path (default: /.artifacts/runner-status-matrix.md)
  --log-json <path>        Ingest log output path (default: /.artifacts/runner-status-ingest-log.json)
  --max-age-hours <int>    Freshness SLO in hours (default: 72)
  --enforce-freshness      accepted for compatibility; policy decided by governance checks
  --now-utc <rfc3339>      Override current UTC time (test support)
USAGE
}

parse_ingest_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --registry)
        REGISTRY_PATH="$2"
        shift 2
        ;;
      --out-json)
        OUT_JSON="$2"
        shift 2
        ;;
      --out-md)
        OUT_MD="$2"
        shift 2
        ;;
      --log-json)
        OUT_LOG_JSON="$2"
        shift 2
        ;;
      --max-age-hours)
        MAX_AGE_HOURS="$2"
        shift 2
        ;;
      --enforce-freshness)
        ENFORCE_FRESHNESS=1
        shift
        ;;
      --now-utc)
        NOW_UTC="$2"
        shift 2
        ;;
      -h|--help)
        ingest_usage
        exit 0
        ;;
      *)
        echo "ERROR: unknown argument: $1" >&2
        ingest_usage >&2
        exit 2
        ;;
    esac
  done
}
