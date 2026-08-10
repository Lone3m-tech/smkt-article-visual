#!/usr/bin/env python3
"""Finalize an article visual's optional packaged wordmark without changing artwork."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from style_contract import load_style_data, style_path

STYLE_FILE = style_path()
LOGO_DIRECTORY = STYLE_FILE.parent / "logo"


def load_image_module():
    try:
        from PIL import Image
    except ImportError as error:
        raise SystemExit(
            "Pillow is required. Install scripts/requirements.txt before running the finalizer."
        ) from error
    return Image


def open_image(path: Path):
    Image = load_image_module()
    try:
        with Image.open(path) as image:
            return image.convert("RGBA")
    except OSError as error:
        raise SystemExit(f"cannot read image: {path}") from error


def load_contract() -> dict[str, object]:
    try:
        static_style = load_style_data()
        if static_style["schema_version"] != 3:
            raise ValueError("unsupported style schema version")
        dimensions = static_style["dimensions"]
        canvas = dimensions["canvas"]["output_contract"]
        logo = dimensions["logo"]
        wordmark = logo["wordmark"]
        reserve = logo["reserve"]
        cover_layout = dimensions["cover"]["layout"]
        cover_title = cover_layout["title_safe_zone"]
        cover_type = cover_layout["title"]
        body_layout = dimensions["content_image"]["layout"]
        body_title = body_layout["title_region"]
        body_stage = body_layout["content_stage"]
        body_space = body_layout["white_space"]
        contract = {
            "asset": logo["asset"],
            "canvas": (canvas["width_px"], canvas["height_px"]),
            "wordmark_box": (wordmark["width"], wordmark["height"]),
            "wordmark_top_left": (wordmark["x"], wordmark["y"]),
            "reserve_top_left": (reserve["x"], reserve["y"]),
            "reserve_size": (reserve["width"], reserve["height"]),
            "cover_title": {
                "x_min": cover_title["x_min"],
                "x_max": cover_title["x_max"],
                "y_min": cover_title["y_min"],
                "y_max": cover_title["y_max"],
                "center_x": cover_title["center_x"],
                "center_y": cover_title["center_y"],
                "fill": cover_title["fill"],
                "size_px": cover_type["size_px"],
                "line_height_px": cover_type["line_height_px"],
                "max_lines": cover_type["max_lines"],
                "max_width_px": cover_type["max_width_px"],
                "color": cover_type["color"],
            },
            "body_title_region": {
                "x_min": body_title["x_min"],
                "x_max": body_title["x_max"],
                "y_min": body_title["y_min"],
                "y_max": body_title["y_max"],
                "title_y": body_title["core_judgment_y"],
                "subtitle_y": body_title["subtitle_y"],
            },
            "body_content_stage": {
                "x_min": body_stage["x_min"],
                "x_max": body_stage["x_max"],
                "y_min": body_stage["y_min"],
                "y_max": body_stage["y_max"],
            },
            "body_white_space": {
                "min_percent": body_space["content_stage_min_percent"],
                "max_percent": body_space["content_stage_max_percent"],
                "outer_margin_min_percent": body_space["outer_margin_min_percent"],
            },
        }
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid style contract: {STYLE_FILE}: {error}") from error

    integers = [
        *contract["canvas"],
        *contract["wordmark_box"],
        *contract["wordmark_top_left"],
        *contract["reserve_top_left"],
        *contract["reserve_size"],
        contract["cover_title"]["x_min"],
        contract["cover_title"]["x_max"],
        contract["cover_title"]["y_min"],
        contract["cover_title"]["y_max"],
        contract["cover_title"]["center_x"],
        contract["cover_title"]["center_y"],
        contract["cover_title"]["size_px"],
        contract["cover_title"]["line_height_px"],
        contract["cover_title"]["max_lines"],
        contract["cover_title"]["max_width_px"],
        *contract["body_title_region"].values(),
        *contract["body_content_stage"].values(),
        *contract["body_white_space"].values(),
    ]
    if (
        not all(isinstance(value, int) and not isinstance(value, bool) for value in integers)
        or contract["canvas"][0] <= 0
        or contract["canvas"][1] <= 0
        or contract["cover_title"]["x_min"] < 0
        or contract["cover_title"]["x_max"] > contract["canvas"][0]
        or contract["cover_title"]["y_min"] < 0
        or contract["cover_title"]["y_max"] > contract["canvas"][1]
        or contract["cover_title"]["max_lines"] < 1
        or contract["cover_title"]["max_width_px"] > contract["cover_title"]["x_max"] - contract["cover_title"]["x_min"]
        or contract["body_title_region"]["y_max"] > contract["body_content_stage"]["y_min"]
        or contract["body_content_stage"]["x_min"] < 0
        or contract["body_content_stage"]["x_max"] > contract["canvas"][0]
        or contract["body_content_stage"]["y_max"] > contract["canvas"][1]
        or contract["body_white_space"]["min_percent"] > contract["body_white_space"]["max_percent"]
    ):
        raise SystemExit("invalid fixed layout contract")
    return contract


def printable_contract(contract: dict[str, object]) -> dict[str, object]:
    return {
        "canvas": {"width": contract["canvas"][0], "height": contract["canvas"][1]},
        "wordmark": {
            "x": contract["wordmark_top_left"][0],
            "y": contract["wordmark_top_left"][1],
            "width": contract["wordmark_box"][0],
            "height": contract["wordmark_box"][1],
        },
        "reserve": {
            "x": contract["reserve_top_left"][0],
            "y": contract["reserve_top_left"][1],
            "width": contract["reserve_size"][0],
            "height": contract["reserve_size"][1],
        },
        "cover_title_safe_zone": contract["cover_title"],
        "body_title_region": contract["body_title_region"],
        "body_content_stage": contract["body_content_stage"],
        "body_white_space": contract["body_white_space"],
    }


def resolve_packaged_wordmark(contract: dict[str, object]) -> Path | None:
    """Return the exact packaged Logo declared by the style contract, if it is safe to use."""
    candidate = LOGO_DIRECTORY / str(contract["asset"])
    if candidate.is_symlink() or not candidate.is_file() or candidate.suffix.lower() != ".png":
        return None
    return candidate


def write_json_atomically(path: Path, payload: dict[str, object]) -> None:
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(temporary_path, path)


def load_manifest_page(manifest_path: Path, image_id: str) -> tuple[dict[str, object], dict[str, object]]:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest["schema_version"] not in {6, 7, 8, 9} or not isinstance(manifest["pages"], list):
            raise ValueError("manifest requires schema 6, 7, 8, or 9 and pages[]")
        pages = manifest["pages"]
        if not pages or any(not isinstance(item, dict) for item in pages):
            raise ValueError("manifest pages must be non-empty objects")
        page_ids = [item.get("id") for item in pages]
        if any(not isinstance(item_id, str) or not item_id for item_id in page_ids):
            raise ValueError("every page requires a non-empty id")
        if len(page_ids) != len(set(page_ids)):
            raise ValueError("page ids must be unique")
        page = next((item for item in pages if item["id"] == image_id), None)
        if page is None:
            raise ValueError(f"page is not planned: {image_id}")

        plan = page.get("plan")
        prompt = page.get("prompt")
        generation = page.get("generation")
        if not isinstance(plan, dict):
            raise ValueError(f"page requires plan: {image_id}")
        if not isinstance(prompt, dict) or prompt.get("status") != "compiled" or not prompt.get("text"):
            raise ValueError(f"page requires compiled prompt: {image_id}")
        if not isinstance(generation, dict) or generation.get("status") != "generated":
            raise ValueError(f"page requires generated asset: {image_id}")
        if not isinstance(generation.get("candidate_file"), str) or not generation["candidate_file"]:
            raise ValueError(f"page requires candidate_file: {image_id}")

        if page.get("role") == "cover":
            if not isinstance(plan.get("title"), str) or not plan["title"]:
                raise ValueError("cover requires an exact title")
        elif page.get("role") in {"body", "body_figure"}:
            if not isinstance(plan.get("core_judgment"), str) or not plan["core_judgment"]:
                raise ValueError(f"body requires core_judgment: {image_id}")
            if not isinstance(plan.get("subtitle"), str) or not plan["subtitle"]:
                raise ValueError(f"body requires subtitle: {image_id}")
        elif page.get("role") == "agenda":
            if not isinstance(plan.get("title"), str) or not plan["title"]:
                raise ValueError("agenda requires an exact title")
            if not isinstance(plan.get("agenda_items"), list) or not plan["agenda_items"]:
                raise ValueError("agenda requires agenda_items")
        elif page.get("role") == "closing":
            if not isinstance(plan.get("closing_text"), str) or not plan["closing_text"]:
                raise ValueError("closing requires closing_text")
        else:
            raise ValueError(f"page requires role cover, body, agenda, or closing: {image_id}")
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid page-centred manifest for finalization: {manifest_path}: {error}") from error
    return manifest, page


def record_finalization(
    manifest_path: Path,
    manifest: dict[str, object],
    page: dict[str, object],
    output_path: Path,
    contract: dict[str, object],
    logo_enabled: bool,
) -> None:
    page["final"] = {
        "status": "finalized",
        "output_path": str(output_path),
        "width_px": contract["canvas"][0],
        "height_px": contract["canvas"][1],
        "logo": {
            "enabled": logo_enabled,
            "status": "applied" if logo_enabled else "skipped",
        },
    }
    page["status"] = "finalized"
    write_json_atomically(manifest_path, manifest)


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize article visual layout and wordmark.")
    parser.add_argument("underlying_image")
    parser.add_argument("output_png")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--image-id", required=True)
    return parser.parse_args(arguments)


def main(arguments: list[str]) -> int:
    if arguments == ["--print-contract"]:
        print(json.dumps(printable_contract(load_contract()), ensure_ascii=False, indent=2))
        return 0

    parsed = parse_arguments(arguments)
    source_path = Path(parsed.underlying_image)
    output_path = Path(parsed.output_png)
    contract = load_contract()
    wordmark_path = resolve_packaged_wordmark(contract)
    logo_enabled = wordmark_path is not None
    manifest, page = load_manifest_page(parsed.manifest, parsed.image_id)

    Image = load_image_module()
    image = open_image(source_path).resize(contract["canvas"], Image.Resampling.LANCZOS)
    if logo_enabled:
        assert wordmark_path is not None
        wordmark = open_image(wordmark_path).resize(contract["wordmark_box"], Image.Resampling.LANCZOS)
        image.alpha_composite(wordmark, dest=contract["wordmark_top_left"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(output_path, format="PNG", optimize=True)
    record_finalization(parsed.manifest, manifest, page, output_path, contract, logo_enabled)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
