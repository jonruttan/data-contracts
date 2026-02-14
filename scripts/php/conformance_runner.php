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
    fwrite(STDOUT, "usage: conformance_runner.php --cases <dir-or-file> --out <file> [--case-file-pattern <glob>]\n");
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
const PHP_CAPABILITIES = [
    'api.http',
    'assert.op.contain',
    'assert.op.regex',
    'assert.op.expr',
    'expr.spec_lang.v1',
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

final class SpecLangEnv {
    public array $vars;
    public ?SpecLangEnv $parent;

    public function __construct(array $vars, ?SpecLangEnv $parent) {
        $this->vars = $vars;
        $this->parent = $parent;
    }
}

function specLangDefaultLimits(): array {
    return [
        'max_steps' => 20000,
        'max_nodes' => 20000,
        'max_literal_bytes' => 262144,
        'timeout_ms' => 200,
    ];
}

function specLangLimitsFromCase(array $case): array {
    $defaults = specLangDefaultLimits();
    $harness = $case['harness'] ?? [];
    if (!is_array($harness)) {
        throw new SchemaError('harness must be a mapping');
    }
    $cfg = $harness['spec_lang'] ?? [];
    if ($cfg === null || $cfg === []) {
        return $defaults;
    }
    if (!is_array($cfg)) {
        throw new SchemaError('harness.spec_lang must be a mapping');
    }
    foreach ($defaults as $field => $default) {
        if (!array_key_exists($field, $cfg)) {
            continue;
        }
        $raw = $cfg[$field];
        if (!is_int($raw)) {
            throw new SchemaError("harness.spec_lang.{$field} must be an integer");
        }
        $min = $field === 'timeout_ms' ? 0 : 1;
        if ($raw < $min) {
            throw new SchemaError("harness.spec_lang.{$field} must be >= {$min}");
        }
        $defaults[$field] = $raw;
    }
    return $defaults;
}

function specLangUnsetSentinel(): object {
    static $sentinel = null;
    if ($sentinel === null) {
        $sentinel = new stdClass();
    }
    return $sentinel;
}

function specLangTick(array &$state): void {
    $state['steps'] += 1;
    if ($state['steps'] > $state['limits']['max_steps']) {
        throw new RuntimeException('spec_lang budget exceeded: steps');
    }
    $timeout = (int)$state['limits']['timeout_ms'];
    if ($timeout > 0) {
        $elapsedMs = (int)floor((microtime(true) - (float)$state['started']) * 1000.0);
        if ($elapsedMs > $timeout) {
            throw new RuntimeException('spec_lang budget exceeded: timeout');
        }
    }
}

function specLangValidateExprShape(mixed $expr, array $limits): void {
    $stack = [$expr];
    $nodes = 0;
    $literalBytes = 0;
    while (count($stack) > 0) {
        $cur = array_pop($stack);
        $nodes += 1;
        if ($nodes > $limits['max_nodes']) {
            throw new RuntimeException('spec_lang budget exceeded: nodes');
        }
        if (is_string($cur)) {
            $literalBytes += strlen($cur);
        }
        if ($literalBytes > $limits['max_literal_bytes']) {
            throw new RuntimeException('spec_lang budget exceeded: literal_size');
        }
        if (is_array($cur) && isListArray($cur)) {
            foreach ($cur as $child) {
                $stack[] = $child;
            }
        }
    }
}

function specLangLookup(SpecLangEnv $env, string $name): mixed {
    $cur = $env;
    $unset = specLangUnsetSentinel();
    while ($cur !== null) {
        if (array_key_exists($name, $cur->vars)) {
            $value = $cur->vars[$name];
            if ($value === $unset) {
                throw new SchemaError("uninitialized variable: {$name}");
            }
            return $value;
        }
        $cur = $cur->parent;
    }
    throw new SchemaError("undefined variable: {$name}");
}

function specLangJsonTypeName(mixed $value): string {
    if ($value === null) {
        return 'null';
    }
    if (is_bool($value)) {
        return 'bool';
    }
    if (is_int($value) || is_float($value)) {
        return 'number';
    }
    if (is_string($value)) {
        return 'string';
    }
    if (is_array($value)) {
        return isListArray($value) ? 'list' : 'dict';
    }
    return 'unknown';
}

function specLangIsClosure(mixed $value): bool {
    return is_array($value) && ($value['__type'] ?? null) === 'closure' && ($value['env'] ?? null) instanceof SpecLangEnv;
}

function specLangRequireArity(string $op, array $args, int $n): void {
    if (count($args) !== $n) {
        throw new SchemaError("spec_lang arity error for {$op}: expected {$n} got " . count($args));
    }
}

function specLangRequireMinArity(string $op, array $args, int $n): void {
    if (count($args) < $n) {
        throw new SchemaError("spec_lang arity error for {$op}: expected at least {$n} got " . count($args));
    }
}

function specLangEvalNonTail(mixed $expr, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    return specLangEvalTail($expr, $env, $subject, $limits, $state);
}

function specLangEvalBuiltin(string $op, array $args, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    if ($op === 'subject') {
        specLangRequireArity($op, $args, 0);
        return $subject;
    }
    if ($op === 'var') {
        specLangRequireArity($op, $args, 1);
        $name = $args[0];
        if (!is_string($name) || trim($name) === '') {
            throw new SchemaError('spec_lang var requires non-empty string name');
        }
        return specLangLookup($env, trim($name));
    }
    if ($op === 'and') {
        specLangRequireMinArity($op, $args, 1);
        foreach ($args as $arg) {
            if (!((bool)specLangEvalNonTail($arg, $env, $subject, $limits, $state))) {
                return false;
            }
        }
        return true;
    }
    if ($op === 'or') {
        specLangRequireMinArity($op, $args, 1);
        foreach ($args as $arg) {
            if ((bool)specLangEvalNonTail($arg, $env, $subject, $limits, $state)) {
                return true;
            }
        }
        return false;
    }
    if ($op === 'not') {
        specLangRequireArity($op, $args, 1);
        return !((bool)specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
    }
    if ($op === 'contains' || $op === 'starts_with' || $op === 'ends_with' || $op === 'json_type' || $op === 'has_key') {
        if (count($args) === 1) {
            $left = $subject;
            $right = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        } elseif (count($args) === 2) {
            $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
            $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        } else {
            throw new SchemaError("spec_lang arity error for {$op}");
        }
        if ($op === 'contains') {
            return str_contains((string)$left, (string)$right);
        }
        if ($op === 'starts_with') {
            return str_starts_with((string)$left, (string)$right);
        }
        if ($op === 'ends_with') {
            return str_ends_with((string)$left, (string)$right);
        }
        if ($op === 'json_type') {
            return specLangJsonTypeName($left) === strtolower(trim((string)$right));
        }
        if (!is_array($left) || isListArray($left)) {
            return false;
        }
        return array_key_exists((string)$right, $left);
    }
    if ($op === 'eq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) === specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'neq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) !== specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'in') {
        specLangRequireArity($op, $args, 2);
        $member = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $container = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (is_array($container)) {
            if (isListArray($container)) {
                return in_array($member, $container, true);
            }
            return array_key_exists((string)$member, $container);
        }
        if (is_string($container)) {
            return str_contains($container, (string)$member);
        }
        throw new SchemaError('spec_lang in expects list/dict/string container');
    }
    if ($op === 'get') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $key = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (is_array($obj) && !isListArray($obj)) {
            return $obj[(string)$key] ?? null;
        }
        if (is_array($obj) && isListArray($obj)) {
            if (!is_int($key) || $key < 0 || $key >= count($obj)) {
                return null;
            }
            return $obj[$key];
        }
        throw new SchemaError('spec_lang get expects dict or list');
    }
    if ($op === 'len') {
        specLangRequireArity($op, $args, 1);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (is_string($value)) {
            return strlen($value);
        }
        if (is_array($value)) {
            return count($value);
        }
        throw new SchemaError('spec_lang len expects string/list/dict');
    }
    if ($op === 'trim' || $op === 'lower' || $op === 'upper') {
        specLangRequireArity($op, $args, 1);
        $value = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if ($op === 'trim') {
            return trim($value);
        }
        if ($op === 'lower') {
            return strtolower($value);
        }
        return strtoupper($value);
    }
    if ($op === 'add' || $op === 'sub') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ((!is_int($left) && !is_float($left)) || (!is_int($right) && !is_float($right))) {
            throw new SchemaError("spec_lang {$op} expects numeric args");
        }
        return $op === 'add' ? $left + $right : $left - $right;
    }
    throw new SchemaError("unsupported spec_lang symbol: {$op}");
}

