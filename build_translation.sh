#!/bin/bash
# Build HTDP 2e Japanese translation (book + appendices) to EPUB and PDF.
#
# English originals (do not build these):
#   extracted/original_markdown_**.md
#   extracted/appendix/*/original_markdown_**.md
# Japanese drafts (build input):
#   ??-*.md in the repository root (00-… book, 15-… appendices, …)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [[ -x "/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc" ]]; then
  PANDOC="/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc"
elif command -v pandoc >/dev/null 2>&1; then
  PANDOC="$(command -v pandoc)"
else
  echo "ERROR: pandoc not found." >&2
  exit 1
fi

BUILD_DIR="$ROOT/build"
mkdir -p "$BUILD_DIR"
TEMP_MD="$BUILD_DIR/htdp2e-ja-combined.md"
OUT_EPUB="$ROOT/htdp2e-ja.epub"
OUT_PDF="$ROOT/htdp2e-ja.pdf"

echo "=== Translation pipeline reminder ==="
echo "  English original (book):     extracted/original_markdown_**.md"
echo "  English original (appendix): extracted/appendix/*/original_markdown_**.md"
echo "  Japanese drafts (build):     ??-*.md  (includes 15-appendix-* …)"
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

echo "=== 1. Combining Japanese translation markdown ==="
echo "  Total files: ${#SOURCE_FILES[@]} (of which appendix-named: $APPENDIX_COUNT)"
: > "$TEMP_MD"
for f in "${SOURCE_FILES[@]}"; do
  echo "  Adding: $(basename "$f")"
  cat "$f" >> "$TEMP_MD"
  printf '\n\n' >> "$TEMP_MD"
done
echo "Combined source -> $TEMP_MD ($(wc -c < "$TEMP_MD") bytes)"
echo "Pandoc: $PANDOC ($("$PANDOC" --version | head -n1))"

echo "=== 2. Generating EPUB ==="
"$PANDOC" "$TEMP_MD" \
  -o "$OUT_EPUB" \
  --toc \
  --toc-depth=3 \
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
PDF_OK=0
if command -v typst >/dev/null 2>&1; then
  if "$PANDOC" "$TEMP_MD" \
      -o "$OUT_PDF" \
      --toc --toc-depth=3 \
      --pdf-engine=typst \
      -V mainfont="Noto Serif CJK JP" \
      -V geometry:margin=1in \
      --metadata title="プログラムの設計方法 第二版（日本語訳）" \
      --metadata author="Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi" \
      --metadata language=ja; then
    PDF_OK=1
  fi
fi

if [[ "$PDF_OK" -eq 0 ]] && command -v xelatex >/dev/null 2>&1; then
  if "$PANDOC" "$TEMP_MD" \
      -o "$OUT_PDF" \
      --toc --toc-depth=3 \
      --pdf-engine=xelatex \
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
echo "Included root ??-*.md (book + appendix translations such as 15-appendix-quick.md)."
