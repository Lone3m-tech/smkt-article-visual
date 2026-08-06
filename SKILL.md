---
name: smkt-article-visual
description: >
  Turn a finished or near-finished Markdown narrative—an article, talk, report, proposal, or workshop outline—into unified explanatory images.
  Use article_package for requests such as 给文章配封面和正文图、补正文配图、把图片插回文章, where images resolve local reading obstacles at paragraph anchors.
  Use presentation_frames for 把文章或演讲稿做成图片式PPT、连续讲述图、提案或课程演示, where images advance a presenter-led narrative.
  First identify the relevant obstacle or narrative beat, produce a reviewable visual framework, then after acceptance generate tactile editorial diagrams with image_gen.
  When delivery intent is ambiguous, default to article_package. Do not use for standalone mood images, platform-specific cover sets, article writing, publishing, research, logo design, or full PPTX/deck production.
---

# smkt-article-visual

## Inputs

```yaml
source_path: ./source.md                    # required Markdown narrative; article_package requires an H1
delivery_mode: article_package | presentation_frames  # infer from request; default: article_package
presentation_title:                         # required only when presentation_frames source has no H1
presentation_output_root:                   # optional; use a separate root when the source already owns an article package
mode: plan | generate | qa                  # default: plan
existing_assets: []                         # optional screenshots, diagrams, or source images
```

Require `source_path`; accept `article_path` as a backwards-compatible alias. Resolve `delivery_mode` from explicit user intent and default to `article_package` when it is unstated. Require a source H1 for `article_package`. In `presentation_frames`, require `presentation_title` only when the source has no H1. When the source root already contains an `article_package` manifest, require `presentation_output_root` so the two delivery packages remain separate.

## Outputs

- `article_package`: `<source_root>/assets/image/cover.png`, accepted content images at `<source_root>/assets/image/<figure-id>.png`, the source Markdown with those images placed at approved anchors, and one `<source_root>/assets/image/manifest.json`.
- `presentation_frames`: `<presentation_root>/assets/image/cover.png`, accepted content images at `<presentation_root>/assets/image/<frame-id>.png` in approved narrative order, an unchanged source Markdown file, and one `<presentation_root>/assets/image/manifest.json`.

## Boundaries

- Do not rewrite source prose. `article_package` inserts only the accepted cover and content-image Markdown; `presentation_frames` makes no source edits.
- Make article placement idempotent. Before inserting an output path, inspect only Markdown references to that exact path: insert when absent; retain or move the single existing reference to the accepted anchor; and stop for human resolution when multiple references exist. Never append a second reference or rewrite surrounding prose.
- Use the host `image_gen` capability for the underlying artwork. Do not use HTML, SVG, Python, or a second renderer to draw, typeset, composite, or repair the artwork. The sole exception is the deterministic Logo placement performed by `scripts/place_brand_wordmark.py` with the pinned Pillow dependency in `scripts/requirements.txt`; it may resample the canvas to its fixed contract dimensions and place only `assets/logo/simplemkt-logo-demo.png` at its fixed coordinates.
- Do not treat generated work as an authentic screenshot, source image, or factual evidence.

## Workflow

### 1. Plan the visual framework

Read [references/article-visual-plan.md](references/article-visual-plan.md) and [references/visual-grammar.md](references/visual-grammar.md). Before generating or editing the source, return the framework for the selected delivery mode and wait for user acceptance, unless the user explicitly asks to generate immediately.

Use one canonical framework for both delivery modes. `article_package` calls each `content_image` a **正文图** in user-facing output; `presentation_frames` calls it a **讲述图**. The generated image contract is identical.

```yaml
visual_plan:
  delivery_mode: article_package | presentation_frames
  cover:
    core_promise:
    visual_metaphor:
    title: exact_source_h1 | presentation_title
    presentation: ppt_cover
    title_breaks: deliberate_for_readability
    title_safe_zone:
    output_path: assets/image/cover.png
    generation_strategy:
      focus: document_entry | narrative_opening
      visual_emphasis:
    delivery:
      article_placement: after_h1 | null
      narrative_order: 0 | null
  content_images:
    - id:
      source_anchor:
      understanding_obstacle:
      core_judgment:
      visual_grammar:
      why_this_grammar:
      rejected_grammars: []
      why_needed:
      must_preserve: []
      visual_explanation_contract:
        visible_title:
        required_labels: []
        relation_words: []
        user_takeaway:
        source_detail_anchors: []
        illustrative_data_note:
      output_path:
      generation_strategy:
        focus: local_reading_comprehension | narrative_progression
        source_scope: one_paragraph | narrative_slice
        article:
          paragraph_anchor: string | null
          prose_to_offload: []
          avoid_repeating: []
        presentation:
          narrative_beat: hook | tension | mechanism | reframe | resolution | null
          previous_handoff: string | null
          next_bridge: string | null
          standalone_test: string | null
      delivery:
        article_placement: after_paragraph | null
        narrative_order: integer | null
```

