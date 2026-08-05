---
name: smkt-article-visual
description: >
  Turn a finished or near-finished Markdown article into one unified-style cover and the necessary explanatory body images.
  First identify every reader obstacle worth visualizing, produce a reviewable visual framework, then after acceptance
  generate tactile editorial diagrams with image_gen and write them into their exact article positions. Use for 给文章配封面和正文解释图、给文章做配图框架、补正文配图、重做文章配图 or 图文并茂.
  Do not use for standalone images, platform-specific cover sets, article writing, publishing, research, logo design, or decks.
---

# smkt-article-visual

Generate one cover and the necessary body figures that make an article easier to understand. The core plans the visual logic; every asset shares one SimpleMkt editorial art direction, while the cover uses a PPT-cover composition and body figures use explanatory-diagram compositions.

## Inputs

```yaml
article_path: ./article.md                  # required
mode: plan | generate | qa                  # default: plan
existing_assets: []                         # optional screenshots, diagrams, or source images
```

The Markdown article is the only required content input. Before planning or generating, read `assets/simplemkt-editorial-style.md`: it supplies the shared SimpleMkt editorial art direction and the separate cover/body composition rules. The cover and body figures must look like one series through their white canvas, palette, typography, linework, material cues, and wordmark, but they must not use the same layout. Pure white constrains the canvas only; it does not mean outline-only line art. Treat the shared art direction as the default visual language.

## Boundaries

- Do not require or inspect a Brief, Theme, Series, CMS frontmatter, platform field, publishing state, or account.
- Do not rewrite article prose. Insert only the accepted cover and body-image Markdown.
- Treat the directory containing `article_path` as `article_root`. Finalize every cover and body figure at the fixed Logo-contract canvas dimensions reported by `scripts/place_brand_wordmark.py --print-contract`. Save the cover as `<article_root>/assets/image/cover.png` and insert the Markdown-relative path `assets/image/cover.png` immediately after the H1. If the article has no H1, insert it immediately after frontmatter.
- Save each body figure as `<article_root>/assets/image/<figure-id>.png` and insert it immediately after its accepted paragraph anchor.
- Make every placement idempotent. Before inserting an output path, inspect only Markdown references to that exact path: insert when absent; retain or move the single existing reference to the accepted anchor; and stop for human resolution when multiple references exist. Never append a second reference or rewrite surrounding prose.
- Maintain one article-level `<article_root>/assets/image/manifest.json`; never create per-image Prompt or Logo-receipt sidecars. It is the sole delivery record for asset paths, exact placement, every generation attempt, actual Prompt, adjustment reason, deterministic Logo result, QA outcome, and the accepted attempt.
- Use the host `image_gen` capability for the underlying artwork. Do not use HTML, SVG, Python, or a second renderer to draw, typeset, composite, or repair the artwork. The sole exception is the deterministic Logo placement performed by `scripts/place_brand_wordmark.py` with the pinned Pillow dependency in `scripts/requirements.txt`; it may resample the canvas to its fixed contract dimensions and place only `assets/logo/simplemkt-logo-demo.png` at its fixed coordinates.
- Do not treat generated work as an authentic screenshot, source image, or factual evidence.

Use this compact manifest shape; append attempts instead of replacing them:

```json
{
  "schema_version": 1,
  "article_path": "article.md",
  "images": [{
    "id": "figure-id",
    "role": "cover | body_figure",
    "output_path": "assets/image/figure-id.png",
    "placement": {"kind": "after_h1 | after_paragraph", "anchor": "..."},
    "accepted_attempt": 2,
    "attempts": [{
      "id": 1,
      "prompt": "complete actual prompt",
      "status": "rejected | generated | accepted",
      "adjustment_reason": "... | null",
      "candidate_file": "... | null",
      "logo": {"status": "pending | applied"}
    }]
  }]
}
```

## Required framework first

Read [references/article-visual-plan.md](references/article-visual-plan.md) and [references/visual-grammar.md](references/visual-grammar.md). Before generating or editing the article, return this framework and wait for user acceptance, unless the user explicitly asks to generate immediately:

