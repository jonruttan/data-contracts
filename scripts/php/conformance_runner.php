#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP conformance runner bootstrap.
 *
 * This script is intentionally minimal and deterministic:
 * - Reads conformance case fixtures from a directory.
 * - Emits JSON report envelope matching report-format.md.
 * - Currently marks cases as runtime-fail placeholders until full
 *   parser/assertion/harness parity is implemented in PHP.
 *
 * Usage:
 *   php scripts/php/conformance_runner.php \
 *     --cases fixtures/conformance/cases \
 *     --out .artifacts/php-conformance-report.json
 */

function usage(): void {
    fwrite(STDOUT, "usage: conformance_runner.php --cases <dir> --out <file>\n");
}

function parseArgs(array $argv): array {
    $out = null;
    $cases = null;
    for ($i = 1; $i < count($argv); $i++) {
        $arg = $argv[$i];
        if ($arg === '--help' || $arg === '-h') {
            usage();
            exit(0);
        }
        if ($arg === '--out' && $i + 1 < count($argv)) {
            $out = $argv[++$i];
            continue;
        }
        if ($arg === '--cases' && $i + 1 < count($argv)) {
            $cases = $argv[++$i];
            continue;
        }
    }
    if ($out === null || $cases === null) {
        usage();
        exit(2);
    }
    return ['out' => $out, 'cases' => $cases];
}

function listYamlFiles(string $dir): array {
    $files = [];
    $items = scandir($dir);
    if ($items === false) {
        throw new RuntimeException("cannot read cases dir: {$dir}");
    }
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }
        $path = rtrim($dir, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . $item;
        if (!is_file($path)) {
            continue;
        }
        if (preg_match('/\.ya?ml$/i', $item)) {
            $files[] = $path;
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

function extractCaseIdsFromYaml(string $path): array {
    // Lightweight line-based extractor for "- id: <value>" within fixture files.
    // This keeps bootstrap dependencies minimal (no YAML extension required).
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $ids = [];
    $lines = preg_split("/\r\n|\n|\r/", $raw);
    foreach ($lines as $line) {
        if (preg_match('/^\s*-\s*id:\s*(.+)\s*$/', $line, $m) === 1) {
            $ids[] = trim($m[1], " \"'");
        }
    }
    return $ids;
}

function main(array $argv): int {
    $args = parseArgs($argv);
    $caseFiles = listYamlFiles($args['cases']);

    $results = [];
    foreach ($caseFiles as $path) {
        foreach (extractCaseIdsFromYaml($path) as $id) {
            $results[] = [
                'id' => $id,
                'status' => 'fail',
                'category' => 'runtime',
                'message' => 'PHP conformance runner bootstrap placeholder',
            ];
        }
    }

    $report = [
        'version' => 1,
        'results' => $results,
    ];
    $json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    if ($json === false) {
        throw new RuntimeException('failed to encode JSON report');
    }

    $outPath = $args['out'];
    $parent = dirname($outPath);
    if (!is_dir($parent)) {
        if (!mkdir($parent, 0777, true) && !is_dir($parent)) {
            throw new RuntimeException("cannot create output dir: {$parent}");
        }
    }
    if (file_put_contents($outPath, $json . "\n") === false) {
        throw new RuntimeException("cannot write report: {$outPath}");
    }
    fwrite(STDOUT, "wrote {$outPath}\n");
    return 0;
}

try {
    exit(main($argv));
} catch (Throwable $e) {
    fwrite(STDERR, "ERROR: " . $e->getMessage() . "\n");
    exit(1);
}
