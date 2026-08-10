# Prompt templates

This file is the executable wording source for every compiled Prompt. The compiler may validate fields, select an applicable block, project Markdown-owned style guidance, and replace `{{placeholders}}`; it must not keep a second copy of these design instructions. Technical specifications and planning metadata are invisible production guidance, never visible artwork.

## Template contracts

<!-- smkt-template:cover-v1 -->
```json
{
  "role": "cover",
  "required_plan": ["source_support", "intent", "title", "core_promise", "primary_carrier", "visual_direction", "visual_progression", "must_show", "must_not_imply", "editorial_treatment", "scene_integrity"],
  "style_sections": ["shared", "cover"],
  "default_layout_variant": "text_left_carrier_right",
  "block_sequence": {
    "base": ["production-frame-v1", "visible-typography-v1", "cover-identity-v1", "cover-editorial-treatment-v1", "cover-semantics-v1", "scene-integrity-v1", "cover-no-annotation-v1"],
    "layout_variant": {
      "text_left_carrier_right": ["cover-layout-text-left-carrier-right-v1"],
      "text_right_carrier_left": ["cover-layout-text-right-carrier-left-v1"],
      "text_top_carrier_bottom": ["cover-layout-text-top-carrier-bottom-v1"],
      "text_centered": ["cover-layout-text-centered-v1"]
    },
    "tail": ["shared-editorial-v1"],
    "projection": {
      "default": [],
      "expanded": ["expanded-style-v1"],
      "full_diagnostic": ["full-diagnostic-style-v1"]
    },
    "delivery": ["delivery-v1"]
  }
}
```

<!-- smkt-template:body-v1 -->
```json
{
  "role": "body",
  "required_plan": ["source_support", "intent", "reader_block", "source_relation", "core_judgment", "subtitle", "grammar", "visual_solution", "must_show", "must_not_imply", "grammar_proof", "scene_integrity"],
  "style_sections": ["shared", "annotation", "body"],
  "block_sequence": {
    "base": ["production-frame-v1", "visible-typography-v1", "body-semantics-v1", "scene-integrity-v1", "body-grammar-v1", "grammar-proof-v1"],
    "grammar": {"comparison": ["comparison-v1"]},
    "source_mode": {"annotated_source": ["annotated-source-v1"]},
    "annotation": {"none": ["annotation-none-v1"], "present": ["annotation-plan-v1"]},
    "render_text": {"true": ["body-title-v1"], "false": ["body-titleless-v1"]},
    "tail": ["body-stage-v1", "shared-editorial-v1"],
    "projection": {
      "default": [],
      "expanded": ["expanded-style-v1"],
      "full_diagnostic": ["full-diagnostic-style-v1"]
    },
    "delivery": ["delivery-v1"]
  }
}
```

<!-- smkt-template:agenda-v1 -->
```json
{
  "role": "agenda",
  "required_plan": ["source_support", "intent", "title", "agenda_items", "must_show", "must_not_imply", "scene_integrity"],
  "style_sections": ["shared", "agenda"],
  "default_layout_variant": "centered_list",
  "block_sequence": {
    "base": ["production-frame-v1", "visible-typography-v1", "agenda-semantics-v1", "scene-integrity-v1", "agenda-identity-v1"],
    "layout_variant": {
      "centered_list": ["agenda-layout-centered-list-v1"],
      "split_list": ["agenda-layout-split-list-v1"],
      "vertical_rail": ["agenda-layout-vertical-rail-v1"],
      "stepped_list": ["agenda-layout-stepped-list-v1"]
    },
    "tail": ["shared-editorial-v1"],
    "projection": {
      "default": [],
      "expanded": ["expanded-style-v1"],
      "full_diagnostic": ["full-diagnostic-style-v1"]
    },
    "delivery": ["delivery-v1"]
  }
}
```

<!-- smkt-template:closing-v1 -->
```json
{
  "role": "closing",
  "required_plan": ["closing_text", "must_show", "must_not_imply", "scene_integrity"],
  "style_sections": ["shared", "closing"],
  "default_layout_variant": "editorial_signoff",
  "block_sequence": {
    "base": ["production-frame-v1", "visible-typography-v1", "scene-integrity-v1", "closing-identity-v1"],
    "layout_variant": {
      "editorial_signoff": ["closing-layout-editorial-signoff-v1"],
      "baseline_signoff": ["closing-layout-baseline-signoff-v1"],
      "echo_signoff": ["closing-layout-echo-signoff-v1"]
    },
    "tail": ["shared-editorial-v1"],
    "projection": {
      "default": [],
      "expanded": ["expanded-style-v1"],
      "full_diagnostic": ["full-diagnostic-style-v1"]
    },
    "delivery": ["delivery-v1"]
  }
}
```

## Executable Prompt blocks

