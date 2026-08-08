---
name: smkt-article-visual
description: "Turn a finished or near-finished Markdown narrative—an article, talk, report, proposal, or workshop outline—into unified explanatory images. Use when the request explicitly asks for 文章配图, 文章视觉包, 文章封面, 正文解释图, or 连续讲述图."
---

# smkt-article-visual

## Inputs
```y
source_path: ./source.md                    # required Markdown narrative; article_package requires an H1
delivery_mode: article_package | presentation_frames  # article_package by default; presentation_frames only on an explicit presentation request
mode: plan | generate | qa                    # default: plan
presentation_title:                         # required only when presentation_frames source has no H1
presentation_output_root:                   # optional; use a separate root when the source already owns an article package
enable_qa: false                            # optional during generate; adds a basic report, time, and token use
existing_assets: []                         # optional screenshots, diagrams, or source images
```

## Outputs
```te
<source_path>                           # article_package：插入已接受图片；presentation_frames：保持不修改

<article_root | presentation_root>/     # article_package 使用 article_root；presentation_frames 使用 presentation_root
└── assets/image/
    ├── cover.png
    ├── <image-id>.png                 # article_package：正文图；presentation_frames：按已批准顺序排列的讲述图
    └── manifest.json
```

## Execution boundaries

- **Source:** Keep source prose unchanged. `article_package` may insert accepted image Markdown; `presentation_frames` makes no source edits.
- **Placement:** Each article image appears at its approved anchor once. No reference → insert; one reference → retain or move; multiple references → stop for human resolution.
- **Artwork:** Generate the image with the host `image_gen` capability. Do not redraw or repair it with another renderer; the packaged finalizer may apply the Logo afterward, but must preserve all model-rendered cover and body text.
- **Evidence:** Treat generated images as illustrations, never as authentic screenshots, source images, or factual evidence.

## Workflow

### 1. Scan and write `plan`
Read [references/visual-grammar.md](references/visual-grammar.md) and `assets/simplemkt-editorial-style.json`. Resolve the delivery root, then create `<delivery_root>/assets/image/manifest.json`. This is the only plan and run record. Apply the style contract's composition budget without duplicating its values here.

Select assets with these judgments:

- Scan the title, opening, argument path, understanding obstacles, supplied source visuals, and—for `article_package`—existing Markdown images.
- Use `article_package` whenever the user asks for 文章配图、文章封面、正文图、文章视觉包, or provides only a Markdown article. Use `presentation_frames` only when the user explicitly requests a presentation, slides, deck, PPT, presentation frames, or supplies `delivery_mode: presentation_frames`; narrative structure alone never changes an article into presentation frames.
- Consider a content image for a mechanism, process, feedback loop, easily confused concept, comparison, boundary, source figure, or conclusion that benefits from structural compression. Skip transitions, already-clear lists or tables, heading repetition, dense exact text, and unsupported factual or screenshot claims.
- Give the cover one promise: identify and invite reading of an article package, or establish the premise of a presentation sequence.
- For each figure, identify its exact source support, local understanding obstacle, one conclusion, selected grammar, and source details that must remain visible. Add `disclosure` only for a real source or dataset that needs attribution, or for invented, non-factual example content; omit it for ordinary source-grounded explanatory illustrations.
- Every image must depict only the selected visual grammar and its source-supported `must_show` relationships. Do not introduce a chart, plot, bar chart, line chart, pie chart, table, dashboard, analytics panel, or other visual structure that is not a supported grammar of this Skill, whether as content, decoration, screenshot, or placeholder.
- In `article_package`, offload the difficult part of one exact paragraph and place the image with minimal interruption. In `presentation_frames`, use supported narrative beats with explicit handoffs, no new claims, and a sequence that resolves the cover promise.


Use one staged JSON contract. Each step adds or updates only its own top-level section; do not prefill future sections, copy the same field into several sections, or create another plan file. A completed article-package manifest has this shape:
```j
{
  "schema_version": 5,
  "source_path": "article.md",
  "delivery_mode": "article_package",
  "stage": "complete",
  "plan": {
    "status": "ready",
    "cover": {
      "title": "exact source H1",
      "core_promise": "...",
      "visual_direction": "concise_metaphor"
    },
    "body_figures": [
      {
        "id": "figure-1",
        "after": "exact paragraph anchor",
        "reader_question": "...",
        "core_judgment": "...",
        "subtitle": "...",
        "grammar": "flow",
        "must_show": ["..."]
      }
    ]
  },
  "style": {
    "status": "compiled",
    "source": "assets/simplemkt-editorial-style.json",
    "prompts": [
      {"id": "cover", "prompt": "complete actual prompt"},
      {"id": "figure-1", "prompt": "complete actual prompt"}
    ]
  },
  "generate": {
    "status": "completed",
    "assets": [
      {"id": "cover", "output_path": "assets/image/cover.png", "status": "generated"},
      {"id": "figure-1", "output_path": "assets/image/figure-1.png", "status": "generated"}
    ]
  },
  "logo": {
    "enabled": true,
    "status": "completed",
    "assets": [
      {"id": "cover", "status": "applied"},
      {"id": "figure-1", "status": "applied"}
    ]
  },
  "layout": {
    "status": "completed",
    "assets": [
      {"id": "cover", "status": "finalized"},
      {"id": "figure-1", "status": "finalized"}
    ]
  },
  "placement": {
    "status": "completed",
    "assets": [
      {"id": "cover", "status": "placed", "alt_text": "..."},
      {"id": "figure-1", "status": "placed", "alt_text": "..."}
    ]
  },
  "qa": {
    "enabled": false,
    "status": "skipped"
  }
}
```
Advance `stage` only through `plan → style → generate → logo → placement → qa → complete`. A failed section keeps the manifest at that stage and adds one observable `issue` or, for QA, `issues`.