function specLangEvalTail(mixed $expr, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    $currentExpr = $expr;
    $currentEnv = $env;
    while (true) {
        specLangTick($state);
        if (is_string($currentExpr) || is_int($currentExpr) || is_float($currentExpr) || is_bool($currentExpr) || $currentExpr === null) {
            return $currentExpr;
        }
        if (!is_array($currentExpr) || !isListArray($currentExpr)) {
            throw new SchemaError('spec_lang expression must be list-based s-expr or scalar literal');
        }
        if (count($currentExpr) === 0) {
            throw new SchemaError('spec_lang expression list must not be empty');
        }
        $head = $currentExpr[0];
        if (!is_string($head) || trim($head) === '') {
            throw new SchemaError('spec_lang expression head must be non-empty string symbol');
        }
        $op = $head;
        $args = array_slice($currentExpr, 1);

        if ($op === 'if') {
            specLangRequireArity($op, $args, 3);
            $cond = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $currentExpr = ((bool)$cond) ? $args[1] : $args[2];
            continue;
        }
        if ($op === 'let') {
            specLangRequireArity($op, $args, 2);
            $rawBindings = $args[0];
            $body = $args[1];
            if (!is_array($rawBindings) || !isListArray($rawBindings)) {
                throw new SchemaError('spec_lang let bindings must be a list');
            }
            $nextEnv = new SpecLangEnv([], $currentEnv);
            $pairs = [];
            $unset = specLangUnsetSentinel();
            foreach ($rawBindings as $binding) {
                if (!is_array($binding) || !isListArray($binding) || count($binding) !== 2) {
                    throw new SchemaError('spec_lang let binding must be [name, expr]');
                }
                $name = $binding[0];
                if (!is_string($name) || trim($name) === '') {
                    throw new SchemaError('spec_lang let binding name must be non-empty string');
                }
                $key = trim($name);
                if (array_key_exists($key, $nextEnv->vars)) {
                    throw new SchemaError("duplicate let binding: {$key}");
                }
                $nextEnv->vars[$key] = $unset;
                $pairs[] = [$key, $binding[1]];
            }
            foreach ($pairs as $pair) {
                [$key, $rhs] = $pair;
                $nextEnv->vars[$key] = specLangEvalNonTail($rhs, $nextEnv, $subject, $limits, $state);
            }
            $currentExpr = $body;
            $currentEnv = $nextEnv;
            continue;
        }
        if ($op === 'fn') {
            specLangRequireArity($op, $args, 2);
            $rawParams = $args[0];
            $body = $args[1];
            if (!is_array($rawParams) || !isListArray($rawParams)) {
                throw new SchemaError('spec_lang fn params must be a list');
            }
            $params = [];
            foreach ($rawParams as $param) {
                if (!is_string($param) || trim($param) === '') {
                    throw new SchemaError('spec_lang fn param must be non-empty string');
                }
                $key = trim($param);
                if (in_array($key, $params, true)) {
                    throw new SchemaError("duplicate fn param: {$key}");
                }
                $params[] = $key;
            }
            return ['__type' => 'closure', 'params' => $params, 'body' => $body, 'env' => $currentEnv];
        }
        if ($op === 'call') {
            specLangRequireMinArity($op, $args, 1);
            $fnValue = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $evalArgs = [];
            foreach (array_slice($args, 1) as $arg) {
                $evalArgs[] = specLangEvalNonTail($arg, $currentEnv, $subject, $limits, $state);
            }
            if (!specLangIsClosure($fnValue)) {
                throw new SchemaError('spec_lang call expects fn closure');
            }
            $params = $fnValue['params'];
            if (count($evalArgs) !== count($params)) {
                throw new SchemaError('spec_lang call argument count mismatch');
            }
            $vars = [];
            foreach ($params as $i => $name) {
                $vars[(string)$name] = $evalArgs[$i];
            }
            $currentEnv = new SpecLangEnv($vars, $fnValue['env']);
            $currentExpr = $fnValue['body'];
            continue;
        }
        return specLangEvalBuiltin($op, $args, $currentEnv, $subject, $limits, $state);
    }
}

