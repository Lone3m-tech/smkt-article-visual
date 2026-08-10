"""Load direct-text editorial prompts and expose fixed delivery layout constants."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any


STYLE_MARKDOWN = Path(__file__).resolve().parent.parent / "assets" / "simplemkt-editorial-style.md"
SECTION_PATTERN = re.compile(
    r"<!--\s*smkt-style:(?P<name>[a-z_]+)\s*-->\s*(?P<payload>.*?)\s*<!--\s*/smkt-style:\1\s*-->",
    re.DOTALL,
)
PRESENTATION_TYPOGRAPHY_PATTERN = re.compile(
    r"<!--\s*smkt-presentation-typography\s*-->\s*(?P<table>.*?)\s*<!--\s*/smkt-presentation-typography\s*-->",
    re.DOTALL,
)
PRESENTATION_TYPOGRAPHY_COLUMNS = ("role", "family", "weight", "color", "size_px", "line_height_px", "max_lines", "alignment")
PRESENTATION_TYPOGRAPHY_ROLES = {
    "cover_title", "body_title", "body_subtitle", "agenda_title", "agenda_item", "closing_message", "label", "note",
}


def style_path() -> Path:
    return STYLE_MARKDOWN


def resolve_path(dimensions: dict[str, Any], dotted_path: str) -> Any:
    """Compatibility helper for callers that address fixed layout constants."""
    value: Any = dimensions
    for component in dotted_path.split("."):
        if not isinstance(value, dict) or component not in value:
            raise ValueError(f"missing fixed layout value: {dotted_path}")
        value = value[component]
    return value


def load_presentation_typography(markdown: str) -> dict[str, dict[str, Any]]:
    """Parse the Markdown-owned presentation type system without defining visual values here."""
    match = PRESENTATION_TYPOGRAPHY_PATTERN.search(markdown)
    if not match:
        raise ValueError("style file requires one smkt-presentation-typography table")
    rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in match.group("table").splitlines()
        if line.strip().startswith("|")
    ]
    if len(rows) < 3 or tuple(rows[0]) != PRESENTATION_TYPOGRAPHY_COLUMNS:
        raise ValueError("presentation typography table requires the canonical columns")
    data_rows = [
        row for row in rows[1:]
        if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row)
    ]
    if any(len(row) != len(PRESENTATION_TYPOGRAPHY_COLUMNS) for row in data_rows):
        raise ValueError("presentation typography table rows must match the canonical columns")

    typography: dict[str, dict[str, Any]] = {}
    for row in data_rows:
        item = dict(zip(PRESENTATION_TYPOGRAPHY_COLUMNS, row, strict=True))
        role = item.pop("role")
        if role in typography or role not in PRESENTATION_TYPOGRAPHY_ROLES:
            raise ValueError("presentation typography table requires each canonical role exactly once")
        try:
            item["size_px"] = int(item["size_px"])
            item["line_height_px"] = int(item["line_height_px"])
            item["max_lines"] = int(item["max_lines"])
        except ValueError as error:
            raise ValueError(f"presentation typography role {role} has a non-integer size or line limit") from error
        if not all(isinstance(item[field], str) and item[field].strip() for field in ("family", "weight", "color", "alignment")):
            raise ValueError(f"presentation typography role {role} has an empty visual field")
        if item["size_px"] <= 0 or item["line_height_px"] < item["size_px"] or item["max_lines"] < 1:
            raise ValueError(f"presentation typography role {role} has an invalid size, line height, or line limit")
        typography[role] = item
    if set(typography) != PRESENTATION_TYPOGRAPHY_ROLES:
        raise ValueError("presentation typography table requires every declared page role")
    return typography


def fixed_dimensions() -> dict[str, Any]:
    """Mechanical layout data belongs to the renderer, not the style prompt."""
    return {
        "series": {"focus": "Cover and body pages share one editorial language but have distinct roles.", "avoid": []},
        "canvas": {
            "output_contract": {"width_px": 1200, "height_px": 675, "background_color": "#FFFFFF"},
            "technical_specification_rendering_rule": {"instruction": "Coordinates, dimensions, and layout metadata are internal guidance. Never render them as image content."},
        },
        "logo": {
            "asset": "simplemkt-logo-demo.png",
            "wordmark": {"x": 1062, "y": 27, "width": 96, "height": 32},
            "reserve": {"x": 1056, "y": 0, "width": 144, "height": 60},
            "prompt_avoid_in_reserve": ["title", "subtitle", "label", "essential diagram content"],
        },
        "color_system": {"semantic_layer": {"brand_color": "#1A6B3A"}},
        "visual_language": {
            "rendering_mode": "Use the direct style prompt below.",
            "rendering_avoid": [],
            "ink_line_character": "Use the direct style prompt below.",
            "black_mass_role": "Use the direct style prompt below.",
            "spot_colour_policy": "Use the direct style prompt below.",
            "treatment": [], "principles": [], "avoid": [],
        },
        "materials": {"editorial_patina": {"allowed": [], "forbidden": []}},
        "linework": {"forbidden": [], "surface_variation": "Use the direct style prompt below."},
        "annotation": {
            "appearance": "Use quiet thin gray leaders and labels; one declared green relation line may be used.",
            "text": "Render only the exact visible label or note content declared by the page plan.",
            "restraint": "Annotations are subordinate to the relationship and never decorative.",
            "allowed_types": ["label", "leader", "connector", "directional_line", "note"],
            "maximum_items": 4, "maximum_text_items": 4,
        },
        "cover": {
            "composition": {"artwork_flow": "one continuous source-derived abstract relationship moves from the title side to one right-side resolution", "visual_rhythm": {"purpose": "quiet entry, measured development, and one resolved focal area"}},
            "mandatory_avoid": ["body diagram", "collage", "logo reserve content", "recognizable entity", "representational illustration"],
        },
        "content_image": {
            "layout": {
                "title_region": {"x_min": 96, "x_max": 1104, "y_min": 72, "y_max": 152, "center_x": 600, "core_judgment_y": 106, "subtitle_y": 140},
                "content_stage": {"x_min": 72, "x_max": 1128, "y_min": 180, "y_max": 588},
                "white_space": {"content_stage_min_percent": 60, "content_stage_max_percent": 72, "outer_margin_min_percent": 10},
            },
            "composition": {
                "quiet_space_percent": {"min": 68, "max": 78}, "semantic_group_limit": 4,
                "supporting_elements": {"normal_min": 0, "normal_max": 3},
                "artwork_footprint": {"max_stage_width_percent": 44, "max_stage_height_percent": 44, "hero_scale": "small", "avoid": ["edge-to-edge hero", "oversized object", "lower-stage fill", "large cutaway hero"]},
            },
            "mandatory_avoid": ["dashboard", "card wall", "unrelated scenery", "logo reserve content"],
        },
    }


@lru_cache(maxsize=1)
def load_style_data() -> dict[str, Any]:
    try:
        markdown = STYLE_MARKDOWN.read_text(encoding="utf-8")
        sections = {match.group("name"): match.group("payload").strip() for match in SECTION_PATTERN.finditer(markdown)}
        required = {"shared", "cover", "body", "agenda", "closing", "annotation"}
        if set(sections) != required or any(not sections[name] for name in required):
            raise ValueError("style file requires exactly shared, cover, body, agenda, closing, and annotation direct-text sections")
        presentation_typography = load_presentation_typography(markdown)
        return {
            "schema_version": 3,
            "style_id": "simplemkt-editorial-direct-text",
            "prompt_contract": {
                "shared": ["shared_prompt"], "annotation": ["annotation"],
                "cover": ["cover_prompt"], "body": ["body_prompt"],
                "agenda": ["agenda_prompt"], "closing": ["closing_prompt"],
            },
            "sections": sections,
            "presentation_typography": presentation_typography,
            "dimensions": fixed_dimensions(),
            "raw_markdown": markdown,
            "diagnostic_markdown": PRESENTATION_TYPOGRAPHY_PATTERN.sub("", markdown).strip(),
        }
    except (OSError, ValueError) as error:
        raise SystemExit(f"invalid direct-text editorial style: {STYLE_MARKDOWN}: {error}") from error