Do not add a content image merely because a heading, paragraph, or speaking beat exists. A cover is required for both delivery modes. Every content image must clarify a mechanism, conditional choice, comparison, overlap, argument, sequence, feedback loop, boundary, hierarchy, temporal progression, continuum, or authorized source image. In `article_package`, require `generation_strategy.focus: local_reading_comprehension`, `source_scope: one_paragraph`, a populated `article` strategy, and `article_placement`. In `presentation_frames`, require `generation_strategy.focus: narrative_progression`, `source_scope: narrative_slice`, a populated `presentation` strategy, and `narrative_order`; the ordered content images must form one spoken narrative. The shared visual contract does not require the plans to choose the same images.

The YAML structure above is the sole canonical `visual_plan` format. [references/article-visual-plan.md](references/article-visual-plan.md) supplies the selection judgment only; do not copy, shorten, or extend it into a competing plan template.

Before entering `generate`, validate the selected plan against this template. Require every cover field and, for every content image, `id`, `source_anchor`, `understanding_obstacle`, `core_judgment`, `visual_grammar`, `why_this_grammar`, `rejected_grammars`, `why_needed`, `must_preserve`, every `visual_explanation_contract` field, `output_path`, every `generation_strategy` field, and every `delivery` field. In `article_package`, first require a source H1; require cover `generation_strategy.focus: document_entry`; require non-null `article_placement`, `article.paragraph_anchor`, `article.prose_to_offload`, and `article.avoid_repeating`; require all presentation-strategy and narrative-order fields to be null. In `presentation_frames`, first require an H1 or explicit `presentation_title`; require cover `generation_strategy.focus: narrative_opening` and `narrative_order: 0`; require unique increasing content-image `narrative_order` values plus non-null `presentation.narrative_beat`, `previous_handoff`, `next_bridge`, and `standalone_test`; require all article-strategy and article-placement fields to be null. Write article placements or narrative orders into their manifest `placement` records; do not infer either from filenames. Fill a missing field only from the source; otherwise stop for clarification. A direct-generation request skips plan acceptance, not plan formation or this completeness check.

### 2. Generate and place

#### 2.1 Prepare the run

- Treat the directory containing `source_path` as `source_root`. In `presentation_frames`, resolve `presentation_root` to `presentation_output_root` when supplied, otherwise `source_root`; it owns generated assets and the manifest while `source_path` stays read-only. Set `delivery_root` to `source_root` for `article_package` and to `presentation_root` for `presentation_frames`.
- Read `assets/simplemkt-editorial-style.md`.
- Run `python3 scripts/place_brand_wordmark.py --print-contract` before compiling any asset.
- Treat that script output as the sole source for Logo canvas, reserve, asset, size, and inset values.
- Finalize every asset at the fixed Logo-contract canvas dimensions reported by that script.
- Inject the exact reserve bounds into every prompt and verify every image-manifest Logo record against them.
- Block generation when the style file, Logo PNG, or contract output is missing or unusable.
- Before the first image, create the delivery-root `assets/image/manifest.json` with `schema_version: 2`, the Markdown-relative `source_path`, `delivery_mode`, and an `images` array. For `presentation_frames`, resolve source paths relative to `presentation_root`.

#### 2.2 Compile each prompt

