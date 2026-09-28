#!/usr/bin/env python3
"""Install the local pet package without network access or third-party packages."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import tempfile


def install(codex_home: Path, replace: bool = False) -> Path:
    source = Path(__file__).resolve().parents[1] / "pet" / "nailong"
    metadata = json.loads((source / "pet.json").read_text(encoding="utf-8"))
    if metadata.get("id") != "nailong" or metadata.get("spriteVersionNumber") != 2:
        raise ValueError("Expected the nailong v2 package.")
    if metadata.get("spritesheetPath") != "spritesheet.webp":
        raise ValueError("Unexpected spritesheet path.")
    sprite = source / "spritesheet.webp"
    if not sprite.is_file() or sprite.stat().st_size == 0:
        raise ValueError("Missing spritesheet.webp.")

    codex_home = codex_home.expanduser().resolve()
    pets = codex_home / "pets"
    target = pets / "nailong"
    if target.is_symlink():
        raise ValueError("Refusing to replace a symlink at the install destination.")
    if target.exists() and not replace:
        raise FileExistsError(f"Already installed: {target}. Use --replace to back it up first.")
    if target.exists() and not target.is_dir():
        raise ValueError(f"Destination is not a directory: {target}")

    pets.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".nailong-install-", dir=pets))
    backup = None
    try:
        for name in ("pet.json", "spritesheet.webp"):
            shutil.copyfile(source / name, staging / name)
        if target.exists():
            backup_root = codex_home / "pet-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = backup_root / f"nailong-{stamp}"
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
    print("Refresh your desktop app's Pets settings, then select 奶龙.")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path,
                        default=Path(os.environ.get("CODEX_HOME") or "~/.codex"))
    parser.add_argument("--replace", action="store_true",
                        help="Back up an existing install before replacing it.")
    args = parser.parse_args()
    try:
        install(args.codex_home, args.replace)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")


if __name__ == "__main__":
    main()
