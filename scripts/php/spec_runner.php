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
    fwrite(STDOUT, "usage: spec_runner.php --cases <dir-or-file> --out <file> [--case-file-pattern <glob>] [--case-formats <csv>]\n");
}

const DEFAULT_CASE_FILE_PATTERN = '*.spec.md';
const PHP_CAPABILITIES = [
    'api.http',
    'assert.op.contain',
    'assert.op.regex',
    'assert.op.evaluate',
    'assert.group.must',
    'assert.group.can',
    'assert.group.cannot',
    'assert_health.ah001',
    'assert_health.ah002',
    'assert_health.ah003',
    'assert_health.ah004',
    'assert_health.ah005',
    'evaluate.spec_lang.v1',
    'requires.capabilities',
];

function parseArgs(array $argv): array {
    $out = null;
    $cases = null;
    $casePattern = DEFAULT_CASE_FILE_PATTERN;
    $caseFormatsRaw = 'md';
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
        if ($arg === '--case-formats') {
            if ($i + 1 >= count($argv)) {
                fwrite(STDERR, "error: --case-formats requires a non-empty value\n");
                usage();
                exit(2);
            }
            $caseFormatsRaw = trim((string)$argv[++$i]);
            if ($caseFormatsRaw === '') {
                fwrite(STDERR, "error: --case-formats requires a non-empty value\n");
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
    $parts = preg_split('/\s*,\s*/', strtolower($caseFormatsRaw)) ?: [];
    $formats = [];
    foreach ($parts as $p) {
        $v = trim((string)$p);
        if ($v === '') {
            continue;
        }
        if ($v !== 'md' && $v !== 'yaml' && $v !== 'json') {
            fwrite(STDERR, "error: unsupported case format: {$v}\n");
            usage();
            exit(2);
        }
        $formats[$v] = true;
    }
    if (count($formats) === 0) {
        fwrite(STDERR, "error: --case-formats requires at least one format\n");
        usage();
        exit(2);
    }
    return [
        'out' => $out,
        'cases' => $cases,
        'case_pattern' => $casePattern,
        'case_formats' => array_keys($formats),
    ];
}

function matchesCasePattern(string $name, string $pattern): bool {
    $regex = '/^' . str_replace(
        ['\*', '\?'],
        ['.*', '.'],
        preg_quote($pattern, '/')
    ) . '$/i';
    return preg_match($regex, $name) === 1;
}

function _pathMatchesFormat(string $name, array $formats, string $pattern): bool {
    $lower = strtolower($name);
    foreach ($formats as $fmt) {
        if ($fmt === 'md') {
            if (matchesCasePattern($name, $pattern)) {
                return true;
            }
            continue;
        }
        if ($fmt === 'yaml') {
            if (str_ends_with($lower, '.spec.yaml') || str_ends_with($lower, '.spec.yml')) {
                return true;
            }
            continue;
        }
        if ($fmt === 'json') {
            if (str_ends_with($lower, '.spec.json')) {
                return true;
            }
        }
    }
    return false;
}

function listCaseFiles(string $path, string $pattern, array $formats): array {
    if (is_file($path)) {
        if (_pathMatchesFormat(basename($path), $formats, $pattern)) {
            return [$path];
        }
        throw new RuntimeException("cases path is a file but does not match enabled formats/pattern: {$path}");
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
        if (_pathMatchesFormat($item, $formats, $pattern)) {
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

function _validateParsedCasePayload(mixed $payload, string $path): array {
    if (is_array($payload) && isListArray($payload)) {
        $cases = [];
        foreach ($payload as $test) {
            if (!is_array($test)) {
                throw new RuntimeException("spec payload in {$path} contains a non-mapping test");
            }
            if (!array_key_exists('id', $test) || !array_key_exists('type', $test)) {
                throw new RuntimeException("spec in {$path} must include 'id' and 'type'");
            }
            $cases[] = $test;
        }
        return $cases;
    }
    if (is_array($payload)) {
        if (!array_key_exists('id', $payload) || !array_key_exists('type', $payload)) {
            throw new RuntimeException("spec in {$path} must include 'id' and 'type'");
        }
        return [$payload];
    }
    throw new RuntimeException("spec payload in {$path} must be a mapping or a list of mappings");
}

function parseYamlCases(string $path): array {
    if (!function_exists('yaml_parse')) {
        throw new RuntimeException('yaml_parse extension is required for YAML spec cases');
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $payload = @yaml_parse($raw);
    return _validateParsedCasePayload($payload, $path);
}

function parseJsonCases(string $path): array {
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    try {
        $payload = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException("invalid JSON in {$path}: " . $e->getMessage());
    }
    return _validateParsedCasePayload($payload, $path);
}

function parseCases(string $path): array {
    $lower = strtolower($path);
    if (str_ends_with($lower, '.spec.yaml') || str_ends_with($lower, '.spec.yml')) {
        return parseYamlCases($path);
    }
    if (str_ends_with($lower, '.spec.json')) {
        return parseJsonCases($path);
    }
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
        if (is_dir($cur . '/.git') || is_file($cur . '/.git')) {
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

function resolveContractPath(string $anchorPath, string $rawPath, string $field): string {
    $raw = trim($rawPath);
    if ($raw === '') {
        throw new SchemaError("{$field} must be non-empty");
    }
    if (str_starts_with($raw, 'external://')) {
        throw new SchemaError("{$field}: external refs are denied by default");
    }
    if (preg_match('/^[A-Za-z]:[\/\\\\]/', $raw) === 1) {
        throw new SchemaError("{$field} must not be OS-absolute");
    }
    $root = contractRootFor($anchorPath);
    if (str_starts_with($raw, '/')) {
        $joined = $root . '/' . ltrim($raw, '/');
    } else {
        $joined = $root . '/' . $raw;
    }
    $candidate = normalizePath($joined);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError("{$field} escapes contract root");
    }
    return $candidate;
}

function resolveTextFilePath(string $fixturePath, array $case): string {
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    if (!array_key_exists('path', $case)) {
        return $docAbs;
    }
    return resolveContractPath($docAbs, (string)$case['path'], 'text.file path');
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
    $stepClass = trim((string)($node['class'] ?? ''));
    if (in_array($stepClass, ['must', 'can', 'cannot'], true) && array_key_exists('checks', $node)) {
        $checks = $node['checks'];
        if (is_array($checks) && isListArray($checks)) {
            $seen = [];
            foreach ($checks as $child) {
                $key = @json_encode($child, JSON_UNESCAPED_SLASHES);
                if (!is_string($key) || $key === '') {
                    $key = serialize($child);
                }
                if (array_key_exists($key, $seen)) {
                    $diags[] = [
                        'code' => 'AH004',
                        'path' => "{$path}.checks",
                        'message' => "redundant sibling assertion branch in '{$stepClass}'",
                    ];
                    break;
                }
                $seen[$key] = true;
            }
        }
        return array_merge($diags, lintAssertionHealth($checks, "{$path}.checks", $stepClass));
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

function specLangLimitsFromHarness(array $case): array {
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

function specLangNormalizeJsonTypeToken(mixed $value): string {
    $token = strtolower(trim((string)$value));
    if ($token === 'boolean') {
        return 'bool';
    }
    if ($token === 'array') {
        return 'list';
    }
    if ($token === 'object') {
        return 'dict';
    }
    return $token;
}

function specLangDeepEquals(mixed $left, mixed $right): bool {
    if (gettype($left) !== gettype($right)) {
        return false;
    }
    if (is_array($left) && is_array($right)) {
        if (isListArray($left) !== isListArray($right)) {
            return false;
        }
        if (isListArray($left)) {
            if (count($left) !== count($right)) {
                return false;
            }
            for ($i = 0; $i < count($left); $i++) {
                if (!specLangDeepEquals($left[$i], $right[$i])) {
                    return false;
                }
            }
            return true;
        }
        $lKeys = array_keys($left);
        $rKeys = array_keys($right);
        sort($lKeys, SORT_STRING);
        sort($rKeys, SORT_STRING);
        if ($lKeys !== $rKeys) {
            return false;
        }
        foreach ($lKeys as $k) {
            if (!specLangDeepEquals($left[$k], $right[$k])) {
                return false;
            }
        }
        return true;
    }
    return $left === $right;
}

function specLangIsIntegerNumber(mixed $value): bool {
    if (is_bool($value) || (!is_int($value) && !is_float($value))) {
        return false;
    }
    if (is_int($value)) {
        return true;
    }
    return floor($value) === $value;
}

function specLangIncludesDeep(array $seq, mixed $needle): bool {
    foreach ($seq as $item) {
        if (specLangDeepEquals($item, $needle)) {
            return true;
        }
    }
    return false;
}

function specLangDistinctDeep(array $seq): array {
    $out = [];
    foreach ($seq as $item) {
        if (!specLangIncludesDeep($out, $item)) {
            $out[] = $item;
        }
    }
    return $out;
}

function specLangDeepMergeDicts(array $left, array $right): array {
    $out = $left;
    foreach ($right as $k => $v) {
        if (
            array_key_exists($k, $out)
            && is_array($out[$k]) && !isListArray($out[$k])
            && is_array($v) && !isListArray($v)
        ) {
            $out[$k] = specLangDeepMergeDicts($out[$k], $v);
            continue;
        }
        $out[$k] = $v;
    }
    return $out;
}

function specLangGetInPath(mixed $obj, array $path): array {
    $cur = $obj;
    foreach ($path as $part) {
        if (is_array($cur) && isListArray($cur)) {
            if (!is_int($part) || $part < 0 || $part >= count($cur)) {
                return [false, null];
            }
            $cur = $cur[$part];
            continue;
        }
        if (is_array($cur) && !isListArray($cur)) {
            $key = (string)$part;
            if (!array_key_exists($key, $cur)) {
                return [false, null];
            }
            $cur = $cur[$key];
            continue;
        }
        return [false, null];
    }
    return [true, $cur];
}

function specLangSchemaTypeOk(mixed $value, string $expected): bool {
    $kind = specLangNormalizeJsonTypeToken($expected);
    return match ($kind) {
        'null' => $value === null,
        'bool' => is_bool($value),
        'number' => (is_int($value) || is_float($value)) && !is_bool($value),
        'integer' => specLangIsIntegerNumber($value),
        'string' => is_string($value),
        'list' => is_array($value) && isListArray($value),
        'dict' => is_array($value) && !isListArray($value),
        default => false,
    };
}

function specLangSchemaValidate(mixed $value, mixed $schema, string $path, array &$out): void {
    if (!is_array($schema) || isListArray($schema)) {
        $out[] = "{$path}: schema must be dict";
        return;
    }
    $allowed = [
        'type', 'required', 'properties', 'allow_extra', 'items', 'min_items', 'max_items',
        'min_length', 'max_length', 'pattern', 'const', 'enum', 'all_of', 'any_of', 'not',
    ];
    foreach ($schema as $k => $_v) {
        if (!in_array((string)$k, $allowed, true)) {
            $out[] = "{$path}: unknown schema key: {$k}";
        }
    }
    if (array_key_exists('type', $schema)) {
        $expected = (string)$schema['type'];
        if (!specLangSchemaTypeOk($value, $expected)) {
            $out[] = "{$path}: type mismatch expected {$expected}";
            return;
        }
    }
    if (array_key_exists('const', $schema) && !specLangDeepEquals($value, $schema['const'])) {
        $out[] = "{$path}: const mismatch";
    }
    if (array_key_exists('enum', $schema)) {
        $enum = $schema['enum'];
        if (!is_array($enum) || !isListArray($enum)) {
            $out[] = "{$path}: enum must be list";
        } else {
            $ok = false;
            foreach ($enum as $item) {
                if (specLangDeepEquals($value, $item)) {
                    $ok = true;
                    break;
                }
            }
            if (!$ok) {
                $out[] = "{$path}: enum mismatch";
            }
        }
    }
    if (is_string($value)) {
        if (array_key_exists('min_length', $schema)) {
            $minLen = $schema['min_length'];
            if (!is_int($minLen)) {
                $out[] = "{$path}: min_length must be int";
            } elseif (strlen($value) < $minLen) {
                $out[] = "{$path}: min_length";
            }
        }
        if (array_key_exists('max_length', $schema)) {
            $maxLen = $schema['max_length'];
            if (!is_int($maxLen)) {
                $out[] = "{$path}: max_length must be int";
            } elseif (strlen($value) > $maxLen) {
                $out[] = "{$path}: max_length";
            }
        }
        if (array_key_exists('pattern', $schema)) {
            $pattern = (string)$schema['pattern'];
            $ok = @preg_match('/' . str_replace('/', '\\/', $pattern) . '/u', $value);
            if ($ok === false) {
                $out[] = "{$path}: invalid pattern";
            } elseif ($ok !== 1) {
                $out[] = "{$path}: pattern mismatch";
            }
        }
    }
    if (is_array($value) && isListArray($value)) {
        if (array_key_exists('min_items', $schema)) {
            $minItems = $schema['min_items'];
            if (!is_int($minItems)) {
                $out[] = "{$path}: min_items must be int";
            } elseif (count($value) < $minItems) {
                $out[] = "{$path}: min_items";
            }
        }
        if (array_key_exists('max_items', $schema)) {
            $maxItems = $schema['max_items'];
            if (!is_int($maxItems)) {
                $out[] = "{$path}: max_items must be int";
            } elseif (count($value) > $maxItems) {
                $out[] = "{$path}: max_items";
            }
        }
        if (array_key_exists('items', $schema)) {
            $itemSchema = $schema['items'];
            foreach ($value as $idx => $item) {
                specLangSchemaValidate($item, $itemSchema, "{$path}[{$idx}]", $out);
            }
        }
    }
    if (is_array($value) && !isListArray($value)) {
        $required = $schema['required'] ?? [];
        if (is_array($required) && isListArray($required)) {
            foreach ($required as $rk) {
                $key = (string)$rk;
                if (!array_key_exists($key, $value)) {
                    $out[] = "{$path}: missing required key {$key}";
                }
            }
        } elseif (array_key_exists('required', $schema)) {
            $out[] = "{$path}: required must be list";
        }
        $props = $schema['properties'] ?? [];
        if (is_array($props) && !isListArray($props)) {
            foreach ($props as $k => $subSchema) {
                $key = (string)$k;
                if (array_key_exists($key, $value)) {
                    specLangSchemaValidate($value[$key], $subSchema, "{$path}.{$key}", $out);
                }
            }
            $allowExtra = $schema['allow_extra'] ?? true;
            if (!is_bool($allowExtra)) {
                $out[] = "{$path}: allow_extra must be bool";
            } elseif (!$allowExtra) {
                foreach ($value as $k => $_v) {
                    $key = (string)$k;
                    if (!array_key_exists($key, $props)) {
                        $out[] = "{$path}: unexpected key {$key}";
                    }
                }
            }
        } elseif (array_key_exists('properties', $schema)) {
            $out[] = "{$path}: properties must be dict";
        }
    }
    if (array_key_exists('all_of', $schema)) {
        $allOf = $schema['all_of'];
        if (!is_array($allOf) || !isListArray($allOf)) {
            $out[] = "{$path}: all_of must be list";
        } else {
            foreach ($allOf as $child) {
                specLangSchemaValidate($value, $child, $path, $out);
            }
        }
    }
    if (array_key_exists('any_of', $schema)) {
        $anyOf = $schema['any_of'];
        if (!is_array($anyOf) || !isListArray($anyOf)) {
            $out[] = "{$path}: any_of must be list";
        } else {
            $matched = false;
            foreach ($anyOf as $child) {
                $tmp = [];
                specLangSchemaValidate($value, $child, $path, $tmp);
                if ($tmp === []) {
                    $matched = true;
                    break;
                }
            }
            if (!$matched) {
                $out[] = "{$path}: any_of mismatch";
            }
        }
    }
    if (array_key_exists('not', $schema)) {
        $tmp = [];
        specLangSchemaValidate($value, $schema['not'], $path, $tmp);
        if ($tmp === []) {
            $out[] = "{$path}: not mismatch";
        }
    }
}

function specLangRequireListArg(string $op, mixed $value): array {
    if (!is_array($value) || !isListArray($value)) {
        throw new SchemaError("spec_lang {$op} expects list");
    }
    return $value;
}

function specLangRequireDictArg(string $op, mixed $value): array {
    if (!is_array($value) || isListArray($value)) {
        throw new SchemaError("spec_lang {$op} expects dict");
    }
    return $value;
}

function specLangRequireNumericArg(string $op, mixed $value): int|float {
    if (is_bool($value) || (!is_int($value) && !is_float($value))) {
        throw new SchemaError("spec_lang {$op} expects numeric args");
    }
    return $value;
}

function specLangRequireIntArg(string $op, mixed $value): int {
    if (!specLangIsIntegerNumber($value)) {
        throw new SchemaError("spec_lang {$op} expects integer args");
    }
    return (int)$value;
}

function specLangRoundHalfAwayFromZero(int|float $v): int {
    if ($v >= 0) {
        return (int)floor($v + 0.5);
    }
    return (int)ceil($v - 0.5);
}

function specLangFsNormalizePath(string $path): string {
    $raw = trim($path);
    if ($raw === '') {
        return '.';
    }
    $absolute = str_starts_with($raw, '/');
    $segments = [];
    foreach (explode('/', $raw) as $part) {
        if ($part === '' || $part === '.') {
            continue;
        }
        if ($part === '..') {
            if (count($segments) > 0 && $segments[count($segments) - 1] !== '..') {
                array_pop($segments);
            } elseif (!$absolute) {
                $segments[] = '..';
            }
            continue;
        }
        $segments[] = $part;
    }
    $normalized = implode('/', $segments);
    if ($absolute) {
        return $normalized === '' ? '/' : '/' . $normalized;
    }
    return $normalized === '' ? '.' : $normalized;
}

function specLangFsSplitSegments(string $path): array {
    $normalized = specLangFsNormalizePath($path);
    if ($normalized === '.' || $normalized === '/') {
        return [];
    }
    $parts = explode('/', $normalized);
    $out = [];
    foreach ($parts as $part) {
        if ($part !== '' && $part !== '.') {
            $out[] = $part;
        }
    }
    return $out;
}

function specLangFsBasename(string $path): string {
    $normalized = specLangFsNormalizePath($path);
    if ($normalized === '/') {
        return '';
    }
    if ($normalized === '.') {
        return '.';
    }
    $parts = specLangFsSplitSegments($normalized);
    if (count($parts) === 0) {
        return '';
    }
    return (string)$parts[count($parts) - 1];
}

function specLangFsDirname(string $path): string {
    $normalized = specLangFsNormalizePath($path);
    if ($normalized === '/') {
        return '/';
    }
    $absolute = str_starts_with($normalized, '/');
    $parts = specLangFsSplitSegments($normalized);
    if (count($parts) === 0) {
        return $absolute ? '/' : '.';
    }
    array_pop($parts);
    if (count($parts) === 0) {
        return $absolute ? '/' : '.';
    }
    $joined = implode('/', $parts);
    return $absolute ? '/' . $joined : $joined;
}

function specLangFsExtname(string $path): string {
    $base = specLangFsBasename($path);
    if ($base === '' || $base === '.' || $base === '..') {
        return '';
    }
    $idx = strrpos($base, '.');
    if ($idx === false || $idx <= 0) {
        return '';
    }
    return substr($base, $idx);
}

function specLangFsStem(string $path): string {
    $base = specLangFsBasename($path);
    $ext = specLangFsExtname($path);
    if ($ext === '') {
        return $base;
    }
    return substr($base, 0, strlen($base) - strlen($ext));
}

function specLangFsNormalizeExt(string $ext): string {
    $token = trim($ext);
    if ($token === '') {
        return '';
    }
    return str_starts_with($token, '.') ? $token : '.' . $token;
}

function specLangFsRelativize(string $base, string $path): string {
    $baseNorm = specLangFsNormalizePath($base);
    $pathNorm = specLangFsNormalizePath($path);
    $baseAbs = str_starts_with($baseNorm, '/');
    $pathAbs = str_starts_with($pathNorm, '/');
    if ($baseAbs !== $pathAbs) {
        return $pathNorm;
    }
    $baseParts = specLangFsSplitSegments($baseNorm);
    $pathParts = specLangFsSplitSegments($pathNorm);
    $i = 0;
    $baseN = count($baseParts);
    $pathN = count($pathParts);
    while ($i < $baseN && $i < $pathN && $baseParts[$i] === $pathParts[$i]) {
        $i += 1;
    }
    $relParts = [];
    for ($j = $i; $j < $baseN; $j++) {
        $relParts[] = '..';
    }
    for ($j = $i; $j < $pathN; $j++) {
        $relParts[] = $pathParts[$j];
    }
    if (count($relParts) === 0) {
        return '.';
    }
    return implode('/', $relParts);
}

function specLangFsCommonPrefix(array $paths): string {
    if (count($paths) === 0) {
        return '.';
    }
    $normalized = [];
    foreach ($paths as $path) {
        if (!is_string($path)) {
            throw new SchemaError('spec_lang ops.fs.path.common_prefix expects list of strings');
        }
        $normalized[] = specLangFsNormalizePath($path);
    }
    $absolute = str_starts_with($normalized[0], '/');
    foreach ($normalized as $n) {
        if (str_starts_with($n, '/') !== $absolute) {
            return '.';
        }
    }
    $split = [];
    foreach ($normalized as $n) {
        $split[] = specLangFsSplitSegments($n);
    }
    $prefix = [];
    $idx = 0;
    while (true) {
        $candidate = null;
        foreach ($split as $parts) {
            if ($idx >= count($parts)) {
                $candidate = null;
                break;
            }
            $value = $parts[$idx];
            if ($candidate === null) {
                $candidate = $value;
                continue;
            }
            if ($candidate !== $value) {
                $candidate = null;
                break;
            }
        }
        if ($candidate === null) {
            break;
        }
        $prefix[] = $candidate;
        $idx += 1;
    }
    if (count($prefix) === 0) {
        return $absolute ? '/' : '.';
    }
    $joined = implode('/', $prefix);
    return $absolute ? '/' . $joined : $joined;
}

function specLangSpecialForms(): array {
    return ['if' => true, 'let' => true, 'fn' => true, 'call' => true, 'var' => true, 'lit' => true];
}

function specLangFlatBuiltinFromStd(string $symbol): string {
    $map = [
        'std.json.parse' => 'json_parse',
        'std.json.stringify' => 'json_stringify',
        'std.schema.match' => 'schema_match',
        'std.schema.errors' => 'schema_errors',
        'ops.fs.path.normalize' => 'ops_fs_path_normalize',
        'ops.fs.path.join' => 'ops_fs_path_join',
        'ops.fs.path.split' => 'ops_fs_path_split',
        'ops.fs.path.dirname' => 'ops_fs_path_dirname',
        'ops.fs.path.basename' => 'ops_fs_path_basename',
        'ops.fs.path.extname' => 'ops_fs_path_extname',
        'ops.fs.path.stem' => 'ops_fs_path_stem',
        'ops.fs.path.is_abs' => 'ops_fs_path_is_abs',
        'ops.fs.path.has_ext' => 'ops_fs_path_has_ext',
        'ops.fs.path.change_ext' => 'ops_fs_path_change_ext',
        'ops.fs.path.relativize' => 'ops_fs_path_relativize',
        'ops.fs.path.common_prefix' => 'ops_fs_path_common_prefix',
        'ops.fs.file.exists' => 'ops_fs_file_exists',
        'ops.fs.file.is_file' => 'ops_fs_file_is_file',
        'ops.fs.file.is_dir' => 'ops_fs_file_is_dir',
        'ops.fs.file.size_bytes' => 'ops_fs_file_size_bytes',
        'ops.fs.file.path' => 'ops_fs_file_path',
        'ops.fs.file.name' => 'ops_fs_file_name',
        'ops.fs.file.parent' => 'ops_fs_file_parent',
        'ops.fs.file.ext' => 'ops_fs_file_ext',
        'ops.fs.file.get' => 'ops_fs_file_get',
        'ops.fs.json.parse' => 'ops_fs_json_parse',
        'ops.fs.json.get' => 'ops_fs_json_get',
        'ops.fs.json.get_or' => 'ops_fs_json_get_or',
        'ops.fs.json.has_path' => 'ops_fs_json_has_path',
        'ops.fs.glob.match' => 'ops_fs_glob_match',
        'ops.fs.glob.filter' => 'ops_fs_glob_filter',
        'ops.fs.glob.any' => 'ops_fs_glob_any',
        'ops.fs.glob.all' => 'ops_fs_glob_all',
    ];
    if (array_key_exists($symbol, $map)) {
        return $map[$symbol];
    }
    $parts = explode('.', $symbol);
    return trim((string)end($parts));
}

function specLangCompileImportsForCase(array $case): array {
    $harness = $case['harness'] ?? [];
    if (!is_array($harness) || isListArray($harness)) {
        return [];
    }
    $cfg = $harness['spec_lang'] ?? [];
    if (!is_array($cfg) || isListArray($cfg)) {
        return [];
    }
    $rawImports = $cfg['imports'] ?? null;
    if ($rawImports === null) {
        return [];
    }
    if (!is_array($rawImports) || !isListArray($rawImports)) {
        throw new SchemaError('harness.spec_lang.imports must be a list');
    }
    $reserved = specLangSpecialForms();
    $out = [];
    foreach ($rawImports as $i => $item) {
        $field = "harness.spec_lang.imports[{$i}]";
        if (!is_array($item) || isListArray($item)) {
            throw new SchemaError("{$field} must be a mapping");
        }
        $from = trim((string)($item['from'] ?? ''));
        if ($from === '' || (!str_starts_with($from, 'std.') && !str_starts_with($from, 'ops.'))) {
            throw new SchemaError("{$field}.from must be a std.* or ops.* namespace");
        }
        $names = $item['names'] ?? null;
        if (!is_array($names) || !isListArray($names) || count($names) === 0) {
            throw new SchemaError("{$field}.names must be a non-empty list");
        }
        $alias = $item['as'] ?? [];
        if (!is_array($alias) || isListArray($alias)) {
            throw new SchemaError("{$field}.as must be a mapping");
        }
        foreach ($names as $j => $rawName) {
            $name = trim((string)$rawName);
            if ($name === '') {
                throw new SchemaError("{$field}.names[{$j}] must be a non-empty string");
            }
            $local = trim((string)($alias[$name] ?? $name));
            if ($local === '') {
                throw new SchemaError("{$field}.as value for {$name} must be a non-empty string");
            }
            if (array_key_exists($local, $reserved)) {
                throw new SchemaError("{$field} import collides with reserved special form: {$local}");
            }
            $fq = "{$from}.{$name}";
            if (array_key_exists($local, $out) && $out[$local] !== $fq) {
                throw new SchemaError("{$field} import collision for local name: {$local}");
            }
            $out[$local] = $fq;
        }
    }
    return $out;
}

function specLangResolveOpSymbol(string $head, array $imports): string {
    if (array_key_exists($head, specLangSpecialForms())) {
        return $head;
    }
    if (str_starts_with($head, 'std.') || str_starts_with($head, 'ops.')) {
        return specLangFlatBuiltinFromStd($head);
    }
    if (array_key_exists($head, $imports)) {
        return specLangFlatBuiltinFromStd((string)$imports[$head]);
    }
    // Internal list-token AST may still carry flat names; normalize at runtime.
    return specLangFlatBuiltinFromStd($head);
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
            return specLangJsonTypeName($left) === specLangNormalizeJsonTypeToken($right);
        }
        if (!is_array($left) || isListArray($left)) {
            return false;
        }
        return array_key_exists((string)$right, $left);
    }
    if (
        $op === 'is_null'
        || $op === 'is_bool'
        || $op === 'is_boolean'
        || $op === 'is_number'
        || $op === 'is_integer'
        || $op === 'is_string'
        || $op === 'is_list'
        || $op === 'is_array'
        || $op === 'is_dict'
        || $op === 'is_object'
    ) {
        specLangRequireArity($op, $args, 1);
        $jsonType = specLangJsonTypeName(specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($op === 'is_null') {
            return $jsonType === 'null';
        }
        if ($op === 'is_bool') {
            return $jsonType === 'bool';
        }
        if ($op === 'is_boolean') {
            return $jsonType === 'bool';
        }
        if ($op === 'is_number') {
            return $jsonType === 'number';
        }
        if ($op === 'is_integer') {
            $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
            return specLangIsIntegerNumber($value);
        }
        if ($op === 'is_string') {
            return $jsonType === 'string';
        }
        if ($op === 'is_list') {
            return $jsonType === 'list';
        }
        if ($op === 'is_array') {
            return $jsonType === 'list';
        }
        if ($op === 'is_object') {
            return $jsonType === 'dict';
        }
        return $jsonType === 'dict';
    }
    if ($op === 'regex_match' || $op === 'matches') {
        specLangRequireArity($op, $args, 2);
        $subjectText = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $pattern = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $ok = @preg_match('/' . str_replace('/', '\\/', $pattern) . '/u', $subjectText);
        if ($ok === false) {
            throw new SchemaError("invalid regex pattern: {$pattern}");
        }
        return $ok === 1;
    }
    if ($op === 'eq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) === specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'neq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) !== specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'equals') {
        specLangRequireArity($op, $args, 2);
        return specLangDeepEquals(
            specLangEvalNonTail($args[0], $env, $subject, $limits, $state),
            specLangEvalNonTail($args[1], $env, $subject, $limits, $state),
        );
    }
    if ($op === 'lt' || $op === 'lte' || $op === 'gt' || $op === 'gte') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (!((is_int($left) || is_float($left)) && (is_int($right) || is_float($right)))) {
            throw new SchemaError("spec_lang {$op} expects numeric args");
        }
        if ($op === 'lt') {
            return $left < $right;
        }
        if ($op === 'lte') {
            return $left <= $right;
        }
        if ($op === 'gt') {
            return $left > $right;
        }
        return $left >= $right;
    }
    if ($op === 'xor') {
        specLangRequireArity($op, $args, 2);
        return ((bool)specLangEvalNonTail($args[0], $env, $subject, $limits, $state))
            xor ((bool)specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
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
    if ($op === 'includes') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $needle = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        foreach ($seq as $item) {
            if (specLangDeepEquals($item, $needle)) {
                return true;
            }
        }
        return false;
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
    if ($op === 'get_in') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        [$ok, $value] = specLangGetInPath($obj, $path);
        return $ok ? $value : null;
    }
    if ($op === 'get_or') {
        specLangRequireArity($op, $args, 3);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $defaultValue = specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        [$ok, $value] = specLangGetInPath($obj, $path);
        return $ok ? $value : $defaultValue;
    }
    if ($op === 'has_path') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        [$ok, $_value] = specLangGetInPath($obj, $path);
        return $ok;
    }
    if ($op === 'len' || $op === 'count') {
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
    if ($op === 'first') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        return count($seq) > 0 ? $seq[0] : null;
    }
    if ($op === 'rest') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        return count($seq) > 1 ? array_slice($seq, 1) : [];
    }
    if ($op === 'last') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        return count($seq) > 0 ? $seq[count($seq) - 1] : null;
    }
    if ($op === 'nth') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $idx = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($idx < 0 || $idx >= count($seq)) {
            return null;
        }
        return $seq[$idx];
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
    if ($op === 'split') {
        if (count($args) === 1) {
            $value = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
            $parts = preg_split('/\s+/', trim($value));
            return $parts === false ? [] : array_values(array_filter($parts, static fn($x) => $x !== ''));
        }
        if (count($args) === 2) {
            $value = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
            $sep = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
            return explode($sep, $value);
        }
        throw new SchemaError('spec_lang arity error for split');
    }
    if ($op === 'join') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $sep = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        return implode($sep, array_map(static fn($x) => (string)$x, $seq));
    }
    if ($op === 'json_parse') {
        specLangRequireArity($op, $args, 1);
        $raw = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!is_string($raw)) {
            throw new SchemaError('spec_lang json_parse expects string input');
        }
        try {
            return json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException $e) {
            throw new SchemaError('spec_lang json_parse invalid JSON');
        }
    }
    if ($op === 'json_stringify') {
        specLangRequireArity($op, $args, 1);
        try {
            return json_encode(
                specLangEvalNonTail($args[0], $env, $subject, $limits, $state),
                JSON_THROW_ON_ERROR | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
            );
        } catch (JsonException $e) {
            throw new SchemaError('spec_lang json_stringify invalid value');
        }
    }
    if ($op === 'add' || $op === 'sub' || $op === 'mul' || $op === 'div' || $op === 'pow') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireNumericArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($op === 'add') {
            return $left + $right;
        }
        if ($op === 'sub') {
            return $left - $right;
        }
        if ($op === 'mul') {
            return $left * $right;
        }
        if ($op === 'div') {
            if ($right == 0) {
                throw new SchemaError('spec_lang div expects non-zero divisor');
            }
            return $left / $right;
        }
        return $left ** $right;
    }
    if ($op === 'mod') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($right === 0) {
            throw new SchemaError('spec_lang mod expects non-zero divisor');
        }
        return $left % $right;
    }
    if ($op === 'abs' || $op === 'negate' || $op === 'inc' || $op === 'dec' || $op === 'round' || $op === 'floor' || $op === 'ceil') {
        specLangRequireArity($op, $args, 1);
        $value = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($op === 'abs') {
            return abs($value);
        }
        if ($op === 'negate') {
            return -$value;
        }
        if ($op === 'inc') {
            return $value + 1;
        }
        if ($op === 'dec') {
            return $value - 1;
        }
        if ($op === 'round') {
            return specLangRoundHalfAwayFromZero($value);
        }
        if ($op === 'floor') {
            return (int)floor((float)$value);
        }
        return (int)ceil((float)$value);
    }
    if ($op === 'clamp' || $op === 'between') {
        specLangRequireArity($op, $args, 3);
        $low = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $high = specLangRequireNumericArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $value = specLangRequireNumericArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        if ($low > $high) {
            throw new SchemaError("spec_lang {$op} expects low <= high");
        }
        if ($op === 'clamp') {
            return min(max($value, $low), $high);
        }
        return $value >= $low && $value <= $high;
    }
    if ($op === 'sum') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $total = 0.0;
        $sawFloat = false;
        foreach ($seq as $item) {
            if (!is_int($item) && !is_float($item)) {
                throw new SchemaError('spec_lang sum expects numeric list values');
            }
            if (is_float($item)) {
                $sawFloat = true;
            }
            $total += (float)$item;
        }
        return $sawFloat ? $total : (int)$total;
    }
    if ($op === 'min' || $op === 'max') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($seq === []) {
            throw new SchemaError("spec_lang {$op} expects non-empty list");
        }
        return $op === 'min' ? min($seq) : max($seq);
    }
    if ($op === 'compare') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ((is_int($left) || is_float($left)) && (is_int($right) || is_float($right))) {
            return $left <=> $right;
        }
        if (is_string($left) && is_string($right)) {
            return $left <=> $right;
        }
        throw new SchemaError('spec_lang compare expects both args to be numbers or strings');
    }
    if ($op === 'range') {
        specLangRequireArity($op, $args, 2);
        $start = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $end = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $out = [];
        for ($i = $start; $i < $end; $i++) {
            $out[] = $i;
        }
        return $out;
    }
    if ($op === 'any' || $op === 'all' || $op === 'none') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $truthy = static fn($v) => (bool)$v;
        if ($op === 'any') {
            foreach ($seq as $item) {
                if ($truthy($item)) {
                    return true;
                }
            }
            return false;
        }
        if ($op === 'all') {
            foreach ($seq as $item) {
                if (!$truthy($item)) {
                    return false;
                }
            }
            return true;
        }
        foreach ($seq as $item) {
            if ($truthy($item)) {
                return false;
            }
        }
        return true;
    }
    if ($op === 'is_empty') {
        specLangRequireArity($op, $args, 1);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (is_string($value)) {
            return $value === '';
        }
        if (is_array($value)) {
            return count($value) === 0;
        }
        throw new SchemaError('spec_lang is_empty expects list/dict/string');
    }
    if ($op === 'distinct') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        return specLangDistinctDeep($seq);
    }
    if ($op === 'sort') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($seq === []) {
            return [];
        }
        $firstType = gettype($seq[0]);
        if (!in_array($firstType, ['string', 'integer', 'double', 'boolean'], true)) {
            throw new SchemaError('spec_lang sort expects scalar list values');
        }
        foreach ($seq as $item) {
            if (gettype($item) !== $firstType) {
                throw new SchemaError('spec_lang sort expects homogeneous list element types');
            }
        }
        $out = $seq;
        sort($out);
        return array_values($out);
    }
    if ($op === 'coalesce') {
        specLangRequireMinArity($op, $args, 1);
        foreach ($args as $arg) {
            $value = specLangEvalNonTail($arg, $env, $subject, $limits, $state);
            if ($value === null || (is_string($value) && $value === '')) {
                continue;
            }
            return $value;
        }
        return null;
    }
    if ($op === 'default_to') {
        specLangRequireArity($op, $args, 2);
        $defaultValue = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $value = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ($value === null || (is_string($value) && $value === '')) {
            return $defaultValue;
        }
        return $value;
    }
    if ($op === 'repeat') {
        specLangRequireArity($op, $args, 2);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $count = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($count < 0) {
            throw new SchemaError('spec_lang repeat expects non-negative count');
        }
        return array_fill(0, $count, $value);
    }
    if ($op === 'take' || $op === 'drop') {
        specLangRequireArity($op, $args, 2);
        $n = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($op === 'take') {
            return array_slice($seq, 0, max($n, 0));
        }
        return array_slice($seq, max($n, 0));
    }
    if ($op === 'slice') {
        specLangRequireArity($op, $args, 3);
        $start = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $end = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        return array_slice($seq, $start, max(0, $end - $start));
    }
    if ($op === 'reverse') {
        specLangRequireArity($op, $args, 1);
        return array_values(array_reverse(specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state))));
    }
    if ($op === 'flatten') {
        specLangRequireArity($op, $args, 1);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $out = [];
        $flatten = static function(array $xs, array &$acc) use (&$flatten): void {
            foreach ($xs as $item) {
                if (is_array($item) && isListArray($item)) {
                    $flatten($item, $acc);
                } else {
                    $acc[] = $item;
                }
            }
        };
        $flatten($seq, $out);
        return $out;
    }
    if ($op === 'zip') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $n = min(count($left), count($right));
        $out = [];
        for ($i = 0; $i < $n; $i++) {
            $out[] = [$left[$i], $right[$i]];
        }
        return $out;
    }
    if ($op === 'concat') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        return array_values(array_merge($left, $right));
    }
    if ($op === 'append') {
        specLangRequireArity($op, $args, 2);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $seq[] = $value;
        return array_values($seq);
    }
    if ($op === 'prepend') {
        specLangRequireArity($op, $args, 2);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        array_unshift($seq, $value);
        return array_values($seq);
    }
    if ($op === 'union' || $op === 'intersection' || $op === 'difference' || $op === 'symmetric_difference') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($op === 'union') {
            return specLangDistinctDeep(array_values(array_merge($left, $right)));
        }
        if ($op === 'intersection') {
            $out = [];
            foreach ($left as $item) {
                if (specLangIncludesDeep($right, $item) && !specLangIncludesDeep($out, $item)) {
                    $out[] = $item;
                }
            }
            return $out;
        }
        if ($op === 'difference') {
            $out = [];
            foreach ($left as $item) {
                if (!specLangIncludesDeep($right, $item) && !specLangIncludesDeep($out, $item)) {
                    $out[] = $item;
                }
            }
            return $out;
        }
        $out = [];
        foreach ($left as $item) {
            if (!specLangIncludesDeep($right, $item) && !specLangIncludesDeep($out, $item)) {
                $out[] = $item;
            }
        }
        foreach ($right as $item) {
            if (!specLangIncludesDeep($left, $item) && !specLangIncludesDeep($out, $item)) {
                $out[] = $item;
            }
        }
        return $out;
    }
    if ($op === 'set_equals' || $op === 'is_subset' || $op === 'is_superset') {
        specLangRequireArity($op, $args, 2);
        $left = specLangDistinctDeep(specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state)));
        $right = specLangDistinctDeep(specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state)));
        if ($op === 'set_equals') {
            if (count($left) !== count($right)) {
                return false;
            }
            foreach ($left as $item) {
                if (!specLangIncludesDeep($right, $item)) {
                    return false;
                }
            }
            return true;
        }
        if ($op === 'is_subset') {
            foreach ($left as $item) {
                if (!specLangIncludesDeep($right, $item)) {
                    return false;
                }
            }
            return true;
        }
        foreach ($right as $item) {
            if (!specLangIncludesDeep($left, $item)) {
                return false;
            }
        }
        return true;
    }
    if ($op === 'contains_all' || $op === 'contains_any') {
        specLangRequireArity($op, $args, 2);
        $container = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $needles = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($op === 'contains_all') {
            foreach ($needles as $item) {
                if (!specLangIncludesDeep($container, $item)) {
                    return false;
                }
            }
            return true;
        }
        foreach ($needles as $item) {
            if (specLangIncludesDeep($container, $item)) {
                return true;
            }
        }
        return false;
    }
    if ($op === 'replace') {
        specLangRequireArity($op, $args, 3);
        $text = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $old = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $new = (string)specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        return str_replace($old, $new, $text);
    }
    if ($op === 'matches_all') {
        specLangRequireArity($op, $args, 2);
        $hay = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $patterns = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        foreach ($patterns as $pattern) {
            $ok = @preg_match('/' . str_replace('/', '\\/', (string)$pattern) . '/u', $hay);
            if ($ok === false) {
                throw new SchemaError("invalid regex pattern: {$pattern}");
            }
            if ($ok !== 1) {
                return false;
            }
        }
        return true;
    }
    if ($op === 'pad_left' || $op === 'pad_right') {
        specLangRequireArity($op, $args, 3);
        $text = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $width = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $fill = (string)specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        if ($fill === '') {
            throw new SchemaError("spec_lang {$op} expects non-empty pad string");
        }
        if ($op === 'pad_left') {
            while (strlen($text) < $width) {
                $text = $fill . $text;
            }
            return $width > 0 ? substr($text, -$width) : '';
        }
        while (strlen($text) < $width) {
            $text .= $fill;
        }
        return $width > 0 ? substr($text, 0, $width) : '';
    }
    if ($op === 'identity') {
        specLangRequireArity($op, $args, 1);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
    }
    if ($op === 'always') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
    }
    if ($op === 'keys') {
        specLangRequireArity($op, $args, 1);
        return array_values(array_keys(specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state))));
    }
    if ($op === 'values') {
        specLangRequireArity($op, $args, 1);
        return array_values(specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state)));
    }
    if ($op === 'entries') {
        specLangRequireArity($op, $args, 1);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $out = [];
        foreach ($obj as $k => $v) {
            $out[] = [(string)$k, $v];
        }
        return $out;
    }
    if ($op === 'pluck') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $key = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $out = [];
        foreach ($seq as $item) {
            if (is_array($item) && !isListArray($item)) {
                $out[] = $item[$key] ?? null;
            } else {
                $out[] = null;
            }
        }
        return $out;
    }
    if ($op === 'merge') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        return array_merge($left, $right);
    }
    if ($op === 'merge_deep') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        return specLangDeepMergeDicts($left, $right);
    }
    if ($op === 'assoc') {
        specLangRequireArity($op, $args, 3);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $value = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $obj[$key] = $value;
        return $obj;
    }
    if ($op === 'dissoc') {
        specLangRequireArity($op, $args, 2);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        unset($obj[$key]);
        return $obj;
    }
    if ($op === 'pick' || $op === 'omit') {
        specLangRequireArity($op, $args, 2);
        $keys = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $set = [];
        foreach ($keys as $k) {
            $set[(string)$k] = true;
        }
        $out = [];
        foreach ($obj as $k => $v) {
            $has = array_key_exists((string)$k, $set);
            if (($op === 'pick' && $has) || ($op === 'omit' && !$has)) {
                $out[(string)$k] = $v;
            }
        }
        return $out;
    }
    if ($op === 'keys_exact' || $op === 'keys_include' || $op === 'keys_exclude') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $keys = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $objSet = [];
        foreach (array_keys($obj) as $k) {
            $objSet[(string)$k] = true;
        }
        $otherSet = [];
        foreach ($keys as $k) {
            $otherSet[(string)$k] = true;
        }
        if ($op === 'keys_exact') {
            return count(array_diff_key($objSet, $otherSet)) === 0
                && count(array_diff_key($otherSet, $objSet)) === 0;
        }
        if ($op === 'keys_include') {
            return count(array_diff_key($otherSet, $objSet)) === 0;
        }
        return count(array_intersect_key($objSet, $otherSet)) === 0;
    }
    if ($op === 'prop_eq') {
        specLangRequireArity($op, $args, 3);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $expected = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $actual = $obj[$key] ?? null;
        return specLangDeepEquals($actual, $expected);
    }
    if ($op === 'map' || $op === 'filter' || $op === 'reject' || $op === 'find' || $op === 'partition' || $op === 'group_by' || $op === 'uniq_by') {
        specLangRequireArity($op, $args, 2);
        $fn = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!specLangIsClosure($fn)) {
            throw new SchemaError("spec_lang {$op} expects fn closure");
        }
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $params = $fn['params'];
        if (count($params) !== 1) {
            throw new SchemaError("spec_lang {$op} closure must accept one argument");
        }
        $applyOne = static function(mixed $item) use ($fn, $subject, $limits, &$state, $params): mixed {
            $vars = [(string)$params[0] => $item];
            return specLangEvalTail($fn['body'], new SpecLangEnv($vars, $fn['env']), $subject, $limits, $state);
        };
        if ($op === 'map') {
            $out = [];
            foreach ($seq as $item) {
                $out[] = $applyOne($item);
            }
            return $out;
        }
        if ($op === 'filter') {
            $out = [];
            foreach ($seq as $item) {
                if ((bool)$applyOne($item)) {
                    $out[] = $item;
                }
            }
            return $out;
        }
        if ($op === 'reject') {
            $out = [];
            foreach ($seq as $item) {
                if (!((bool)$applyOne($item))) {
                    $out[] = $item;
                }
            }
            return $out;
        }
        if ($op === 'find') {
            foreach ($seq as $item) {
                if ((bool)$applyOne($item)) {
                    return $item;
                }
            }
            return null;
        }
        if ($op === 'partition') {
            $yes = [];
            $no = [];
            foreach ($seq as $item) {
                if ((bool)$applyOne($item)) {
                    $yes[] = $item;
                } else {
                    $no[] = $item;
                }
            }
            return [$yes, $no];
        }
        if ($op === 'group_by') {
            $grouped = [];
            foreach ($seq as $item) {
                $key = (string)$applyOne($item);
                if (!array_key_exists($key, $grouped)) {
                    $grouped[$key] = [];
                }
                $grouped[$key][] = $item;
            }
            return $grouped;
        }
        $out = [];
        $seen = [];
        foreach ($seq as $item) {
            $marker = $applyOne($item);
            if (!specLangIncludesDeep($seen, $marker)) {
                $seen[] = $marker;
                $out[] = $item;
            }
        }
        return $out;
    }
    if ($op === 'reduce') {
        specLangRequireArity($op, $args, 3);
        $fn = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!specLangIsClosure($fn)) {
            throw new SchemaError('spec_lang reduce expects fn closure');
        }
        $params = $fn['params'];
        if (count($params) !== 2) {
            throw new SchemaError('spec_lang reduce closure must accept two arguments');
        }
        $acc = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        foreach ($seq as $item) {
            $vars = [(string)$params[0] => $acc, (string)$params[1] => $item];
            $acc = specLangEvalTail($fn['body'], new SpecLangEnv($vars, $fn['env']), $subject, $limits, $state);
        }
        return $acc;
    }
    if ($op === 'sort_by') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $key = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $out = array_values($seq);
        usort($out, function($a, $b) use ($key, $subject, $limits, &$state): int {
            if (is_string($key)) {
                $ka = is_array($a) && !isListArray($a) ? (string)($a[$key] ?? '') : (string)$a;
                $kb = is_array($b) && !isListArray($b) ? (string)($b[$key] ?? '') : (string)$b;
                return $ka <=> $kb;
            }
            if (!specLangIsClosure($key)) {
                throw new SchemaError('spec_lang sort_by expects string key or fn closure');
            }
            $params = $key['params'];
            if (count($params) !== 1) {
                throw new SchemaError('spec_lang sort_by closure must accept one argument');
            }
            $varA = [(string)$params[0] => $a];
            $varB = [(string)$params[0] => $b];
            $ka = specLangEvalTail($key['body'], new SpecLangEnv($varA, $key['env']), $subject, $limits, $state);
            $kb = specLangEvalTail($key['body'], new SpecLangEnv($varB, $key['env']), $subject, $limits, $state);
            return ($ka <=> $kb);
        });
        return $out;
    }
    if ($op === 'where') {
        specLangRequireArity($op, $args, 2);
        $spec = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        foreach ($spec as $k => $pred) {
            $actual = $obj[(string)$k] ?? null;
            if (specLangIsClosure($pred)) {
                if (count($pred['params']) !== 1) {
                    throw new SchemaError('spec_lang where callable predicate must accept one argument');
                }
                $vars = [(string)$pred['params'][0] => $actual];
                $predicateValue = specLangEvalTail($pred['body'], new SpecLangEnv($vars, $pred['env']), $subject, $limits, $state);
                if (!((bool)$predicateValue)) {
                    return false;
                }
            } else {
                if (!specLangDeepEquals($actual, $pred)) {
                    return false;
                }
            }
        }
        return true;
    }
    if ($op === 'compose' || $op === 'pipe') {
        specLangRequireArity($op, $args, 3);
        $f = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $g = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $x = specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        if (!specLangIsClosure($f) || !specLangIsClosure($g)) {
            throw new SchemaError("spec_lang {$op} expects fn closures");
        }
        $applyOne = static function(array $closure, mixed $arg, mixed $subject, array $limits, array &$state): mixed {
            $params = $closure['params'];
            if (count($params) !== 1) {
                throw new SchemaError('spec_lang compose/pipe closures must accept one argument');
            }
            $vars = [(string)$params[0] => $arg];
            return specLangEvalTail($closure['body'], new SpecLangEnv($vars, $closure['env']), $subject, $limits, $state);
        };
        if ($op === 'compose') {
            return $applyOne($f, $applyOne($g, $x, $subject, $limits, $state), $subject, $limits, $state);
        }
        return $applyOne($g, $applyOne($f, $x, $subject, $limits, $state), $subject, $limits, $state);
    }
    if ($op === 'zip_with') {
        specLangRequireArity($op, $args, 3);
        $fn = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!specLangIsClosure($fn)) {
            throw new SchemaError('spec_lang zip_with expects fn closure');
        }
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $params = $fn['params'];
        if (count($params) !== 2) {
            throw new SchemaError('spec_lang zip_with closure must accept two arguments');
        }
        $n = min(count($left), count($right));
        $out = [];
        for ($i = 0; $i < $n; $i++) {
            $vars = [(string)$params[0] => $left[$i], (string)$params[1] => $right[$i]];
            $out[] = specLangEvalTail($fn['body'], new SpecLangEnv($vars, $fn['env']), $subject, $limits, $state);
        }
        return $out;
    }
    if (
        $op === 'ops_fs_path_normalize'
        || $op === 'ops_fs_path_split'
        || $op === 'ops_fs_path_dirname'
        || $op === 'ops_fs_path_basename'
        || $op === 'ops_fs_path_extname'
        || $op === 'ops_fs_path_stem'
        || $op === 'ops_fs_path_is_abs'
        || $op === 'ops_fs_path_common_prefix'
    ) {
        specLangRequireArity($op, $args, 1);
        $arg = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if ($op === 'ops_fs_path_common_prefix') {
            $paths = specLangRequireListArg($op, $arg);
            return specLangFsCommonPrefix($paths);
        }
        $path = $arg;
        if (!is_string($path)) {
            throw new SchemaError("spec_lang {$op} expects string path");
        }
        if ($op === 'ops_fs_path_normalize') {
            return specLangFsNormalizePath($path);
        }
        if ($op === 'ops_fs_path_split') {
            return specLangFsSplitSegments($path);
        }
        if ($op === 'ops_fs_path_dirname') {
            return specLangFsDirname($path);
        }
        if ($op === 'ops_fs_path_basename') {
            return specLangFsBasename($path);
        }
        if ($op === 'ops_fs_path_extname') {
            return specLangFsExtname($path);
        }
        if ($op === 'ops_fs_path_stem') {
            return specLangFsStem($path);
        }
        return str_starts_with(specLangFsNormalizePath($path), '/');
    }
    if (
        $op === 'ops_fs_path_join'
        || $op === 'ops_fs_path_has_ext'
        || $op === 'ops_fs_path_change_ext'
        || $op === 'ops_fs_path_relativize'
    ) {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (!is_string($left) || !is_string($right)) {
            throw new SchemaError("spec_lang {$op} expects string args");
        }
        if ($op === 'ops_fs_path_join') {
            $combined = $left === '' ? $right : rtrim($left, '/') . '/' . $right;
            return specLangFsNormalizePath($combined);
        }
        if ($op === 'ops_fs_path_has_ext') {
            return specLangFsExtname($left) === specLangFsNormalizeExt($right);
        }
        if ($op === 'ops_fs_path_relativize') {
            return specLangFsRelativize($left, $right);
        }
        $normalized = specLangFsNormalizePath($left);
        $base = specLangFsBasename($normalized);
        if ($base === '' || $base === '.') {
            return $normalized;
        }
        $parent = specLangFsDirname($normalized);
        $stem = specLangFsStem($normalized);
        $next = $stem . specLangFsNormalizeExt($right);
        if ($parent === '/') {
            return '/' . $next;
        }
        if ($parent === '.') {
            return $next;
        }
        return $parent . '/' . $next;
    }
    if (
        $op === 'ops_fs_file_exists'
        || $op === 'ops_fs_file_is_file'
        || $op === 'ops_fs_file_is_dir'
        || $op === 'ops_fs_file_size_bytes'
        || $op === 'ops_fs_file_path'
        || $op === 'ops_fs_file_name'
        || $op === 'ops_fs_file_parent'
        || $op === 'ops_fs_file_ext'
    ) {
        specLangRequireArity($op, $args, 1);
        $meta = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($op === 'ops_fs_file_exists') {
            return (bool)($meta['exists'] ?? false);
        }
        if ($op === 'ops_fs_file_is_file') {
            return (string)($meta['type'] ?? '') === 'file';
        }
        if ($op === 'ops_fs_file_is_dir') {
            return (string)($meta['type'] ?? '') === 'dir';
        }
        if ($op === 'ops_fs_file_size_bytes') {
            $size = $meta['size_bytes'] ?? null;
            if (is_int($size)) {
                return $size;
            }
            return null;
        }
        $rawPath = $meta['path'] ?? null;
        if (!is_string($rawPath)) {
            return null;
        }
        if ($op === 'ops_fs_file_path') {
            return $rawPath;
        }
        if ($op === 'ops_fs_file_name') {
            return specLangFsBasename($rawPath);
        }
        if ($op === 'ops_fs_file_parent') {
            return specLangFsDirname($rawPath);
        }
        return specLangFsExtname($rawPath);
    }
    if ($op === 'ops_fs_file_get') {
        specLangRequireArity($op, $args, 3);
        $meta = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $key = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $default = specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        return array_key_exists($key, $meta) ? $meta[$key] : $default;
    }
    if ($op === 'ops_fs_json_parse') {
        specLangRequireArity($op, $args, 1);
        $raw = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!is_string($raw)) {
            throw new SchemaError('spec_lang ops.fs.json.parse expects string input');
        }
        try {
            return json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException $e) {
            throw new SchemaError('spec_lang ops.fs.json.parse invalid JSON');
        }
    }
    if ($op === 'ops_fs_json_get') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        [$ok, $value] = specLangGetInPath($obj, $path);
        return $ok ? $value : null;
    }
    if ($op === 'ops_fs_json_get_or') {
        specLangRequireArity($op, $args, 3);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $default = specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        [$ok, $value] = specLangGetInPath($obj, $path);
        return $ok ? $value : $default;
    }
    if ($op === 'ops_fs_json_has_path') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $path = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        [$ok, $_value] = specLangGetInPath($obj, $path);
        return $ok;
    }
    if ($op === 'ops_fs_glob_match') {
        specLangRequireArity($op, $args, 2);
        $path = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $pattern = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (!is_string($path) || !is_string($pattern)) {
            throw new SchemaError('spec_lang ops.fs.glob.match expects string args');
        }
        return fnmatch($pattern, $path);
    }
    if ($op === 'ops_fs_glob_filter' || $op === 'ops_fs_glob_any' || $op === 'ops_fs_glob_all') {
        specLangRequireArity($op, $args, 2);
        $paths = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $pattern = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (!is_string($pattern)) {
            throw new SchemaError("spec_lang {$op} expects string pattern");
        }
        $matched = [];
        foreach ($paths as $raw) {
            if (!is_string($raw)) {
                throw new SchemaError("spec_lang {$op} expects list of strings");
            }
            if (fnmatch($pattern, $raw)) {
                $matched[] = $raw;
            }
        }
        if ($op === 'ops_fs_glob_filter') {
            return $matched;
        }
        if ($op === 'ops_fs_glob_any') {
            return count($matched) > 0;
        }
        return count($matched) === count($paths);
    }
    if ($op === 'schema_match' || $op === 'schema_errors') {
        specLangRequireArity($op, $args, 2);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $schema = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $errs = [];
        specLangSchemaValidate($value, $schema, '$', $errs);
        return $op === 'schema_match' ? ($errs === []) : $errs;
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
        if (is_array($currentExpr) && !isListArray($currentExpr)) {
            $out = [];
            foreach ($currentExpr as $k => $v) {
                $out[(string)$k] = specLangEvalNonTail($v, $currentEnv, $subject, $limits, $state);
            }
            return $out;
        }
        if (!is_array($currentExpr) || !isListArray($currentExpr)) {
            throw new SchemaError('spec_lang expression must be list-based s-expr or scalar literal');
        }
        if (count($currentExpr) === 0) {
            throw new SchemaError('spec_lang expression list must not be empty');
        }
        $head = $currentExpr[0];
        if (!is_string($head)) {
            $out = [];
            foreach ($currentExpr as $item) {
                $out[] = specLangEvalNonTail($item, $currentEnv, $subject, $limits, $state);
            }
            return $out;
        }
        if (trim($head) === '') {
            throw new SchemaError('spec_lang expression head must be non-empty string symbol');
        }
        $imports = $state['imports'] ?? [];
        $op = specLangResolveOpSymbol($head, is_array($imports) ? $imports : []);
        $args = array_slice($currentExpr, 1);

        if ($op === 'if') {
            specLangRequireArity($op, $args, 3);
            $cond = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $currentExpr = ((bool)$cond) ? $args[1] : $args[2];
            continue;
        }
        if ($op === 'lit') {
            specLangRequireArity($op, $args, 1);
            return $args[0];
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

function specLangEvalPredicate(
    mixed $expr,
    mixed $subject,
    array $limits,
    array $symbols = [],
    array $imports = [],
): bool {
    specLangValidateExprShape($expr, $limits);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits, 'imports' => $imports];
    $root = [];
    foreach ($symbols as $rawName => $value) {
        $name = trim((string)$rawName);
        if ($name === '') {
            throw new SchemaError('spec_lang symbol name must be non-empty');
        }
        $root[$name] = $value;
    }
    $root['subject'] = $subject;
    $value = specLangEvalTail($expr, new SpecLangEnv($root, null), $subject, $limits, $state);
    return (bool)$value;
}

function compileYamlExprLiteral(mixed $value, string $fieldPath): mixed {
    if (is_array($value)) {
        if (isListArray($value)) {
            $out = [];
            foreach ($value as $idx => $item) {
                $out[] = compileYamlExprLiteral($item, "{$fieldPath}[{$idx}]");
            }
            return $out;
        }
        $out = [];
        foreach ($value as $k => $v) {
            $out[(string)$k] = compileYamlExprLiteral($v, "{$fieldPath}." . (string)$k);
        }
        return $out;
    }
    if (is_string($value) || is_int($value) || is_float($value) || is_bool($value) || $value === null) {
        return $value;
    }
    throw new SchemaError("{$fieldPath}: unsupported literal value type");
}

function compileYamlExprToSexpr(mixed $node, string $fieldPath): mixed {
    if (is_string($node) || is_int($node) || is_float($node) || is_bool($node) || $node === null) {
        return $node;
    }
    if (is_array($node) && isListArray($node)) {
        throw new SchemaError(
            "{$fieldPath}: list expressions are not allowed; use operator-keyed mapping AST and wrap literal lists with lit"
        );
    }
    if (!is_array($node)) {
        throw new SchemaError("{$fieldPath}: expression node must be scalar or mapping");
    }
    $keys = array_keys($node);
    if (count($keys) === 0) {
        throw new SchemaError("{$fieldPath}: expression mapping must not be empty");
    }
    if (array_key_exists('lit', $node)) {
        if (count($keys) !== 1) {
            throw new SchemaError("{$fieldPath}: lit wrapper must be the only key in a mapping");
        }
        return ['lit', compileYamlExprLiteral($node['lit'], "{$fieldPath}.lit")];
    }
    if (count($keys) !== 1) {
        throw new SchemaError("{$fieldPath}: expression mapping must have exactly one operator key");
    }
    $op = trim((string)$keys[0]);
    if ($op === '') {
        throw new SchemaError("{$fieldPath}: operator key must be non-empty");
    }
    $rawArgs = $node[$keys[0]];
    if ($op === 'ref') {
        throw new SchemaError("{$fieldPath}.ref: ref mapping is not supported; use var: subject");
    }
    if ($op === 'var') {
        if (is_array($rawArgs)) {
            throw new SchemaError("{$fieldPath}.var: var list form is not supported; use var: <name>");
        }
        if (!is_string($rawArgs) || trim($rawArgs) === '') {
            throw new SchemaError("{$fieldPath}.var: variable name must be a non-empty string");
        }
        return ['var', trim($rawArgs)];
    }
    if ($op === 'fn') {
        if (!is_array($rawArgs) || !isListArray($rawArgs) || count($rawArgs) !== 2) {
            throw new SchemaError("{$fieldPath}.fn: fn args must be [params, body]");
        }
        $rawParams = $rawArgs[0];
        if (!is_array($rawParams) || !isListArray($rawParams)) {
            throw new SchemaError("{$fieldPath}.fn[0]: params must be a list of variable names");
        }
        $params = [];
        foreach ($rawParams as $idx => $param) {
            if (!is_string($param) || trim($param) === '') {
                throw new SchemaError("{$fieldPath}.fn[0][{$idx}]: param name must be a non-empty string");
            }
            $params[] = trim($param);
        }
        $body = compileYamlExprToSexpr($rawArgs[1], "{$fieldPath}.fn[1]");
        return ['fn', $params, $body];
    }
    if (!is_array($rawArgs) || !isListArray($rawArgs)) {
        throw new SchemaError("{$fieldPath}.{$op}: operator args must be a list");
    }
    $args = [];
    foreach ($rawArgs as $idx => $arg) {
        $args[] = compileYamlExprToSexpr($arg, "{$fieldPath}.{$op}[{$idx}]");
    }
    return array_merge([$op], $args);
}

function asNonEmptyStringList(mixed $value, string $field): array {
    if ($value === null) {
        return [];
    }
    if (!is_array($value) || !isListArray($value)) {
        throw new SchemaError("{$field} must be a list of non-empty strings");
    }
    $out = [];
    foreach ($value as $idx => $item) {
        if (!is_string($item) || trim($item) === '') {
            throw new SchemaError("{$field}[{$idx}] must be a non-empty string");
        }
        $out[] = trim($item);
    }
    return $out;
}

function resolveLibraryPath(string $baseDocPath, string $relPath): string {
    $raw = trim($relPath);
    if ($raw === '') {
        throw new SchemaError('harness.spec_lang.includes item must be non-empty');
    }
    if (str_starts_with($raw, 'external://')) {
        throw new SchemaError('harness.spec_lang.includes external refs are denied by default');
    }
    $resolved = resolveContractPath($baseDocPath, $raw, 'harness.spec_lang.includes');
    if (!is_file($resolved)) {
        throw new SchemaError("library path does not exist: {$relPath}");
    }
    return $resolved;
}

function loadSpecLangLibraryDoc(string $path): array {
    $imports = [];
    $bindings = [];
    $exports = [];
    foreach (parseCases($path) as $case) {
        $type = trim((string)($case['type'] ?? ''));
        if ($type !== 'spec.export') {
            continue;
        }
        foreach (asNonEmptyStringList($case['imports'] ?? null, 'imports') as $imp) {
            $imports[] = $imp;
        }
        $rawAssert = $case['assert'] ?? null;
        $assertSteps = [];
        if (is_array($rawAssert) && isListArray($rawAssert)) {
            foreach ($rawAssert as $step) {
                if (!is_array($step) || isListArray($step)) {
                    continue;
                }
                $sid = trim((string)($step['id'] ?? ''));
                if ($sid !== '') {
                    $assertSteps[$sid] = $step;
                }
            }
        }
        $harness = $case['harness'] ?? null;
        $chain = (is_array($harness) && !isListArray($harness)) ? ($harness['chain'] ?? null) : null;
        $producerExports = (is_array($chain) && !isListArray($chain)) ? ($chain['exports'] ?? null) : null;
        if (!is_array($producerExports) || !isListArray($producerExports)) {
            continue;
        }
        foreach ($producerExports as $entryIdx => $entryRaw) {
            if (!is_array($entryRaw) || isListArray($entryRaw)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] must be a mapping");
            }
            $name = trim((string)($entryRaw['as'] ?? ''));
            if ($name === '') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].as is required");
            }
            if (array_key_exists($name, $bindings)) {
                continue;
            }
            $fromSource = trim((string)($entryRaw['from'] ?? ''));
            if ($fromSource !== 'assert.function') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].from must be assert.function");
            }
            $stepId = ltrim(trim((string)($entryRaw['path'] ?? '')), '/');
            if ($stepId === '') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].path is required for from=assert.function");
            }
            if (!array_key_exists($stepId, $assertSteps)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] unresolved assert step id: {$stepId}");
            }
            $srcStep = $assertSteps[$stepId];
            if (trim((string)($srcStep['class'] ?? '')) !== 'must') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] source assert step must use class=must");
            }
            $checks = $srcStep['checks'] ?? null;
            if (!is_array($checks) || !isListArray($checks) || count($checks) === 0) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] source assert step requires non-empty checks");
            }
            $paramsRaw = $entryRaw['params'] ?? null;
            if (!is_array($paramsRaw) || !isListArray($paramsRaw)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].params must be a list");
            }
            $params = [];
            foreach ($paramsRaw as $pIdx => $rawParam) {
                if (!is_string($rawParam) || trim($rawParam) === '') {
                    throw new SchemaError("harness.chain.exports[{$entryIdx}].params[{$pIdx}] must be non-empty string");
                }
                $params[] = trim($rawParam);
            }
            $exprs = [];
            foreach ($checks as $cIdx => $rawCheck) {
                $exprs[] = compileYamlExprToSexpr($rawCheck, "{$path} harness.chain.exports[{$entryIdx}].checks[{$cIdx}]");
            }
            $body = $exprs[count($exprs) - 1];
            for ($i = count($exprs) - 2; $i >= 0; $i -= 1) {
                $body = ['std.logic.and', $exprs[$i], $body];
            }
            $bindings[$name] = ['fn', $params, $body];
            $exports[] = $name;
        }
    }
    if (count($bindings) === 0) {
        throw new SchemaError("library file has no spec.export chain exports: {$path}");
    }
    return [
        'path' => $path,
        'imports' => array_values(array_unique($imports)),
        'bindings' => $bindings,
        'exports' => array_values(array_unique($exports)),
    ];
}

