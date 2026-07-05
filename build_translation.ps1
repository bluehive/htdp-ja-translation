# Build HTDP 2e Japanese translation to EPUB and PDF using Pandoc.
# Runs natively on Windows PowerShell.

$ErrorActionPreference = "Stop"

# Configuration - Modify these paths if pandoc is not in your system PATH
$PandocPath = "pandoc" # Or full path, e.g. "C:\Program Files\Pandoc\pandoc.exe"
$PdfEngine = "typst" # PDF engine to use: typst, lualatex, xelatex, etc.
$FontName = "BIZ UDMincho" # Font name for Japanese PDF rendering (standard on Win 10/11: BIZ UDMincho, MS Mincho, etc.)

$BuildDir = Join-Path $PSScriptRoot "build"
$TempMd = Join-Path $BuildDir "htdp2e-ja-combined.md"
$OutEpub = Join-Path $PSScriptRoot "htdp2e-ja.epub"
$OutPdf = Join-Path $PSScriptRoot "htdp2e-ja.pdf"

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

Write-Host "=== 1. Combining markdown source files ===" -ForegroundColor Green
$SourceFiles = Get-ChildItem -Path $PSScriptRoot -Filter "??-*.md" | Sort-Object Name

if ($SourceFiles.Count -eq 0) {
    Write-Error "No source markdown files (??-*.md) found in the root directory!"
}

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
    "geometry:margin=1in",
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