<!-- smkt-prompt-block:production-frame-v1 -->
```text
Create one finished image for a source-faithful editorial presentation.

Priority: exact declared visible text; source meaning and exclusions; page-role layout; visual style.

All source notes and planning instructions are invisible guidance. Never render them as text.

Do not add visible text, claims, logos, watermarks, interface elements, or decorative elements unless this page explicitly declares them.
```

<!-- smkt-prompt-block:visible-typography-v1 -->
```text
Apply this page's visible typography exactly as stated here. Do not substitute, restate, or add another typography rule elsewhere in the image: {{page_typography}}
```

### A. Source semantics and non-misrepresentation

<!-- smkt-prompt-block:cover-semantics-v1 -->
```text
Everything in this block is invisible semantic direction, never visible text. Do not render, quote, label, or paraphrase any wording from it: {{plan_source_support}}. Turn its source-supported promise into the visual: {{plan_core_promise}}. The primary carrier is {{plan_primary_carrier}}. Make these source requirements visible: {{plan_must_show}}. Do not imply: {{plan_must_not_imply}}.
```

<!-- smkt-prompt-block:body-semantics-v1 -->
```text
Everything in this block is invisible semantic direction, never visible text. Do not render, quote, label, or paraphrase any wording from it: {{plan_source_support}}. The reader block is: {{plan_reader_block}}. Preserve this source relationship: {{plan_source_relation}}. Make the source relationship legible through this visual solution: {{plan_visual_solution}}. Show: {{plan_must_show}}. The title and subtitle may orient the reader but never prove this relationship; its proof must remain in the content stage. Explicitly do not imply: {{plan_must_not_imply}}.
```

<!-- smkt-prompt-block:agenda-semantics-v1 -->
```text
Everything in this block is invisible semantic direction, never visible text. The agenda is an orientation page, not a body grammar: use only this planned sequence of source-supported presentation beats: {{plan_source_support}}. Make these requirements visible: {{plan_must_show}}. Do not imply: {{plan_must_not_imply}}.
```

<!-- smkt-prompt-block:scene-integrity-v1 -->
```text
Scene integrity is non-negotiable: {{plan_scene_integrity}}.
```

<!-- smkt-prompt-block:comparison-v1 -->
```text
Make these source-supported comparison differences visibly distinct in objects, positions, connections, sequence, or boundaries: {{plan_comparison_basis}}.
```

<!-- smkt-prompt-block:annotated-source-v1 -->
```text
Use the supplied source asset only as annotated source material: {{plan_source_asset}}; do not fabricate a screenshot or substitute invented evidence.
```

### B. Structure and information encoding

<!-- smkt-prompt-block:cover-no-annotation-v1 -->
```text
Do not add labels, leaders, connectors, directional arrows, notes, relation words, source excerpts, data, microcopy, or any visible text beyond the exact cover title. The cover uses no annotation plan and must remain one editorial subject rather than a body diagram. A declared quiet trace is the sole permitted non-semantic graphic mark: it contains no text, arrow, metric, causal encoding, or claim.
```

<!-- smkt-prompt-block:body-grammar-v1 -->
```text
Use {{grammar_name}} as the one dominant visual grammar, never a second grammar. Its required topology is: {{grammar_topology_prompt}}. It must visibly prove: {{grammar_must_visually_prove}}. Generic symbols, anonymous nodes, or arrows alone do not prove the source relationship: every non-self-evident source step or term must be identified by the exact short label or note declared in this page's annotation plan. Do not substitute: {{grammar_forbidden_substitutions}}.
```

<!-- smkt-prompt-block:grammar-proof-v1 -->
```text
Make this selected grammar visibly provable in the finished image through these reader-visible facts: {{plan_grammar_proof}}. Each proof must be visible in the content stage itself, not supplied only by the title or subtitle. Do not let one generic illustrative scene substitute for this evidence.
```

<!-- smkt-prompt-block:annotation-none-v1 -->
```text
The page annotation plan is none. Use this only because every required source relationship is self-evident from its depicted object and position. Inside the content stage, add no local labels, leaders, connectors, directional lines, or notes beyond the source-derived visual relationship itself.
```

<!-- smkt-prompt-block:annotation-plan-v1 -->
```text
Apply only this page's declared information encoding:
{{plan_annotation_items}}
Render every declared visible label or note exactly once, even if its target groups multiple objects or regions. When a declared `label` and `note` have the same target, render them as one two-level callout: the exact label first, then the exact note directly beneath it in the declared note role. They share one local leader; never place either in a card, caption block, or separate detached text area. Its visual language is: {{annotation_appearance}} {{annotation_text}} {{annotation_restraint}} Do not add any annotation not declared here.
```

### C. Page identity