function resolveSpecLangLibraryGraph(array $entryDocs): array {
    $docs = [];
    $visiting = [];
    $visited = [];
    $ordered = [];
    $dfs = function(string $path) use (&$dfs, &$docs, &$visiting, &$visited, &$ordered): void {
        if (($visited[$path] ?? false) === true) {
            return;
        }
        if (($visiting[$path] ?? false) === true) {
            throw new SchemaError("library import cycle detected at: {$path}");
        }
        $visiting[$path] = true;
        if (!array_key_exists($path, $docs)) {
            $docs[$path] = loadSpecLangLibraryDoc($path);
        }
        foreach ($docs[$path]['imports'] as $rel) {
            $dep = resolveLibraryPath($path, (string)$rel);
            $dfs($dep);
        }
        unset($visiting[$path]);
        $visited[$path] = true;
        $ordered[] = $path;
    };
    foreach ($entryDocs as $entry) {
        $dfs((string)$entry);
    }
    $out = [];
    foreach ($ordered as $path) {
        $out[] = $docs[$path];
    }
    return $out;
}

function compileSpecLangSymbolBindings(array $bindings, array $limits): array {
    $slots = [];
    foreach ($bindings as $rawName => $_expr) {
        $name = trim((string)$rawName);
        if ($name === '') {
            throw new SchemaError('spec_lang symbol binding name must be non-empty');
        }
        if (array_key_exists($name, $slots)) {
            throw new SchemaError("duplicate symbol binding: {$name}");
        }
        $slots[$name] = specLangUnsetSentinel();
    }
    $env = new SpecLangEnv($slots, null);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits];
    foreach ($bindings as $rawName => $rawExpr) {
        $name = trim((string)$rawName);
        specLangValidateExprShape($rawExpr, $limits);
        $env->vars[$name] = specLangEvalNonTail($rawExpr, $env, null, $limits, $state);
    }
    return $env->vars;
}

