#!/bin/bash
# Build HTDP 2e Japanese translation (book + appendices) to EPUB and PDF.
#
# English originals (do not build these):
#   extracted/original_markdown_**.md
#   extracted/appendix/*/original_markdown_**.md
# Japanese drafts (build input):
#   ??-*.md in the repository root (00-… book, 15-… appendices, …)
#
# Figures (Issue #9):
#   Drafts keep [image: …] placeholders.
#   This script fetches missing PNGs (optional), expands placeholders into
#   build/expanded/, then runs pandoc with --resource-path so assets resolve.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

# Prefer user-local tools (e.g. typst installed under ~/.local/bin)
export PATH="${HOME}/.local/bin:${PATH}"

if [[ -x "/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc" ]]; then
  PANDOC="/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc"
elif command -v pandoc >/dev/null 2>&1; then
  PANDOC="$(command -v pandoc)"
else
  echo "ERROR: pandoc not found." >&2
  exit 1
fi

BUILD_DIR="$ROOT/build"
EXPANDED_DIR="$BUILD_DIR/expanded"
mkdir -p "$BUILD_DIR"
TEMP_MD="$BUILD_DIR/htdp2e-ja-combined.md"
OUT_EPUB="$ROOT/htdp2e-ja.epub"
OUT_PDF="$ROOT/htdp2e-ja.pdf"
FIGURES_PY="$ROOT/tools/htdp_figures.py"

# SKIP_FIGURE_FETCH=1 to skip network
# FIGURES_GATE=report|warn|error (default report). Legacy: FAIL_ON_MISSING_FIGURES=1 => error
SKIP_FIGURE_FETCH="${SKIP_FIGURE_FETCH:-0}"
if [[ -n "${FAIL_ON_MISSING_FIGURES:-}" && "${FAIL_ON_MISSING_FIGURES}" == "1" ]]; then
  FIGURES_GATE="${FIGURES_GATE:-error}"
else
  FIGURES_GATE="${FIGURES_GATE:-report}"
fi
export FIGURES_GATE

echo "=== Translation pipeline reminder ==="
echo "  English original (book):     extracted/original_markdown_**.md"
echo "  English original (appendix): extracted/appendix/*/original_markdown_**.md"
echo "  Japanese drafts (build):     ??-*.md  (includes 15-appendix-* …)"
echo "  Figures policy:              figures-policy.md"
echo "  Fetch figures:               python3 tools/htdp_figures.py fetch"
echo "  Regenerate book originals:   python3 extract_to_markdown.py"
echo "  Regenerate appendix:         python3 download_appendix_docs.py && python3 extract_appendix_to_markdown.py"
echo

# Japanese translation markdown in sorted order (00-, 01-, … 15-appendix-…, …)
mapfile -t SOURCE_FILES < <(find "$ROOT" -maxdepth 1 -type f -name '??-*.md' | sort)

