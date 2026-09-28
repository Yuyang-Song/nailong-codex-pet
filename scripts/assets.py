#!/usr/bin/env python3
"""Inspect the checked-in atlas, export previews, or build a release archive."""

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PET = ROOT / "pet" / "nailong"
STATES = [
    ("idle", [280, 110, 110, 140, 140, 320]),
    ("running-right", [120] * 7 + [220]),
    ("running-left", [120] * 7 + [220]),
    ("waving", [140] * 3 + [280]),
    ("jumping", [140] * 4 + [280]),
    ("failed", [140] * 7 + [240]),
    ("waiting", [150] * 5 + [260]),
    ("running", [120] * 5 + [220]),
    ("review", [150] * 5 + [280]),
]


def validate():
    meta = json.loads((PET / "pet.json").read_text(encoding="utf-8"))
    if (meta.get("id"), meta.get("spriteVersionNumber"), meta.get("spritesheetPath")) != (
        "nailong", 2, "spritesheet.webp"
    ):
        raise ValueError("Unexpected pet identity, sprite version, or file path")
    with Image.open(PET / "spritesheet.webp") as image:
        if image.format != "WEBP" or image.size != (1536, 2288) or image.mode != "RGBA":
            raise ValueError("Expected a 1536x2288 RGBA WebP")
        atlas = image.copy()
    used = 0
    for row in range(11):
        count = len(STATES[row][1]) if row < 9 else 8
        for col in range(8):
            cell = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            # v2 has a dedicated neutral/default gaze cell at row 0, column 6.
            active = col < count or (row == 0 and col == 6)
            nonempty = cell.getchannel("A").getbbox() is not None
            if active != nonempty:
                raise ValueError(f"Unexpected alpha occupancy at row {row}, column {col}")
            used += int(active)
    return atlas, {"ok": True, "width": 1536, "height": 2288, "active_cells": used,
                   "spriteVersionNumber": 2,
                   "sha256": hashlib.sha256((PET / "spritesheet.webp").read_bytes()).hexdigest()}


def previews(atlas):
    target = ROOT / "docs" / "previews"
    target.mkdir(parents=True, exist_ok=True)
    sequences = [(name, [(row, col) for col in range(len(times))], times)
                 for row, (name, times) in enumerate(STATES)]
    sequences.append(("look", [(9 + i // 8, i % 8) for i in range(16)], [160] * 16))
    for name, cells, durations in sequences:
        frames = []
        for row, col in cells:
            sprite = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            frame = Image.new("RGBA", (192, 208), "#f6f3ed")
            frame.alpha_composite(sprite)
            frames.append(frame.convert("RGB"))
        frames[0].save(target / f"{name}.gif", save_all=True, append_images=frames[1:],
                       duration=durations, loop=0, disposal=2, optimize=False)


def build():
    target = ROOT / "dist"
    target.mkdir(exist_ok=True)
    archive = target / "nailong.zip"
    members = [(PET / name, "nailong/" + name) for name in ("pet.json", "spritesheet.webp")]
    members += [(ROOT / name, name) for name in ("LICENSE", "ASSETS.md", "README.md", "README.zh-CN.md")]
    # Fixed ZIP metadata makes packaging reproducible from identical input files.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path, name in members:
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 28, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            output.writestr(info, path.read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (target / "SHA256SUMS").write_text(f"{digest}  nailong.zip\n", encoding="utf-8")
    print(f"Built {archive.name}; SHA-256: {digest}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "previews", "build"))
    args = parser.parse_args()
    atlas, report = validate()
    print(json.dumps(report, indent=2))
    if args.command == "previews":
        previews(atlas)
    elif args.command == "build":
        build()


if __name__ == "__main__":
    main()
