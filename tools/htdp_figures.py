#!/usr/bin/env python3
"""
HtDP / Racket-doc figure assets for the Japanese translation.

Issue #9 (figures p0):
  - Download official PNG assets automatically (not hand-captioned).
  - Keep binaries out of git (assets/htdp-figures/ is gitignored).
  - Expand `[image: …]` placeholders to Markdown images at build time.

Usage:
  python3 tools/htdp_figures.py fetch [--force] [--report PATH]
  python3 tools/htdp_figures.py expand --in FILE --out FILE [--source book|quick|…]
  python3 tools/htdp_figures.py report [--out PATH]
  python3 tools/htdp_figures.py expand-tree   # rewrite each ??-*.md into build/expanded/
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "htdp-figures"
BUILD = ROOT / "build"
HTML_BOOK = ROOT / "original_html"
HTML_APPENDIX = ROOT / "appendix_original_html"

# Book edition path is versioned (e.g. 2026-5-28). Override without code edit:
#   export HTDP_BOOK_BASE=https://htdp.org/YYYY-M-D/Book/
# Optional per-manual overrides: HTDP_FIGURES_BASE_QUICK, _HTDP_LANGS, _GUI, _RACKET_CHEAT
_DEFAULT_BOOK_BASE = "https://htdp.org/2026-5-28/Book/"


def load_source_bases() -> dict[str, str]:
    """Resolve download base URLs (env overrides > defaults)."""
    book = (
        os.environ.get("HTDP_BOOK_BASE")
        or os.environ.get("HTDP_FIGURES_BOOK_BASE")
        or _DEFAULT_BOOK_BASE
    ).rstrip("/") + "/"
    return {
        "book": book,
        "quick": (
            os.environ.get("HTDP_FIGURES_BASE_QUICK")
            or "https://docs.racket-lang.org/quick/"
        ).rstrip("/")
        + "/",
        "htdp-langs": (
            os.environ.get("HTDP_FIGURES_BASE_HTDP_LANGS")
            or "https://docs.racket-lang.org/htdp-langs/"
        ).rstrip("/")
        + "/",
        "racket-cheat": (
            os.environ.get("HTDP_FIGURES_BASE_RACKET_CHEAT")
            or "https://docs.racket-lang.org/racket-cheat/"
        ).rstrip("/")
        + "/",
        "gui": (
            os.environ.get("HTDP_FIGURES_BASE_GUI")
            or "https://docs.racket-lang.org/gui/"
        ).rstrip("/")
        + "/",
    }


SOURCE_BASES: dict[str, str] = load_source_bases()
BOOK_BASE = SOURCE_BASES["book"]

# `[image: pict_240.png]` or `[image:pict_240.png]` or with alt after em dash
PLACEHOLDER_RE = re.compile(
    r"\[image:\s*([^\]\s—]+)(?:\s*[—-]\s*([^\]]+))?\]"
)
IMG_SRC_RE = re.compile(
    r"""src\s*=\s*["']([^"']+\.(?:png|gif|jpe?g|svg))["']""",
    re.I,
)

USER_AGENT = "htdp-ja-translation-figures/1.0 (+https://github.com/bluehive/htdp-ja-translation)"


def source_for_md_name(name: str) -> str:
    """Map a Japanese draft filename to an image source bucket."""
    base = Path(name).name
    if "appendix-quick" in base:
        return "quick"
    if "appendix-htdp-langs" in base:
        return "htdp-langs"
    if "appendix-gui" in base:
        return "gui"
    if "appendix-racket-cheat" in base:
        return "racket-cheat"
    return "book"


def asset_rel(source: str, filename: str) -> str:
    """POSIX path relative to repo root (for Markdown + pandoc --resource-path)."""
    return f"assets/htdp-figures/{source}/{filename}"


def asset_path(source: str, filename: str) -> Path:
    return ASSETS / source / filename


def discover_html_index() -> dict[str, set[str]]:
    """filename -> set of sources that reference it in local HTML."""
    index: dict[str, set[str]] = defaultdict(set)

    def absorb(path: Path, source: str) -> None:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return
        for src in IMG_SRC_RE.findall(text):
            index[Path(src).name].add(source)

    if HTML_BOOK.is_dir():
        for html in HTML_BOOK.glob("*.html"):
            absorb(html, "book")

    if HTML_APPENDIX.is_dir():
        for manual in SOURCE_BASES:
            if manual == "book":
                continue
            d = HTML_APPENDIX / manual
            if not d.is_dir():
                continue
            for html in d.rglob("*.html"):
                absorb(html, manual)

    return index


def collect_needed_from_markdown() -> dict[tuple[str, str], list[str]]:
    """
    (source, filename) -> list of referring draft basenames.
    Source is inferred from the draft filename (book vs appendix manual).
    """
    needed: dict[tuple[str, str], list[str]] = defaultdict(list)
    for md in sorted(ROOT.glob("??-*.md")):
        source = source_for_md_name(md.name)
        text = md.read_text(encoding="utf-8")
        for m in PLACEHOLDER_RE.finditer(text):
            filename = m.group(1).strip()
            needed[(source, filename)].append(md.name)
    return needed


def download_one(url: str, dest: Path, *, force: bool = False) -> tuple[str, str]:
    """
    Returns (status, detail) where status is:
      ok | skip | fail
    """
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return "skip", f"exists ({dest.stat().st_size} bytes)"

    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").lower()
    except urllib.error.HTTPError as e:
        return "fail", f"HTTP {e.code} {url}"
    except Exception as e:  # noqa: BLE001 — report any network failure
        return "fail", f"{type(e).__name__}: {e} ({url})"

    if not data:
        return "fail", f"empty body {url}"
    if "html" in ctype and not dest.suffix.lower() in {".html", ".htm"}:
        # soft 404 pages sometimes return 200 text/html
        head = data[:200].lstrip().lower()
        if head.startswith(b"<!doctype") or head.startswith(b"<html"):
            return "fail", f"got HTML instead of image ({url})"

    dest.write_bytes(data)
    return "ok", f"{len(data)} bytes -> {dest.relative_to(ROOT)}"


def resolve_url(source: str, filename: str, html_index: dict[str, set[str]]) -> list[str]:
    """Candidate download URLs, preferred source first then other known homes."""
    bases_order: list[str] = [source]
    for alt in html_index.get(filename, set()):
        if alt not in bases_order:
            bases_order.append(alt)
    for alt in SOURCE_BASES:
        if alt not in bases_order:
            bases_order.append(alt)

    urls: list[str] = []
    for s in bases_order:
        base = SOURCE_BASES.get(s)
        if not base:
            continue
        urls.append(base.rstrip("/") + "/" + filename)
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def cmd_fetch(args: argparse.Namespace) -> int:
    html_index = discover_html_index()
    needed = collect_needed_from_markdown()
    if not needed:
        print("No [image: …] placeholders found in ??-*.md", file=sys.stderr)
        return 1

    ok = skip = fail = 0
    failures: list[str] = []
    successes: list[str] = []

    items = sorted(needed.items(), key=lambda kv: (kv[0][0], kv[0][1]))
    print(f"Fetching {len(items)} unique (source, file) pairs into {ASSETS.relative_to(ROOT)}/")

    for (source, filename), refs in items:
        dest = asset_path(source, filename)
        urls = resolve_url(source, filename, html_index)
        status = "fail"
        detail = "no URL candidates"
        used_url = ""
        for url in urls:
            status, detail = download_one(url, dest, force=args.force)
            used_url = url
            if status in {"ok", "skip"}:
                break
            # try next URL on fail
        if status == "ok":
            ok += 1
            successes.append(f"OK   {source}/{filename}  {detail}")
        elif status == "skip":
            skip += 1
            successes.append(f"SKIP {source}/{filename}  {detail}")
        else:
            fail += 1
            ref_s = ", ".join(sorted(set(refs))[:5])
            failures.append(f"FAIL {source}/{filename}  {detail}  (refs: {ref_s})")
        # polite pacing only on network hits
        if status == "ok":
            time.sleep(args.sleep)

        if args.verbose and status != "skip":
            print(f"  [{status}] {source}/{filename} <- {used_url} ({detail})")

    report_lines = [
        "# HtDP figures fetch report",
        "",
        f"- needed pairs: **{len(items)}**",
        f"- downloaded: **{ok}**",
        f"- skipped (already present): **{skip}**",
        f"- failed: **{fail}**",
        f"- assets dir: `{ASSETS.relative_to(ROOT)}/` (gitignored)",
        "",
    ]
    if failures:
        report_lines.append("## Failures")
        report_lines.append("")
        report_lines.extend(f"- `{line}`" for line in failures)
        report_lines.append("")
    report_lines.append("## Notes")
    report_lines.append("")
    report_lines.append(
        "Images are intentionally not committed. Re-run "
        "`python3 tools/htdp_figures.py fetch` after clone."
    )
    report_lines.append("")

    report_path = Path(args.report) if args.report else BUILD / "figures-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Downloaded: {ok}, skipped: {skip}, failed: {fail}")
    print(f"Report -> {report_path}")
    if failures:
        print("Failures:", file=sys.stderr)
        for line in failures[:20]:
            print(f"  {line}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  … and {len(failures) - 20} more", file=sys.stderr)
    # Non-zero only if everything failed; partial success is still usable
    return 0 if (ok + skip) > 0 else 1


def png_pixel_size(path: Path) -> tuple[int, int] | None:
    """Return (width, height) for a PNG, or None if unreadable."""
    try:
        with path.open("rb") as f:
            if f.read(8) != b"\x89PNG\r\n\x1a\n":
                return None
            f.read(8)  # length + IHDR
            import struct

            w, h = struct.unpack(">II", f.read(8))
            return int(w), int(h)
    except OSError:
        return None


# Inline formula strips from HtDP are short in height; forcing width=90% blows them up.
FORMULA_MAX_HEIGHT_PX = 40


def md_image(source: str, filename: str, alt: str | None) -> str:
    """
    Expand to Markdown image.

    - Empty alt avoids EPUB figcaptions that are just filenames.
    - Large diagrams (height > FORMULA_MAX_HEIGHT_PX): width=90% for EPUB fit.
    - Formula-like strips (height ≤ threshold): no width attribute (natural size).
    """
    label = (alt or "").strip()
    if label.lower() in {"", "image"}:
        label = ""
    else:
        label = label.replace("[", "\\[").replace("]", "\\]")

    rel = asset_rel(source, filename)
    path = asset_path(source, filename)
    size = png_pixel_size(path) if path.exists() else None
    if size is not None:
        _w, h = size
        if h > FORMULA_MAX_HEIGHT_PX:
            return f"![{label}]({rel}){{width=90%}}"
        return f"![{label}]({rel})"
    # Missing file: keep diagram-friendly default so large missing assets still scale
    return f"![{label}]({rel}){{width=90%}}"


def _line_is_image_only(line: str) -> bool:
    """True if line is only placeholders (+ whitespace / table pipes / blockquote markers)."""
    # strip blockquote prefix repeatedly
    s = line.strip()
    while s.startswith(">"):
        s = s[1:].lstrip()
    # remove table pipes and spaces
    core = re.sub(r"[|\s]", "", s)
    if not core:
        return False
    # remove all placeholders; leftover should be empty
    leftover = PLACEHOLDER_RE.sub("", s)
    leftover = re.sub(r"[|\s>`]", "", leftover)
    return leftover == "" and PLACEHOLDER_RE.search(s) is not None


def expand_text(text: str, source: str, *, lift_fence_images: bool = True) -> tuple[str, int]:
    """
    Expand placeholders. Returns (new_text, replacement_count).

    Inside fenced code blocks, pure-image lines are lifted out of the fence
    so Pandoc/Typst can embed the PNG. Mixed code lines keep a short
    textual marker (filename) so Racket examples stay readable.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    count = 0
    in_fence = False
    fence_lang = ""
    pending_code: list[str] = []

    def close_code_if_open() -> None:
        if pending_code:
            out.append(f"```{fence_lang}\n")
            out.extend(pending_code)
            out.append("```\n")
            pending_code.clear()

    def fence_lang_of(line: str) -> str:
        return line.strip()[3:].strip()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.lstrip("\ufeff")
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_lang = fence_lang_of(stripped)
                pending_code = []
            else:
                close_code_if_open()
                in_fence = False
                fence_lang = ""
            i += 1
            continue

        if in_fence:
            if lift_fence_images and _line_is_image_only(line):
                if pending_code:
                    out.append(f"```{fence_lang}\n")
                    out.extend(pending_code)
                    out.append("```\n\n")
                    pending_code = []
                pieces: list[str] = []
                for m in PLACEHOLDER_RE.finditer(line):
                    count += 1
                    pieces.append(md_image(source, m.group(1).strip(), m.group(2)))
                out.append("\n\n".join(pieces) + "\n\n")
            else:

                def repl_code(m: re.Match[str]) -> str:
                    nonlocal count
                    count += 1
                    return f"<image:{m.group(1).strip()}>"

                pending_code.append(PLACEHOLDER_RE.sub(repl_code, line))
            i += 1
            continue

        def repl_out(m: re.Match[str]) -> str:
            nonlocal count
            count += 1
            return md_image(source, m.group(1).strip(), m.group(2))

        out.append(PLACEHOLDER_RE.sub(repl_out, line))
        i += 1

    if in_fence:
        close_code_if_open()

    return "".join(out), count


