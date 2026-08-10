#!/usr/bin/env python3
"""Compile one page Prompt by binding Markdown-owned contracts."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from style_contract import load_style_data


COMPILER_VERSION = 10
TEMPLATE_FILE = Path(__file__).resolve().parent.parent / "references" / "prompt-templates.md"
GRAMMAR_FILE = Path(__file__).resolve().parent.parent / "references" / "visual-grammar.md"
TEMPLATE_CONTRACT_PATTERN = re.compile(
    r"<!--\s*smkt-template:(?P<name>[a-z0-9-]+)\s*-->\s*```json\s*(?P<payload>.*?)\s*```",
    re.DOTALL,
)
PROMPT_BLOCK_PATTERN = re.compile(
    r"<!--\s*smkt-prompt-block:(?P<name>[a-z0-9-]+)\s*-->\s*```text\s*(?P<payload>.*?)\s*```",
    re.DOTALL,
)
GRAMMAR_PATTERN = re.compile(
    r"<!--\s*smkt-grammar:(?P<name>[a-z_]+)\s*-->\s*```json\s*(?P<payload>.*?)\s*```",
    re.DOTALL,
)
PLACEHOLDER_PATTERN = re.compile(r"{{(?P<name>[a-z0-9_]+)}}")
ROLE_ALIASES = {
    "cover": "cover",
    "body": "body",
    "body_figure": "body",
    "agenda": "agenda",
    "closing": "closing",
}
PROJECTION_MODES = {"default", "expanded", "full_diagnostic"}
ANNOTATION_TYPES = {"label", "leader", "connector", "directional_line", "note"}


def write_json_atomically(path: Path, payload: dict[str, Any]) -> None:
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary_path, path)


def natural_value(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(natural_value(item) for item in value)
    if isinstance(value, str):
        return value.replace("_", " ")
    return str(value)


def required_string(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"plan requires non-empty {field}")
    return value.strip()


def required_list(payload: dict[str, Any], field: str, *, non_empty: bool) -> list[Any]:
    value = payload.get(field)
    if not isinstance(value, list) or (non_empty and not value):
        raise ValueError(f"plan requires {'non-empty ' if non_empty else ''}list {field}")
    return value


def iter_block_references(value: Any):
    """Yield template-owned block names from a declarative block sequence."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from iter_block_references(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_block_references(item)
    else:
        raise ValueError("template block_sequence values must be strings, lists, or objects")


def sequence_blocks(sequence: dict[str, Any], field: str, key: str | None = None, *, allow_empty: bool = False) -> list[str]:
    value = sequence.get(field)
    if key is not None:
        if not isinstance(value, dict):
            raise ValueError(f"template block_sequence.{field} must map conditions to blocks")
        if key not in value and allow_empty:
            return []
        value = value.get(key)
    if not isinstance(value, list) or (not allow_empty and not value) or any(not isinstance(name, str) or not name for name in value):
        label = f"{field}.{key}" if key is not None else field
        raise ValueError(f"template block_sequence.{label} must be a non-empty block list")
    return value


def load_prompt_templates() -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    try:
        markdown = TEMPLATE_FILE.read_text(encoding="utf-8")
        contract_matches = list(TEMPLATE_CONTRACT_PATTERN.finditer(markdown))
        block_matches = list(PROMPT_BLOCK_PATTERN.finditer(markdown))
        contracts = {match.group("name"): json.loads(match.group("payload")) for match in contract_matches}
        blocks = {match.group("name"): match.group("payload").strip() for match in block_matches}
        if len(contracts) != len(contract_matches) or len(blocks) != len(block_matches):
            raise ValueError("template contract and block names must be unique")
        expected_templates = {"cover-v1", "body-v1", "agenda-v1", "closing-v1"}
        if set(contracts) != expected_templates or any(not text for text in blocks.values()):
            raise ValueError("template contracts require cover-v1, body-v1, agenda-v1, closing-v1, and non-empty blocks")
        for template_name, template in contracts.items():
            sequence = template.get("block_sequence")
            if not isinstance(sequence, dict):
                raise ValueError(f"template requires block_sequence: {template_name}")
            references = list(iter_block_references(sequence))
            if not references or not set(references) <= set(blocks):
                raise ValueError(f"template sequence references unknown blocks: {template_name}")
        return contracts, blocks
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid prompt template contract: {TEMPLATE_FILE}: {error}") from error