```yaml
visual_plan:
  cover:
    article_judgment:
    visual_metaphor:
    title: exact_article_h1
    presentation: ppt_cover
    title_breaks: deliberate_for_readability
    title_safe_zone:
    output_path: assets/image/cover.png
    placement: after_h1
  body_figures:
    - id:
      paragraph_anchor:
      reader_problem:
      visual_grammar:
      why_this_grammar:
      rejected_grammars: []
      why_needed:
      must_preserve: []
      visual_explanation_contract:
        visible_title:
        required_labels: []
        relation_words: []
        reader_takeaway:
        source_detail_anchors: []
        illustrative_data_note:
      output_path:
```

Do not add a body image merely because a heading exists. A cover is required; every body figure must clarify a mechanism, conditional choice, comparison, overlap, argument, sequence, feedback loop, boundary, hierarchy, temporal progression, continuum, or authorized source image.

## Generate and place

### 1. Prepare the run

- Read `assets/simplemkt-editorial-style.md`.
- Run `python3 scripts/place_brand_wordmark.py --print-contract` before compiling any asset.
- Treat that script output as the sole source for Logo canvas, reserve, asset, size, and inset values.
- Inject the exact reserve bounds into every prompt and verify every article-manifest Logo record against them.
- Block generation when the style file, Logo PNG, or contract output is missing or unusable.
- Before the first image, create `<article_root>/assets/image/manifest.json` with `schema_version`, the Markdown-relative `article_path`, and an `images` array.

### 2. Compile each prompt

- Read the article H1 and compile one independent prompt for the cover and every accepted body figure.
- Render the cover H1 character-for-character. Permit deliberate line breaks only for readability; never shorten, rewrite, reorder, or substitute it.
- Use the cover-specific PPT-cover composition: one prominent title in a continuous quiet safe zone plus one dominant visual metaphor. Do not turn it into an explanatory diagram.
- Preserve the selected body-figure grammar and any supplied source topology.
- Include the complete `visual_explanation_contract`. Treat `visible_title` as the centered core judgment, not a section heading.
- For every 1200×675 body figure, inject the fixed title/subtitle band: shared center `x=600`, vertical bounds `y=76–176`, 16px below the Logo reserve ending at `y=60`; reserve `y=200–675` for the diagram. Do not left-align or top-left-align either line.
- Preserve every concrete `source_detail_anchor` as linked detail within the one dominant grammar structure. Never replace it with anonymous placeholder lines, generic tokens, or empty paper nodes whose labels carry all the meaning.
- Apply the typography contract to every visible string. Reject mixed Chinese font styles and handwritten semantic text.
- Use a pure `#FFFFFF` canvas with no tint or texture.
- Derive an annotated editorial engraving or pencil-sketch subject from the selected grammar and source-detail anchors. Do not default to botanical, animal, or generic-object metaphors.
- Assign every non-text element to the fixed editorial vocabulary. Make every core element visibly depict its assigned role instead of relying on a label alone. Do not invent icons, machines, containers, or abstract patterns.
- Use direct labels and leaders by default. Use construction lines only when they clarify the subject.
- Do not add decorative registration marks, corner crosses, floating strokes, isolated color blocks, or any element that does not communicate a planned label, relation, or structure.
- Reserve the exact top-right Logo zone as pure white. Do not let the model render a wordmark, title, subtitle, label, connector, or diagram element there.
- Use supplied source lines whenever available. When a compact fictional illustrative paragraph, example, claim, number, date, percentage, source-like chart, or other illustrative content is clearer, permit it only with the exact lower-left small-gray-italic note `图中示例仅为解释用途，并非事实`. It must not masquerade as a real quote, source, or fact.

### 3. Record and finalize each attempt

- Create one image record per planned figure with `id`, `role`, `output_path`, and exact `placement`.
- Append, never overwrite, one attempt before every generation.
- Give each attempt an increasing integer `id`, the complete actual `prompt`, `status` (`generated`, `rejected`, or `accepted`), `adjustment_reason`, optional `candidate_file`, and `logo` state.
- Use `null` for a first-pass adjustment reason. Require an adjustment reason for every rejection or rework.
- Retain a rejected candidate PNG only when the user asks to compare it later; otherwise retain its manifest record but no rejected image file.
- When Python 3.10+ and the pinned Pillow dependency are available, run:

  ```bash
  python3 scripts/place_brand_wordmark.py <underlying-image> assets/logo/simplemkt-logo-demo.png <final-image> \
    --article-manifest <article_root>/assets/image/manifest.json \
    --image-id <figure-id> --attempt-id <attempt-id>
  ```

