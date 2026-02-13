#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP spec runner.
 *
 * Executes Markdown-embedded `yaml spec-test` cases and emits a normalized
 * JSON report.
 *
 * Usage:
 *   php scripts/php/spec_runner.php --cases <dir-or-file> --out <file>
 */

function usage(): void {
    fwrite(STDOUT, "usage: spec_runner.php --cases <dir-or-file> --out <file> [--case-file-pattern <glob>]\n");
}

const DEFAULT_CASE_FILE_PATTERN = '*.spec.md';

function parseArgs(array $argv): array {
    $out = null;
    $cases = null;
    $casePattern = DEFAULT_CASE_FILE_PATTERN;
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
        if ($arg === '--case-file-pattern') {
            if ($i + 1 >= count($argv)) {
                fwrite(STDERR, "error: --case-file-pattern requires a non-empty value\n");
                usage();
                exit(2);
            }
            $casePattern = trim((string)$argv[++$i]);
            if ($casePattern === '') {
                fwrite(STDERR, "error: --case-file-pattern requires a non-empty value\n");
                usage();
                exit(2);
            }
            continue;
        }
    }
    if ($out === null || $cases === null) {
        usage();
        exit(2);
    }
    return ['out' => $out, 'cases' => $cases, 'case_pattern' => $casePattern];
}

function matchesCasePattern(string $name, string $pattern): bool {
    $regex = '/^' . str_replace(
        ['\*', '\?'],
        ['.*', '.'],
        preg_quote($pattern, '/')
    ) . '$/i';
    return preg_match($regex, $name) === 1;
}

function listCaseFiles(string $path, string $pattern): array {
    if (is_file($path)) {
        if (matchesCasePattern(basename($path), $pattern)) {
            return [$path];
        }
        throw new RuntimeException("cases path is a file but does not match case pattern ({$pattern}): {$path}");
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
        if (matchesCasePattern($item, $pattern)) {
            $files[] = $itemPath;
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

class SchemaError extends RuntimeException {}
class AssertionFailure extends RuntimeException {}

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
        throw new RuntimeException('yaml_parse extension is required for PHP spec runner');
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
                if (!array_key_exists('id', $test) || !array_key_exists('type', $test)) {
                    throw new RuntimeException("spec-test in {$path} must include 'id' and 'type'");
                }
                $cases[] = $test;
            }
        } elseif (is_array($payload)) {
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

function isAbsolutePath(string $path): bool {
    if ($path === '') {
        return false;
    }
    if ($path[0] === '/' || $path[0] === '\\') {
        return true;
    }
    return preg_match('/^[A-Za-z]:[\/\\\\]/', $path) === 1;
}

function normalizePath(string $path): string {
    $path = str_replace('\\', '/', $path);
    $isAbs = strlen($path) > 0 && $path[0] === '/';
    $parts = preg_split('~/+~', $path) ?: [];
    $stack = [];
    foreach ($parts as $part) {
        if ($part === '' || $part === '.') {
            continue;
        }
        if ($part === '..') {
            if (count($stack) > 0) {
                array_pop($stack);
            }
            continue;
        }
        $stack[] = $part;
    }
    $joined = implode('/', $stack);
    if ($isAbs) {
        return '/' . $joined;
    }
    return $joined;
}

function contractRootFor(string $docPath): string {
    $docAbs = normalizePath((string)realpath($docPath));
    $cur = dirname($docAbs);
    while (true) {
        if (is_dir($cur . '/.git')) {
            return $cur;
        }
        $parent = dirname($cur);
        if ($parent === $cur) {
            break;
        }
        $cur = $parent;
    }
    return dirname($docAbs);
}

function pathWithinRoot(string $targetPath, string $rootPath): bool {
    $target = rtrim(normalizePath($targetPath), '/');
    $root = rtrim(normalizePath($rootPath), '/');
    if ($target === $root) {
        return true;
    }
    return str_starts_with($target . '/', $root . '/');
}

function resolveTextFilePath(string $fixturePath, array $case): string {
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    if (!array_key_exists('path', $case)) {
        return $docAbs;
    }
    $rel = (string)$case['path'];
    if (isAbsolutePath($rel)) {
        throw new SchemaError('text.file path must be relative');
    }
    $candidate = normalizePath(dirname($docAbs) . '/' . $rel);
    $root = contractRootFor($docAbs);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError('text.file path escapes contract root');
    }
    return $candidate;
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

function resolveAssertHealthMode(array $case): string {
    $mode = strtolower(trim((string)(getenv('SPEC_RUNNER_ASSERT_HEALTH') ?: 'ignore')));
    if ($mode === '') {
        $mode = 'ignore';
    }
    if (isset($case['assert_health'])) {
        if (!is_array($case['assert_health'])) {
            throw new SchemaError('assert_health must be a mapping when provided');
        }
        if (array_key_exists('mode', $case['assert_health'])) {
            $mode = strtolower(trim((string)$case['assert_health']['mode']));
        }
    }
    if (!in_array($mode, ['ignore', 'warn', 'error'], true)) {
        throw new SchemaError('assert_health.mode must be one of: ignore, warn, error');
    }
    return $mode;
}

function evalAssertNode(
    mixed $node,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    callable $evalLeaf
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalAssertNode($child, $inheritedTarget, $caseId, "{$path}[{$i}]", $evalLeaf);
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
                evalAssertNode($child, $target, $caseId, "{$path}.must[{$i}]", $evalLeaf);
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalAssertNode($child, $target, $caseId, "{$path}.can[{$i}]", $evalLeaf);
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Try next branch.
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
                    evalAssertNode($child, $target, $caseId, "{$path}.cannot[{$i}]", $evalLeaf);
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
    $evalLeaf($node, $target, $caseId, $path);
}

function evalTextLeaf(array $leaf, string $subject, string $target, string $caseId, string $path): void {
    if ($target !== 'text') {
        throw new SchemaError('unknown assert target for text.file');
    }
    foreach ($leaf as $op => $raw) {
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
                    throw new AssertionFailure(
                        "[case_id={$caseId} assert_path={$path} target={$target} op=contain] contain assertion failed"
                    );
                }
            } else {
                $ok = @preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject);
                if ($ok !== 1) {
                    throw new AssertionFailure(
                        "[case_id={$caseId} assert_path={$path} target={$target} op=regex] regex assertion failed"
                    );
                }
            }
        }
    }
}