function specLangEvalPredicate(mixed $expr, mixed $subject, array $limits): bool {
    specLangValidateExprShape($expr, $limits);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits];
    $value = specLangEvalTail($expr, new SpecLangEnv([], null), $subject, $limits, $state);
    return (bool)$value;
}

function evalTextLeaf(
    array $leaf,
    string $subject,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits
): void {
    foreach ($leaf as $op => $raw) {
        if ($op === 'target') {
            continue;
        }
        if ($op !== 'contain' && $op !== 'regex' && $op !== 'expr') {
            throw new SchemaError("unsupported op: {$op}");
        }
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        foreach ($raw as $value) {
            if ($op === 'expr') {
                if (!specLangEvalPredicate($value, $subject, $specLangLimits)) {
                    throw new AssertionFailure(
                        "[case_id={$caseId} assert_path={$path} target={$target} op=expr] expr assertion failed"
                    );
                }
                continue;
            }
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

function evalTextAssertNode(
    mixed $node,
    string $subject,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    array $specLangLimits
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalTextAssertNode($child, $subject, $inheritedTarget, $caseId, "{$path}[{$i}]", $specLangLimits);
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
                evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.must[{$i}]", $specLangLimits);
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.can[{$i}]", $specLangLimits);
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
                    evalTextAssertNode($child, $subject, $target, $caseId, "{$path}.cannot[{$i}]", $specLangLimits);
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
    evalTextLeaf($node, $subject, $target, $caseId, $path, $specLangLimits);
}

function evaluateTextFileCase(array $case, string $subject): array {
    try {
        $resolvedMode = resolveAssertHealthMode($case);
    } catch (SchemaError $e) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    }
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
        $specLangLimits = specLangLimitsFromCase($case);
        evalTextAssertNode($assertSpec, $subject, null, (string)$case['id'], 'assert', $specLangLimits);
    } catch (SchemaError $e) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    } catch (AssertionFailure $e) {
        return ['status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
    } catch (Throwable $e) {
        return ['status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
    }
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function resolveApiHttpUrl(string $fixturePath, string $url): array {
    $trim = trim($url);
    if ($trim === '') {
        throw new SchemaError('api.http request.url is required');
    }
    $parts = @parse_url($trim);
    if ($parts !== false && is_array($parts) && array_key_exists('scheme', $parts)) {
        return ['source_type' => 'url', 'url' => $trim];
    }
    if (isAbsolutePath($trim)) {
        throw new SchemaError('api.http request.url relative path must not be absolute');
    }
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    $candidate = normalizePath(dirname($docAbs) . '/' . $trim);
    $root = contractRootFor($docAbs);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError('api.http request.url relative path escapes contract root');
    }
    return ['source_type' => 'file', 'path' => $candidate];
}

function evalApiHttpLeaf(
    array $leaf,
    array $resp,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits
): void {
    foreach ($leaf as $op => $raw) {
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        if ($target === 'status' || $target === 'headers' || $target === 'body_text') {
            $subject = $target === 'status'
                ? (string)$resp['status']
                : ($target === 'headers' ? (string)$resp['headers_text'] : (string)$resp['body_text']);
            if ($op !== 'contain' && $op !== 'regex' && $op !== 'json_type' && $op !== 'expr') {
                throw new SchemaError("unsupported op: {$op}");
            }
            foreach ($raw as $value) {
                if ($op === 'expr') {
                    if (!specLangEvalPredicate($value, $subject, $specLangLimits)) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=expr] expr assertion failed"
                        );
                    }
                    continue;
                }
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
                $parsed = json_decode($subject, true);
                $want = strtolower(trim((string)$value));
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
        if ($target === 'body_json') {
            if ($op !== 'contain' && $op !== 'regex' && $op !== 'json_type' && $op !== 'expr') {
                throw new SchemaError("unsupported op: {$op}");
            }
            $parsed = json_decode((string)$resp['body_text'], true);
            if ($parsed === null && trim((string)$resp['body_text']) !== 'null') {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] body_json parse failed"
                );
            }
            foreach ($raw as $value) {
                if ($op === 'expr') {
                    if (!specLangEvalPredicate($value, $parsed, $specLangLimits)) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=expr] expr assertion failed"
                        );
                    }
                    continue;
                }
                if ($op === 'json_type') {
                    $want = strtolower(trim((string)$value));
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
                    continue;
                }
                $subject = json_encode($parsed, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
                if ($subject === false) {
                    throw new RuntimeException('failed to serialize body_json');
                }
                if ($op === 'contain') {
                    if (strpos($subject, (string)$value) === false) {
                        throw new AssertionFailure(
                            "[case_id={$caseId} assert_path={$path} target={$target} op=contain] contain assertion failed"
                        );
                    }
                } else {
                    $v = (string)$value;
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
        throw new SchemaError("unknown assert target for api.http: {$target}");
    }
}