- Compile every cover from the exact source H1 or explicit `presentation_title` using the shared PPT-cover contract: one prominent title in a continuous quiet safe zone plus one dominant visual metaphor. Render no text other than that exact title unless the user explicitly requests it. In `article_package`, make the metaphor act as a document entry; in `presentation_frames`, make it establish the narrative opening without adding title-external text.
- Compile every content image from the shared content-image contract: use `core_judgment` as its centered core judgment, preserve the selected grammar and source topology, and include the complete `visual_explanation_contract`. Then append only the selected mode's strategy block. In `article_package`, draw from the exact local paragraph, offload its declared reader obstacle, preserve `prose_to_offload`, and avoid repeating `avoid_repeating`. In `presentation_frames`, draw from the approved narrative slice, establish the core judgment after `previous_handoff`, make `next_bridge` credible, and pass `standalone_test`. Delivery mode changes image selection, source scope, semantic framing, information density, and composition strategy; it must not change the shared visual template.
- Compile every prompt from four blocks: role and required text, meaning, visual core drawn from `assets/simplemkt-editorial-style.md`, and risk-specific exclusions. Keep exclusions to six or fewer, normally one to three; use positive editorial vocabulary instead of pasting broad failure lists into the prompt.
- Keep QA-only material out of image prompts: manifest and placement checks, full anti-decoration variants, exclusion lists for unrelated grammars, and final Logo-placement receipts.
- Treat `assets/simplemkt-editorial-style.md` as the sole source for canvas, typography, title band, content-element vocabulary, material treatment, Logo reserve, and disclosure presentation. Inject those rules without restating or overriding their values in the plan or Prompt.
- Preserve every concrete `source_detail_anchor` as linked detail within the one dominant grammar structure. Never replace it with anonymous placeholder lines, generic tokens, or empty paper nodes whose labels carry all the meaning.
- Use supplied source lines whenever available. When a compact fictional illustrative paragraph, example, claim, number, date, percentage, source-like chart, or other illustrative content is clearer, permit it only with the exact lower-left small-gray-italic note `图中示例仅为解释用途，并非事实`. It must not masquerade as a real quote, source, or fact.

#### 2.3 Record and finalize each attempt

- Maintain one delivery-root `assets/image/manifest.json`; never create per-image Prompt or Logo-receipt sidecars. It is the sole delivery record for asset paths, selected delivery mode, exact placement or narrative order, every generation attempt, actual Prompt, adjustment reason, deterministic Logo result, QA outcome, and the accepted attempt.
- Use this compact manifest shape and append attempts instead of replacing them:

  ```json
  {
    "schema_version": 2,
    "source_path": "source.md",
    "delivery_mode": "article_package | presentation_frames",
    "images": [{
      "id": "figure-id",
      "role": "cover | content_image",
      "output_path": "assets/image/figure-id.png",
      "placement": {"kind": "after_h1 | after_paragraph | narrative_order", "anchor": "... | null", "sequence": "integer | null"},
      "accepted_attempt": null,
      "attempts": [{
        "id": 1,
        "prompt": "complete actual prompt",
        "status": "pending | generated | rejected | accepted",
        "adjustment_reason": "... | null",
        "candidate_file": "... | null",
        "logo": {"status": "pending | applied"}
      }]
    }]
  }
  ```

- Create one image record per planned cover or content image with `id`, `role`, `output_path`, and exact article placement or narrative order. In `presentation_frames`, record the cover as `placement.kind: narrative_order, sequence: 0` and each content image with its exact approved sequence.
- Append, never overwrite, one attempt before every generation.
- Give each attempt an increasing integer `id`, the complete actual `prompt`, `status` (`pending`, `generated`, `rejected`, or `accepted`), `adjustment_reason`, optional `candidate_file`, and `logo` state. Set it to `pending` before generation, then update it after the generation result is known.
- Use `null` for a first-pass adjustment reason. Require an adjustment reason for every rejection or rework.
- Retain a rejected candidate PNG only when the user asks to compare it later; otherwise retain its manifest record but no rejected image file.
- When Python 3.10+ and the pinned Pillow dependency are available, run:

  ```bash
  python3 scripts/place_brand_wordmark.py <underlying-image> assets/logo/simplemkt-logo-demo.png <final-image> \
    --article-manifest <delivery_root>/assets/image/manifest.json \
    --image-id <figure-id> --attempt-id <attempt-id>
  ```

- Use that finalizer to create the fixed-contract final asset and atomically record its Logo geometry.
- Do not auto-install dependencies, substitute another compositor, or continue without the Logo record.

#### 2.4 Place and accept

- In `article_package`, insert the cover immediately after the required H1 and insert each content image after its exact paragraph anchor using the idempotent placement rule.
- In `presentation_frames`, preserve source prose unchanged and verify the cover exists once at sequence `0`, followed by each content-image file once in approved narrative order.
- Use concise alt text that describes the image's explanatory role.
- After QA, mark exactly one attempt per image as `accepted` and set `accepted_attempt` to that ID.
- Mark every rejected attempt with its adjustment reason.
- Re-read the saved source. In `article_package`, verify every planned path resolves once and appears once at its planned location. In `presentation_frames`, verify no image Markdown was added, the cover path resolves once, and every approved content-image path resolves once before reporting completion.