if [[ ${#SOURCE_FILES[@]} -eq 0 ]]; then
  echo "ERROR: No source markdown files (??-*.md) found in the repository root." >&2
  exit 1
fi

APPENDIX_COUNT=0
for f in "${SOURCE_FILES[@]}"; do
  base="$(basename "$f")"
  if [[ "$base" == *appendix* ]]; then
    APPENDIX_COUNT=$((APPENDIX_COUNT + 1))
  fi
done

echo "=== 0. Figures: fetch + expand placeholders ==="
if [[ -f "$FIGURES_PY" ]]; then
  if [[ "$SKIP_FIGURE_FETCH" != "1" ]]; then
    echo "  Fetching referenced PNGs (skipped files already present)…"
    python3 "$FIGURES_PY" fetch || echo "  WARNING: figure fetch reported errors (continuing)." >&2
  else
    echo "  SKIP_FIGURE_FETCH=1 — not downloading."
  fi
  echo "  Figures gate mode: $FIGURES_GATE"
  if ! python3 "$FIGURES_PY" gate --mode "$FIGURES_GATE"; then
    echo "ERROR: figures gate failed (FIGURES_GATE=$FIGURES_GATE)." >&2
    exit 1
  fi
  echo "  Expanding [image:…] placeholders -> $EXPANDED_DIR"
  python3 "$FIGURES_PY" expand-tree --out-dir "$EXPANDED_DIR"
  mapfile -t BUILD_SOURCES < <(find "$EXPANDED_DIR" -maxdepth 1 -type f -name '??-*.md' | sort)
  if [[ ${#BUILD_SOURCES[@]} -eq 0 ]]; then
    echo "ERROR: expand-tree produced no markdown files." >&2
    exit 1
  fi
else
  echo "  WARNING: $FIGURES_PY missing; building without figure expansion." >&2
  BUILD_SOURCES=("${SOURCE_FILES[@]}")
fi

echo "=== 1. Combining Japanese translation markdown ==="
echo "  Total files: ${#BUILD_SOURCES[@]} (of which appendix-named sources: $APPENDIX_COUNT)"
: > "$TEMP_MD"
for f in "${BUILD_SOURCES[@]}"; do
  echo "  Adding: $(basename "$f")"
  cat "$f" >> "$TEMP_MD"
  printf '\n\n' >> "$TEMP_MD"
done
echo "Combined source -> $TEMP_MD ($(wc -c < "$TEMP_MD") bytes)"
echo "Pandoc: $PANDOC ($("$PANDOC" --version | head -n1))"

# Resolve assets/htdp-figures/… paths relative to repo root
RESOURCE_PATH="$ROOT"

echo "=== 2. Generating EPUB ==="
EPUB_CSS="$ROOT/epub-figures.css"
EPUB_CSS_ARGS=()
if [[ -f "$EPUB_CSS" ]]; then
  echo "  EPUB CSS: $EPUB_CSS"
  EPUB_CSS_ARGS=(--css="$EPUB_CSS")
fi
"$PANDOC" "$TEMP_MD" \
  -o "$OUT_EPUB" \
  --toc \
  --toc-depth=3 \
  --resource-path="$RESOURCE_PATH" \
  "${EPUB_CSS_ARGS[@]}" \
  --metadata title="プログラムの設計方法 第二版（日本語訳）" \
  --metadata author="Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi" \
  --metadata language=ja

if [[ -f "$OUT_EPUB" ]]; then
  ls -lh "$OUT_EPUB"
  echo "SUCCESS: EPUB -> $OUT_EPUB"
else
  echo "ERROR: EPUB generation failed." >&2
  exit 1
fi

echo "=== 3. Generating PDF ==="
# Typst path (preferred): tuned like min-exp-small experiment so ~89-col
# ASCII grammar tables keep a single border line (no soft-wrap collapse).
#   mainfont  = body Japanese
#   monofont  = fixed-pitch for fenced code / ASCII boxes
#   fontsize  = 10pt body; code inherits smaller mono in pandoc/typst default
#   margins   = 0.75in L/R (wider text measure than 1in)
PDF_OK=0
if command -v typst >/dev/null 2>&1; then
  echo "  PDF engine: typst ($(typst --version 2>/dev/null | head -n1))"
  if "$PANDOC" "$TEMP_MD" \
      -o "$OUT_PDF" \
      --toc --toc-depth=3 \
      --pdf-engine=typst \
      --resource-path="$RESOURCE_PATH" \
      -V mainfont="Noto Serif CJK JP" \
      -V monofont="Noto Sans Mono CJK JP" \
      -V fontsize=10pt \
      -V margin-left=0.75in \
      -V margin-right=0.75in \
      -V margin-top=1in \
      -V margin-bottom=1in \
      --metadata title="プログラムの設計方法 第二版（日本語訳）" \
      --metadata author="Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi" \
      --metadata language=ja; then
    PDF_OK=1
  else
    echo "  WARNING: typst PDF failed; trying next engine..." >&2
  fi
fi

if [[ "$PDF_OK" -eq 0 ]] && command -v xelatex >/dev/null 2>&1; then
  if "$PANDOC" "$TEMP_MD" \
      -o "$OUT_PDF" \
      --toc --toc-depth=3 \
      --pdf-engine=xelatex \
      --resource-path="$RESOURCE_PATH" \
      -V mainfont="Noto Serif CJK JP" \
      -V geometry:margin=1in \
      --metadata title="プログラムの設計方法 第二版（日本語訳）" \
      --metadata author="Matthias Felleisen et al. (翻訳)" \
      --metadata language=ja; then
    PDF_OK=1
  fi
fi

if [[ "$PDF_OK" -eq 0 ]] && command -v soffice >/dev/null 2>&1; then
  ODT="$BUILD_DIR/htdp2e-ja.odt"
  "$PANDOC" "$TEMP_MD" -o "$ODT" --toc --toc-depth=3 \
    --resource-path="$RESOURCE_PATH" \
    --metadata title="プログラムの設計方法 第二版（日本語訳）" \
    --metadata author="Matthias Felleisen et al. (翻訳)"
  soffice --headless --convert-to pdf --outdir "$BUILD_DIR" "$ODT" 2>&1 || true
  if [[ -f "$BUILD_DIR/htdp2e-ja.pdf" ]]; then
    mv -f "$BUILD_DIR/htdp2e-ja.pdf" "$OUT_PDF"
    PDF_OK=1
  fi
fi

if [[ "$PDF_OK" -eq 1 && -f "$OUT_PDF" ]]; then
  ls -lh "$OUT_PDF"
  echo "SUCCESS: PDF -> $OUT_PDF"
else
  echo "WARNING: PDF generation skipped or failed (install typst, xelatex, or LibreOffice)." >&2
fi

echo "=== Done ==="
echo "Included expanded ??-*.md (book + appendix). Figures: assets/htdp-figures/ (gitignored)."