function evalApiHttpAssertNode(
    mixed $node,
    array $resp,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    array $specLangLimits
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalApiHttpAssertNode($child, $resp, $inheritedTarget, $caseId, "{$path}[{$i}]", $specLangLimits);
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
                evalApiHttpAssertNode($child, $resp, $target, $caseId, "{$path}.must[{$i}]", $specLangLimits);
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalApiHttpAssertNode($child, $resp, $target, $caseId, "{$path}.can[{$i}]", $specLangLimits);
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
                    evalApiHttpAssertNode($child, $resp, $target, $caseId, "{$path}.cannot[{$i}]", $specLangLimits);
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
    evalApiHttpLeaf($node, $resp, $target, $caseId, $path, $specLangLimits);
}

function evaluateApiHttpCase(string $fixturePath, array $case): array {
    $request = $case['request'] ?? null;
    if (!is_array($request)) {
        throw new SchemaError('api.http requires request mapping');
    }
    $method = strtoupper(trim((string)($request['method'] ?? '')));
    if ($method === '') {
        throw new SchemaError('api.http request.method is required');
    }
    if (!array_key_exists('url', $request) || trim((string)$request['url']) === '') {
        throw new SchemaError('api.http request.url is required');
    }
    $resolved = resolveApiHttpUrl($fixturePath, (string)$request['url']);
    $headersText = '';
    $status = 200;
    $bodyText = '';
    if ($resolved['source_type'] === 'file') {
        $body = file_get_contents((string)$resolved['path']);
        if ($body === false) {
            throw new RuntimeException("cannot read fixture file: {$resolved['path']}");
        }
        $bodyText = (string)$body;
    } else {
        $headers = [];
        $hdrs = $request['headers'] ?? [];
        if ($hdrs !== null && !is_array($hdrs)) {
            throw new SchemaError('api.http request.headers must be a mapping');
        }
        if (is_array($hdrs)) {
            foreach ($hdrs as $k => $v) {
                $headers[] = (string)$k . ': ' . (string)$v;
            }
        }
        $bodyData = null;
        if (array_key_exists('body_text', $request) && array_key_exists('body_json', $request)) {
            throw new SchemaError('api.http request.body_text and request.body_json are mutually exclusive');
        }
        if (array_key_exists('body_text', $request)) {
            $bodyData = (string)$request['body_text'];
        } elseif (array_key_exists('body_json', $request)) {
            $encoded = json_encode($request['body_json'], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
            if ($encoded === false) {
                throw new SchemaError('api.http request.body_json must be json-serializable');
            }
            $bodyData = $encoded;
            $headers[] = 'Content-Type: application/json';
        }
        $timeout = 5;
        if (isset($case['harness']) && is_array($case['harness']) && array_key_exists('timeout_seconds', $case['harness'])) {
            $timeout = (int)$case['harness']['timeout_seconds'];
            if ($timeout <= 0) {
                $timeout = 5;
            }
        }
        $opts = [
            'http' => [
                'method' => $method,
                'header' => implode("\r\n", $headers),
                'ignore_errors' => true,
                'timeout' => $timeout,
            ],
        ];
        if ($bodyData !== null) {
            $opts['http']['content'] = $bodyData;
        }
        $ctx = stream_context_create($opts);
        $body = @file_get_contents((string)$resolved['url'], false, $ctx);
        if ($body === false) {
            throw new RuntimeException("api.http request failed: {$resolved['url']}");
        }
        $bodyText = (string)$body;
        $responseHeaders = $http_response_header ?? [];
        if (is_array($responseHeaders) && count($responseHeaders) > 0) {
            $headersText = implode("\n", $responseHeaders);
            if (preg_match('/\s(\d{3})\s/', (string)$responseHeaders[0], $m) === 1) {
                $status = (int)$m[1];
            }
        }
    }

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

    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromCase($case);
    evalApiHttpAssertNode(
        $assertSpec,
        [
            'status' => $status,
            'headers_text' => $headersText,
            'body_text' => $bodyText,
        ],
        null,
        (string)$case['id'],
        'assert',
        $specLangLimits
    );
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

    if ($type === 'text.file') {
        try {
            $subjectPath = resolveTextFilePath($fixturePath, $case);
        } catch (SchemaError $e) {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'schema',
                'message' => $e->getMessage(),
            ];
        }

        $subject = file_get_contents($subjectPath);
        if ($subject === false) {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'runtime',
                'message' => "cannot read fixture file: {$subjectPath}",
            ];
        }
        $res = evaluateTextFileCase($case, $subject);
    } elseif ($type === 'api.http') {
        try {
            $res = evaluateApiHttpCase($fixturePath, $case);
        } catch (SchemaError $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
        } catch (AssertionFailure $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
        } catch (Throwable $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
        }
    } else {
        return [
            'id' => $id,
            'status' => 'fail',
            'category' => 'runtime',
            'message' => "unsupported type for php bootstrap: {$type}",
        ];
    }
    return [
        'id' => $id,
        'status' => $res['status'],
        'category' => $res['category'],
        'message' => $res['message'],
    ];
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
