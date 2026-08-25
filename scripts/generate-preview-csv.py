#!/usr/bin/env python3
"""Generate Google Sheets Preview column formulas from icon-previews PNGs."""

import csv
import json
from pathlib import Path

REPO = "zezorzan/zeroheight-integration-test"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/icon-previews"

ROOT = Path(__file__).resolve().parents[1]
PREVIEWS = ROOT / "icon-previews"
SHEET_CSV = Path("/tmp/icon-sheet/ranking-now.csv")
MAPPING_JSON = Path("/tmp/icon-sheet/mapping.json")
OUT_PREVIEW = ROOT / "sheet-preview-all.csv"
OUT_FULL = ROOT / "sheet-preview-with-rank.csv"


def filename_for(rank: str, name: str) -> str:
    return f"{int(rank):03d}-{name}.png"


def main() -> None:
    rows = list(csv.DictReader(SHEET_CSV.open()))
    mapping = {item["rank"]: item for item in json.loads(MAPPING_JSON.read_text())["matched"]}

    preview_lines = []
    full_rows = []

    for row in rows:
        rank = row["#"]
        name = row["Name"].strip().lower()
        mapped_name = mapping.get(rank, {}).get("name", name)
        fname = filename_for(rank, mapped_name)
        fpath = PREVIEWS / fname

        if fpath.exists():
            url = f"{BASE_URL}/{fname}"
            formula = f'=IMAGE("{url}")'
        else:
            formula = ""
            print(f"WARN missing PNG: rank {rank} -> {fname}")

        preview_lines.append(formula)
        full_rows.append({"Rank": rank, "Name": row["Name"], "Preview": formula, "File": fname})

    OUT_PREVIEW.write_text("\n".join(preview_lines) + "\n")
    with OUT_FULL.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Rank", "Name", "Preview", "File"])
        writer.writeheader()
        writer.writerows(full_rows)

    have = sum(1 for line in preview_lines if line)
    print(f"Wrote {OUT_PREVIEW} ({have}/{len(preview_lines)} previews)")


if __name__ == "__main__":
    main()
