#!/usr/bin/env python3
"""Fetch first-page thumbnails from arXiv papers and save as JPEGs."""

import os
import sys
import urllib.request
import tempfile
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "assets" / "images" / "papers"

PAPERS = [
    ("2604.00007", "dynin-omni"),
    ("2603.27176", "medic-ad"),
    ("2509.22820", "mmpb"),
    ("2510.11268", "class-vectors"),
    ("2506.08391", "second"),
]

def fetch_thumbnail(arxiv_id: str, name: str) -> Path:
    out_path = OUTPUT_DIR / f"{name}.jpg"
    if out_path.exists():
        print(f"  {name}.jpg already exists, skipping")
        return out_path

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    print(f"  Downloading {pdf_url} ...")

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        req = urllib.request.Request(pdf_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            tmp.write(resp.read())
        tmp_path = tmp.name

    try:
        import subprocess
        from PIL import Image
        import glob as globmod

        ppm_prefix = tmp_path + "_out"
        subprocess.run(
            ["/opt/homebrew/bin/pdftoppm", "-jpeg", "-f", "1", "-l", "1", "-r", "150", tmp_path, ppm_prefix],
            check=True, capture_output=True,
        )
        ppm_files = sorted(globmod.glob(ppm_prefix + "*.jpg") + globmod.glob(ppm_prefix + "*.jpeg"))
        if not ppm_files:
            raise RuntimeError("pdftoppm produced no output files")
        img = Image.open(ppm_files[0])
        w, h = img.size
        side = min(w, h)
        img = img.crop((0, 0, side, side))
        img = img.resize((160, 160))
        img.save(out_path, "JPEG", quality=90)
        for f in ppm_files:
            os.unlink(f)
        print(f"  Saved {out_path}")
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

    return out_path


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for arxiv_id, name in PAPERS:
        try:
            fetch_thumbnail(arxiv_id, name)
        except Exception as e:
            print(f"  ERROR for {name}: {e}", file=sys.stderr)