function firstNonEmptyLine(string $text): ?string {
    $lines = preg_split('/\R/', $text) ?: [];
    foreach ($lines as $line) {
        $trim = trim((string)$line);
        if ($trim !== '') {
            return $trim;
        }
    }
    return null;
}

function evalCliLeaf(array $leaf, array $captured, string $target, string $caseId, string $path): void {
    foreach ($leaf as $op => $raw) {
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        if ($target === 'stdout' || $target === 'stderr') {
            $subject = $target === 'stdout' ? (string)$captured['stdout'] : (string)$captured['stderr'];
            if ($op !== 'contain' && $op !== 'regex' && $op !== 'json_type') {
                throw new SchemaError("unsupported op: {$op}");
            }
            foreach ($raw as $value) {
                if ($op === 'contain') {
                    $v = (string)$value;
                    if (strpos($subject, $v) === false) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=contain] contain assertion failed"
                        );
                    }
                    continue;
                }
                if ($op === 'regex') {
                    $v = (string)$value;
                    $ok = @preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject);
                    if ($ok !== 1) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=regex] regex assertion failed"
                        );
                    }
                    continue;
                }
                $want = strtolower(trim((string)$value));
                $parsed = json_decode($subject, true);
                if ($want === 'list') {
                    if (!is_array($parsed) || !isListArray($parsed)) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=json_type] json_type(list) failed"
                        );
                    }
                } elseif ($want === 'dict') {
                    if (!is_array($parsed) || isListArray($parsed)) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=json_type] json_type(dict) failed"
                        );
                    }
                } else {
                    throw new SchemaError("unsupported json_type: {$value}");
                }
            }
            continue;
        }
        if ($target === 'stdout_path') {
            if ($op !== 'exists') {
                throw new SchemaError("unsupported op for stdout_path: {$op}");
            }
            $line = firstNonEmptyLine((string)$captured['stdout']);
            if ($line === null) {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op=exists] expected stdout to contain a path"
                );
            }
            foreach ($raw as $value) {
                if ($value !== true && $value !== null) {
                    throw new SchemaError('stdout_path.exists only supports value: true (or null)');
                }
                if (!file_exists($line)) {
                    throw new AssertionFailure(
                        "[case_id={$caseId} assert_path={$path} target={$target} op=exists] path does not exist"
                    );
                }
            }
            continue;
        }
        if ($target === 'stdout_path_text') {
            $line = firstNonEmptyLine((string)$captured['stdout']);
            if ($line === null) {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] expected stdout to contain a path"
                );
            }
            $subject = file_get_contents($line);
            if ($subject === false) {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] cannot read stdout path"
                );
            }
            if ($op !== 'contain' && $op !== 'regex') {
                throw new SchemaError("unsupported op: {$op}");
            }
            foreach ($raw as $value) {
                $v = (string)$value;
                if ($op === 'contain') {
                    if (strpos($subject, $v) === false) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=contain] contain assertion failed"
                        );
                    }
                } else {
                    $ok = @preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject);
                    if ($ok !== 1) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=regex] regex assertion failed"
                        );
                    }
                }
            }
            continue;
        }
        throw new SchemaError("unknown assert target: {$target}");
    }
}

function evaluateTextFileCase(string $fixturePath, array $case): array {
    $mode = resolveAssertHealthMode($case);
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $mode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $mode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
    }

    $subjectPath = resolveTextFilePath($fixturePath, $case);
    $subject = file_get_contents($subjectPath);
    if ($subject === false) {
        throw new RuntimeException("cannot read fixture file: {$subjectPath}");
    }
    $assertSpec = $case['assert'] ?? [];
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalTextLeaf(
            $leaf,
            $subject,
            $target,
            $caseId,
            $path
        )
    );
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function parseEntrypointCommand(string $entrypoint): array {
    $parts = str_getcsv($entrypoint, ' ', '"', '\\');
    $cmd = [];
    foreach ($parts as $part) {
        $p = trim((string)$part);
        if ($p !== '') {
            $cmd[] = $p;
        }
    }
    if (count($cmd) === 0) {
        throw new SchemaError('cli.run requires non-empty harness.entrypoint');
    }
    return $cmd;
}