function loadSpecLangSymbolsFromEntryDocs(array $entryDocs, array $limits): array {
    $graph = resolveSpecLangLibraryGraph($entryDocs);

    $mergedBindings = [];
    $exportAllow = [];
    foreach ($graph as $doc) {
        foreach ($doc['bindings'] as $name => $expr) {
            if (array_key_exists($name, $mergedBindings)) {
                throw new SchemaError("duplicate exported library symbol across imports: {$name}");
            }
            $mergedBindings[$name] = $expr;
        }
        foreach ($doc['exports'] as $name) {
            $exportAllow[(string)$name] = true;
        }
    }

    $compiled = compileSpecLangSymbolBindings($mergedBindings, $limits);
    if (count($exportAllow) > 0) {
        $filtered = [];
        foreach ($exportAllow as $name => $_true) {
            $filtered[$name] = $compiled[$name];
        }
        return $filtered;
    }

    return $compiled;
}

function loadSpecLangSymbolsForCase(string $fixturePath, array $case, array $limits): array {
    $harness = $case['harness'] ?? [];
    if (!is_array($harness) || isListArray($harness)) {
        return [];
    }
    if (!array_key_exists('spec_lang', $harness) || $harness['spec_lang'] === null) {
        return [];
    }
    $cfg = $harness['spec_lang'];
    if (!is_array($cfg) || isListArray($cfg)) {
        throw new SchemaError('harness.spec_lang must be a mapping');
    }
    $libPaths = asNonEmptyStringList($cfg['includes'] ?? null, 'harness.spec_lang.includes');
    if (count($libPaths) > 0) {
        throw new SchemaError(
            'harness.spec_lang.includes is not supported for executable cases; use harness.chain imports'
        );
    }
    $consumerExports = asNonEmptyStringList($cfg['exports'] ?? null, 'harness.spec_lang.exports');
    if (count($consumerExports) > 0) {
        throw new SchemaError(
            'harness.spec_lang.exports is not supported for executable cases; use harness.chain imports'
        );
    }

    return [];
}

