#!/bin/bash
# Build HTDP 2e Japanese drafts to EPUB and PDF.
# Canonical rules: BUILD.md

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

COPY_GDRIVE=1
if [[ "${1:-}" == "--no-gdrive" ]]; then
  COPY_GDRIVE=0
fi

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
LOCK="$BUILD_DIR/build.lock"
OUT_EPUB="$ROOT/htdp2e-ja.epub"
OUT_PDF="$ROOT/htdp2e-ja.pdf"
LUA="$ROOT/tools/pagebreak.lua"
CSS="$ROOT/tools/epub.css"
COMBINE="$ROOT/tools/combine_book.py"
TYPST_HEADER="$ROOT/tools/typst-header.typ"
TYPST_SRC="$BUILD_DIR/htdp2e-ja.typ"
GDRIVE_DIR="${GDRIVE_DIR:-$HOME/GoogleDrive}"
FONT_SANS="Noto Sans CJK JP"
FONT_MONO="Noto Sans Mono CJK JP"

exec 9>"$LOCK"
if ! flock -n 9; then
  echo "ERROR: another build_translation.sh is running (see $LOCK)." >&2
  exit 1
fi

echo "=== HTDP JA build (see BUILD.md) ==="
echo "  Pandoc: $PANDOC ($("$PANDOC" --version | head -n1))"
echo "  Font:   $FONT_SANS / $FONT_MONO"

echo "=== 1. Combining: 本文 → 付録 ==="
python3 "$COMBINE" "$TEMP_MD"

COMMON=(
  --toc --toc-depth=3 -M toc-title:目次
  --lua-filter="$LUA"
  --metadata=title:"プログラムの設計方法 第二版（日本語訳）"
  --metadata=author:"Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi"
  --metadata=language:ja
)

echo "=== 2. EPUB ==="
"$PANDOC" "$TEMP_MD" \
  -o "$OUT_EPUB" \
  "${COMMON[@]}" \
  --css="$CSS" \
  -V mainfont="$FONT_SANS" \
  -V monofont="$FONT_MONO"

ls -lh "$OUT_EPUB"
echo "SUCCESS: EPUB -> $OUT_EPUB"

echo "=== 3. PDF (Typst / Noto Sans CJK JP) ==="
PDF_OK=0
if command -v typst >/dev/null 2>&1; then
  "$PANDOC" "$TEMP_MD" \
    -t typst \
    -o "$TYPST_SRC" \
    "${COMMON[@]}" \
    --include-in-header="$TYPST_HEADER" \
    -V mainfont="$FONT_SANS" \
    -V monofont="$FONT_MONO" \
    -V lang=ja
  python3 "$ROOT/tools/patch_typst.py" "$TYPST_SRC"
  if typst compile --root "$ROOT" "$TYPST_SRC" "$OUT_PDF"; then
    PDF_OK=1
  fi
fi

if [[ "$PDF_OK" -eq 0 ]] && command -v xelatex >/dev/null 2>&1; then
  echo "Typst failed or missing; trying XeLaTeX"
  if "$PANDOC" "$TEMP_MD" \
      -o "$OUT_PDF" \
      "${COMMON[@]}" \
      --pdf-engine=xelatex \
      -V mainfont="$FONT_SANS" \
      -V monofont="$FONT_MONO" \
      -V CJKmainfont="$FONT_SANS" \
      -V geometry:margin=1in; then
    PDF_OK=1
  fi
fi

if [[ "$PDF_OK" -eq 1 && -f "$OUT_PDF" ]]; then
  ls -lh "$OUT_PDF"
  echo "SUCCESS: PDF -> $OUT_PDF"
else
  echo "ERROR: PDF generation failed." >&2
  exit 1
fi

if [[ "$COPY_GDRIVE" -eq 1 ]]; then
  if [[ -d "$GDRIVE_DIR" ]]; then
    echo "=== 4. Copy to $GDRIVE_DIR ==="
    cp -f "$OUT_EPUB" "$OUT_PDF" "$GDRIVE_DIR/"
    ls -lh "$GDRIVE_DIR/htdp2e-ja.epub" "$GDRIVE_DIR/htdp2e-ja.pdf"
  else
    echo "WARNING: $GDRIVE_DIR not mounted; skip copy." >&2
  fi
fi

echo "=== Done ==="
