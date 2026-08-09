---
name: smkt-article-visual
description: "Turn a finished or near-finished Markdown narrative—an article, talk, report, proposal, or workshop outline—into unified explanatory images. Use when the request explicitly asks for 文章配图, 文章视觉包, 文章封面, 正文解释图, or 连续讲述图."
---

# smkt-article-visual

## Inputs

```yaml
source_path: ./source.md
delivery_mode: article_package | presentation_frames
mode: plan | generate | qa
presentation_title:
presentation_output_root:
enable_qa: false
existing_assets: []
```

## Outputs

```text
<article_root | presentation_root>/assets/image/
├── cover.png
├── <image-id>.png
└── manifest.json
```

## Boundaries

- Keep source prose unchanged. In `article_package`, insert only accepted image Markdown; `presentation_frames` never edits source prose.
- Generate with the host `image_gen` capability. Do not redraw generated artwork with another renderer. The packaged finalizer may add the Logo only.
- Generated illustrations are explanatory artwork, never authentic screenshots, source images, or factual evidence.

## Page-centred manifest

`manifest.json` is a page record, not a collection of workflow buckets. Top level stores only package metadata; every page stores its own plan, Prompt, generation, finalization, placement, and QA fields. Fill those fields as work advances. Do not create top-level `plan`, `style`, `generate`, `logo`, `layout`, `placement`, `qa`, or global `stage` fields.

```json
{
  "schema_version": 6,
  "source_path": "article.md",
  "delivery_mode": "article_package",
  "pages": [
    {
      "id": "cover",
      "role": "cover",
      "status": "qa_passed",
      "plan": {
        "source_support": "article H1",
        "title": "exact source H1",
        "core_promise": "...",
        "visual_direction": "concise_metaphor",
        "must_show": ["..."]
      },
      "prompt": {
        "status": "compiled",
        "style_id": "simplemkt-editorial",
        "text": "complete actual Prompt sent to image_gen"
      },
      "generation": {
        "status": "generated",
        "candidate_file": "assets/image/cover.png"
      },
      "final": {
        "status": "finalized",
        "output_path": "assets/image/cover.png",
        "width_px": 1200,
        "height_px": 675,
        "logo": {"enabled": true, "status": "applied"}
      },
      "placement": {
        "status": "placed",
        "after": "article H1",
        "alt_text": "..."
      },
      "qa": {"status": "passed", "checks": []}
    },
    {
      "id": "figure-1",
      "role": "body_figure",
      "status": "planned",
      "plan": {
        "after": "exact paragraph anchor",
        "reader_question": "...",
        "core_judgment": "...",
        "subtitle": "...",
        "grammar": "flow",
        "must_show": ["..."]
      }
    }
  ]
}
```

Allowed per-page lifecycle values are `planned`, `prompt_ready`, `generated`, `finalized`, `placed`, `qa_passed`, `qa_failed`, and `qa_skipped`. A rework replaces only that page's `prompt`, `generation`, `final`, and later fields; retain a history only when the user asks.

## Workflow

### 1. Plan pages

Read [references/visual-grammar.md](references/visual-grammar.md) and `assets/simplemkt-editorial-style.json`. Read the title, argument path, reader obstacles, supplied assets, and existing Markdown images. Select images only for a mechanism, process, feedback loop, comparison, boundary, source figure, or conclusion that benefits from visual compression.

Create one `pages[]` item per selected image with `status: planned` and its `plan` object. The plan chooses the grammar from the original narrative; style never chooses or replaces it.

- A cover needs exact `title`, `core_promise`, and `visual_direction`; add `must_show` when the source requires non-negotiable visual details.
- An ordinary body figure needs exact `after`, `reader_question`, `core_judgment`, `subtitle`, `grammar`, and non-empty `must_show`. A deliberately titleless banner may instead use exact `before` plus `render_text: false`; it still needs the same semantic fields and must-show details.
- `comparison` also needs `comparison_basis` with visible source-supported differences.
- A supplied real asset needs `source_mode: annotated_source` and a resolvable `source_asset` from `existing_assets`.
- If a required field cannot be supported by the source, leave the page at `planned`, add `plan.issue`, and stop for clarification.

In `mode: plan`, show only the planned pages as Markdown tables and stop.

### 2. Compile each page Prompt

For every page with a ready `plan`, read the style contract and write `page.prompt = {status: "compiled", style_id, text}`. `text` is the complete actual Prompt; never store a shorthand such as “apply typography”. Set that page to `prompt_ready`. When `render_text: false`, keep the judgment and subtitle as plan metadata but explicitly forbid all rendered text; the title-color rule does not apply.

Keep essential content out of the Logo reserve. Every Prompt must forbid a model-rendered Logo, wordmark, watermark, technical annotation, UI, chart, dashboard, and unsupported visual structure. Append `dimensions.canvas.technical_specification_rendering_rule.instruction` verbatim.

- Cover Prompt: use the exact H1 or `presentation_title`, core promise, visual direction, source-derived hero, and cover rules. State that the title is brand green, appears exactly once, and uses only contract-approved line wrapping.
- Body Prompt: use that page's source anchor, reader question, `core_judgment`, `subtitle`, selected grammar, `must_show`, useful `avoid`, optional disclosure, and content-image rules. State explicitly that `core_judgment` appears once in brand green and `subtitle` appears once below it in neutral gray; never rely only on the typography contract. Preserve the selected grammar's topology and source-specific relationships.
- Apply the color system: recognizable real-world entities retain plausible gently desaturated local color; ordinary structural lines use the declared neutral colors; brand green is never an entity colour, default hatching, or decorative route.

### 3. Generate each page

Use `image_gen` with `page.prompt.text`. Write the generated image to the page's target path, then set:

```json
"generation": {"status": "generated", "candidate_file": "assets/image/<id>.png"}
```

Set only that page's status to `generated`. A failed generation writes `generation.status: "failed"` and `generation.issue`; it never changes another page.

### 4. Finalize canvas and Logo

Run the finalizer for each generated page. It reads only that page, preserves model-rendered text and artwork, normalizes the delivery size, and overlays the packaged transparent Logo when present.

```bash
python3 scripts/place_brand_wordmark.py <generated-image> <same-final-path> \
  --manifest <delivery_root>/assets/image/manifest.json \
  --image-id <image-id>
```

The script writes that page's `final` object and moves only that page to `finalized`.

### 5. Place pages

For `article_package`, put the cover immediately after the H1 and each ordinary body figure after its own exact `plan.after` anchor. A titleless banner goes before its exact `plan.before` anchor. Re-read the article and record `page.placement = {status, after|before, alt_text}`. For `presentation_frames`, leave source prose unchanged and record each page's accepted sequence. Set only that page to `placed`.

### 6. QA pages

When `enable_qa: true` or `mode: qa`, inspect each relevant page independently. Check source fidelity, selected grammar, exact text when text is rendered, brand-green core title and neutral-gray subtitle for titled body figures, readable hierarchy, natural entity colors, white canvas, no outer frame or title divider, no unsupported green connector, Logo state, output dimensions, and placement. Record `page.qa` with observable checks and issues, then set the page to `qa_passed` or `qa_failed`.

When `enable_qa: false`, write `page.qa = {"status": "skipped"}` after the page is otherwise delivered. The package is complete only when every planned page is `qa_passed` or `qa_skipped`; derive this result from `pages[]` rather than writing a global workflow stage.