<!-- smkt-prompt-block:cover-identity-v1 -->
```text
Create a single cover image. The only visible text anywhere in the image is exactly: {{plan_title}}. Render it exactly once, with no subtitle or other text, with only readability-driven wrapping. The selected cover layout variant alone decides its placement. This instruction overrides every non-title sentence elsewhere in the Prompt. The title is the strongest visual element; never place artwork in its safe zone.

Use {{plan_visual_direction}} as the cover direction. Begin with this low-weight, source-derived entry: {{plan_progression_entry}}. Develop the same carrier as: {{plan_progression_development}}. Resolve it as: {{plan_progression_resolution}}. Follow the cover flow and rhythm: {{cover_artwork_flow}} {{cover_visual_rhythm}}.

Use one source-derived abstract editorial metaphor rather than a body diagram, data preview, card wall, collage, or representational illustration. The selected carrier may make one relationship and up to two source-supported states visible only through density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve. Never render a recognizable person, animal, product, tool, vehicle, building, landscape, plant, body part, or industry object. Do not use {{cover_mandatory_avoid}}.
```

<!-- smkt-prompt-block:cover-editorial-treatment-v1 -->
```text
Apply this required cover editorial treatment:
{{plan_editorial_treatment}}
All non-highlighted title characters are deep ink. The declared selection field is the title-level brand-green emphasis; any separate carrier accent is governed only by the cover visual style. This treatment may change the rhythm of the one exact title, but must never add, omit, reorder, paraphrase, or duplicate title characters. It is not a body annotation system, interface, diagram, or source claim.
```

<!-- smkt-prompt-block:cover-layout-text-left-carrier-right-v1 -->
```text
Use the text-left/carrier-right layout: left-align the exact title as one two-line block, vertically centered, in a continuous pure-white title-safe field that begins at the left safe margin and expands horizontally as the title requires. Keep the whole title-safe field clear, within the page safe margins and clear of the Logo reserve. Build one continuous abstract carrier on the right, with most visual mass held in the right half. The carrier may enter only unused whitespace and must yield to the complete adaptive title-safe field.
```

<!-- smkt-prompt-block:cover-layout-text-right-carrier-left-v1 -->
```text
Use the text-right/carrier-left layout: right-align the exact title as one two-line block, vertically centered, in a continuous pure-white title-safe field that ends at the right safe margin and expands leftward as the title requires. Keep the whole title-safe field clear, within the page safe margins and clear of the Logo reserve. Build one continuous abstract carrier on the left, with most visual mass held in the left half. The carrier may enter only unused whitespace and must yield to the complete adaptive title-safe field.
```

<!-- smkt-prompt-block:cover-layout-text-top-carrier-bottom-v1 -->
```text
Use the text-top/carrier-bottom layout: left-align the exact title as one two-line block in the upper third, not near the top edge, in a continuous pure-white title-safe band that expands horizontally as the title requires. Keep the whole band within the page safe margins and clear of the Logo reserve. Build one continuous abstract carrier below the title, with its visual mass held in the lower half. The carrier must yield to the complete adaptive title-safe band.
```

<!-- smkt-prompt-block:cover-layout-text-centered-v1 -->
```text
Use the text-centered layout: center the exact title as one two-line block both horizontally and vertically, in a continuous pure-white title-safe field that expands horizontally as the title requires. Keep the whole field within the page safe margins and clear of the Logo reserve. Do not create a distinct left, right, top, or bottom carrier; any abstract marks are only a very low-density peripheral echo, visibly secondary to the centered title and never inside its title-safe field.
```

<!-- smkt-prompt-block:agenda-identity-v1 -->
```text
Create a single presentation agenda image. Render exactly once as the agenda title: {{plan_title}}. Render exactly these numbered agenda items in this order, with no added, omitted, or paraphrased item:
{{plan_agenda_items}}
Do not render a subtitle, paragraph copy, source excerpt, or extra text.

{{plan_agenda_carrier}}
```

<!-- smkt-prompt-block:agenda-layout-centered-list-v1 -->
```text
Use the centered-list layout: center the title above one compact, evenly spaced vertical sequence of the exact numbered items. Keep the sequence narrow, calm, and clearly subordinate to the title.
```

<!-- smkt-prompt-block:agenda-layout-split-list-v1 -->
```text
Use the split-list layout: place the title as one calm left-side typographic anchor. Place the exact numbered items as one compact, evenly spaced vertical sequence in the right-side reading field. Keep the two fields visually connected by white space, not by a card, divider, or arrow.
```

<!-- smkt-prompt-block:agenda-layout-vertical-rail-v1 -->
```text
Use the vertical-rail layout: place the title in the upper-left field. Arrange the exact numbered items as three to five ordered anchors beside one thin quiet vertical rail in the central-to-right reading field. The rail has no arrowhead, label, metric, or claim; it is the only visual organizer of the sequence.
```