For a full article or presentation delivery, require cover `title` to reproduce the exact source H1 or `presentation_title`, plus both cover fields and every figure's unique filename-safe `id`, `core_judgment`, `subtitle`, `grammar`, and non-empty `must_show`; `subtitle` is one source-supported clarification, never a second conclusion. An explicitly scoped body-only batch may omit `plan.cover`; it then generates and finalizes only its planned body IDs. Reserve `cover` and use only lowercase letters, digits, and hyphens for figure IDs. For `article_package`, also require a source H1, exact `after`, and `reader_question`. For `presentation_frames`, require an H1 or `presentation_title`, then replace `after` and `reader_question` with `source_slice`, `beat`, `previous_handoff`, and `next_bridge`; listed order is narrative order. Add `avoid` only when useful. Add `disclosure` only for source attribution or invented non-factual examples; otherwise omit it. When `grammar` is `comparison`, require `comparison_basis` with at least two source-supported, visibly different left/right conditions; at least one must be a different object, position, connection, sequence, or boundary, not only a label. When a figure uses a supplied real asset, require both `source_mode: annotated_source` and a resolvable `source_asset` from `existing_assets`; otherwise omit both. Source mode never replaces `grammar`. Fill a missing required field only from the source; otherwise set `plan.status: blocked`, add one `issue`, and stop for clarification.

Write `schema_version: 5`, the delivery-root-relative `source_path`, `delivery_mode`, `stage: plan`, and the validated `plan` section. In `mode: plan`, show only the `plan` section as Markdown tables and stop; do not print the raw manifest unless requested.

Use `核心承诺 | 视觉方向` for the cover table. For article figures use `ID | 段落锚点 | 读者问题 | 核心判断 | 图法 | 必须呈现`; for presentation figures use `ID | 原文切片 | 叙事节拍 | 核心判断 | 图法 | 必须呈现 | 前后承接`. Append `对比依据` only for `comparison`, and `来源素材` only for figures that use `source_asset`.


### 2. Compile `style`
In `mode: generate`, reuse a ready `plan` from the manifest; if none exists, complete step 1 first. Read `assets/simplemkt-editorial-style.json`, apply its static canvas and Logo reserve, and compile one complete actual Prompt for `cover` and each planned figure. Append `dimensions.canvas.technical_specification_rendering_rule.instruction` verbatim to every compiled image Prompt, regardless of delivery mode. Keep essential content out of the Logo reserve. It must be continuous, unmarked white background: never ask the model to render a wordmark, white Logo block, placeholder, dashed box, border, frame, or badge there. In every generation Prompt, forbid any model-rendered logo, brand name, wordmark, emblem, seal, signature, or watermark anywhere, in Chinese, Latin, or another script. The finalizer automatically detects only the regular PNG named by `dimensions.logo.asset` in `assets/logo/`: when present it is the only permitted branding; when absent it skips Logo application.

Compile the cover Prompt from the exact H1 or `presentation_title`, `core_promise`, `visual_direction`, and cover style. Require the model to render the exact title once in the title-safe zone with the alignment, vertical alignment, and title style declared by the cover contract; allow only the contract-declared line wrapping for readability, never omit, paraphrase, or add title text. Keep the title-safe zone otherwise continuous white background and constrain artwork to its declared artwork regions. Require one source-derived editorial subject, enforce `cover.composition.allow_multi_object_scene`, and append every `cover.mandatory_avoid` item. Apply the declared `materials.editorial_patina` only as a low-contrast treatment of source-derived semantic material; it cannot introduce nostalgic subject matter, ornamental collage, or a decorative route. Never substitute generic chart, map, mountain, river, landscape, or data-preview panels for article meaning. The finalizer preserves the model-rendered title and only applies the Logo.