def cmd_expand(args: argparse.Namespace) -> int:
    in_path = Path(args.input)
    text = in_path.read_text(encoding="utf-8")
    source = args.source or source_for_md_name(in_path.name)
    new_text, n = expand_text(text, source, lift_fence_images=not args.no_lift)
    out_path = Path(args.output) if args.output else in_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text, encoding="utf-8")
    print(f"Expanded {n} placeholders ({source}) -> {out_path}")
    return 0


def cmd_expand_tree(args: argparse.Namespace) -> int:
    """Expand each root ??-*.md into build/expanded/ for the build pipeline."""
    out_dir = Path(args.out_dir) if args.out_dir else BUILD / "expanded"
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    files = sorted(ROOT.glob("??-*.md"))
    for md in files:
        source = source_for_md_name(md.name)
        text = md.read_text(encoding="utf-8")
        new_text, n = expand_text(text, source, lift_fence_images=not args.no_lift)
        dest = out_dir / md.name
        dest.write_text(new_text, encoding="utf-8")
        total += n
        print(f"  {md.name}: {n} expansions -> {dest.relative_to(ROOT)}")
    print(f"Total expansions: {total}")
    # write list for shell
    list_path = out_dir / "filelist.txt"
    list_path.write_text("\n".join(str(out_dir / m.name) for m in files) + "\n", encoding="utf-8")
    return 0



