#!/bin/bash
# Build Japanese HtDP translation to PDF.
# Uses local pandoc and soffice.
# Step-by-step: add more md files as translation progresses.

set -e

PANDOC="/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc"
OUT_DIR="/home/mevius/htdp-ja-translation"
cd "$OUT_DIR"

echo "=== Combining markdown files ==="

# Concat main translated files (add more chapters as translated)
cat 00-toc-and-front.md \
    01-preface.md \
    02-prologue.md \
    > htdp2e-ja-partial.md

echo "Combined -> htdp2e-ja-partial.md (current translated front matter + TOC)"

echo "=== Converting to ODT (intermediate for good JP support) ==="
"$PANDOC" htdp2e-ja-partial.md \
    -o htdp2e-ja-partial.odt \
    --toc \
    --toc-depth=3 \
    -V mainfont="Noto Serif CJK JP" \
    --metadata title="プログラムの設計方法 第二版（日本語訳）" \
    --metadata author="Matthias Felleisen et al. (翻訳)"

echo "=== Converting ODT to PDF via LibreOffice ==="
soffice --headless --convert-to pdf --outdir . htdp2e-ja-partial.odt 2>&1

PDF_OUT="htdp2e-ja-partial.pdf"
if [ -f "$PDF_OUT" ]; then
    cp -v "$PDF_OUT" "/home/mevius/ダウンロード/How_to_Design_Programs_2e_JA_partial.pdf" || true
    ls -lh "$PDF_OUT"
    echo "PDF generated and copied to ~/ダウンロード/"
    echo "SUCCESS: Partial Japanese translation PDF ready."
else
    echo "PDF generation failed. Check logs."
    exit 1
fi

echo "=== To continue full translation: add more .md chapter files and re-run this script ==="
