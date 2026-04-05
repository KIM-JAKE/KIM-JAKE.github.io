#!/usr/bin/env python3
"""Fetch Figure 1 thumbnails from arXiv papers and save as JPEGs.

Strategy: extract all embedded images from pages 1-3 of the PDF,
then pick the largest RGB image with a reasonable aspect ratio.
This reliably captures the overview/teaser figure used in most ML papers.
"""

import os
import sys
import glob
import tempfile
import urllib.request
import subprocess
from pathlib import Path

PDFIMAGES = "/opt/homebrew/bin/pdfimages"
OUTPUT_DIR = Path(__file__).parent.parent / "assets" / "images" / "papers"

PAPERS = [
    ("2604.00007", "dynin-omni"),
    ("2603.27176", "medic-ad"),
    ("2509.22820", "mmpb"),
    ("2510.11268", "class-vectors"),
    ("2506.08391", "second"),
]


def best_figure(tmp_dir: str):
    """Pick the best candidate figure from extracted images."""
    from PIL import Image

    from PIL import ImageStat

    candidates = []
    for path in glob.glob(os.path.join(tmp_dir, "*")):
        try:
            img = Image.open(path)
        except Exception:
            continue
        w, h = img.size
        # Skip: non-RGB, tiny images, extreme banners
        if img.mode != "RGB":
            continue
        if w < 250 or h < 150:
            continue
        aspect = w / h
        if aspect > 4.5 or aspect < 0.3:
            continue
        # Skip near-blank images (alpha masks, white pages)
        stat = ImageStat.Stat(img)
        avg_std = sum(stat.stddev) / len(stat.stddev)
        if avg_std < 8:
            continue
        area = w * h
        candidates.append((area, path, img))

    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def fetch_thumbnail(arxiv_id: str, name: str) -> None:
    from PIL import Image

    out_path = OUTPUT_DIR / f"{name}.jpg"

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    print(f"  Downloading {pdf_url} ...")

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_pdf:
        req = urllib.request.Request(pdf_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            tmp_pdf.write(resp.read())
        pdf_path = tmp_pdf.name

    with tempfile.TemporaryDirectory() as tmp_dir:
        img_prefix = os.path.join(tmp_dir, "img")
        subprocess.run(
            [PDFIMAGES, "-j", "-f", "1", "-l", "4", pdf_path, img_prefix],
            capture_output=True,
        )
        os.unlink(pdf_path)

        best = best_figure(tmp_dir)
        if best is None:
            # Fallback: render page 2 as raster
            print(f"    No suitable figure found, falling back to page render")
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp2:
                req2 = urllib.request.Request(
                    f"https://arxiv.org/pdf/{arxiv_id}",
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                with urllib.request.urlopen(req2, timeout=60) as resp:
                    tmp2.write(resp.read())
                pdf_path2 = tmp2.name
            ppm_prefix = os.path.join(tmp_dir, "page")
            subprocess.run(
                ["/opt/homebrew/bin/pdftoppm", "-jpeg", "-f", "2", "-l", "2", "-r", "150",
                 pdf_path2, ppm_prefix],
                capture_output=True,
            )
            os.unlink(pdf_path2)
            pages = sorted(glob.glob(ppm_prefix + "*.jpg") + glob.glob(ppm_prefix + "*.jpeg"))
            if not pages:
                print(f"    ERROR: could not get any image", file=sys.stderr)
                return
            best = pages[0]

        img = Image.open(best).convert("RGB")
        w, h = img.size
        # Center-crop to square
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 4  # bias toward top where figure usually is
        img = img.crop((left, top, left + side, top + side))
        img = img.resize((200, 200), Image.LANCZOS)
        img.save(out_path, "JPEG", quality=92)
        print(f"  Saved {out_path} (source: {os.path.basename(best)}, original: {w}x{h})")


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    papers = PAPERS
    if len(sys.argv) > 1:
        # Allow passing specific arxiv_id:name pairs
        papers = [tuple(a.split(":")) for a in sys.argv[1:]]
    for arxiv_id, name in papers:
        print(f"\n[{name}]")
        try:
            fetch_thumbnail(arxiv_id, name)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