### 3. QA and completion

#### Placement and manifest

- Verify every cover uses its exact approved title character-for-character, contains no other text unless explicitly requested, and follows the shared PPT-cover composition rather than a content-image layout.
- In `article_package`, verify the cover exists once at the document opening and every content image exists once after its planned anchor; article prose is unchanged. In `presentation_frames`, verify the cover resolves once at sequence `0`, there is one resolving content-image file for every approved sequence item, the sequence forms the approved narrative, the source prose is unchanged, and no image Markdown was inserted.
- In `article_package`, verify each content image resolves its declared local reader obstacle, visibly offloads its declared nearby prose, and does not merely restate that paragraph. In `presentation_frames`, verify each content image establishes its declared beat after the previous handoff, can pass its standalone test, and makes the planned next bridge credible.
- In `presentation_frames`, verify the cover's `core_promise` is introduced by the first content image, no adjacent content images repeat the same core judgment or grammar without an explicit reason, and the final `user_takeaway` resolves the cover promise.
- Verify the one image manifest has one record per planned cover or content image, records the selected delivery mode, a complete Prompt and outcome for every attempt, one accepted attempt per image, and a Logo record matching the fixed contract.
- Verify every rejected or reworked attempt has an adjustment reason. Rejected candidates must have no image file unless explicitly retained for comparison.

#### Meaning, structure, and typography

- Verify every content image reads as planned core judgment → short explanation → one grammar-matched structure → evidence note when needed.
- Verify the labels, relation words, user takeaway, and concrete source-detail anchors required by the plan remain visible in that structure.
- Verify Chinese uses one editorial-serif family, English uses only the restrained companion face, and no semantic text is handwritten.
- On 1200×675 content images, verify: 52px semibold green core judgment; 28px regular gray subtitle; 32px medium structural heading; 28px regular paper-node label; 16px italic gray note.
- Verify the core judgment and subtitle share horizontal center `x=600`, both remain within `y=76–176`, and no diagram element begins above `y=200`.

#### Content-element and material contract

- Verify each non-text element uses its assigned excerpt-sheet, narrow-paper-strip, cut-paper-field, or direct-ink vocabulary.
- Verify each core element visibly depicts its role-specific source detail. Reject empty or interchangeable paper nodes.
- Reject invented icons, machines, containers, abstract patterns, and mixed paper families.
- When an engraving or pencil-sketch subject appears, verify direct labels, leaders, and anchor points semantically annotate it. Direct labels and guides must not receive paper-node shadows.
- Verify every paper primitive has the specified deliberately faint floating depth. Reject card, panel, sticker, UI-container, dark-shadow, mixed-elevation, and decorative-grid treatment.

#### Logo, disclosure, and finish

- Verify every final asset matches the fixed Logo-contract canvas dimensions, contains only the packaged Logo at the contract coordinates, and has no model-rendered duplicate wordmark.
- Verify title and subtitle bounds never intersect the fixed top-right Logo reserve.
- Reject a content image when its title/subtitle band is not fixed at centered `x=600`, `y=76–176`, starts before the 16px gap beneath the Logo reserve, or shares the top row with the Logo.
- When a figure uses non-factual illustrative text, claim, number, date, percentage, source-like chart, or other example, verify the exact lower-left 16px italic `#8C8C8C` note `图中示例仅为解释用途，并非事实`.
- Verify pure-white canvas separately from diagram material richness.
- Reject source-topology loss, unresolved or duplicate asset paths, and unplanned decorative registration marks, corner crosses, floating strokes, isolated color blocks, or ornamental arrows.

Do not report generation or delivery complete merely because image files exist. Complete only when the framework was accepted or generation was explicitly requested; in `article_package`, the saved article contains one resolving cover and one resolving content image for every planned anchor; in `presentation_frames`, the cover resolves first, every approved content image resolves once in its approved narrative order, and the source remains unchanged; all assets and the selected delivery mode pass the one QA checklist; and no planned image is missing or unrelated. Image models are probabilistic, so this guarantees the same visual contract—not byte-identical pixels across model versions.
