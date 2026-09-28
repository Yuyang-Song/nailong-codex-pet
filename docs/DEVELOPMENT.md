# Development and asset layout

[Back to README](../README.md) · [中文说明](../README.zh-CN.md)

## Setup

Use Python 3.9+ and install the development image dependency in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/assets.py validate
python scripts/assets.py previews
python scripts/assets.py build
```

The installer does not need Pillow. `assets.py` does: it checks the atlas, derives documentation previews from the final asset, and creates `dist/nailong.zip` with a SHA-256 checksum. The ZIP contains the installable folder plus license, artwork notice, and both READMEs; the repository is the source for documentation images and development material.

These scripts never call an image API. `build` packages existing files; it does not regenerate or redraw the character. ZIP metadata is fixed, so identical inputs produce an identical archive.

## Atlas contract

The canvas is 1536 × 2288 pixels: 8 columns and 11 rows, with 192 × 208 cells. Indices below are zero-based.

| Row | State | Used cells |
| --- | --- | --- |
| 0 | idle | 0–5, plus neutral gaze in cell 6 |
| 1 | running-right | 0–7 |
| 2 | running-left | 0–7 |
| 3 | waving | 0–3 |
| 4 | jumping | 0–4 |
| 5 | failed | 0–7 |
| 6 | waiting | 0–5 |
| 7 | running / active work | 0–5 |
| 8 | review | 0–5 |
| 9 | gaze, first half | 0–7 |
| 10 | gaze, second half | 0–7 |

Unused cells are fully transparent. Gaze angles run clockwise in screen coordinates, starting at up:

```text
row 9:  000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5
row 10: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5
```

090 means screen-right; 270 means screen-left. 000 is looking up, not resting/front-facing. Preserve body position while the head and eyes move.

## How this version was made

The character reference and separate animation strips were generated with Codex's built-in image generation using the local hatch-pet workflow. The process used a magenta background, deterministic extraction and composition, edge cleanup, and independent visual reviews. No code or assets were copied from the prior-art repositories linked in the research notes.

The initial visual brief was a round yellow Nailong-style dinosaur with a large belly, small arms, stubby feet, a short tail, and smooth toy-like shading. Each action used the same canonical reference. Gaze rows used four approved cardinal poses to preserve direction meaning and identity.

Two extraction issues were fixed before release: per-pose normalization changed apparent size during running/jumping, and mirroring an uneven source strip cut a tail tip. Stable row scaling fixed the first; mirroring each already-extracted frame fixed the second. The published WebP is the final corrected, cleaned atlas.

Original generation prompts and temporary raw strips are not distributed as a reproducible source pipeline. The editable source of truth here is the final raster atlas. This repository does not redistribute the local hatch-pet skill or its implementation.

## Making changes

Edit or replace complete animation rows while preserving the cell geometry and transparent unused slots. Review frames at native size, particularly tails, feet, eyes, row-boundary gaze transitions, and differences between task work and locomotion. Do not mistake a passing dimensions check for a passing animation review.

After a change, run validation, regenerate previews, visually inspect the affected cycles, and rebuild the release archive. Check that both language versions of the README remain consistent. The utility validator checks metadata, dimensions, image mode, and occupancy; the original release's deeper visual and edge checks are recorded in `qa/` and are not automatically repeated by this utility.

## Release

Build and inspect `dist/nailong.zip`, then attach it and `dist/SHA256SUMS` to a GitHub release. Tag the exact reviewed commit. Keep original code/documentation licensing separate from third-party character rights as described in [ASSETS.md](../ASSETS.md).

## Imperial skins and local preview

Each skin is a complete independent pet in `pet/<skin-id>/`. To validate, export all previews and package a selected skin:

```bash
python scripts/install.py --list
python scripts/assets.py validate --skin nailong-shihao
python scripts/assets.py previews --skin nailong-shihao
python scripts/assets.py build --skin nailong-shihao
python scripts/assets.py validate --skin nailong-yefan
python scripts/assets.py previews --skin nailong-yefan
python scripts/assets.py build --skin nailong-yefan
```

Open `preview.html` from the full checkout to select skins, actions, speed and background. It reads the same atlas cells and native action timing. It is a local preview, not a client settings extension. Per-skin QA records live in `qa/<skin-id>/`.

The imperial `jumping` rows deliberately use narrative effects: Shi Hao enters a rift and disappears before the final inscription; Ye Fan's cauldron grows before the final inscription. These were requested exceptions to otherwise stable silhouettes and prop sizes. The checked desktop renderer gives this five-frame state 840 ms (140/140/140/140/280); package metadata cannot extend it. `signature-slow.gif` is explicitly a slower documentation preview. Both faces are uncovered, with long hair and stern expressions.

For a multi-skin release, build all three IDs after final documentation changes, attach every ZIP plus the combined `SHA256SUMS`, and tag the reviewed commit. Each ZIP remains independent; documentation image galleries require the full repository.
