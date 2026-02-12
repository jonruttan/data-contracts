#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP conformance runner bootstrap.
 *
 * This script is intentionally minimal and deterministic:
 * - Reads conformance case fixtures from a directory.
 * - Executes a small text.file subset (must + contain/regex).
 * - Emits JSON report envelope matching report-format.md.
 * - Marks unsupported case types as runtime failures.
 *
 * Usage:
 *   php scripts/php/conformance_runner.php \
 *     --cases fixtures/conformance/cases \
 *     --out .artifacts/php-conformance-report.json
 */

function usage(): void {
    fwrite(STDOUT, "usage: conformance_runner.php --cases <dir-or-file> --out <file>\n");
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

function listYamlFiles(string $path): array {
    if (is_file($path)) {
        if (preg_match('/\.ya?ml$/i', $path) === 1) {
            return [$path];
        }
        throw new RuntimeException("cases path is a file but not YAML: {$path}");
    }
    $files = [];
    $items = scandir($path);
    if ($items === false) {
        throw new RuntimeException("cannot read cases path: {$path}");
    }
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }
        $itemPath = rtrim($path, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . $item;
        if (!is_file($itemPath)) {
            continue;
        }
        if (preg_match('/\.ya?ml$/i', $item)) {
            $files[] = $itemPath;
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

function splitCaseBlocks(string $raw): array {
    $lines = preg_split("/\r\n|\n|\r/", $raw);
    $blocks = [];
    $current = [];
    foreach ($lines as $line) {
        if (preg_match('/^\s*-\s*id:\s*(.+)\s*$/', $line) === 1) {
            if (!empty($current)) {
                $blocks[] = implode("\n", $current);
                $current = [];
            }
        }
        if (!empty($current) || preg_match('/^\s*-\s*id:\s*(.+)\s*$/', $line) === 1) {
            $current[] = $line;
        }
    }
    if (!empty($current)) {
        $blocks[] = implode("\n", $current);
    }
    return $blocks;
}

function parseInlineList(string $body): array {
    $out = [];
    $s = trim($body);
    if ($s === '') {
        return $out;
    }
    preg_match_all('/"((?:[^"\\\\]|\\\\.)*)"|\'((?:[^\'\\\\]|\\\\.)*)\'|([^,\s][^,]*)/', $s, $m, PREG_SET_ORDER);
    foreach ($m as $g) {
        if ($g[1] !== '') {
            $out[] = stripcslashes($g[1]);
        } elseif ($g[2] !== '') {
            $out[] = stripcslashes($g[2]);
        } else {
            $out[] = trim($g[3]);
        }
    }
    return $out;
}

function parseCaseBlock(string $block): array {
    $id = null;
    $type = null;
    $assertHealthMode = null;
    $contains = [];
    $regexes = [];

    if (preg_match('/^\s*-\s*id:\s*(.+)\s*$/m', $block, $m) === 1) {
        $id = trim($m[1], " \"'");
    }
    if (preg_match('/^\s*type:\s*(.+)\s*$/m', $block, $m) === 1) {
        $type = trim($m[1], " \"'");
    }
    if (preg_match('/^\s*mode:\s*(.+)\s*$/m', $block, $m) === 1) {
        $assertHealthMode = trim($m[1], " \"'");
    }

    preg_match_all('/^\s*-\s*contain:\s*\[(.*)\]\s*$/m', $block, $mContain, PREG_SET_ORDER);
    foreach ($mContain as $row) {
        foreach (parseInlineList($row[1]) as $v) {
            $contains[] = $v;
        }
    }

    preg_match_all('/^\s*-\s*regex:\s*\[(.*)\]\s*$/m', $block, $mRegex, PREG_SET_ORDER);
    foreach ($mRegex as $row) {
        foreach (parseInlineList($row[1]) as $v) {
            $regexes[] = $v;
        }
    }

    return [
        'id' => $id,
        'type' => $type,
        'assert_health_mode' => $assertHealthMode,
        'contain' => $contains,
        'regex' => $regexes,
    ];
}

function evaluateTextFileCase(array $case, string $subject): array {
    $mode = $case['assert_health_mode'];
    if ($mode !== null && !in_array(strtolower($mode), ['ignore', 'warn', 'error'], true)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'invalid assert_health.mode'];
    }

    foreach ($case['contain'] as $value) {
        if (strpos($subject, $value) === false) {
            return ['status' => 'fail', 'category' => 'assertion', 'message' => "contain assertion failed"];
        }
    }
    foreach ($case['regex'] as $pattern) {
        $ok = @preg_match('/' . str_replace('/', '\/', $pattern) . '/u', $subject);
        if ($ok !== 1) {
            return ['status' => 'fail', 'category' => 'assertion', 'message' => "regex assertion failed"];
        }
    }
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function evaluateCase(string $fixturePath, array $case): array {
    $id = (string)($case['id'] ?? '');
    $type = (string)($case['type'] ?? '');
    if ($id === '' || $type === '') {
        return [
            'id' => $id !== '' ? $id : 'UNKNOWN',
            'status' => 'fail',
            'category' => 'schema',
            'message' => 'case missing id or type',
        ];
    }

    if ($type !== 'text.file') {
        return [
            'id' => $id,
            'status' => 'fail',
            'category' => 'runtime',
            'message' => "unsupported type for php bootstrap: {$type}",
        ];
    }

    $subject = file_get_contents($fixturePath);
    if ($subject === false) {
        return [
            'id' => $id,
            'status' => 'fail',
            'category' => 'runtime',
            'message' => "cannot read fixture file: {$fixturePath}",
        ];
    }
    $res = evaluateTextFileCase($case, $subject);
    return [
        'id' => $id,
        'status' => $res['status'],
        'category' => $res['category'],
        'message' => $res['message'],
    ];
}

function main(array $argv): int {
    $args = parseArgs($argv);
    $caseFiles = listYamlFiles($args['cases']);

    $results = [];
    foreach ($caseFiles as $path) {
        $raw = file_get_contents($path);
        if ($raw === false) {
            throw new RuntimeException("cannot read fixture file: {$path}");
        }
        foreach (splitCaseBlocks($raw) as $block) {
            $results[] = evaluateCase($path, parseCaseBlock($block));
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
