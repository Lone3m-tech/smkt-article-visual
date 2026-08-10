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
        "typography": {
            "chinese_family": "high-contrast Songti-like editorial serif",
            "core_judgment": {"weight": "semibold", "color": "#1A6B3A", "max_lines": 1, "alignment": "center"},
            "subtitle": {"weight": "regular", "color": "#6B6B6B", "max_lines": 1, "alignment": "center"},
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
            "layout": {
                "title_safe_zone": {"x_min": 72, "x_max": 852, "y_min": 250, "y_max": 414, "center_x": 462, "center_y": 337, "fill": "#FFFFFF"},
                "title": {"family": "high-contrast Songti-like editorial serif", "weight": "semibold", "color": "#1A6B3A", "max_lines": 2, "size_px": 64, "line_height_px": 78, "max_width_px": 780},
            },
            "composition": {"artwork_flow": "one continuous source-derived subject moves from the title side to one right-side resolution", "visual_rhythm": {"purpose": "quiet entry, measured development, and one resolved focal area"}},
            "mandatory_avoid": ["body diagram", "collage", "logo reserve content"],
        },
        "content_image": {
            "layout": {
                "title_region": {"x_min": 96, "x_max": 1104, "y_min": 72, "y_max": 152, "center_x": 600, "core_judgment_y": 106, "subtitle_y": 140},
                "content_stage": {"x_min": 72, "x_max": 1128, "y_min": 180, "y_max": 588},
                "white_space": {"content_stage_min_percent": 60, "content_stage_max_percent": 72, "outer_margin_min_percent": 10},
            },
            "composition": {
                "quiet_space_percent": {"min": 55, "max": 68}, "semantic_group_limit": 4,
                "supporting_elements": {"normal_min": 0, "normal_max": 3},
                "artwork_footprint": {"max_stage_width_percent": 64, "max_stage_height_percent": 62, "hero_scale": "medium", "avoid": ["edge-to-edge hero", "oversized object"]},
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
        return {
            "schema_version": 3,
            "style_id": "simplemkt-editorial-direct-text",
            "prompt_contract": {
                "shared": ["shared_prompt"], "annotation": ["annotation"],
                "cover": ["cover_prompt"], "body": ["body_prompt"],
                "agenda": ["agenda_prompt"], "closing": ["closing_prompt"],
            },
            "sections": sections,
            "dimensions": fixed_dimensions(),
            "raw_markdown": markdown,
        }
    except (OSError, ValueError) as error:
        raise SystemExit(f"invalid direct-text editorial style: {STYLE_MARKDOWN}: {error}") from error
