#!/usr/bin/env python3
"""Normalize an article visual and place its fixed-contract packaged wordmark."""

from __future__ import annotations

import json
import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as error:
    raise SystemExit(
        "Pillow is required. Install scripts/requirements.txt before running the Logo finalizer."
    ) from error


LOGO_CONTRACT = {
    "asset": "simplemkt-logo-demo.png",
    "canvas": (1200, 675),
    "wordmark_box": (96, 32),
    "wordmark_top_left": (1062, 27),
    "reserve_top_left": (1056, 0),
    "reserve_size": (144, 60),
}


def open_image(path: Path) -> Image.Image:
    try:
        with Image.open(path) as image:
            return image.convert("RGBA")
    except OSError as error:
        raise SystemExit(f"cannot read image: {path}") from error


def load_contract() -> dict[str, object]:
    contract = {**LOGO_CONTRACT}

    canvas_width, canvas_height = contract["canvas"]
    wordmark_x, wordmark_y = contract["wordmark_top_left"]
    wordmark_width, wordmark_height = contract["wordmark_box"]
    reserve_x, reserve_y = contract["reserve_top_left"]
    reserve_width, reserve_height = contract["reserve_size"]
    if (
        canvas_width <= 0
        or canvas_height <= 0
        or wordmark_width <= 0
        or wordmark_height <= 0
        or reserve_width <= 0
        or reserve_height <= 0
        or wordmark_x < reserve_x
        or wordmark_y < reserve_y
        or wordmark_x + wordmark_width > reserve_x + reserve_width
        or wordmark_y + wordmark_height > reserve_y + reserve_height
    ):
        raise SystemExit("invalid fixed Logo contract: wordmark must fit wholly inside the protected reserve")
    return contract


def printable_contract(contract: dict[str, object]) -> dict[str, object]:
    return {
        "asset": contract["asset"],
        "canvas": {"width": contract["canvas"][0], "height": contract["canvas"][1]},
        "wordmark": {
            "x": contract["wordmark_top_left"][0],
            "y": contract["wordmark_top_left"][1],
            "width": contract["wordmark_box"][0],
            "height": contract["wordmark_box"][1],
            "coordinate_origin": "top-left",
        },
        "reserve": {
            "x": contract["reserve_top_left"][0],
            "y": contract["reserve_top_left"][1],
            "width": contract["reserve_size"][0],
            "height": contract["reserve_size"][1],
            "coordinate_origin": "top-left",
        },
    }


def write_json_atomically(path: Path, payload: dict[str, object]) -> None:
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(temporary_path, path)


def record_logo_in_article_manifest(
    manifest_path: Path, image_id: str, attempt_id: int, receipt: dict[str, object]
) -> None:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        images = manifest["images"]
        image_record = next(item for item in images if item["id"] == image_id)
        attempt = next(item for item in image_record["attempts"] if item["id"] == attempt_id)
    except (KeyError, OSError, StopIteration, TypeError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(
            f"invalid article image manifest or missing image attempt: {manifest_path}: {error}"
        ) from error

    attempt["logo"] = {"status": "applied", **receipt}
    write_json_atomically(manifest_path, manifest)


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize an article visual and place its packaged wordmark."
    )
    parser.add_argument("underlying_image")
    parser.add_argument("wordmark_png")
    parser.add_argument("output_png")
    parser.add_argument("--article-manifest", type=Path, required=True)
    parser.add_argument("--image-id", required=True)
    parser.add_argument("--attempt-id", type=int, required=True)
    return parser.parse_args(arguments)


def main(arguments: list[str]) -> int:
    if arguments == ["--print-contract"]:
        print(json.dumps(printable_contract(load_contract()), ensure_ascii=False, indent=2))
        return 0

    parsed = parse_arguments(arguments)

    source_path = Path(parsed.underlying_image)
    wordmark_path = Path(parsed.wordmark_png)
    output_path = Path(parsed.output_png)
    contract = load_contract()
    if wordmark_path.name != contract["asset"]:
        raise SystemExit(f"wordmark asset must match fixed contract: {contract['asset']}")

    source = open_image(source_path).resize(contract["canvas"], Image.Resampling.LANCZOS)
    wordmark = open_image(wordmark_path).resize(contract["wordmark_box"], Image.Resampling.LANCZOS)
    reserve = Image.new("RGBA", contract["reserve_size"], "#FFFFFF")
    source.alpha_composite(reserve, dest=contract["reserve_top_left"])
    source.alpha_composite(wordmark, dest=contract["wordmark_top_left"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    source.convert("RGB").save(output_path, format="PNG", optimize=True)
    receipt = {
        "canvas": {"width": contract["canvas"][0], "height": contract["canvas"][1]},
        "wordmark": {
            "x": contract["wordmark_top_left"][0],
            "y": contract["wordmark_top_left"][1],
            "width": contract["wordmark_box"][0],
            "height": contract["wordmark_box"][1],
            "coordinate_origin": "top-left",
        },
        "reserve": {
            "x": contract["reserve_top_left"][0],
            "y": contract["reserve_top_left"][1],
            "width": contract["reserve_size"][0],
            "height": contract["reserve_size"][1],
            "coordinate_origin": "top-left",
        },
        "asset": wordmark_path.name,
    }
    record_logo_in_article_manifest(
        parsed.article_manifest, parsed.image_id, parsed.attempt_id, receipt
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
