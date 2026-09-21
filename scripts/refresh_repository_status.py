import argparse
import concurrent.futures
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ('README.md', 'README.zh-CN.md', 'README.ja.md')
ENTRY = re.compile(r'^- \[[^]]+\]\(https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)(?:[)/#])')
# GitHub product/documentation routes can look like owner/repository pairs.
NON_REPOSITORY_ROUTES = {'features', 'topics', 'collections', 'settings', 'orgs', 'users', 'marketplace', 'sponsors', 'enterprise', 'resources', 'solutions'}


def listed_repos(text):
    return {m.group(1).removesuffix('.git') for line in text.splitlines()
            if (m := ENTRY.match(line)) and m.group(1).split('/')[0].lower() not in NON_REPOSITORY_ROUTES}


def mark_archived(text, archived):
    changed = []
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        match = ENTRY.match(line)
        if not match or match.group(1).lower() not in archived or '📦' in line:
            continue
        lines[i] = re.sub(r'(\) - )', r'\1📦 Archived — ', line, count=1)
        if lines[i] != line:
            changed.append(match.group(1))
    return ''.join(lines), changed


def fetch(repo):
    process = subprocess.run(['gh', 'api', f'repos/{repo}'], capture_output=True, text=True, encoding='utf-8')
    if process.returncode:
        return {'requested': repo, 'error': 'GitHub metadata unavailable'}
    data = json.loads(process.stdout)
    return {'requested': repo, **{key: data.get(key) for key in ('full_name', 'archived', 'pushed_at', 'html_url')}}


def main():
    parser = argparse.ArgumentParser(description='Flag confirmed archived catalogue entries in all three languages; content verification dates never advance automatically.')
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--report', type=Path, default=ROOT/'artifacts'/'archived.md')
    args = parser.parse_args()
    repos = listed_repos((ROOT/'README.md').read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        metadata = list(pool.map(fetch, sorted(repos)))
    archived = {row['requested'].lower() for row in metadata if row.get('archived') is True}
    report = ['## Repository status scan', '', 'GitHub archival metadata only; model facts, prices and content verification dates were not refreshed.', '']
    for filename in FILES:
        path = ROOT/filename
        updated, changes = mark_archived(path.read_text(encoding='utf-8'), archived)
        if args.write and changes:
            path.write_text(updated, encoding='utf-8')
        report.extend(f'- `{filename}`: flag `{repo}` as archived.' for repo in changes)
    for row in metadata:
        if row.get('error'):
            report.append(f"- Unverified metadata: `{row['requested']}` (retry separately).")
        elif row.get('full_name', '').lower() != row['requested'].lower():
            report.append(f"- Canonical repository moved: `{row['requested']}` → `{row['full_name']}`; review description before changing it.")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text('\n'.join(report)+'\n', encoding='utf-8')
    args.report.with_suffix('.json').write_text(json.dumps(metadata, indent=2)+'\n', encoding='utf-8')
    print(f'Checked {len(metadata)} repositories; {len(archived)} archived; report: {args.report}')
    return 1 if any(row.get('error') for row in metadata) else 0


if __name__ == '__main__':
    raise SystemExit(main())
