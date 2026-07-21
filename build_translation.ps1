# Build HTDP 2e Japanese translation to EPUB and PDF using Pandoc.
# Runs natively on Windows PowerShell.
#
# Translation source of truth (English original for translators):
#   extracted/original_markdown_**.md
# Build input (Japanese drafts):
#   ??-*.md in the repository root (book 00-14, appendices 15-appendix-*, …)
#
# Do NOT build from original_markdown_*.md — those are the English originals.
# Translate from extracted/original_markdown_**.md (and extracted/appendix/…)
# into the root ??-*.md files, then run this script.
# Regenerate English extracts:  python extract_to_markdown.py
# Regenerate appendix extracts: python download_appendix_docs.py ; python extract_appendix_to_markdown.py

$ErrorActionPreference = "Stop"

# Configuration - Modify these paths if pandoc is not in your system PATH
$PandocPath = "pandoc" # Or full path, e.g. "C:\Program Files\Pandoc\pandoc.exe"
$PdfEngine = "typst" # PDF engine to use: typst, lualatex, xelatex, etc.
$FontName = "BIZ UDMincho" # Font name for Japanese PDF rendering (standard on Win 10/11: BIZ UDMincho, MS Mincho, etc.)

$BuildDir = Join-Path $PSScriptRoot "build"
$TempMd = Join-Path $BuildDir "htdp2e-ja-combined.md"
$OutEpub = Join-Path $PSScriptRoot "htdp2e-ja.epub"
$OutPdf = Join-Path $PSScriptRoot "htdp2e-ja.pdf"
$ExtractedDir = Join-Path $PSScriptRoot "extracted"

Write-Host "=== Translation pipeline reminder ===" -ForegroundColor Cyan
Write-Host "  English original (book):     extracted/original_markdown_**.md"
Write-Host "  English original (appendix): extracted/appendix/*/original_markdown_**.md"
Write-Host "  Japanese drafts (build):     ??-*.md"
Write-Host "  Regenerate book originals:   python extract_to_markdown.py"
Write-Host "  Regenerate appendix:         python download_appendix_docs.py ; python extract_appendix_to_markdown.py"
if (Test-Path $ExtractedDir) {
    $origCount = (Get-ChildItem -Path $ExtractedDir -Filter "original_markdown_*.md" -ErrorAction SilentlyContinue).Count
    $appendixDir = Join-Path $ExtractedDir "appendix"
    $appendixCount = 0
    if (Test-Path $appendixDir) {
        $appendixCount = (Get-ChildItem -Path $appendixDir -Recurse -Filter "original_markdown_*.md" -ErrorAction SilentlyContinue).Count
    }
    Write-Host "  Found $origCount book + $appendixCount appendix original_markdown file(s)" -ForegroundColor DarkGray
}
Write-Host ""

# 1. Create build directory
if (-not (Test-Path $BuildDir)) {
    New-Item -ItemType Directory -Path $BuildDir | Out-Null
}

# 2. Re-detect environment path for recently installed tools (like typst via winget)
# Try to find typst.exe in Winget packages folder if not in PATH
if (-not (Get-Command "typst" -ErrorAction SilentlyContinue)) {
    $WingetPath = Get-ChildItem -Path "$env:USERPROFILE\AppData\Local\Microsoft\WinGet\Packages" -Filter "typst.exe" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName
    if ($WingetPath) {
        $env:PATH += ";$(Split-Path $WingetPath)"
        Write-Host "Found typst at: $WingetPath and added to PATH." -ForegroundColor Cyan
    }
}

Write-Host "=== 1. Combining Japanese translation markdown (??-*.md, book + appendices) ===" -ForegroundColor Green
$SourceFiles = Get-ChildItem -Path $PSScriptRoot -Filter "??-*.md" | Sort-Object Name

if ($SourceFiles.Count -eq 0) {
    Write-Error "No source markdown files (??-*.md) found in the root directory! Translate from extracted/original_markdown_**.md (and appendix originals) into ??-*.md first."
}