def ascii_broken_inventory() -> list[str]:
    """Report remaining classic +--- Figure boxes in book chapters 00-14."""
    try:
        from tools.fix_ascii_figures import inventory
    except Exception:
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "fix_ascii_figures", ROOT / "tools" / "fix_ascii_figures.py"
            )
            mod = importlib.util.module_from_spec(spec)
            assert spec.loader is not None
            spec.loader.exec_module(mod)
            inventory = mod.inventory
        except Exception:
            return []
    hits: list[str] = []
    for md in sorted(ROOT.glob("??-*.md")):
        if not md.name[:2].isdigit():
            continue
        if not (0 <= int(md.name[:2]) <= 14):
            continue
        hits.extend(inventory(md))
    return hits

def inventory_stats() -> tuple[dict[tuple[str, str], list[str]], int, int, int, list[str]]:
    """needed, present, missing, bare_count, missing_keys."""
    needed = collect_needed_from_markdown()
    present = missing = 0
    missing_keys: list[str] = []
    for (source, filename), _refs in sorted(needed.items()):
        p = asset_path(source, filename)
        if p.exists() and p.stat().st_size > 0:
            present += 1
        else:
            missing += 1
            missing_keys.append(f"{source}/{filename}")
    bare = 0
    for md in ROOT.glob("??-*.md"):
        bare += len(PLACEHOLDER_RE.findall(md.read_text(encoding="utf-8")))
    return needed, present, missing, bare, missing_keys


