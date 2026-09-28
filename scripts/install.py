#!/usr/bin/env python3
"""Install the local pet package without network access or third-party packages."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import tempfile


PACKAGES = Path(__file__).resolve().parents[1] / "pet"


def available_skins():
    """Only list complete local packages, never planned skins or concept art."""
    return sorted(path.name for path in PACKAGES.iterdir()
                  if path.is_dir() and not path.is_symlink()
                  and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", path.name)
                  and (path / "pet.json").is_file()
                  and (path / "spritesheet.webp").is_file())


def install(codex_home: Path, replace: bool = False, skin: str = "nailong") -> Path:
    if skin not in available_skins():
        raise ValueError(f"Unknown or incomplete skin: {skin}")
    source = PACKAGES / skin
    metadata = json.loads((source / "pet.json").read_text(encoding="utf-8"))
    if metadata.get("id") != skin or metadata.get("spriteVersionNumber") != 2:
        raise ValueError("Expected a v2 package with an id matching its skin directory.")
    if metadata.get("spritesheetPath") != "spritesheet.webp":
        raise ValueError("Unexpected spritesheet path.")
    sprite = source / "spritesheet.webp"
    if not sprite.is_file() or sprite.stat().st_size == 0:
        raise ValueError("Missing spritesheet.webp.")

    codex_home = codex_home.expanduser().resolve()
    pets = codex_home / "pets"
    target = pets / skin
    if target.is_symlink():
        raise ValueError("Refusing to replace a symlink at the install destination.")
    if target.exists() and not replace:
        raise FileExistsError(f"Already installed: {target}. Use --replace to back it up first.")
    if target.exists() and not target.is_dir():
        raise ValueError(f"Destination is not a directory: {target}")

    pets.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{skin}-install-", dir=pets))
    backup = None
    try:
        for name in ("pet.json", "spritesheet.webp"):
            shutil.copyfile(source / name, staging / name)
        if target.exists():
            backup_root = codex_home / "pet-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = backup_root / f"{skin}-{stamp}"
            target.rename(backup)
        staging.rename(target)
    except Exception:
        if backup is not None and backup.exists() and not target.exists():
            backup.rename(target)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    print(f"Installed: {target}")
    if backup is not None:
        print(f"Previous version backed up: {backup}")
    print(f"Refresh your desktop app's Pets settings, then select {metadata.get('displayName', skin)}.")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path,
                        default=Path(os.environ.get("CODEX_HOME") or "~/.codex"))
    parser.add_argument("--replace", action="store_true",
                        help="Back up an existing install before replacing it.")
    parser.add_argument("--list", action="store_true",
                        help="Print available skin IDs as JSON without installing anything.")
    parser.add_argument("--skin", default="nailong",
                        help="Skin ID to install (default: nailong). Use --list for available IDs.")
    args = parser.parse_args()
    try:
        if args.list:
            print(json.dumps({"skins": available_skins()}, ensure_ascii=False))
            return
        install(args.codex_home, args.replace, args.skin)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")


if __name__ == "__main__":
    main()
