#!/usr/bin/env python3
"""Verify that compiler de-duplication keeps every displaced rule covered."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from compile_page_prompt import compile_prompt, load_grammar_contracts
from style_contract import load_style_data


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEMO_MANIFEST = SKILL_ROOT / "examples" / "demo-article" / "assets" / "image" / "manifest.json"
EXPECTED_REMOVALS = {
    "cover": ["cover:Cover composition", "cover:Cover typography", "cover:Cover abstract treatment"],
    "outer-dry-inner-wet": ["body:Body composition", "annotation:Visible text"],
    "open-absorb-ventilate": ["body:Body composition", "annotation:Visible text"],
}


def require(text: str, needle: str, page_id: str) -> None:
    if needle not in text:
        raise AssertionError(f"{page_id}: missing preserved rule: {needle}")


def main() -> int:
    manifest = json.loads(DEMO_MANIFEST.read_text(encoding="utf-8"))
    style = load_style_data()
    grammars = load_grammar_contracts()
    previous_total = 0
    compact_total = 0

    for page in manifest["pages"]:
        page_id = page["id"]
        previous = page.get("prompt", {}).get("text")
        if not isinstance(previous, str) or not previous:
            raise AssertionError(f"{page_id}: demo baseline Prompt is missing")
        prompt, _, _, projection_mode, removed = compile_prompt(page, style, manifest["delivery_mode"])
        if projection_mode != "default":
            raise AssertionError(f"{page_id}: expected default projection")
        if removed != EXPECTED_REMOVALS[page_id]:
            raise AssertionError(f"{page_id}: unexpected de-duplication trace: {removed}")
        if len(prompt) >= len(previous):
            raise AssertionError(f"{page_id}: Prompt did not become shorter")

        require(prompt, page["plan"]["source_support"], page_id)
        for fact in page["plan"]["must_show"]:
            require(prompt, fact, page_id)

        if page["role"] == "cover":
            for needle in (
                "Create a single cover image.",
                "The title is the strongest visual element",
                "Use one source-derived abstract editorial metaphor",
                "only through density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve",
                "title-safe field",
                "The sole selection field keeps its thin brand-green outline and may end with up to two small terminal dots",
                "within at most 3% of the abstract carrier area",
                "Never render a recognizable person, animal, product, tool, vehicle, building, landscape, plant, body part, or industry object.",
            ):
                require(prompt, needle, page_id)
        else:
            grammar = grammars[page["plan"]["grammar"]]
            require(prompt, grammar["topology_prompt"], page_id)
            for fact in page["plan"]["grammar_proof"]["visible_evidence"]:
                require(prompt, fact, page_id)
            for needle in (
                "Use one primary object plus two to four source-supported related objects, states, or parts",
                "let one meaningful near-overlap, unequal gap, or partial crop create tension",
                "68–78% quiet space",
                "44% of the content-stage width",
                "Render every declared visible label or note exactly once",
                "Attach every label or note to its target",
                "Do not use landscape, trees, plants, animals, people, or architecture as filler",
            ):
                require(prompt, needle, page_id)
            if prompt.count("68–78% quiet space") != 1 or prompt.count("44% of the content-stage width") != 1:
                raise AssertionError(f"{page_id}: body layout rule is still duplicated")

        previous_total += len(previous)
        compact_total += len(prompt)

    reduction = 1 - compact_total / previous_total
    if reduction < 0.10:
        raise AssertionError(f"demo Prompt reduction is only {reduction:.1%}; expected at least 10%")
    print(
        f"prompt de-duplication passed: {previous_total} -> {compact_total} characters "
        f"({reduction:.1%} reduction); all displaced-rule coverage checks passed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