def cmd_report(args: argparse.Namespace) -> int:
    needed, present, missing, bare, _missing_keys = inventory_stats()
    rows: list[str] = []
    for (source, filename), refs in sorted(needed.items()):
        p = asset_path(source, filename)
        status = "ok" if p.exists() and p.stat().st_size > 0 else "MISSING"
        rows.append(
            f"| `{source}/{filename}` | {status} | {len(set(refs))} | {', '.join(sorted(set(refs))[:3])} |"
        )

    lines = [
        "# HtDP figures inventory",
        "",
        f"- book base URL: `{SOURCE_BASES['book']}`",
        f"- placeholder occurrences in drafts: **{bare}**",
        f"- unique (source, file) pairs: **{len(needed)}**",
        f"- present on disk: **{present}**",
        f"- missing on disk: **{missing}**",
        "",
        "| asset | status | ref files | sample refs |",
        "|-------|--------|-----------|-------------|",
        *rows,
        "",
    ]
    out = Path(args.out) if args.out else BUILD / "figures-inventory.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    broken = ascii_broken_inventory()
    print(f"Inventory -> {out} (present={present}, missing={missing}, bare_placeholders={bare})")
    print(f"  BOOK_BASE={SOURCE_BASES['book']}")
    print(f"  broken ASCII figures (book 00–14): {len(broken)}")
    for h in broken[:20]:
        print(f"    - {h}")
    # append to report file
    extra = ["", f"- broken ASCII figure fences (00–14): **{len(broken)}**", ""]
    if broken:
        extra.append("| location |")
        extra.append("|----------|")
        extra.extend(f"| `{h}` |" for h in broken)
        extra.append("")
    out.write_text(out.read_text(encoding="utf-8") + "\n".join(extra) + "\n", encoding="utf-8")
    if args.fail_on_missing and missing:
        return 2
    return 0


