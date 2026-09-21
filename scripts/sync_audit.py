#!/usr/bin/env python3
"""
sync_audit.py — structural drift auditor for the tri-lingual READMEs.

The three README files (en / zh-CN / ja) must stay in lockstep. Headings are
*translated*, so they cannot be compared by text. What must match is the
STRUCTURE:

  * the same number of headings, at the same levels, in the same order
  * the same list entries inside each positional section, in the same order,
    identified by the entry's first markdown link target (URLs are not
    translated)

Usage:
    python3 scripts/sync_audit.py             # full report, exit 1 on drift
    python3 scripts/sync_audit.py --summary   # totals + issue count only
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "en": ROOT / "README.md",
    "zh": ROOT / "README.zh-CN.md",
    "ja": ROOT / "README.ja.md",
}

HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*$")
ENTRY_RE = re.compile(r"^-\s+\[(?P<label>[^\]]+)\]\((?P<url>[^)\s]+)")


def norm_url(url: str) -> str:
    u = url.strip().rstrip("/")
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.lower()


def is_anchor(url: str) -> bool:
    """In-page anchors are derived from *translated* headings, so they are
    expected to differ between languages and carry no structural signal."""
    return url.startswith("#")


class Section:
    __slots__ = ("level", "title", "line", "urls", "table_rows", "table_urls", "prompts")

    def __init__(self, level: int, title: str, line: int):
        self.level = level
        self.title = title
        self.line = line
        self.urls: list[str] = []
        self.table_rows = 0
        self.table_urls: list[str] = []
        self.prompts = 0

    def __repr__(self) -> str:
        return f"<{'#' * self.level} {self.title} @L{self.line} n={len(self.urls)}>"


def parse(path: Path) -> list[Section]:
    sections = [Section(0, "(preamble)", 0)]
    in_fence = False
    in_scenarios = False
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        h = HEADING_RE.match(raw)
        if h:
            if len(h.group(1)) == 2:
                in_scenarios = "🗺" in h.group(2)
            sections.append(Section(len(h.group(1)), h.group(2), lineno))
            continue
        if raw.startswith("|"):
            sections[-1].table_rows += 1
            for target in re.findall(r"\]\((https?://[^)\s]+)\)", raw):
                if "shields.io/" not in target:
                    sections[-1].table_urls.append(norm_url(target))
        if in_scenarios and raw.startswith("**"):
            sections[-1].prompts += 1
        e = ENTRY_RE.match(raw)
        if e:
            url = e.group("url")
            if not is_anchor(url):
                sections[-1].urls.append(norm_url(url))
    return sections


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()

    parsed: dict[str, list[Section]] = {}
    for lang, path in FILES.items():
        if not path.exists():
            print(f"MISSING FILE: {path}")
            return 2
        parsed[lang] = parse(path)

    print("=" * 74)
    print("TOTALS")
    print("=" * 74)
    for lang in FILES:
        secs = parsed[lang]
        print(
            f"  {lang:<3} headings={len(secs) - 1:<4} entries={sum(len(s.urls) for s in secs)}"
        )

    problems = 0
    base = parsed["en"]

    for lang in ("zh", "ja"):
        other = parsed[lang]
        print()
        print("=" * 74)
        print(f"DRIFT — en vs {lang}")
        print("=" * 74)

        # 1. heading skeleton (levels only; titles are translated)
        base_levels = [s.level for s in base]
        other_levels = [s.level for s in other]
        if base_levels != other_levels:
            problems += 1
            print(f"  [SKELETON] heading count/level mismatch "
                  f"(en={len(base) - 1}, {lang}={len(other) - 1})")
            for i in range(max(len(base_levels), len(other_levels))):
                a = base[i] if i < len(base) else None
                b = other[i] if i < len(other) else None
                if (a.level if a else None) != (b.level if b else None):
                    print(f"    first divergence at heading #{i}:")
                    print(f"      en : {a!r}")
                    print(f"      {lang} : {b!r}")
                    break

        # 2. positional entry comparison
        for i in range(min(len(base), len(other))):
            a, b = base[i], other[i]
            if a.table_rows != b.table_rows:
                problems += 1
                print(f"  [TABLE ROWS] #{i} {a.title!r}: en={a.table_rows}, {lang}={b.table_rows}")
            if a.table_urls != b.table_urls:
                problems += 1
                print(f"  [TABLE LINKS] #{i} {a.title!r}: source links/order differ in {lang}")
            if a.prompts != b.prompts:
                problems += 1
                print(f"  [SCENARIOS] #{i} {a.title!r}: en={a.prompts}, {lang}={b.prompts}")
            if a.urls == b.urls:
                continue
            # Multiset comparison: a URL may legitimately appear more than once in
            # a section, so plain membership tests would hide duplicate drift.
            ca, cb = Counter(a.urls), Counter(b.urls)
            missing = list((ca - cb).elements())
            extra = list((cb - ca).elements())
            if missing or extra:
                problems += 1
                print(f"  [ENTRIES] #{i} en:{a.title!r} (L{a.line}) "
                      f"vs {lang}:{b.title!r} (L{b.line})  "
                      f"[en={len(a.urls)} {lang}={len(b.urls)}]")
                for u in missing:
                    print(f"    - missing in {lang}: {u}")
                for u in extra:
                    print(f"    + extra in {lang}:   {u}")
            else:
                problems += 1
                print(f"  [ORDER] #{i} {a.title!r}: same entries, different order")
                for j, (x, y) in enumerate(zip(a.urls, b.urls)):
                    if x != y:
                        print(f"    first divergence at position {j}: en={x} / {lang}={y}")
                        break

    # 3. Repeated URLs inside one section.
    #
    # These are usually legitimate: a vendor section lists many products that all
    # point at one marketing domain (8 OpenAI models -> openai.com, 3 Cursor
    # releases -> cursor.com/changelog). That is only a problem if the repeat
    # count DIFFERS between languages, which means an entry was lost or cloned.
    print()
    print("=" * 74)
    print("REPEATED URLS WITHIN A SECTION (asymmetric only)")
    print("=" * 74)
    asym = False
    for i in range(min(len(s) for s in parsed.values())):
        counts = {lang: Counter(parsed[lang][i].urls) for lang in FILES}
        urls = set()
        for c in counts.values():
            urls |= {u for u, n in c.items() if n > 1}
        for u in sorted(urls):
            per = {lang: counts[lang][u] for lang in FILES}
            if len(set(per.values())) > 1:
                asym = True
                problems += 1
                print(f"  #{i} {parsed['en'][i].title!r}: {u}")
                print(f"      counts: {per}")
    if not asym:
        print("  none (all repeats are symmetric across en/zh/ja)")

    print()
    print("=" * 74)
    if problems:
        print(f"RESULT: {problems} drift issue group(s)")
        return 1
    print("RESULT: en/zh/ja fully in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