Compile each figure Prompt from its exact source anchor or slice, `reader_question` or narrative handoff, `core_judgment`, `subtitle`, `grammar`, every `must_show`, useful `avoid`, optional `disclosure`, optional `source_mode` and `source_asset`, and the content-image style. Include a disclosure note only when `disclosure` is present; otherwise do not render, reserve space for, or invent one. When `grammar` is `comparison`, compile every `comparison_basis` condition as a visible left/right difference in objects, positions, connections, sequence, or boundary; labels may name the conditions but cannot be their only difference. Every content image is generated as its final composition: require `core_judgment` and `subtitle` to render exactly once in the declared title region, with no diagram element in that region; require every semantic object and connection to stay inside the declared content stage; and state the content-stage minimum and maximum white-space percentage. Apply the typography, colour roles, linework, editorial patina, composition budget, and mandatory avoids declared by the content-image style contract. The finalizer must not clear, crop, replace, or reflow body titles, subtitles, or content-stage artwork. The content stage contains one dominant grammar—not a card wall, summary table, dashboard, or competing grammar. First depict `must_show` as objects, positions, states, and connections; add only the style-contract-limited labels or short explanations needed to distinguish them. Do not add manifest, placement, or QA instructions to an image Prompt.

Set `stage: style` and write `style.status: compiled`, its source path, and exactly one `{id, prompt}` entry for every planned asset. Prompt text lives only in `style.prompts`. If the style file is missing or a complete Prompt cannot be compiled, set `style.status: failed`, add one `issue`, and stop.


### 3. Run `generate`
Set `stage: generate` and `generate.status: in_progress`, then use the host `image_gen` capability for every entry in `style.prompts`. Write each successful image to `assets/image/cover.png` or `assets/image/<id>.png`, then append its `{id, output_path, status: generated}` record under `generate.assets`. Set `generate.status: completed` only when all planned assets exist and are readable. On failure, set `generate.status: failed`, add one observable `issue`, and stop; do not create an automatic retry loop when QA is disabled.

Keep only the delivered generation state. Replace an asset record when the user explicitly requests rework; add optional `history` only when the user also asks to retain earlier versions.


### 4. Finalize `layout` and `logo`
Require Python 3.10+ and the pinned Pillow dependency, then finalize every generated path. The finalizer automatically detects the exact regular PNG named by `dimensions.logo.asset` in `assets/logo/`. It clears the Logo reserve and overlays that Logo when found; when it is absent or a symlink, it clears the reserve and skips Logo application. It preserves the model-rendered cover title, all body title regions, and the content stage unchanged: it does not crop, clear, replace, or reflow any title, subtitle, or explanatory artwork.

```bash
python3 scripts/place_brand_wordmark.py <generated-image> <same-final-path> \
  --manifest <delivery_root>/assets/image/manifest.json \
  --image-id <image-id>
```

Use `cover` for the cover ID and the planned figure `id` for a body image. The finalizer updates `stage`, records every asset as `layout.finalized`, and records `logo.enabled: true` plus application only when the packaged Logo was detected; otherwise it records `logo.enabled: false` and `status: skipped`. Do not auto-install dependencies or substitute another compositor.


### 5. Record `placement`
Set `stage: placement`. In `article_package`, insert the cover immediately after the H1 and each figure after its exact `after` anchor using the idempotent placement rule. Record each asset as `placed` with concise `alt_text`. In `presentation_frames`, keep the source unchanged, verify cover sequence `0` followed by figures in plan order, and record each asset as `ordered`. Set `placement.status: completed` only after re-reading the source and resolving every path exactly once.


### 6. Record `qa` and complete
Set `stage: qa`. When `enable_qa: false`, write `qa: {"enabled": false, "status": "skipped"}`. When `enable_qa: true` or `mode: qa`, require completed generation, Logo handling, and placement, then check source fidelity and grammar, layout, Logo finalization, and delivery. Verify the model-rendered cover H1 is exact, readable, and centered in its fixed safe zone. Verify that no model-rendered logo, brand name, wordmark, emblem, seal, signature, or watermark remains; when the packaged Logo was detected it must appear exactly once in its fixed wordmark box, and when it was absent no branding may appear. Fail any coordinate, color code, dimension, spacing target, layout annotation, filename, schema field, or other technical specification that becomes visible in the image. For every body figure, visually verify that `core_judgment` and `subtitle` each appear exactly once, are readable, stay inside the title region, and that content-stage white space meets the declared percentage. Verify that a figure without `disclosure` has no disclosure note, and that every required note is present, source-supported, and concise. For `comparison`, visually verify every `comparison_basis` condition and confirm the left/right halves still differ when their labels are hidden. Verify the colour roles: only `core_judgment` uses green; subtitles, labels, disclosure notes, and ordinary connectors use their declared neutral colours; non-text element boundaries use the pale contract colour and never dark borders. Verify that editorial patina remains localized, neutral-white, and subordinate to reading; fail yellowing, fake aging, ornamental collage, decorative retro motifs, or texture that hides semantic structure. QA is report-only: write `passed`, or write `failed` with observable `issues`; do not regenerate or repair automatically.

Set `stage: complete` only when every planned asset was generated, layout and Logo handling completed or were explicitly skipped where allowed, placement completed, and QA is `skipped` or `passed`. When QA fails, keep `stage: qa` and report the failure; do not report completion merely because image files exist.
