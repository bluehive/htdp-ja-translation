#!/usr/bin/env python3
"""
Recursively download Racket documentation manuals used as appendices
for the HTDP Japanese translation project.

Seeds (TOC / entry pages):
  - https://docs.racket-lang.org/quick/index.html
  - https://docs.racket-lang.org/htdp-langs/index.html
  - https://docs.racket-lang.org/racket-cheat/index.html
  - https://docs.racket-lang.org/gui/index.html

For each seed, crawls every HTML page under the same manual directory
(e.g. /gui/*.html) and saves originals under appendix_original_html/<manual>/.
"""

from __future__ import annotations

import re
import time
import urllib.error
import urllib.request
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent
OUT_ROOT = ROOT / "appendix_original_html"

SEEDS = [
    "https://docs.racket-lang.org/quick/index.html",
    "https://docs.racket-lang.org/htdp-langs/index.html",
    "https://docs.racket-lang.org/racket-cheat/index.html",
    "https://docs.racket-lang.org/gui/index.html",
]

USER_AGENT = "htdp-ja-translation/1.0 (+local appendix mirror; polite crawl)"
DELAY_SEC = 0.12
TIMEOUT = 60
MAX_PAGES_PER_MANUAL = 500


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def normalize_html_url(url: str, origin: str) -> str | None:
    """Return a clean absolute .html URL under origin, or None if not crawlable."""
    p = urlparse(url)
    if p.scheme not in ("http", "https", ""):
        return None
    if p.netloc and p.netloc != urlparse(origin).netloc:
        return None
    path = p.path or "/"
    if path.endswith("/"):
        path = path + "index.html"
    if not path.endswith(".html"):
        return None
    return f"{origin}{path}"


def manual_dir_prefix(seed_url: str) -> tuple[str, str, str]:
    """Return (origin, dir_prefix, manual_name)."""
    p = urlparse(seed_url)
    origin = f"{p.scheme}://{p.netloc}"
    # /quick/index.html -> /quick/
    dir_prefix = p.path.rsplit("/", 1)[0] + "/"
    manual_name = dir_prefix.strip("/").split("/")[-1]
    return origin, dir_prefix, manual_name


def extract_links(html: str, base_url: str) -> list[str]:
    hrefs = re.findall(r'''href\s*=\s*["']([^"'#]+)''', html, flags=re.I)
    out = []
    for h in hrefs:
        if h.startswith("javascript:"):
            continue
        out.append(urljoin(base_url, h))
    return out


def crawl_manual(seed_url: str) -> list[Path]:
    origin, dir_prefix, manual_name = manual_dir_prefix(seed_url)
    out_dir = OUT_ROOT / manual_name
    out_dir.mkdir(parents=True, exist_ok=True)

    seed = normalize_html_url(seed_url, origin)
    assert seed is not None

    seen: set[str] = set()
    queue: deque[str] = deque([seed])
    saved: list[Path] = []

    print(f"\n=== Manual: {manual_name} ===")
    print(f"  seed: {seed}")
    print(f"  dir:  {dir_prefix}")
    print(f"  out:  {out_dir.relative_to(ROOT)}")

    while queue and len(seen) < MAX_PAGES_PER_MANUAL:
        url = queue.popleft()
        url = normalize_html_url(url, origin)
        if url is None:
            continue
        path = urlparse(url).path
        if not path.startswith(dir_prefix):
            continue
        if url in seen:
            continue
        seen.add(url)

        rel_name = path[len(dir_prefix) :]  # e.g. index.html, frame_.html
        if not rel_name or "/" in rel_name:
            # keep nested paths if any
            dest = out_dir / rel_name
            dest.parent.mkdir(parents=True, exist_ok=True)
        else:
            dest = out_dir / rel_name

        try:
            if dest.exists() and dest.stat().st_size > 0:
                data = dest.read_bytes()
                print(f"  [{len(saved)+1}] skip (exists) {rel_name} ({len(data):,} bytes)")
            else:
                data = fetch_bytes(url)
                dest.write_bytes(data)
                print(f"  [{len(saved)+1}] saved {rel_name} ({len(data):,} bytes)")
                time.sleep(DELAY_SEC)
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            print(f"  FAIL {url}: {e}")
            continue

        saved.append(dest)
        try:
            html = data.decode("utf-8", errors="replace")
        except Exception:
            continue
        for link in extract_links(html, url):
            n = normalize_html_url(link, origin)
            if n is None:
                continue
            npath = urlparse(n).path
            if npath.startswith(dir_prefix) and n not in seen:
                queue.append(n)

    print(f"  TOTAL pages for {manual_name}: {len(saved)}")
    return saved


def main() -> int:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    all_saved: list[Path] = []
    for seed in SEEDS:
        all_saved.extend(crawl_manual(seed))

    # Manifest
    lines = [
        "# Appendix original HTML (Racket docs mirrors)",
        "",
        "Downloaded recursively from docs.racket-lang.org for use as",
        "translation sources (see `extract_appendix_to_markdown.py`).",
        "",
        "## Seeds",
        "",
    ]
    for s in SEEDS:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("## Local tree")
    lines.append("")
    for manual_dir in sorted(OUT_ROOT.iterdir()):
        if not manual_dir.is_dir():
            continue
        files = sorted(manual_dir.rglob("*.html"))
        lines.append(f"### `{manual_dir.name}/` ({len(files)} pages)")
        lines.append("")
        for f in files:
            rel = f.relative_to(OUT_ROOT)
            lines.append(f"- `{rel}`")
        lines.append("")
    (OUT_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nDone. {len(all_saved)} HTML files under {OUT_ROOT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
