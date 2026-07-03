#!/usr/bin/env python3
"""Download all main HTML pages from HtDP 2e online edition for translation reference.
Keeps original HTML. Code inside will be preserved later.
"""
import urllib.request
import os
import time

BASE = "https://htdp.org/2026-5-28/Book/"
PAGES = [
    "index.html",
    "part_preface.html",
    "part_prologue.html",
    "part_one.html",
    "i1-2.html",
    "part_two.html",
    "i2-3.html",
    "part_three.html",
    "i3-4.html",
    "part_four.html",
    "i4-5.html",
    "part_five.html",
    "i5-6.html",
    "part_six.html",
    "part_epilogue.html",
]

OUT_DIR = "original_html"
os.makedirs(OUT_DIR, exist_ok=True)

def download(page):
    url = BASE + page
    out_path = os.path.join(OUT_DIR, page)
    if os.path.exists(out_path):
        print(f"Skip (exists): {page}")
        return
    print(f"Fetching: {url}")
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            html = resp.read()
        with open(out_path, "wb") as f:
            f.write(html)
        print(f"  Saved {len(html)} bytes -> {out_path}")
    except Exception as e:
        print(f"  ERROR: {e}")
    time.sleep(0.5)  # polite

if __name__ == "__main__":
    for p in PAGES:
        download(p)
    print("Done downloading. Now you can parse with extract_content.py or similar.")