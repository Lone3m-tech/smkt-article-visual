# Prompt templates

This file is the executable wording source for every compiled Prompt. The compiler may validate fields, select an applicable block, project Markdown-owned style guidance, and replace `{{placeholders}}`; it must not keep a second copy of these design instructions. Technical specifications and planning metadata are invisible production guidance, never visible artwork.

## Template contracts

<!-- smkt-template:cover-v1 -->
```json
{
  "role": "cover",
  "required_plan": ["source_support", "intent", "title", "core_promise", "primary_carrier", "visual_direction", "visual_progression", "must_show", "must_not_imply", "editorial_treatment", "scene_integrity"],
  "style_sections": ["shared", "cover"],
  "block_sequence": {
    "base": ["cover-identity-v1", "cover-editorial-treatment-v1", "cover-semantics-v1", "scene-integrity-v1", "cover-no-annotation-v1", "shared-editorial-v1"],
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
    "base": ["body-semantics-v1", "scene-integrity-v1", "body-grammar-v1", "grammar-proof-v1"],
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
  "block_sequence": {
    "base": ["agenda-semantics-v1", "scene-integrity-v1", "agenda-identity-v1", "shared-editorial-v1"],
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
  "block_sequence": {
    "base": ["scene-integrity-v1", "closing-identity-v1", "shared-editorial-v1"],
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
Its visual language is: {{annotation_appearance}} {{annotation_text}} {{annotation_restraint}} Do not add any annotation not declared here.
```

### C. Page identity

<!-- smkt-prompt-block:cover-identity-v1 -->
```text
Create a single cover image. The only visible text anywhere in the image is exactly: {{plan_title}}. Render it exactly once, with no subtitle or other text, in {{cover_title_color}}, {{cover_title_family}}, {{cover_title_weight}}, left aligned in a continuous pure-white title-safe zone occupying the left 40% of the canvas. Keep it to at most two lines with only readability-driven wrapping, and vertically center the complete title block in that left field. This instruction overrides every non-title sentence elsewhere in the Prompt. The title is the strongest visual element; never place artwork in its safe zone.

Use {{plan_visual_direction}} as the cover direction. Build one continuous left-to-right reading movement from the title side toward a right-side resolution. Begin outside the title zone with this low-weight, source-derived entry: {{plan_progression_entry}}. Develop the same carrier as: {{plan_progression_development}}. Resolve it as: {{plan_progression_resolution}}. Keep the semantic illustration primarily in the right 55% of the canvas. Its low-density, nonessential edge may extend into the remaining left whitespace by no more than 20% of the illustration area, but never into the title-safe zone. Follow the cover flow and rhythm: {{cover_artwork_flow}} {{cover_visual_rhythm}}.

Use one source-derived abstract editorial metaphor rather than a body diagram, data preview, card wall, collage, or representational illustration. The right-side carrier may make one relationship and up to two source-supported states visible only through density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve. Never render a recognizable person, animal, product, tool, vehicle, building, landscape, plant, body part, or industry object. Do not use {{cover_mandatory_avoid}}.
```

<!-- smkt-prompt-block:cover-editorial-treatment-v1 -->
```text
Apply this required cover editorial treatment:
{{plan_editorial_treatment}}
All non-highlighted title characters are deep ink. The sole declared selection field is the only brand-green area anywhere on the cover. This treatment may change the rhythm of the one exact title, but must never add, omit, reorder, paraphrase, or duplicate title characters. It is not a body annotation system, interface, diagram, or source claim.
```

<!-- smkt-prompt-block:agenda-identity-v1 -->
```text
Create a single presentation agenda image. Render exactly once as the centered agenda title: {{plan_title}}. Render exactly these numbered agenda items in this order, with no added, omitted, or paraphrased item:
{{plan_agenda_items}}
Do not render a subtitle, paragraph copy, source excerpt, or extra text.
```

<!-- smkt-prompt-block:closing-identity-v1 -->
```text
Create a single standard presentation closing image. The only visible text anywhere in the image is exactly: {{plan_closing_text}}. Render it exactly once, centered, with no subtitle, call to action, source excerpt, or other text.
```

<!-- smkt-prompt-block:body-title-v1 -->
```text
Create a single explanatory body image. Render exactly once in the pure-white upper title region: {{plan_core_judgment}}. Use the core-title role: {{body_title_family}}, {{body_core_weight}}, {{body_core_color}}, at most {{body_core_max_lines}} line, {{body_core_alignment}} aligned around the title-region center at x={{body_title_center_x}}; never left or right align it. Render exactly once directly below it: {{plan_subtitle}}. Use the subtitle role: {{body_subtitle_weight}}, {{body_subtitle_color}}, at most {{body_subtitle_max_lines}} line, {{body_subtitle_alignment}} aligned around that same center; never left or right align it. Treat the two lines as one centered text block. Keep this title region free of artwork, frame, and divider.
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