<!-- smkt-prompt-block:agenda-layout-stepped-list-v1 -->
```text
Use the stepped-list layout: place the title in the upper-left field. Set the exact numbered items as three to five compact steps progressing through a gentle descending diagonal. Use spacing and baseline shifts only to make the order legible; do not use an arrow, card, badge, or separate illustration.
```

<!-- smkt-prompt-block:closing-identity-v1 -->
```text
Create a single standard presentation closing image. The only visible text anywhere in the image is exactly: {{plan_closing_text}}. Render it exactly once, with no subtitle, call to action, source excerpt, or other text. The selected closing layout variant alone decides its placement.

{{plan_closing_carrier}}
```

<!-- smkt-prompt-block:closing-layout-editorial-signoff-v1 -->
```text
Use the editorial-signoff layout: place the closing message once as a calm compact block in the upper-left title-safe field. Render exactly one tiny non-semantic dry-ink end mark in lower-right non-Logo whitespace; it has no carrier, text, arrow, metric, or claim. Preserve a broad quiet field through the rest of the page.
```

<!-- smkt-prompt-block:closing-layout-baseline-signoff-v1 -->
```text
Use the baseline-signoff layout: place the closing message once in the lower-left safe field and anchor it with exactly one short, broken, low-contrast dry-ink baseline beneath it. The baseline is horizontal, non-directional, and visibly incomplete; it is not an underline, carrier, end mark, frame, arrow, metric, or claim. Render no other mark or graphic.
```

<!-- smkt-prompt-block:closing-layout-echo-signoff-v1 -->
```text
Use the echo-signoff layout: center the closing message with generous white space and place the one required low-density abstract carrier in lower-right whitespace. Do not add another end mark.
```

<!-- smkt-prompt-block:body-title-v1 -->
```text
Create a single explanatory body image. Render exactly once in the pure-white upper title region: {{plan_core_judgment}}, centered around the title-region center at x={{body_title_center_x}}; never left or right align it. Render exactly once directly below it: {{plan_subtitle}}, centered around that same center; never left or right align it. Treat the two lines as one centered text block. Keep this title region free of artwork, frame, and divider.
```

<!-- smkt-prompt-block:body-titleless-v1 -->
```text
Create a single titleless explanatory body image. Render no title or subtitle. Render only the exact labels or notes declared by this page's annotation plan; if its mode is none, render no text.
```

<!-- smkt-prompt-block:body-stage-v1 -->
```text
Keep all semantic elements inside one calm, asymmetric content cluster with {{body_quiet_space_min}}–{{body_quiet_space_max}}% quiet space, no more than {{body_semantic_group_limit}} semantic groups, and {{body_supporting_elements_min}}–{{body_supporting_elements_max}} supporting elements. Treat this as a hard layout constraint, not a preference: the full drawn cluster is a small editorial vignette surrounded by white paper. Vary the related objects' scale, spacing, and vertical placement; do not arrange them as an even row, mirrored pair, grid, card wall, or unrelated decorative collage. The drawn cluster occupies at most {{body_artwork_max_stage_width}}% of the content-stage width and {{body_artwork_max_stage_height}}% of its height. Use a {{body_hero_scale}} hero scale: scale down objects instead of enlarging one central object to explain internal detail; do not let a cutaway, product, person, or other primary object fill the lower content stage, reach the stage edges, or occupy more than two thirds of the cluster. Keep any declared labels and explanations local and subordinate. Split the page instead of adding competing structures when the relationship cannot remain legible. Do not use {{body_artwork_avoid}} or {{body_mandatory_avoid}}.
```

### D. Shared editorial language

<!-- smkt-prompt-block:shared-editorial-v1 -->
```text
Apply this direct production style prompt exactly. Follow the page-specific colour direction as an additional constraint:

{{style_page_prompt}}

Page-specific colour direction: {{plan_colour_direction}}
```

<!-- smkt-prompt-block:expanded-style-v1 -->
```text
For this expanded production pass, give extra weight to the direct production style prompt already provided; do not add new visual rules.
```

<!-- smkt-prompt-block:full-diagnostic-style-v1 -->
```text
This is a diagnostic render. Treat the complete style source below as internal invisible guidance: retain every applicable design intent, but never display its Markdown, JSON, field names, coordinates, colour codes, dimensions, limits, or examples as artwork or text.

{{style_full_diagnostic}}
```

### E. Delivery constraints

<!-- smkt-prompt-block:delivery-v1 -->
```text
Create one finished {{canvas_width}} by {{canvas_height}} 16:9 editorial image on an opaque flat pure-white {{canvas_background}} canvas. Keep the upper-right Logo reserve completely clear of {{logo_reserve_avoid}}. Render no Logo, wordmark, brand name, seal, signature, or watermark; the packaged transparent Logo is applied only after generation.

{{technical_specification_instruction}}
```
