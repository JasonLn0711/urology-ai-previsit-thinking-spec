#!/usr/bin/env python3
"""Bump repository version files for the thinking-spec repo."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
VERSION_JSON = ROOT / "meta" / "version.json"
CHANGELOG = ROOT / "CHANGELOG.md"

VERSION_RE = re.compile(r"^v(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)$")


def parse_version(raw: str) -> tuple[int, int, int]:
    value = raw.strip()
    match = VERSION_RE.match(value)
    if not match:
        raise SystemExit(f"Invalid VERSION value: {value!r}. Expected vMAJOR.MINOR.PATCH.")
    return tuple(int(match.group(name)) for name in ("major", "minor", "patch"))


def format_version(version: tuple[int, int, int]) -> str:
    return f"v{version[0]}.{version[1]}.{version[2]}"


def bump(version: tuple[int, int, int], part: str) -> tuple[int, int, int]:
    major, minor, patch = version
    if part == "major":
        return major + 1, 0, 0
    if part == "minor":
        return major, minor + 1, 0
    if part == "patch":
        return major, minor, patch + 1
    raise SystemExit(f"Unsupported bump part: {part}")


def read_current_version() -> str:
    if not VERSION_FILE.exists():
        raise SystemExit("VERSION file does not exist.")
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def update_version_json(new_version: str, date: str, part: str, summary: str) -> None:
    data = {
        "current_version": new_version,
        "last_updated": date,
        "status": f"{part} release",
        "summary": summary,
    }
    VERSION_JSON.parent.mkdir(parents=True, exist_ok=True)
    VERSION_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_changelog(new_version: str, date: str, part: str, summary: str) -> None:
    if CHANGELOG.exists():
        existing = CHANGELOG.read_text(encoding="utf-8")
    else:
        existing = "# Changelog\n\nThis repository uses the versioning rules in `VERSIONING.md`.\n"

    entry = (
        f"## {new_version} - {date}\n\n"
        f"Type: {part}\n\n"
        "Summary:\n\n"
        f"- {summary}\n\n"
    )

    lines = existing.splitlines(keepends=True)
    insert_at = len(lines)
    for index, line in enumerate(lines):
        if index > 0 and line.startswith("## "):
            insert_at = index
            break

    if insert_at == len(lines):
        if existing and not existing.endswith("\n"):
            existing += "\n"
        updated = existing + "\n" + entry
    else:
        updated = "".join(lines[:insert_at])
        if updated and not updated.endswith("\n\n"):
            updated = updated.rstrip() + "\n\n"
        updated += entry
        updated += "".join(lines[insert_at:])

    CHANGELOG.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Bump repo version files.")
    parser.add_argument("--part", choices=("patch", "minor", "major"), required=True)
    parser.add_argument("--summary", required=True, help="One concise changelog bullet.")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    current = read_current_version()
    next_version = format_version(bump(parse_version(current), args.part))

    if args.dry_run:
        print(f"{current} -> {next_version}")
        print(f"date: {args.date}")
        print(f"type: {args.part}")
        print(f"summary: {args.summary}")
        return

    VERSION_FILE.write_text(next_version + "\n", encoding="utf-8")
    update_version_json(next_version, args.date, args.part, args.summary)
    update_changelog(next_version, args.date, args.part, args.summary)
    print(f"Bumped {current} -> {next_version}")


if __name__ == "__main__":
    main()