function compileAssertionLeafExpr(array $leaf, string $path): array {
    if (array_key_exists('evaluate', $leaf)) {
        throw new SchemaError('explicit evaluate leaf is not supported; use expression mapping directly');
    }
    if (count($leaf) === 0) {
        throw new SchemaError('assertion leaf must be a non-empty expression mapping');
    }
    $compiled = compileYamlExprToSexpr($leaf, $path);
    if (!is_array($compiled) || !isListArray($compiled)) {
        throw new SchemaError('assertion expression must compile to a list-based s-expr');
    }
    return $compiled;
}

function assertLeafPredicate(
    string $caseId,
    string $path,
    string $target,
    string $op,
    mixed $expr,
    mixed $subject,
    array $specLangLimits,
    array $specLangSymbols = [],
    array $specLangImports = []
): void {
    if (!specLangEvalPredicate($expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports)) {
        $msg = $op === 'evaluate' ? 'evaluate assertion failed' : "{$op} assertion failed";
        throw new AssertionFailure(
            "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] {$msg}"
        );
    }
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
    $stepClass = trim((string)($node['class'] ?? ''));
    if (in_array($stepClass, ['must', 'can', 'cannot'], true) && array_key_exists('checks', $node)) {
        $stepId = trim((string)($node['id'] ?? ''));
        if ($stepId === '') {
            throw new SchemaError("{$path}.id must be a non-empty string");
        }
        $extra = array_diff(array_keys($node), ['id', 'class', 'target', 'checks']);
        if (count($extra) > 0) {
            throw new SchemaError('unknown key in assert step: ' . (string)array_values($extra)[0]);
        }
        $target = trim((string)($node['target'] ?? ''));
        if ($target === '') {
            $target = $inheritedTarget ?? '';
        }
        $children = $node['checks'];
        if (!is_array($children) || !isListArray($children)) {
            throw new SchemaError('assert step checks must be a list');
        }
        if (count($children) === 0) {
            throw new SchemaError('assert step checks must not be empty');
        }
        $stepPath = $path;
        if ($stepClass === 'must') {
            foreach ($children as $i => $child) {
                evalAssertNode($child, $target, $caseId, "{$stepPath}.checks[{$i}]", $evalLeaf);
            }
            return;
        }
        if ($stepClass === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalAssertNode($child, $target, $caseId, "{$stepPath}.checks[{$i}]", $evalLeaf);
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
        $passed = 0;
        foreach ($children as $i => $child) {
            try {
                evalAssertNode($child, $target, $caseId, "{$stepPath}.checks[{$i}]", $evalLeaf);
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

function evalTextLeaf(
    array $leaf,
    string $subject,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    if ($target !== 'text') {
        throw new SchemaError('unknown assert target for text.file');
    }
    $expr = compileAssertionLeafExpr($leaf, $path);
    assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
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

function evalCliLeaf(
    array $leaf,
    array $captured,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    $expr = compileAssertionLeafExpr($leaf, $path);
    if ($target === 'stdout' || $target === 'stderr') {
        $subject = $target === 'stdout' ? (string)$captured['stdout'] : (string)$captured['stderr'];
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'stdout_path') {
        $line = firstNonEmptyLine((string)$captured['stdout']);
        $subject = $line === null ? '' : $line;
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'stdout_path_text') {
        $line = firstNonEmptyLine((string)$captured['stdout']);
        if ($line === null) {
            throw new AssertionFailure(
                "[case_id={$caseId} assert_path={$path} target={$target} op=evaluate] expected stdout to contain a path"
            );
        }
        $loaded = file_get_contents($line);
        if ($loaded === false) {
            throw new AssertionFailure(
                "[case_id={$caseId} assert_path={$path} target={$target} op=evaluate] cannot read stdout path"
            );
        }
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $loaded, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    throw new SchemaError("unknown assert target: {$target}");
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
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangImports = specLangCompileImportsForCase($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
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
            $path,
            $specLangLimits,
            $specLangSymbols,
            $specLangImports
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

function evaluateCliRunCase(string $fixturePath, array $case): array {
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
    $supportedHarnessKeys = ['entrypoint', 'env', 'spec_lang'];
    foreach (array_keys($h) as $k) {
        if (!in_array((string)$k, $supportedHarnessKeys, true)) {
            throw new SchemaError("unsupported harness key(s): {$k}");
        }
    }

    $entrypoint = trim((string)($h['entrypoint'] ?? ''));
    if ($entrypoint === '') {
        throw new RuntimeException('cli.run requires explicit harness.entrypoint');
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
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangImports = specLangCompileImportsForCase($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
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
            $path,
            $specLangLimits,
            $specLangSymbols,
            $specLangImports
        )
    );

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
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    $candidate = resolveContractPath($docAbs, $trim, 'api.http request.url');
    return ['source_type' => 'file', 'path' => $candidate];
}

function resolveApiHttpMode(array $case): string {
    $harness = $case['harness'] ?? null;
    if (!is_array($harness)) {
        return 'deterministic';
    }
    $apiHttp = $harness['api_http'] ?? null;
    if (!is_array($apiHttp)) {
        return 'deterministic';
    }
    $mode = trim((string)($apiHttp['mode'] ?? 'deterministic'));
    if ($mode === '') {
        $mode = 'deterministic';
    }
    if ($mode !== 'deterministic' && $mode !== 'live') {
        throw new SchemaError("api.http mode must be one of: deterministic, live");
    }
    return $mode;
}

function parseApiHttpOAuthConfig(string $fixturePath, array $case, string $mode): ?array {
    $harness = $case['harness'] ?? null;
    if (!is_array($harness)) {
        return null;
    }
    $apiHttp = $harness['api_http'] ?? null;
    if (!is_array($apiHttp)) {
        return null;
    }
    $auth = $apiHttp['auth'] ?? null;
    if ($auth === null) {
        return null;
    }
    if (!is_array($auth)) {
        throw new SchemaError('api.http harness.auth must be a mapping');
    }
    $oauth = $auth['oauth'] ?? null;
    if ($oauth === null) {
        return null;
    }
    if (!is_array($oauth)) {
        throw new SchemaError('api.http harness.auth.oauth must be a mapping');
    }

    $grantType = trim((string)($oauth['grant_type'] ?? ''));
    if ($grantType !== 'client_credentials') {
        throw new SchemaError('api.http oauth grant_type must be client_credentials');
    }
    $tokenUrl = trim((string)($oauth['token_url'] ?? ''));
    if ($tokenUrl === '') {
        throw new SchemaError('api.http oauth token_url is required');
    }
    $clientIdEnv = trim((string)($oauth['client_id_env'] ?? ''));
    if ($clientIdEnv === '') {
        throw new SchemaError('api.http oauth client_id_env is required');
    }
    $clientSecretEnv = trim((string)($oauth['client_secret_env'] ?? ''));
    if ($clientSecretEnv === '') {
        throw new SchemaError('api.http oauth client_secret_env is required');
    }
    $authStyle = trim((string)($oauth['auth_style'] ?? 'basic'));
    if ($authStyle === '') {
        $authStyle = 'basic';
    }
    if ($authStyle !== 'basic' && $authStyle !== 'body') {
        throw new SchemaError('api.http oauth auth_style must be one of: basic, body');
    }

    $clientId = getenv($clientIdEnv);
    if ($clientId === false || trim((string)$clientId) === '') {
        throw new SchemaError("oauth env var is required: {$clientIdEnv}");
    }
    $clientSecret = getenv($clientSecretEnv);
    if ($clientSecret === false || trim((string)$clientSecret) === '') {
        throw new SchemaError("oauth env var is required: {$clientSecretEnv}");
    }

    $resolved = resolveApiHttpUrl($fixturePath, $tokenUrl);
    if ($resolved['source_type'] === 'url' && $mode !== 'live') {
        throw new SchemaError('api.http oauth token_url network usage requires harness.api_http.mode=live');
    }

    return [
        'resolved' => $resolved,
        'scope' => isset($oauth['scope']) ? (string)$oauth['scope'] : null,
        'audience' => isset($oauth['audience']) ? (string)$oauth['audience'] : null,
        'auth_style' => $authStyle,
        'token_field' => trim((string)($oauth['token_field'] ?? 'access_token')) ?: 'access_token',
        'client_id' => (string)$clientId,
        'client_secret' => (string)$clientSecret,
    ];
}

function fetchApiHttpOAuthToken(array $cfg): array {
    $started = microtime(true);
    $resolved = $cfg['resolved'];
    $tokenField = (string)$cfg['token_field'];
    if (($resolved['source_type'] ?? '') === 'file') {
        $raw = @file_get_contents((string)$resolved['path']);
        if ($raw === false) {
            throw new RuntimeException('api.http oauth token fetch failed');
        }
        $payload = json_decode((string)$raw, true);
        if (!is_array($payload) || !array_key_exists($tokenField, $payload)) {
            throw new RuntimeException("api.http oauth token response missing field: {$tokenField}");
        }
        $token = trim((string)$payload[$tokenField]);
        if ($token === '') {
            throw new RuntimeException('api.http oauth token response access token is empty');
        }
        return [
            'token' => $token,
            'token_fetch_ms' => (int)round((microtime(true) - $started) * 1000),
            'used_cached_token' => false,
        ];
    }

    $body = ['grant_type' => 'client_credentials'];
    if (isset($cfg['scope']) && $cfg['scope'] !== null && trim((string)$cfg['scope']) !== '') {
        $body['scope'] = (string)$cfg['scope'];
    }
    if (isset($cfg['audience']) && $cfg['audience'] !== null && trim((string)$cfg['audience']) !== '') {
        $body['audience'] = (string)$cfg['audience'];
    }
    if (($cfg['auth_style'] ?? 'basic') === 'body') {
        $body['client_id'] = (string)$cfg['client_id'];
        $body['client_secret'] = (string)$cfg['client_secret'];
    }
    $headers = ['Content-Type: application/x-www-form-urlencoded'];
    if (($cfg['auth_style'] ?? 'basic') === 'basic') {
        $headers[] = 'Authorization: Basic ' . base64_encode((string)$cfg['client_id'] . ':' . (string)$cfg['client_secret']);
    }
    $opts = [
        'http' => [
            'method' => 'POST',
            'header' => implode("\r\n", $headers),
            'content' => http_build_query($body),
            'ignore_errors' => true,
            'timeout' => 10,
        ],
    ];
    $ctx = stream_context_create($opts);
    $raw = @file_get_contents((string)$resolved['url'], false, $ctx);
    if ($raw === false) {
        throw new RuntimeException('api.http oauth token fetch failed');
    }
    $payload = json_decode((string)$raw, true);
    if (!is_array($payload) || !array_key_exists($tokenField, $payload)) {
        throw new RuntimeException("api.http oauth token response missing field: {$tokenField}");
    }
    $token = trim((string)$payload[$tokenField]);
    if ($token === '') {
        throw new RuntimeException('api.http oauth token response access token is empty');
    }
    return [
        'token' => $token,
        'token_fetch_ms' => (int)round((microtime(true) - $started) * 1000),
        'used_cached_token' => false,
    ];
}

function evalApiHttpLeaf(
    array $leaf,
    array $resp,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    $expr = compileAssertionLeafExpr($leaf, $path);
    if ($target === 'status' || $target === 'headers' || $target === 'body_text') {
        $subject = $target === 'status'
            ? (string)$resp['status']
            : ($target === 'headers' ? (string)$resp['headers_text'] : (string)$resp['body_text']);
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'body_json') {
        $parsed = json_decode((string)$resp['body_text'], true);
        if ($parsed === null && trim((string)$resp['body_text']) !== 'null') {
            throw new AssertionFailure(
                "[case_id={$caseId} assert_path={$path} target={$target} op=evaluate] body_json parse failed"
            );
        }
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $parsed, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'context_json') {
        $context = $resp['context_json'] ?? null;
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $context, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    throw new SchemaError("unknown assert target for api.http: {$target}");
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
    $mode = resolveApiHttpMode($case);
    $resolved = resolveApiHttpUrl($fixturePath, (string)$request['url']);
    if ($resolved['source_type'] === 'url' && $mode !== 'live') {
        throw new SchemaError('api.http request.url network usage requires harness.api_http.mode=live');
    }
    $oauthCfg = parseApiHttpOAuthConfig($fixturePath, $case, $mode);
    $headersText = '';
    $status = 200;
    $bodyText = '';
    $oauthMeta = [
        'auth_mode' => $oauthCfg === null ? 'none' : 'oauth',
        'oauth_token_source' => $oauthCfg === null ? 'none' : 'env_ref',
        'token_url_host' => null,
        'scope_requested' => false,
        'token_fetch_ms' => 0,
        'used_cached_token' => false,
    ];
    $headerMap = [];
    $hdrs = $request['headers'] ?? [];
    if ($hdrs !== null && !is_array($hdrs)) {
        throw new SchemaError('api.http request.headers must be a mapping');
    }
    if (is_array($hdrs)) {
        foreach ($hdrs as $k => $v) {
            $headerMap[(string)$k] = (string)$v;
        }
    }
    if ($oauthCfg !== null) {
        $tokenResp = fetchApiHttpOAuthToken($oauthCfg);
        $parts = @parse_url(($oauthCfg['resolved']['source_type'] ?? '') === 'url'
            ? (string)$oauthCfg['resolved']['url']
            : (string)$oauthCfg['resolved']['path']);
        $oauthMeta['token_url_host'] = is_array($parts) && isset($parts['host'])
            ? (string)$parts['host']
            : '';
        $oauthMeta['scope_requested'] = $oauthCfg['scope'] ?? false;
        $oauthMeta['token_fetch_ms'] = (int)$tokenResp['token_fetch_ms'];
        $oauthMeta['used_cached_token'] = (bool)$tokenResp['used_cached_token'];
        if (!array_key_exists('Authorization', $headerMap)) {
            $headerMap['Authorization'] = 'Bearer ' . (string)$tokenResp['token'];
        }
    }

    if ($resolved['source_type'] === 'file') {
        $body = file_get_contents((string)$resolved['path']);
        if ($body === false) {
            throw new RuntimeException("cannot read fixture file: {$resolved['path']}");
        }
        $bodyText = (string)$body;
    } else {
        $headers = [];
        foreach ($headerMap as $k => $v) {
            $headers[] = (string)$k . ': ' . (string)$v;
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

    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangImports = specLangCompileImportsForCase($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalApiHttpLeaf(
            $leaf,
            [
                'status' => $status,
                'headers_text' => $headersText,
                'body_text' => $bodyText,
                'context_json' => [
                    'profile_id' => 'api.http/v1',
                    'profile_version' => 1,
                    'value' => [
                        'status' => $status,
                        'headers' => [],
                        'body_text' => $bodyText,
                        'body_json' => json_decode((string)$bodyText, true),
                    ],
                    'meta' => [
                        'auth_mode' => $oauthMeta['auth_mode'],
                        'oauth_token_source' => $oauthMeta['oauth_token_source'],
                    ],
                    'context' => [
                        'oauth' => [
                            'token_url_host' => $oauthMeta['token_url_host'],
                            'scope_requested' => $oauthMeta['scope_requested'],
                            'token_fetch_ms' => $oauthMeta['token_fetch_ms'],
                            'used_cached_token' => $oauthMeta['used_cached_token'],
                        ],
                    ],
                ],
            ],
            $target,
            $caseId,
            $path,
            $specLangLimits,
            $specLangSymbols,
            $specLangImports
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
            $res = evaluateCliRunCase($fixturePath, $case);
        } elseif ($type === 'api.http') {
            $res = evaluateApiHttpCase($fixturePath, $case);
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
    $caseFiles = listCaseFiles($args['cases'], (string)$args['case_pattern'], $args['case_formats']);

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