def load_grammar_contracts() -> dict[str, dict[str, Any]]:
    try:
        markdown = GRAMMAR_FILE.read_text(encoding="utf-8")
        matches = list(GRAMMAR_PATTERN.finditer(markdown))
        contracts = {match.group("name"): json.loads(match.group("payload")) for match in matches}
        if not contracts or len(contracts) != len(matches):
            raise ValueError("visual grammar names must be present and unique")
        for name, contract in contracts.items():
            if not isinstance(contract.get("topology_prompt"), str) or not contract["topology_prompt"].strip():
                raise ValueError(f"grammar requires topology_prompt: {name}")
            for field in ("use_when", "not_for", "must_visually_prove", "forbidden_substitutions", "recommended_encodings"):
                if not isinstance(contract.get(field), list) or not contract[field]:
                    raise ValueError(f"grammar requires non-empty {field}: {name}")
            encodings = set(contract["recommended_encodings"])
            if not encodings <= ANNOTATION_TYPES:
                raise ValueError(f"grammar has unsupported recommended encoding: {name}")
            if not isinstance(contract.get("directional_line_allowed"), bool):
                raise ValueError(f"grammar requires directional_line_allowed: {name}")
            if contract["directional_line_allowed"] != ("directional_line" in encodings):
                raise ValueError(f"grammar directional-line declaration conflicts: {name}")
        return contracts
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid visual grammar contract: {GRAMMAR_FILE}: {error}") from error


