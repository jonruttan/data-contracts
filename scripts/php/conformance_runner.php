#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP conformance runner bootstrap.
 *
 * This script is intentionally minimal and deterministic:
 * - Reads conformance case fixtures from a directory.
 * - Executes a small text.file subset using real YAML parsing.
 * - Supports assertion tree subset: list + must/can/cannot groups + contain/regex leaves.
 * - Emits JSON report envelope matching report-format.md.
 * - Marks unsupported case types as runtime failures.
 *
 * Usage:
 *   php scripts/php/conformance_runner.php \
 *     --cases docs/spec/conformance/cases \
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

function listCaseFiles(string $path): array {
    if (is_file($path)) {
        if (preg_match('/\.spec\.md$/i', $path) === 1) {
            return [$path];
        }
        throw new RuntimeException("cases path is a file but not supported (*.spec.md): {$path}");
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
        if (preg_match('/\.spec\.md$/i', $item)) {
            $files[] = $itemPath;
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

class SchemaError extends RuntimeException {}
class AssertionFailure extends RuntimeException {}
const PHP_CAPABILITIES = [
    'assert.op.contain',
    'assert.op.regex',
    'assert.group.must',
    'assert.group.can',
    'assert.group.cannot',
    'assert_health.ah001',
    'assert_health.ah002',
    'assert_health.ah003',
    'assert_health.ah004',
    'assert_health.ah005',
    'requires.capabilities',
];
const ALWAYS_TRUE_REGEX = ['.*', '^.*$', '\\A.*\\Z'];

function isListArray(mixed $value): bool {
    if (!is_array($value)) {
        return false;
    }
    if ($value === []) {
        return true;
    }
    return array_keys($value) === range(0, count($value) - 1);
}

function isSpecTestOpeningFence(string $line): ?array {
    $trimmed = ltrim($line, " \t");
    if ($trimmed === '') {
        return null;
    }
    $first = $trimmed[0];
    if ($first !== '`' && $first !== '~') {
        return null;
    }
    $i = 0;
    $n = strlen($trimmed);
    while ($i < $n && $trimmed[$i] === $first) {
        $i++;
    }
    if ($i < 3) {
        return null;
    }
    $info = trim(substr($trimmed, $i));
    if ($info === '') {
        return null;
    }
    $tokens = preg_split('/\s+/', strtolower($info)) ?: [];
    $set = array_fill_keys($tokens, true);
    if (!isset($set['spec-test']) || (!isset($set['yaml']) && !isset($set['yml']))) {
        return null;
    }
    return [$first, $i];
}

function isClosingFence(string $line, string $char, int $minLen): bool {
    $trimmed = rtrim(ltrim($line, " \t"));
    if ($trimmed === '' || $trimmed[0] !== $char) {
        return false;
    }
    $i = 0;
    $n = strlen($trimmed);
    while ($i < $n && $trimmed[$i] === $char) {
        $i++;
    }
    return $i >= $minLen && $i === $n;
}

function parseMarkdownCases(string $path): array {
    if (!function_exists('yaml_parse')) {
        throw new RuntimeException('yaml_parse extension is required for PHP conformance runner');
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $lines = preg_split('/\R/', $raw) ?: [];
    $i = 0;
    $cases = [];
    while ($i < count($lines)) {
        $open = isSpecTestOpeningFence($lines[$i]);
        if ($open === null) {
            $i++;
            continue;
        }
        [$fenceChar, $fenceLen] = $open;
        $i++;
        $blockLines = [];
        while ($i < count($lines) && !isClosingFence($lines[$i], $fenceChar, $fenceLen)) {
            $blockLines[] = $lines[$i];
            $i++;
        }
        if ($i >= count($lines)) {
            break;
        }
        $payload = @yaml_parse(implode("\n", $blockLines));
        if (is_array($payload) && isListArray($payload)) {
            foreach ($payload as $test) {
                if (!is_array($test)) {
                    throw new RuntimeException("spec-test block in {$path} contains a non-mapping test");
                }
                if (!array_key_exists('type', $test) && array_key_exists('kind', $test)) {
                    $test['type'] = $test['kind'];
                    unset($test['kind']);
                }
                if (!array_key_exists('id', $test) || !array_key_exists('type', $test)) {
                    throw new RuntimeException("spec-test in {$path} must include 'id' and 'type'");
                }
                $cases[] = $test;
            }
        } elseif (is_array($payload)) {
            if (!array_key_exists('type', $payload) && array_key_exists('kind', $payload)) {
                $payload['type'] = $payload['kind'];
                unset($payload['kind']);
            }
            if (!array_key_exists('id', $payload) || !array_key_exists('type', $payload)) {
                throw new RuntimeException("spec-test in {$path} must include 'id' and 'type'");
            }
            $cases[] = $payload;
        } else {
            throw new RuntimeException("spec-test block in {$path} must be a mapping or a list of mappings");
        }
        $i++;
    }
    return $cases;
}

function parseCases(string $path): array {
    return parseMarkdownCases($path);
}

function lintAssertionHealth(mixed $node, string $path = 'assert', ?string $groupCtx = null): array {
    $diags = [];
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            $diags = array_merge($diags, lintAssertionHealth($child, "{$path}[{$i}]", $groupCtx));
        }
        return $diags;
    }
    if (!is_array($node)) {
        return $diags;
    }
    foreach (['must', 'can', 'cannot'] as $group) {
        if (array_key_exists($group, $node)) {
            $children = $node[$group];
            if (is_array($children) && isListArray($children)) {
                $seen = [];
                foreach ($children as $child) {
                    $key = @json_encode($child, JSON_UNESCAPED_SLASHES);
                    if (!is_string($key) || $key === '') {
                        $key = serialize($child);
                    }
                    if (array_key_exists($key, $seen)) {
                        $diags[] = [
                            'code' => 'AH004',
                            'path' => "{$path}.{$group}",
                            'message' => "redundant sibling assertion branch in '{$group}'",
                        ];
                        break;
                    }
                    $seen[$key] = true;
                }
            }
            return array_merge($diags, lintAssertionHealth($children, "{$path}.{$group}", $group));
        }
    }
    foreach (['contain', 'regex'] as $op) {
        if (!array_key_exists($op, $node)) {
            continue;
        }
        $raw = $node[$op];
        if (!is_array($raw) || !isListArray($raw)) {
            continue;
        }
        $vals = array_map(static fn($x) => (string)$x, $raw);
        if (count($vals) !== count(array_unique($vals))) {
            $diags[] = [
                'code' => 'AH003',
                'path' => "{$path}.{$op}",
                'message' => "duplicate values in '{$op}' list can hide intent drift",
            ];
        }
        if ($op === 'contain' && in_array('', $vals, true)) {
            $msg = 'contain with empty string is always true';
            if ($groupCtx === 'cannot') {
                $msg = "cannot(contain:'') is always false";
            }
            $diags[] = ['code' => 'AH001', 'path' => "{$path}.contain", 'message' => $msg];
        }
        if ($op !== 'regex') {
            continue;
        }
        foreach ($vals as $v) {
            if (in_array($v, ALWAYS_TRUE_REGEX, true)) {
                $msg = 'regex pattern is trivially always true';
                if ($groupCtx === 'cannot') {
                    $msg = 'cannot(regex always-true) is always false';
                }
                $diags[] = ['code' => 'AH002', 'path' => "{$path}.regex", 'message' => $msg];
            }
            if (
                str_contains($v, '(?<=') ||
                str_contains($v, '(?<!') ||
                str_contains($v, '(?P<') ||
                preg_match('/\(\?<([A-Za-z_][A-Za-z0-9_]*)>/', $v) === 1 ||
                str_contains($v, '\\k<') ||
                str_contains($v, '(?(') ||
                str_contains($v, '(?>') ||
                preg_match('/\(\?[aiLmsux-]+(?::|\))/', $v) === 1 ||
                preg_match('/(?<!\\\\)(?:\\\\\\\\)*[+*?]\+/', $v) === 1
            ) {
                $diags[] = [
                    'code' => 'AH005',
                    'path' => "{$path}.regex",
                    'message' => 'regex uses non-portable construct',
                ];
                break;
            }
        }
    }
    return $diags;
}

function formatAssertionHealthWarning(array $d): string {
    return "WARN: ASSERT_HEALTH {$d['code']} at {$d['path']}: {$d['message']}";
}

function formatAssertionHealthError(array $diags): string {
    $parts = [];
    foreach ($diags as $d) {
        $parts[] = "{$d['code']}@{$d['path']}";
    }
    return "assertion health check failed (" . count($diags) . " issue(s)): " . implode('; ', $parts);
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

    if (array_key_exists('all', $node) || array_key_exists('any', $node)) {
        throw new SchemaError("assert group aliases 'all'/'any' are not supported; use 'must'/'can'");
    }

    $presentGroups = [];
    foreach (['must', 'can', 'cannot'] as $g) {
        if (array_key_exists($g, $node)) {
            $presentGroups[] = $g;
        }
    }

    if (count($presentGroups) > 1) {
        throw new SchemaError('assert group must include exactly one key (must/can/cannot)');
    }

    if (count($presentGroups) === 1) {
        $group = $presentGroups[0];
        $children = $node[$group];
        if (!is_array($children) || !isListArray($children) || count($children) === 0) {
            throw new SchemaError("assert.{$group} must be a non-empty list");
        }
        $extra = array_diff(array_keys($node), [$group, 'target']);
        if (count($extra) > 0) {
            throw new SchemaError('unknown key in assert group: ' . (string)array_values($extra)[0]);
        }

        if ($group === 'must') {
            foreach ($children as $i => $child) {
                evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.must[{$i}]");
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.can[{$i}]");
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Continue trying other branches.
                }
            }
            if (!$anyPassed) {
                throw new AssertionFailure("all 'can' branches failed");
            }
            return;
        }
        if ($group === 'cannot') {
            $passed = 0;
            foreach ($children as $i => $child) {
                try {
                    evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.cannot[{$i}]");
                    $passed += 1;
                } catch (AssertionFailure $e) {
                    // Expected failing branch for cannot.
                }
            }
            if ($passed > 0) {
                throw new AssertionFailure("'cannot' failed: {$passed} branch(es) passed");
            }
            return;
        }
    }

    if (array_key_exists('target', $node)) {
        throw new SchemaError('leaf assertion must not include key: target; move target to a parent group');
    }
    if ($target === null || $target === '') {
        throw new SchemaError('assertion leaf requires inherited target from a parent group');
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
    $resolvedMode = strtolower((string)($mode ?? 'ignore'));
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $resolvedMode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $resolvedMode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
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

function evaluateRequires(array $case): ?array {
    if (!array_key_exists('requires', $case)) {
        return null;
    }
    $requires = $case['requires'];
    if (!is_array($requires)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires must be a mapping when provided'];
    }
    $caps = $requires['capabilities'] ?? [];
    if (!is_array($caps) || !isListArray($caps)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires.capabilities must be a list'];
    }
    $needed = [];
    foreach ($caps as $c) {
        $s = trim((string)$c);
        if ($s !== '') {
            $needed[] = $s;
        }
    }
    $whenMissing = strtolower(trim((string)($requires['when_missing'] ?? 'fail')));
    if ($whenMissing === '') {
        $whenMissing = 'fail';
    }
    if ($whenMissing !== 'skip' && $whenMissing !== 'fail') {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires.when_missing must be one of: skip, fail'];
    }
    $capsSet = array_fill_keys(PHP_CAPABILITIES, true);
    $missing = [];
    foreach ($needed as $cap) {
        if (!array_key_exists($cap, $capsSet)) {
            $missing[] = $cap;
        }
    }
    if (count($missing) === 0) {
        return null;
    }
    sort($missing, SORT_STRING);
    if ($whenMissing === 'skip') {
        return ['status' => 'skip', 'category' => null, 'message' => null];
    }
    return [
        'status' => 'fail',
        'category' => 'runtime',
        'message' => "missing required capabilities for implementation 'php': " . implode(', ', $missing),
    ];
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

    $requiresResult = evaluateRequires($case);
    if ($requiresResult !== null) {
        return [
            'id' => $id,
            'status' => $requiresResult['status'],
            'category' => $requiresResult['category'],
            'message' => $requiresResult['message'],
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
    $caseFiles = listCaseFiles($args['cases']);

    $results = [];
    foreach ($caseFiles as $path) {
        foreach (parseCases($path) as $case) {
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
