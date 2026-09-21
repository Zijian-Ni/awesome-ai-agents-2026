#!/usr/bin/env python3
"""Check every README content URL; HTTP reachability is not claim verification.

Only badge/analytics hosts are skipped. 404/410 after GET are broken; access
blocks, rate limits and transport failures remain unresolved, never 'OK'.
Use --report to retain machine-readable evidence; --strict also fails unresolved
checks. TLS verification stays enabled. No third-party dependencies.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md", "README.zh-CN.md", "README.ja.md"]
SKIP_HOSTS = {
    "img.shields.io", "shields.io", "hits.seeyoufarm.com",
    "visitor-badge.glitch.me", "api.star-history.com", "madewithlove.now.sh",
    "forthebadge.com", "badgen.net", "flat.badgen.net",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AwesomeAI-maintenance/1.0)",
           "Accept": "text/html,application/json,*/*;q=0.8"}
SSL_CTX = ssl.create_default_context()


def extract_links(text):
    for lineno, line in enumerate(text.splitlines(), 1):
        for match in re.finditer(r'\]\((https?://[^\s)"\']+)\)', line):
            yield match.group(1), lineno


def should_skip(url):
    host = (urlsplit(url).hostname or "").lower().removeprefix("www.")
    return host in SKIP_HOSTS


def request(url, method, timeout):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as response:
            return response.status, response.geturl()
    except urllib.error.HTTPError as error:
        try:
            return error.code, error.geturl()
        finally:
            error.close()


def check_url(url, retries=1, timeout=12):
    result = {"url": url, "status": "SKIP", "code": None, "final_url": url}
    if should_skip(url):
        result["detail"] = "Badge/analytics host; not a content source"
        return result
    for attempt in range(retries + 1):
        try:
            code, final_url = request(url, "HEAD", timeout)
            # Many healthy sites reject HEAD, including with 404. Only a GET
            # can confirm these as broken. Do not accept a HEAD-only error.
            if code >= 400:
                code, final_url = request(url, "GET", timeout)
            result.update(code=code, final_url=final_url)
            if 200 <= code < 400:
                result["status"] = "OK"
                return result
            if code in (404, 410):
                result["status"] = "DEAD"
                return result
            result["status"] = "BLOCKED" if code in (401, 403, 418, 429) else "ERROR"
            result["detail"] = "Access not verified" if result["status"] == "BLOCKED" else "HTTP failure"
            if code not in (429, 500, 502, 503, 504):
                return result
        except Exception as error:
            result.update(status="ERROR", detail=str(error))
        if attempt < retries:
            time.sleep(2 ** attempt)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--files", nargs="+", default=FILES)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=12)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    if args.workers < 1 or args.timeout <= 0 or args.retries < 0:
        parser.error("workers/timeout must be positive; retries must be nonnegative")
    links = {}
    for name in args.files:
        path = ROOT / name
        for url, line in extract_links(path.read_text(encoding="utf-8")):
            url = urldefrag(url)[0]  # remote anchors require content-level review
            links.setdefault(url, []).append({"file": name, "line": line})
    print(f"Checking {len(links)} unique URLs across {len(args.files)} files...", flush=True)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        pending = {executor.submit(check_url, u, args.retries, args.timeout): u for u in links}
        for future in concurrent.futures.as_completed(pending):
            result = future.result()
            result["locations"] = links[result["url"]]
            results.append(result)
            if len(results) % 50 == 0 or len(results) == len(links):
                print(f"  [{len(results)}/{len(links)}] checked", flush=True)
    results.sort(key=lambda r: r["url"])
    counts = Counter(r["status"] for r in results)
    summary = {s: counts[s] for s in ("OK", "SKIP", "DEAD", "BLOCKED", "ERROR")}
    print("SUMMARY: " + " | ".join(f"{n} {s}" for s, n in summary.items()))
    for result in results:
        if result["status"] in ("DEAD", "BLOCKED", "ERROR"):
            first = result["locations"][0]
            print(f"  {result['status']} [{result['code']}] {first['file']}:{first['line']} {result['url']}")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps({
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "scope": "HTTP reachability only; redirects and 200 responses do not verify claims or remote anchors",
            "summary": summary, "results": results,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if counts["BLOCKED"] or counts["ERROR"]:
        print("Some URLs remain unverified; inspect the report or verify their primary sources manually.")
    elif not counts["DEAD"]:
        print("All checked content URLs returned successful HTTP responses; badge hosts were excluded.")
    return 1 if counts["DEAD"] or (args.strict and (counts["BLOCKED"] or counts["ERROR"])) else 0


if __name__ == "__main__":
    sys.exit(main())