def load_page(manifest_path: Path, image_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("schema_version") not in {6, 7, 8, 9} or not isinstance(manifest.get("pages"), list):
            raise ValueError("manifest requires schema 6, 7, 8, or 9 and pages[]")
        if manifest.get("delivery_mode") not in {"article_package", "presentation_frames"}:
            raise ValueError("manifest requires delivery_mode article_package or presentation_frames")
        page = next((item for item in manifest["pages"] if item.get("id") == image_id), None)
        if not isinstance(page, dict):
            raise ValueError(f"page is not planned: {image_id}")
        if page.get("status") not in {"planned", "prompt_ready"}:
            raise ValueError(f"page must be planned or prompt_ready before compilation: {image_id}")
        if not isinstance(page.get("plan"), dict):
            raise ValueError(f"page requires plan: {image_id}")
        if page.get("role") not in ROLE_ALIASES:
            raise ValueError(f"page role must be cover, body, agenda, or closing: {image_id}")
        return manifest, page
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid page-centred manifest: {manifest_path}: {error}") from error


def validate_annotation_plan(plan: dict[str, Any], role: str, grammar: dict[str, Any] | None, style: dict[str, Any]) -> dict[str, Any]:
    raw = plan.get("annotation_plan")
    if raw is None:
        if role == "body":
            raise ValueError("body plan requires an explicit annotation_plan")
        normalized = {"mode": "none", "items": [], "limits": {"max_items": 0, "max_text_items": 0}}
    else:
        if not isinstance(raw, dict):
            raise ValueError("annotation_plan must be an object")
        mode = raw.get("mode")
        items = raw.get("items", [])
        limits = raw.get("limits", {})
        if mode not in {"none", "minimal", "required"}:
            raise ValueError("annotation_plan.mode must be none, minimal, or required")
        if not isinstance(items, list) or not isinstance(limits, dict):
            raise ValueError("annotation_plan requires items[] and limits{}")
        normalized = {"mode": mode, "items": items, "limits": limits}

    if role != "body":
        if normalized["mode"] != "none" or normalized["items"]:
            raise ValueError(f"{role} annotation_plan must use mode none with no items")
        return normalized

    if normalized["mode"] == "none":
        if normalized["items"]:
            raise ValueError("annotation_plan.mode none cannot contain items")
        if grammar and grammar["topology_prompt"].startswith("Make the source-supported ordered steps"):
            raise ValueError("flow body requires a label or note for its source-supported steps")
        return normalized
    if not normalized["items"]:
        raise ValueError("annotation_plan minimal or required needs at least one item")

    annotation_style = style["dimensions"]["annotation"]
    limits = normalized["limits"]
    max_items = limits.get("max_items", annotation_style["maximum_items"])
    max_text_items = limits.get("max_text_items", annotation_style["maximum_text_items"])
    if not isinstance(max_items, int) or not isinstance(max_text_items, int) or max_items < 1 or max_text_items < 0:
        raise ValueError("annotation_plan limits must be non-negative integers")
    if max_items > annotation_style["maximum_items"] or max_text_items > annotation_style["maximum_text_items"]:
        raise ValueError("annotation_plan limits exceed the style maximum")
    if len(normalized["items"]) > max_items:
        raise ValueError("annotation_plan has more items than max_items")

    allowed_by_grammar = set(grammar["recommended_encodings"])
    text_items = 0
    for item in normalized["items"]:
        if not isinstance(item, dict):
            raise ValueError("annotation_plan items must be objects")
        annotation_type = item.get("type")
        if annotation_type not in ANNOTATION_TYPES or annotation_type not in annotation_style["allowed_types"]:
            raise ValueError("annotation_plan item has unsupported type")
        if annotation_type not in allowed_by_grammar:
            raise ValueError(f"annotation type {annotation_type} is not recommended by the selected grammar")
        if annotation_type == "directional_line" and not grammar["directional_line_allowed"]:
            raise ValueError("selected grammar does not allow directional_line")
        required_string(item, "target")
        required_string(item, "source_support")
        content = item.get("content", "")
        if not isinstance(content, str):
            raise ValueError("annotation_plan item content must be text")
        if annotation_type in {"label", "note"} and not content.strip():
            raise ValueError(f"annotation type {annotation_type} requires content")
        if content.strip():
            text_items += 1
    if text_items > max_text_items:
        raise ValueError("annotation_plan has more text items than max_text_items")
    if grammar and grammar["topology_prompt"].startswith("Make the source-supported ordered steps") and not any(
        item["type"] in {"label", "note"} for item in normalized["items"]
    ):
        raise ValueError("flow body requires at least one label or note for its source-supported steps")
    return normalized


def validate_scene_integrity(plan: dict[str, Any]) -> dict[str, Any]:
    raw = plan.get("scene_integrity")
    if not isinstance(raw, dict):
        raise ValueError("scene_integrity must be an object")
    mode = raw.get("mode")
    if mode not in {"representational", "abstract"}:
        raise ValueError("scene_integrity.mode must be representational or abstract")
    if mode == "abstract":
        required_string(raw, "rationale")
        return raw
    subject_count = raw.get("subject_count")
    if not isinstance(subject_count, int) or subject_count < 1:
        raise ValueError("representational scene_integrity requires subject_count of at least 1")
    for field in ("continuity_rules", "forbidden"):
        values = required_list(raw, field, non_empty=True)
        if any(not isinstance(value, str) or not value.strip() for value in values):
            raise ValueError(f"scene_integrity {field} must contain non-empty text")
    return raw


def validate_grammar_proof(plan: dict[str, Any], role: str) -> None:
    if role != "body":
        return
    raw = plan.get("grammar_proof")
    if not isinstance(raw, dict):
        raise ValueError("body plan requires grammar_proof")
    evidence = required_list(raw, "visible_evidence", non_empty=True)
    if len(evidence) < 2 or any(not isinstance(value, str) or not value.strip() for value in evidence):
        raise ValueError("grammar_proof requires at least two non-empty visible_evidence statements")


def validate_agenda_items(plan: dict[str, Any]) -> None:
    items = required_list(plan, "agenda_items", non_empty=True)
    if not 3 <= len(items) <= 5:
        raise ValueError("agenda requires three to five agenda_items")
    titles: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("agenda_items must contain objects")
        title = item.get("title")
        source_support = item.get("source_support")
        if not isinstance(title, str) or not title.strip() or not isinstance(source_support, str) or not source_support.strip():
            raise ValueError("agenda_items require non-empty title and source_support")
        normalized_title = title.strip()
        if normalized_title in titles:
            raise ValueError("agenda_items titles must be unique")
        titles.add(normalized_title)


def resolve_colour_plan(plan: dict[str, Any], role: str, scene_integrity: dict[str, Any]) -> dict[str, Any]:
    """Resolve the two standard green modes without adding a page-plan field."""
    raw = plan.get("colour_plan")
    if isinstance(raw, dict):
        return raw
    if raw is not None:
        raise ValueError("colour_plan must be an object")

    if role == "cover" and scene_integrity["mode"] == "representational":
        raw = {
            "mode": "brand_green_subject_fill",
            "local_colours": [{
                "target": "one or two connected local regions of the cover's primary carrier",
                "colour_family": "brand green",
                "rationale": "representational covers prioritize one translucent dry-brush subject fill",
            }],
            "limits": {"max_local_colours": 1, "gradients": "forbidden", "coverage": "primary_subject_partial_fill"},
        }
    else:
        raw = {
            "mode": "brand_green_accent",
            "local_colours": [{
                "target": "one tiny semantic detail or source-supported auxiliary relationship",
                "colour_family": "brand green",
                "rationale": "the default mode keeps green subordinate to the source relationship",
            }],
            "limits": {"max_local_colours": 1, "gradients": "forbidden", "coverage": "small_detail_only"},
        }
    plan["colour_plan"] = raw
    return raw


def validate_colour_plan(plan: dict[str, Any], role: str, scene_integrity: dict[str, Any]) -> None:
    raw = resolve_colour_plan(plan, role, scene_integrity)
    mode = raw.get("mode")
    if mode not in {"brand_green_accent", "brand_green_subject_fill", "small_optional_spot", "source_factual", "monochrome_exception"}:
        raise ValueError("colour_plan.mode must be brand_green_accent, brand_green_subject_fill, small_optional_spot, source_factual, or monochrome_exception")
    local_colours = raw.get("local_colours")
    limits = raw.get("limits")
    expected_coverage = "primary_subject_partial_fill" if mode == "brand_green_subject_fill" else "small_detail_only"
    if not isinstance(limits, dict) or limits.get("max_local_colours") != 1 or limits.get("gradients") != "forbidden" or limits.get("coverage") != expected_coverage:
        raise ValueError(f"colour_plan limits require max_local_colours 1, gradients forbidden, and coverage {expected_coverage}")
    if mode == "brand_green_subject_fill" and scene_integrity["mode"] != "representational":
        raise ValueError("brand_green_subject_fill requires a representational scene_integrity")
    if mode == "monochrome_exception":
        if local_colours not in (None, []):
            raise ValueError("monochrome_exception cannot declare local_colours")
        required_string(raw, "rationale")
        return
    if not isinstance(local_colours, list) or len(local_colours) != 1:
        raise ValueError("colour_plan requires exactly one local_colour")
    for item in local_colours:
        if not isinstance(item, dict):
            raise ValueError("colour_plan local_colours must contain objects")
        for field in ("target", "colour_family"):
            required_string(item, field)
        required_string(item, "source_support" if mode == "source_factual" else "rationale")
        if mode == "brand_green_subject_fill" and item["colour_family"].strip().casefold() != "brand green":
            raise ValueError("brand_green_subject_fill requires colour_family brand green")


def format_colour_plan(plan: dict[str, Any]) -> str:
    raw = plan.get("colour_plan")
    if raw is None:
        return "No optional spot colour is declared. Use only pure white, deep ink, restrained gray, and at most one small brand-green semantic accent."
    if raw["mode"] == "monochrome_exception":
        return f'This source requires a monochrome exception: {raw["rationale"].strip()}. Use no local colours.'
    if raw["mode"] == "brand_green_subject_fill":
        item = raw["local_colours"][0]
        return (
            f'{item["target"].strip()}: use brand green only on one primary subject, across one or two connected local regions, '
            f'as one translucent uneven dry-brush or wax-pencil gesture with substantial white paper visible, justified by {item["rationale"].strip()}. '
            "Keep the deep-ink contour dominant. Do not follow interior seams or material boundaries; use no green relation line, second green subject, secondary green detail, opaque fill, gradient, shadow, or material rendering."
        )
    evidence_key = "source_support" if raw["mode"] == "source_factual" else "rationale"
    values = [
        f'{item["target"].strip()}: one tiny flat {item["colour_family"].strip()} accent detail only, justified by {item[evidence_key].strip()}'
        for item in raw["local_colours"]
    ]
    return "; ".join(values) + "; keep it visually minor, never a hero or main-object fill; use no gradients and no more than one local colour."


def format_scene_integrity(plan: dict[str, Any]) -> str:
    raw = plan["scene_integrity"]
    if raw["mode"] == "abstract":
        return f'Use an abstract non-embodied composition only: {raw["rationale"].strip()}.'
    continuity = "; ".join(value.strip() for value in raw["continuity_rules"])
    forbidden = "; ".join(value.strip() for value in raw["forbidden"])
    return f'Depict exactly {raw["subject_count"]} complete embodied subject(s). Continuity rules: {continuity}. Never depict: {forbidden}.'


def format_grammar_proof(plan: dict[str, Any], role: str) -> str:
    if role != "body":
        return "No body grammar proof is required for this page."
    return "; ".join(value.strip() for value in plan["grammar_proof"]["visible_evidence"])


def format_agenda_items(plan: dict[str, Any]) -> str:
    return "\n".join(
        f'{index}. "{item["title"].strip()}"'
        for index, item in enumerate(plan["agenda_items"], start=1)
    )


def validate_plan(plan: dict[str, Any], template: dict[str, Any], role: str, delivery_mode: str, grammars: dict[str, dict[str, Any]], style: dict[str, Any]) -> dict[str, Any]:
    for field in template["required_plan"]:
        if field == "must_show":
            required_list(plan, field, non_empty=True)
        elif field == "must_not_imply":
            required_list(plan, field, non_empty=False)
        elif field == "visual_progression":
            progression = plan.get(field)
            if not isinstance(progression, dict):
                raise ValueError("cover requires visual_progression")
            for key in ("entry", "development", "resolution"):
                required_string(progression, key)
        elif field == "agenda_items":
            validate_agenda_items(plan)
        elif field not in {"grammar_proof", "scene_integrity"}:
            required_string(plan, field)

    grammar = None
    if role in {"agenda", "closing"} and delivery_mode != "presentation_frames":
        raise ValueError(f"{role} is available only in presentation_frames delivery mode")
    if role == "body":
        if delivery_mode == "article_package":
            required_string(plan, "source_anchor")
        else:
            required_string(plan, "source_slice")
            for field in ("beat", "previous_handoff", "next_bridge"):
                required_string(plan, field)
        if plan["grammar"] not in grammars:
            raise ValueError(f"body grammar has no contract: {plan['grammar']}")
        grammar = grammars[plan["grammar"]]
        if plan["grammar"] == "comparison" and len(required_list(plan, "comparison_basis", non_empty=True)) < 2:
            raise ValueError("comparison body requires at least two comparison_basis conditions")
        if plan.get("source_mode") == "annotated_source":
            required_string(plan, "source_asset")
    scene_integrity = validate_scene_integrity(plan)
    validate_grammar_proof(plan, role)
    validate_colour_plan(plan, role, scene_integrity)
    return validate_annotation_plan(plan, role, grammar, style)


def format_annotation_items(annotation_plan: dict[str, Any]) -> str:
    items: list[str] = []
    for item in annotation_plan["items"]:
        visible = f'render exactly "{item["content"].strip()}"' if item.get("content", "").strip() else "render no text"
        items.append(f'{item["type"]} targets {item["target"].strip()}; {visible}; source support: {item["source_support"].strip()}')
    return "\n".join(f"- {item}" for item in items)


def build_context(plan: dict[str, Any], dimensions: dict[str, Any], role: str, delivery_mode: str, grammar: dict[str, Any] | None, annotation_plan: dict[str, Any], style: dict[str, Any]) -> dict[str, str]:
    canvas = dimensions["canvas"]
    output = canvas["output_contract"]
    logo = dimensions["logo"]
    color = dimensions["color_system"]
    visual = dimensions["visual_language"]
    materials = dimensions["materials"]
    linework = dimensions["linework"]
    series = dimensions["series"]
    context = {
        "canvas_width": str(output["width_px"]),
        "canvas_height": str(output["height_px"]),
        "canvas_background": output["background_color"],
        "logo_reserve_avoid": natural_value(logo["prompt_avoid_in_reserve"]),
        "technical_specification_instruction": canvas["technical_specification_rendering_rule"]["instruction"],
        "series_focus": series["focus"],
        "brand_color": color["semantic_layer"]["brand_color"],
        "visual_rendering_mode": visual["rendering_mode"],
        "visual_rendering_avoid": natural_value(visual["rendering_avoid"]),
        "visual_ink_line_character": visual["ink_line_character"],
        "visual_black_mass_role": visual["black_mass_role"],
        "visual_spot_colour_policy": visual["spot_colour_policy"],
        "visual_treatment": natural_value(visual["treatment"]),
        "visual_principles": natural_value(visual["principles"]),
        "materials_allowed": natural_value(materials["editorial_patina"]["allowed"]),
        "materials_forbidden": natural_value(materials["editorial_patina"]["forbidden"]),
        "linework_forbidden": natural_value(linework["forbidden"]),
        "linework_surface_variation": linework["surface_variation"],
        "series_avoid": natural_value(series["avoid"] + visual["avoid"]),
        "plan_colour_direction": format_colour_plan(plan),
        "plan_scene_integrity": format_scene_integrity(plan),
        "plan_grammar_proof": format_grammar_proof(plan, role),
        "plan_source_support": str(plan.get("source_support", "")),
        "plan_must_show": natural_value(plan["must_show"]),
        "plan_must_not_imply": natural_value(plan["must_not_imply"]) or "anything beyond the source-supported relationship",
        "annotation_appearance": dimensions["annotation"]["appearance"],
        "annotation_text": dimensions["annotation"]["text"],
        "annotation_restraint": dimensions["annotation"]["restraint"],
        "plan_annotation_items": format_annotation_items(annotation_plan),
        "style_full_diagnostic": style["raw_markdown"].strip(),
        "style_page_prompt": "\n\n".join(
            part for part in (
                style["sections"]["shared"],
                style["sections"][role],
                style["sections"]["annotation"] if role == "body" and annotation_plan["mode"] != "none" else "",
            ) if part
        ),
    }
    if role == "cover":
        cover = dimensions["cover"]
        title = cover["layout"]["title"]
        progression = plan["visual_progression"]
        context.update({
            "plan_title": plan["title"], "cover_title_color": title["color"],
            "cover_title_family": title["family"], "cover_title_weight": title["weight"],
            "cover_title_max_lines": str(title["max_lines"]),
            "plan_visual_direction": plan["visual_direction"].replace("_", " "),
            "plan_core_promise": plan["core_promise"], "plan_primary_carrier": plan["primary_carrier"],
            "plan_progression_entry": progression["entry"], "plan_progression_development": progression["development"],
            "plan_progression_resolution": progression["resolution"],
            "cover_artwork_flow": cover["composition"]["artwork_flow"],
            "cover_visual_rhythm": cover["composition"]["visual_rhythm"]["purpose"],
            "cover_mandatory_avoid": natural_value(cover["mandatory_avoid"]),
            "style_expanded_guidance": "",
        })
        return context

    if role == "agenda":
        context.update({
            "plan_title": plan["title"],
            "plan_agenda_items": format_agenda_items(plan),
            "style_expanded_guidance": "",
        })
        return context

    if role == "closing":
        context.update({
            "plan_closing_text": plan["closing_text"],
            "style_expanded_guidance": "",
        })
        return context

    body = dimensions["content_image"]
    typography = dimensions["typography"]
    core = typography["core_judgment"]
    subtitle = typography["subtitle"]
    context.update({
        "plan_core_judgment": plan["core_judgment"], "plan_subtitle": plan["subtitle"],
        "body_title_family": typography["chinese_family"], "body_core_weight": core["weight"],
        "body_core_color": core["color"], "body_core_max_lines": str(core["max_lines"]),
        "body_core_alignment": core["alignment"], "body_subtitle_weight": subtitle["weight"],
        "body_subtitle_color": subtitle["color"], "body_subtitle_max_lines": str(subtitle["max_lines"]),
        "body_subtitle_alignment": subtitle["alignment"],
        "body_title_center_x": str(body["layout"]["title_region"]["center_x"]),
        "grammar_name": plan["grammar"].replace("_", " "),
        "grammar_topology_prompt": grammar["topology_prompt"],
        "grammar_must_visually_prove": natural_value(grammar["must_visually_prove"]),
        "grammar_forbidden_substitutions": natural_value(grammar["forbidden_substitutions"]),
        "plan_reader_block": plan["reader_block"],
        "plan_source_relation": plan["source_relation"], "plan_visual_solution": plan["visual_solution"],
        "body_quiet_space_min": str(body["composition"]["quiet_space_percent"]["min"]),
        "body_quiet_space_max": str(body["composition"]["quiet_space_percent"]["max"]),
        "body_semantic_group_limit": str(body["composition"]["semantic_group_limit"]),
        "body_supporting_elements_min": str(body["composition"]["supporting_elements"]["normal_min"]),
        "body_supporting_elements_max": str(body["composition"]["supporting_elements"]["normal_max"]),
        "body_artwork_max_stage_width": str(body["composition"]["artwork_footprint"]["max_stage_width_percent"]),
        "body_artwork_max_stage_height": str(body["composition"]["artwork_footprint"]["max_stage_height_percent"]),
        "body_hero_scale": body["composition"]["artwork_footprint"]["hero_scale"],
        "body_artwork_avoid": natural_value(body["composition"]["artwork_footprint"]["avoid"]),
        "body_mandatory_avoid": natural_value(body["mandatory_avoid"]),
        "plan_comparison_basis": natural_value(plan.get("comparison_basis", [])),
        "plan_source_asset": str(plan.get("source_asset", "")),
        "style_expanded_guidance": "",
    })
    return context


def render_block(name: str, blocks: dict[str, str], context: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group("name")
        if key not in context:
            raise ValueError(f"prompt block {name} references unknown placeholder: {key}")
        return context[key]
    rendered = PLACEHOLDER_PATTERN.sub(replace, blocks[name]).strip()
    if PLACEHOLDER_PATTERN.search(rendered):
        raise ValueError(f"prompt block {name} has unresolved placeholders")
    return rendered


def compile_prompt(page: dict[str, Any], style: dict[str, Any], delivery_mode: str) -> tuple[str, str, list[str], str]:
    plan = page["plan"]
    role = ROLE_ALIASES[page["role"]]
    template_id = f"{role}-v1"
    templates, blocks = load_prompt_templates()
    grammars = load_grammar_contracts()
    template = templates[template_id]
    expected_sections = {
        "cover": ["shared", "cover"],
        "body": ["shared", "annotation", "body"],
        "agenda": ["shared", "agenda"],
        "closing": ["shared", "closing"],
    }[role]
    if template.get("role") != role or template.get("style_sections") != expected_sections:
        raise ValueError(f"template contract mismatch: {template_id}")
    annotation_plan = validate_plan(plan, template, role, delivery_mode, grammars, style)
    grammar = grammars[plan["grammar"]] if role == "body" else None
    context = build_context(plan, style["dimensions"], role, delivery_mode, grammar, annotation_plan, style)
    projection_mode = page.get("prompt_projection", "default")
    if projection_mode not in PROJECTION_MODES:
        raise ValueError("prompt_projection must be default, expanded, or full_diagnostic")
    sequence = template["block_sequence"]

    block_names = sequence_blocks(sequence, "base")
    if role == "body":
        block_names += sequence_blocks(sequence, "grammar", plan["grammar"], allow_empty=True)
        if plan.get("source_mode"):
            block_names += sequence_blocks(sequence, "source_mode", plan["source_mode"], allow_empty=True)
        annotation_key = "none" if annotation_plan["mode"] == "none" else "present"
        block_names += sequence_blocks(sequence, "annotation", annotation_key)
        text_key = "false" if plan.get("render_text") is False else "true"
        block_names += sequence_blocks(sequence, "render_text", text_key)
        block_names += sequence_blocks(sequence, "tail")
    block_names += sequence_blocks(sequence, "projection", projection_mode, allow_empty=True)
    block_names += sequence_blocks(sequence, "delivery")

    included_rules = style["prompt_contract"]["shared"] + style["prompt_contract"][role]
    if role == "body":
        included_rules.append(f"grammar:{plan['grammar']}")
        if annotation_plan["mode"] != "none":
            included_rules.append("annotation")
    included_rules.append(f"projection:{projection_mode}")
    return "\n\n".join(render_block(name, blocks, context) for name in block_names), template_id, included_rules, projection_mode


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile one article-visual page Prompt from Markdown-owned contracts.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--image-id", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(arguments)


def main(arguments: list[str]) -> int:
    parsed = parse_arguments(arguments)
    manifest, page = load_page(parsed.manifest, parsed.image_id)
    style = load_style_data()
    try:
        prompt_text, template_id, included_rules, projection_mode = compile_prompt(page, style, manifest["delivery_mode"])
    except ValueError as error:
        raise SystemExit(f"cannot compile page Prompt: {page['id']}: {error}") from error
    if parsed.dry_run:
        print(prompt_text)
        return 0
    page["prompt"] = {
        "status": "compiled", "compiler_version": COMPILER_VERSION, "template_id": template_id,
        "projection_mode": projection_mode, "style_id": style["style_id"],
        "style_source": "assets/simplemkt-editorial-style.md",
        "grammar_source": "references/visual-grammar.md" if ROLE_ALIASES[page["role"]] == "body" else None,
        "included_rules": included_rules, "text": prompt_text,
    }
    page["status"] = "prompt_ready"
    write_json_atomically(parsed.manifest, manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
