#!/usr/bin/env bash

parse_yaml_file_to_json() {
  local yaml_file="$1"
  php -r '
$data = yaml_parse_file($argv[1]);
if ($data === false) {
  fwrite(STDERR, "ERROR: failed parsing YAML file\n");
  exit(2);
}
echo json_encode($data, JSON_UNESCAPED_SLASHES);
' "${yaml_file}"
}
