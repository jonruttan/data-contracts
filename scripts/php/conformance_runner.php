#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP conformance runner bootstrap.
 *
 * This script is intentionally minimal and deterministic:
 * - Reads conformance case fixtures from a directory.
 * - Executes a small text.file subset using real YAML parsing.
 * - Supports assertion tree subset: list + must groups + contain/regex leaves.
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

class SchemaError extends RuntimeException {}
class AssertionFailure extends RuntimeException {}

function isListArray(mixed $value): bool {
    if (!is_array($value)) {
        return false;
    }
    if ($value === []) {
        return true;
    }
    return array_keys($value) === range(0, count($value) - 1);
}

function parseYamlCases(string $path): array {
    if (!function_exists('yaml_parse')) {
        throw new RuntimeException('yaml_parse extension is required for PHP conformance runner');
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $payload = @yaml_parse($raw);
    if (!is_array($payload)) {
        throw new RuntimeException("invalid YAML payload in fixture file: {$path}");
    }
    $cases = $payload['cases'] ?? null;
    if (!is_array($cases) || !isListArray($cases)) {
        throw new RuntimeException("fixture cases must be a list: {$path}");
    }
    return $cases;
}

function evalTextLeaf(array $leaf, string $subject, string $target, string $caseId, string $path): void {
    foreach ($leaf as $op => $raw) {
        if ($op === 'target') {
            continue;
        }
        if ($op !== 'contain' && $op !== 'regex') {
            throw new SchemaError("unsupported op: {$op}");
        }
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        foreach ($raw as $value) {
            $v = (string)$value;
            if ($op === 'contain') {
                if (strpos($subject, $v) === false) {
                    throw new AssertionFailure("[case_id={$caseId} assert_path={$path} target={$target} op=contain] contain assertion failed");
                }
            } else {
                $ok = @preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject);
                if ($ok !== 1) {
                    throw new AssertionFailure("[case_id={$caseId} assert_path={$path} target={$target} op=regex] regex assertion failed");
                }
            }
        }
    }
}

function evalTextAssertNode(mixed $node, string $subject, ?string $inheritedTarget, string $caseId, string $path): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalTextAssertNode($child, $subject, $inheritedTarget, $caseId, "{$path}[{$i}]");
        }
        return;
    }
    if (!is_array($node)) {
        throw new SchemaError('assert node must be a mapping or list');
    }
    $target = $inheritedTarget;
    if (array_key_exists('target', $node)) {
        $target = trim((string)$node['target']);
    }
    if (array_key_exists('must', $node)) {
        $children = $node['must'];
        if (!is_array($children) || !isListArray($children) || count($children) === 0) {
            throw new SchemaError('assert.must must be a non-empty list');
        }
        foreach ($children as $i => $child) {
            evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.must[{$i}]");
        }
        return;
    }
    if ($target !== 'text') {
        throw new SchemaError('unknown assert target for text.file');
    }
    evalTextLeaf($node, $subject, $target, $caseId, $path);
}

function evaluateTextFileCase(array $case, string $subject): array {
    $mode = isset($case['assert_health']['mode']) ? (string)$case['assert_health']['mode'] : null;
    if ($mode !== null && !in_array(strtolower($mode), ['ignore', 'warn', 'error'], true)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'invalid assert_health.mode'];
    }

    try {
        $assertSpec = $case['assert'] ?? [];
        evalTextAssertNode($assertSpec, $subject, null, (string)$case['id'], 'assert');
    } catch (SchemaError $e) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    } catch (AssertionFailure $e) {
        return ['status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
    } catch (Throwable $e) {
        return ['status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
    }
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function evaluateCase(string $fixturePath, mixed $case): array {
    if (!is_array($case)) {
        return [
            'id' => 'UNKNOWN',
            'status' => 'fail',
            'category' => 'schema',
            'message' => 'case must be a mapping',
        ];
    }
    $id = isset($case['id']) ? (string)$case['id'] : '';
    $type = isset($case['type']) ? (string)$case['type'] : '';
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
        foreach (parseYamlCases($path) as $case) {
            $results[] = evaluateCase($path, $case);
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