def cmd_gate(args: argparse.Namespace) -> int:
    """
    Staged quality gate for missing figure assets.

    Modes (FIGURES_GATE or --mode):
      report — always exit 0; write inventory (default)
      warn   — exit 0; print warnings if missing > 0
      error  — exit 2 if any referenced asset is missing
    """
    mode = (args.mode or os.environ.get("FIGURES_GATE") or "report").strip().lower()
    if mode not in {"report", "warn", "error"}:
        print(f"ERROR: unknown gate mode {mode!r} (use report|warn|error)", file=sys.stderr)
        return 2

    # reuse report writer
    rc = cmd_report(argparse.Namespace(out=args.out or "", fail_on_missing=False))
    _needed, present, missing, bare, missing_keys = inventory_stats()
    print(f"Gate mode={mode}: present={present} missing={missing} bare_placeholders={bare}")

    if missing == 0:
        print("Gate: OK (no missing figure assets)")
        return rc

    msg = f"Gate: {missing} missing figure asset(s)"
    if mode == "report":
        print(msg + " (report only; not failing)")
        for k in missing_keys[:15]:
            print(f"  - {k}")
        return 0
    if mode == "warn":
        print("WARNING: " + msg, file=sys.stderr)
        for k in missing_keys[:15]:
            print(f"  - {k}", file=sys.stderr)
        return 0
    # error
    print("ERROR: " + msg, file=sys.stderr)
    for k in missing_keys[:30]:
        print(f"  - {k}", file=sys.stderr)
    return 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="Download figure PNGs referenced by ??-*.md")
    f.add_argument("--force", action="store_true", help="Re-download even if present")
    f.add_argument("--sleep", type=float, default=0.15, help="Delay between successful downloads")
    f.add_argument("--report", type=str, default="", help="Report markdown path")
    f.add_argument("-v", "--verbose", action="store_true")
    f.set_defaults(func=cmd_fetch)

    e = sub.add_parser("expand", help="Expand placeholders in one markdown file")
    e.add_argument("--in", dest="input", required=True)
    e.add_argument("--out", dest="output", default="")
    e.add_argument("--source", default="", help="Override source bucket (book/quick/…)")
    e.add_argument("--no-lift", action="store_true", help="Do not lift pure-image lines out of fences")
    e.set_defaults(func=cmd_expand)

    t = sub.add_parser("expand-tree", help="Expand all root ??-*.md into build/expanded/")
    t.add_argument("--out-dir", default="")
    t.add_argument("--no-lift", action="store_true")
    t.set_defaults(func=cmd_expand_tree)

    r = sub.add_parser("report", help="Write inventory of placeholders vs downloaded assets")
    r.add_argument("--out", default="")
    r.add_argument("--fail-on-missing", action="store_true")
    r.set_defaults(func=cmd_report)

    g = sub.add_parser(
        "gate",
        help="Staged gate: report|warn|error on missing assets (env FIGURES_GATE)",
    )
    g.add_argument(
        "--mode",
        default="",
        help="report (default) | warn | error; overrides FIGURES_GATE",
    )
    g.add_argument("--out", default="", help="Inventory markdown path")
    g.set_defaults(func=cmd_gate)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