$AppendixNamed = @($SourceFiles | Where-Object { $_.Name -like "*appendix*" })
Write-Host "  Total files: $($SourceFiles.Count) (appendix-named: $($AppendixNamed.Count))" -ForegroundColor DarkGray

# Create empty combined file with UTF-8 encoding (with BOM for Pandoc compatibility on Windows)
New-Item -ItemType File -Path $TempMd -Force | Out-Null

foreach ($file in $SourceFiles) {
    Write-Host "  Adding: $($file.Name)"
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    # Append content with a newline
    Add-Content -Path $TempMd -Value $content -Encoding UTF8
    Add-Content -Path $TempMd -Value "" -Encoding UTF8
}

Write-Host "Combined source written to: $TempMd"
Write-Host "Note: English originals stay under extracted/; build uses Japanese ??-*.md only." -ForegroundColor DarkGray

# 3. Check if Pandoc is available
try {
    $pandocVersion = & $PandocPath --version
    Write-Host "Pandoc version: $($pandocVersion[0])" -ForegroundColor Cyan
} catch {
    Write-Error "Pandoc was not found. Please ensure it is installed and in your PATH, or configure `$PandocPath in the script."
}

# 4. Generate EPUB
Write-Host "=== 2. Generating EPUB file ===" -ForegroundColor Green
$EpubArgs = @(
    $TempMd,
    "-o",
    $OutEpub,
    "--toc",
    "--toc-depth=3",
    "--metadata",
    "title=プログラムの設計方法 第二版（日本語訳）",
    "--metadata",
    "author=Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi",
    "--metadata",
    "language=ja"
)

& $PandocPath $EpubArgs
if (Test-Path $OutEpub) {
    $size = (Get-Item $OutEpub).Length / 1KB
    $msg = "SUCCESS: EPUB generated at {0} ({1:N1} KB)" -f $OutEpub, $size
    Write-Host $msg -ForegroundColor Green
} else {
    Write-Error "Failed to generate EPUB file."
}

# 5. Generate PDF
Write-Host "=== 3. Generating PDF file ===" -ForegroundColor Green
# Typst-oriented flags (aligned with min-exp-small): monofont + 0.75in side margins
# keep wide ASCII grammar tables from soft-wrapping in PDF.
$MonoFontName = if ($env:HTDP_MONOFONT) { $env:HTDP_MONOFONT } else { "Noto Sans Mono CJK JP" }
$PdfArgs = @(
    $TempMd,
    "-o",
    $OutPdf,
    "--toc",
    "--toc-depth=3",
    "--pdf-engine",
    $PdfEngine,
    "-V",
    "mainfont=$FontName",
    "-V",
    "monofont=$MonoFontName",
    "-V",
    "fontsize=10pt",
    "-V",
    "margin-left=0.75in",
    "-V",
    "margin-right=0.75in",
    "-V",
    "margin-top=1in",
    "-V",
    "margin-bottom=1in",
    "--metadata",
    "title=プログラムの設計方法 第二版（日本語訳）",
    "--metadata",
    "author=Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi",
    "--metadata",
    "language=ja"
)

Write-Host "Running Pandoc with PDF engine: $PdfEngine. (This might take a minute...)"
try {
    & $PandocPath $PdfArgs
    if (Test-Path $OutPdf) {
        $size = (Get-Item $OutPdf).Length / 1MB
        $msg = "SUCCESS: PDF generated at {0} ({1:N2} MB)" -f $OutPdf, $size
        Write-Host $msg -ForegroundColor Green
    } else {
        Write-Error "Failed to generate PDF file."
    }
} catch {
    Write-Warning "PDF generation failed. Error: $_"
}

# 6. Clean up temporary files
Write-Host "=== 4. Cleaning up temporary files ===" -ForegroundColor Green
if (Test-Path $TempMd) {
    Remove-Item $TempMd
}
Write-Host "Done." -ForegroundColor Green
Write-Host "English originals remain in extracted/original_markdown_**.md for translation work." -ForegroundColor Cyan