function applyEnvAllowlist(array $env): array {
    $raw = getenv('SPEC_RUNNER_ENV_ALLOWLIST');
    if ($raw === false) {
        return $env;
    }
    $raw = trim((string)$raw);
    if ($raw === '') {
        return $env;
    }
    $allowed = array_filter(
        array_map('trim', explode(',', $raw)),
        static fn(string $name): bool => $name !== ''
    );
    if (count($allowed) === 0) {
        return [];
    }
    $filtered = [];
    foreach ($allowed as $name) {
        if (array_key_exists($name, $env)) {
            $filtered[$name] = (string)$env[$name];
        }
    }
    return $filtered;
}

function evaluateCliRunCase(array $case): array {
    $mode = resolveAssertHealthMode($case);
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $mode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $mode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
    }

    $h = $case['harness'] ?? [];
    if (!is_array($h)) {
        throw new SchemaError('harness must be a mapping');
    }
    $supportedHarnessKeys = ['entrypoint', 'env'];
    foreach (array_keys($h) as $k) {
        if (!in_array((string)$k, $supportedHarnessKeys, true)) {
            throw new SchemaError("unsupported harness key(s): {$k}");
        }
    }

    $entrypoint = trim((string)($h['entrypoint'] ?? getenv('SPEC_RUNNER_ENTRYPOINT') ?: ''));
    if ($entrypoint === '') {
        throw new RuntimeException('cli.run requires harness.entrypoint or SPEC_RUNNER_ENTRYPOINT');
    }
    $command = parseEntrypointCommand($entrypoint);

    $argv = $case['argv'] ?? [];
    if (is_string($argv)) {
        $argv = [$argv];
    }
    if (!is_array($argv) || !isListArray($argv)) {
        throw new SchemaError('argv must be a list or string');
    }
    foreach ($argv as $arg) {
        $command[] = (string)$arg;
    }

    $env = getenv();
    if (!is_array($env)) {
        $env = [];
    }
    $env = applyEnvAllowlist($env);
    if (array_key_exists('env', $h)) {
        if (!is_array($h['env'])) {
            throw new SchemaError('harness.env must be a mapping');
        }
        foreach ($h['env'] as $k => $v) {
            $name = (string)$k;
            if ($v === null) {
                unset($env[$name]);
            } else {
                $env[$name] = (string)$v;
            }
        }
    }

    $descriptors = [
        0 => ['pipe', 'r'],
        1 => ['pipe', 'w'],
        2 => ['pipe', 'w'],
    ];
    $proc = proc_open($command, $descriptors, $pipes, null, $env);
    if (!is_resource($proc)) {
        throw new RuntimeException('failed to launch cli.run entrypoint');
    }

    fwrite($pipes[0], '');
    fclose($pipes[0]);
    $stdout = stream_get_contents($pipes[1]);
    fclose($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[2]);
    $exitCode = proc_close($proc);

    $got = (int)$exitCode;
    $want = isset($case['exit_code']) ? (int)$case['exit_code'] : 0;
    if ($got !== $want) {
        throw new AssertionFailure("[case_id={$case['id']}] exit_code expected={$want} actual={$got}");
    }

    $captured = ['stdout' => (string)$stdout, 'stderr' => (string)$stderr];
    $assertSpec = $case['assert'] ?? [];
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalCliLeaf(
            $leaf,
            $captured,
            $target,
            $caseId,
            $path
        )
    );

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

    try {
        if ($type === 'text.file') {
            $res = evaluateTextFileCase($fixturePath, $case);
        } elseif ($type === 'cli.run') {
            $res = evaluateCliRunCase($case);
        } else {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'runtime',
                'message' => "unknown spec-test type: {$type}",
            ];
        }
    } catch (SchemaError $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    } catch (AssertionFailure $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
    } catch (Throwable $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
    }

    return ['id' => $id, 'status' => $res['status'], 'category' => $res['category'], 'message' => $res['message']];
}

function main(array $argv): int {
    $args = parseArgs($argv);
    $caseFiles = listCaseFiles($args['cases'], (string)$args['case_pattern']);

    $results = [];
    foreach ($caseFiles as $path) {
        foreach (parseCases($path) as $case) {
            $results[] = evaluateCase($path, $case);
        }
    }

    $report = ['version' => 1, 'results' => $results];
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

    foreach ($results as $r) {
        if (($r['status'] ?? '') === 'fail') {
            return 1;
        }
    }
    return 0;
}

try {
    exit(main($argv));
} catch (Throwable $e) {
    fwrite(STDERR, "ERROR: " . $e->getMessage() . "\n");
    exit(1);
}
