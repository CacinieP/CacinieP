#!/usr/bin/env python3
"""Refresh GitHub star counts in README.md.

Scans README.md for links of the form
    https://github.com/CacinieP/<repo>
fetches each repo's stargazers_count via the REST API, and rewrites the
trailing ``★N`` token on the same line to match. Lines without a ``★``
marker are left untouched, so plain link references elsewhere are safe.

Env:
    GITHUB_TOKEN  - token with public_repo read access (or GITHUB_TOKEN)
    GH_USER       - owner login whose repos should be tracked
"""
from __future__ import annotations

import os
import re
import sys
import urllib.request

README = "README.md"
STAR_RE = re.compile(r"★\s*\d+")
# Match a link to the configured user's repo, capturing the repo name.
LINK_RE_TEMPLATE = r"https?://github\.com/{user}/([A-Za-z0-9_.\-]+)"


def api_stars(owner: str, repo: str, token: str) -> int | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            import json
            return int(json.load(resp)["stargazers_count"])
    except Exception as exc:  # noqa: BLE001
        print(f"  ! {repo}: {exc}", file=sys.stderr)
        return None


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    user = os.environ.get("GH_USER")
    if not token or not user:
        print("GITHUB_TOKEN and GH_USER must be set", file=sys.stderr)
        return 2

    with open(README, encoding="utf-8") as fh:
        lines = fh.readlines()

    link_re = re.compile(LINK_RE_TEMPLATE.format(user=re.escape(user)))
    changed = 0
    for i, line in enumerate(lines):
        m = link_re.search(line)
        if not m or not STAR_RE.search(line):
            continue
        repo = m.group(1).rstrip(")")
        stars = api_stars(user, repo, token)
        if stars is None:
            continue
        new_line = STAR_RE.sub(f"★{stars}", line)
        if new_line != line:
            lines[i] = new_line
            changed += 1
            print(f"  ~ {repo} -> ★{stars}")

    with open(README, "w", encoding="utf-8") as fh:
        fh.writelines(lines)

    print(f"Updated {changed} star count(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