- Use that finalizer to create the fixed-contract final asset and atomically record its Logo geometry.
- Do not auto-install dependencies, substitute another compositor, or continue without the Logo record.

### 4. Place and accept

- Insert the cover after the H1 and each body image after its exact paragraph anchor using the idempotent placement rule.
- Use concise alt text that describes the image's explanatory role.
- After QA, mark exactly one attempt per image as `accepted` and set `accepted_attempt` to that ID.
- Mark every rejected attempt with its adjustment reason.
- Re-read saved Markdown. Verify every planned path resolves once and appears once at its planned location before reporting completion.

## QA and completion

### Placement and manifest

- Verify the cover exists once at the document opening, uses the article H1 character-for-character, and follows PPT-cover composition rather than a body-figure layout.
- Verify every body image exists once after its planned anchor and article prose is unchanged.
- Verify the one article image manifest has one record per planned figure, a complete Prompt and outcome for every attempt, one accepted attempt per image, and a Logo record matching the fixed contract.
- Verify every rejected or reworked attempt has an adjustment reason. Rejected candidates must have no image file unless explicitly retained for comparison.

### Meaning, structure, and typography

- Verify every body figure reads as planned core judgment → short explanation → one grammar-matched structure → evidence note when needed.
- Verify the labels, relation words, takeaway, and concrete source-detail anchors required by the plan remain visible in that structure.
- Verify Chinese uses one editorial-serif family, English uses only the restrained companion face, and no semantic text is handwritten.
- On 1200×675 body figures, verify: 52px semibold green core judgment; 28px regular gray subtitle; 32px medium structural heading; 28px regular paper-node label; 16px italic gray note.
- Verify the core judgment and subtitle share horizontal center `x=600`, both remain within `y=76–176`, and no diagram element begins above `y=200`.

### Content-element and material contract

- Verify each non-text element uses its assigned excerpt-sheet, narrow-paper-strip, cut-paper-field, or direct-ink vocabulary.
- Verify each core element visibly depicts its role-specific source detail. Reject empty or interchangeable paper nodes.
- Reject invented icons, machines, containers, abstract patterns, and mixed paper families.
- When an engraving or pencil-sketch subject appears, verify direct labels, leaders, and anchor points semantically annotate it. Direct labels and guides must not receive paper-node shadows.
- Verify every paper primitive has the specified deliberately faint floating depth. Reject card, panel, sticker, UI-container, dark-shadow, mixed-elevation, and decorative-grid treatment.

### Logo, disclosure, and finish

- Verify every final asset matches the fixed Logo-contract canvas dimensions, contains only the packaged Logo at the contract coordinates, and has no model-rendered duplicate wordmark.
- Verify title and subtitle bounds never intersect the fixed top-right Logo reserve.
- Reject a body figure when its title/subtitle band is not fixed at centered `x=600`, `y=76–176`, starts before the 16px gap beneath the Logo reserve, or shares the top row with the Logo.
- When a figure uses non-factual illustrative text, claim, number, date, percentage, source-like chart, or other example, verify the exact lower-left 16px italic `#8C8C8C` note `图中示例仅为解释用途，并非事实`.
- Verify pure-white canvas separately from diagram material richness.
- Reject source-topology loss, unresolved or duplicate asset paths, and unplanned decorative registration marks, corner crosses, floating strokes, isolated color blocks, or ornamental arrows.

Do not report generation or delivery complete merely because image files exist. Complete only when the framework was accepted or generation was explicitly requested, the saved article contains one resolving cover and one resolving image for every planned figure at their exact anchors, all assets and placements pass QA, and no planned image is missing or unrelated. Image models are probabilistic, so this guarantees the same visual contract—not byte-identical pixels across model versions.
