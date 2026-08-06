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
mode: plan | generate | qa                  # default: plan; qa runs a standalone basic review
enable_logo: true                           # optional during generate; applies the packaged Logo after image generation
enable_qa: false                            # optional during generate; adds a basic report, time, and token use
existing_assets: []                         # optional screenshots, diagrams, or source images
```

Require `source_path`; accept `article_path` as a backwards-compatible alias. Resolve `delivery_mode` from explicit user intent and default to `article_package` when it is unstated. Require a source H1 for `article_package`. In `presentation_frames`, require `presentation_title` only when the source has no H1. During `generate`, leave `enable_logo` at its default `true` to apply the packaged Logo after generation, or set it to `false` for the same layout without the final Logo overlay. Leave `enable_qa` at its default `false` for faster delivery, or set it to `true` for the optional basic output report. When the source root already contains an `article_package` manifest, require `presentation_output_root` so the two delivery packages remain separate.

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

Use one compact canonical framework for both delivery modes. It is the user-facing planning surface: keep only the judgments a person needs to approve. `article_package` calls each `body_figure` a **正文图** in user-facing output; `presentation_frames` calls it a **讲述图**. The generated image contract is identical.

```yaml
visual_plan:
  delivery_mode: article_package | presentation_frames
  cover:
    core_promise:
    visual_direction: concise_metaphor | restrained_abstract_direction
  body_figures:
    # Use exactly one of the following entry shapes, selected by delivery_mode.
    # article_package only
    - id:
      after: exact paragraph anchor
      reader_question:
      core_judgment:
      grammar:
      must_show: []
      avoid: []                         # optional; use only for likely repetition or misreading
      disclosure: null                  # optional; illustrative_only when non-factual content is needed

    # presentation_frames only: replace the article_package entry shape above.
    - id:
      source_slice:
      beat: hook | tension | mechanism | reframe | resolution
      core_judgment:
      grammar:
      must_show: []
      previous_handoff:
      next_bridge:
      disclosure: null
```

Do not add a body figure merely because a heading, paragraph, or speaking beat exists. A cover is required for both delivery modes. Every body figure must clarify a mechanism, conditional choice, comparison, overlap, argument, sequence, feedback loop, boundary, hierarchy, temporal progression, continuum, or authorized source image. In `article_package`, `after` is the exact one-paragraph reading anchor and `reader_question` states the local obstacle. In `presentation_frames`, `source_slice`, `beat`, `previous_handoff`, and `next_bridge` define the narrative movement. The shared visual contract does not require the plans to choose the same images.

The YAML structure above is the sole canonical `visual_plan` format. [references/article-visual-plan.md](references/article-visual-plan.md) supplies the selection judgment only; do not copy, shorten, or extend it into a competing plan template. Do not expose derived paths, title layout, Logo geometry, prompt blocks, QA fields, manifest records, or null fields from the other mode in the plan.

Before entering `generate`, validate the selected plan. Require `delivery_mode`, both cover fields, and every figure's `id`, `core_judgment`, `grammar`, and non-empty `must_show`. In `article_package`, require a source H1 and an exact `after` plus `reader_question` for every figure. In `presentation_frames`, require an H1 or explicit `presentation_title`, then require `source_slice`, `beat`, `previous_handoff`, and `next_bridge`; order figures by their listed sequence. `avoid` and `disclosure` remain optional and appear only when useful. Fill a missing required field only from the source; otherwise stop for clarification.

After acceptance, compile the plan in memory before generation. Derive the exact cover title from the H1 or `presentation_title`, the PPT-cover placement, title treatment, Logo overlay zone, output paths, manifest placement records, and all mode-specific generation and QA checks from this Skill and the style file. For `article_package`, derive `assets/image/<id>.png` and place it once after `after`; for `presentation_frames`, derive `assets/image/<id>.png`, cover sequence `0`, then the listed figure order. Do not make this internal compilation a second user-facing plan or a second persisted record.

### 2. Generate and place

#### 2.1 Prepare the run

- Treat the directory containing `source_path` as `source_root`. In `presentation_frames`, resolve `presentation_root` to `presentation_output_root` when supplied, otherwise `source_root`; it owns generated assets and the manifest while `source_path` stays read-only. Set `delivery_root` to `source_root` for `article_package` and to `presentation_root` for `presentation_frames`.
- Read `assets/simplemkt-editorial-style.md`.
- Run `python3 scripts/place_brand_wordmark.py --print-contract` before compiling any asset.
- Treat that script output as the sole source for Logo canvas, reserve, asset, size, and inset values.
- Generate and deliver every asset at the fixed Logo-contract canvas dimensions reported by that script. When `enable_logo: true`, the finalizer also normalizes the canvas while applying the Logo; when it is `false`, do not substitute another renderer or compositor.
- Inject the exact Logo overlay coordinates into every prompt. Keep title, subtitle, labels, connectors, and other essential semantics clear of that overlay zone, but never request or paint a pre-rendered white rectangle; the Logo finalizer must not erase the underlying artwork.
- Always reserve the Logo overlay zone in the visual contract. `enable_logo` controls only the final deterministic overlay, never the title, content-stage, or prompt-layout rules.
- Block generation when the style file or contract output is missing or unusable. Block for a missing or unusable Logo PNG only when `enable_logo: true`.
- Before the first image, create the delivery-root `assets/image/manifest.json` with `schema_version: 3`, a `provenance` object, the Markdown-relative `source_path`, `delivery_mode`, a `logo` object, and an `images` array. For `presentation_frames`, resolve source paths relative to `presentation_root`.
- Set provenance `skill_id` and `canonical_repository` to the exact fixed values below. Resolve `release_version` and `release_commit` only from installed release metadata or the current Git checkout; otherwise use `null`. Give every run a new non-secret `run_id`. Never infer unavailable release data or reuse a run ID.

#### 2.2 Compile each prompt

- Compile every cover from the exact source H1 or explicit `presentation_title` using the shared PPT-cover contract: one prominent title in a continuous quiet safe zone plus one concise `visual_direction`. That direction may be a recognizable, vivid metaphor that maps the title's central tension, transformation, or promise, or a restrained abstract composition that conveys the same core idea. Keep it to one dominant subject, action, or abstract composition; reject multi-object scenes, generic paper, and unnecessary diagram complexity. Render no text other than that exact title unless the user explicitly requests it. In `article_package`, make the direction act as a document entry; in `presentation_frames`, make it establish the narrative opening without adding title-external text.
- Before compiling a body prompt, derive these generation requirements in memory from the plan and source; they are Prompt requirements, not extra plan fields or a later QA brief:
  1. **Source lock:** use the exact paragraph after `after` or exact `source_slice`; extract its objects, actors, actions, states, positions, evidence details, and relationships. Use a supplied source line, multi-line excerpt, or illustrative body copy when it helps explain the relationship; otherwise use an abstract structure. Retain only the local text needed to support that relationship, rather than making the original or invented paragraph the image's main reading task. Do not invent an unrelated domain scenario, industry example, or environmental narrative to fill the figure.
  2. **Grammar lock:** use `grammar` as the one primary organizing structure, and make `core_judgment`, `reader_question` or `beat`, and every `must_show` visibly true within that structure.
  3. **Content density:** select semantic form before material treatment. Build the smallest sufficient explanatory system—normally two to four primary semantic groups, with only the internal detail needed to preserve the source relationship. Labels clarify the depiction; they do not replace it. Paper is optional and valid only when a document, text, claim, source, or material artifact is itself part of the explanation.
  4. **Truth boundary:** when a compact fictional example, claim, number, date, percentage, source-like chart, or other illustrative content is clearer, include the exact lower-left small-gray-italic note `图中示例仅为解释用途，并非事实` in that same image prompt. Do not leave disclosure for QA to add later.
  5. **Visual contract:** inject the centered title treatment, content stage, pure-white canvas, Logo overlay exclusion, typography, line, material, and elevation rules from `assets/simplemkt-editorial-style.md`.
- Compile every body figure from that source lock into the shared content-image contract: use `core_judgment` as its centered core judgment and the selected grammar—not a metaphor—as the primary organizing structure. Keep every semantic object, label, connector, anchor, and optional paper surface inside the style file's invisible content stage; do not draw that stage as a default frame. Do not turn every detail into a separate top-level node, and do not compress necessary meaning into empty geometry. Every depicted element must clarify the primary relationship and follow ordinary physical, causal, and semantic expectations. In `article_package`, answer `reader_question` without restating prose and honor `avoid` when supplied. In `presentation_frames`, establish `beat` after `previous_handoff` and make `next_bridge` credible. Delivery mode changes image selection, source scope, semantic framing, information density, and composition strategy; it must not change the shared visual template.
- Compile every prompt from four blocks: role and required text, source-locked meaning, visual core drawn from `assets/simplemkt-editorial-style.md`, and minimal risk-specific exclusions. Keep exclusions to six or fewer, normally one to three; use positive editorial vocabulary instead of pasting broad failure lists into the prompt.
- Keep QA-only material out of image prompts: manifest and placement checks, full anti-decoration variants, exclusion lists for unrelated grammars, and final Logo-placement receipts.
- Treat `assets/simplemkt-editorial-style.md` as the sole source for canvas, typography, title band, content-element vocabulary, material treatment, Logo overlay zone, and disclosure presentation. Inject those rules without restating or overriding their values in the plan or Prompt.
- Preserve every concrete source detail named in `must_show` as linked detail within the one dominant grammar structure. Never replace it with anonymous placeholder lines, generic tokens, or empty nodes whose labels carry all the meaning.
- Do not defer content, density, illustrative disclosure, or source specificity to QA. The generated Prompt carries those requirements; QA only verifies the resulting source relationship, layout, brand finalization, and delivery.

#### 2.3 Record and finalize each attempt

- Maintain one delivery-root `assets/image/manifest.json`; never create per-image Prompt or Logo-receipt sidecars. It is the sole delivery record for provenance, asset paths, selected delivery mode, exact placement or narrative order, every generation attempt, actual Prompt, adjustment reason, deterministic Logo result, QA outcome, and the accepted attempt.
- Use this compact manifest shape and append attempts instead of replacing them:

  ```json
  {
    "schema_version": 3,
    "provenance": {
      "skill_id": "smkt-article-visual",
      "canonical_repository": "https://github.com/Lone3m-tech/smkt-article-visual",
      "release_version": "vX.Y.Z | null",
      "release_commit": "full commit SHA | null",
      "run_id": "unique non-secret run identifier"
    },
    "source_path": "source.md",
    "delivery_mode": "article_package | presentation_frames",
    "logo": {"requested": true, "status": "pending | applied | skipped"},
    "qa": {"requested": false, "status": "pending | skipped | passed | failed"},
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
        "logo": {"status": "pending | applied | skipped"}
      }]
    }]
  }
  ```

- Create one image record per planned cover or content image with `id`, `role`, `output_path`, and exact article placement or narrative order. In `presentation_frames`, record the cover as `placement.kind: narrative_order, sequence: 0` and each content image with its exact approved sequence.
- Set `logo.requested` from `enable_logo`. Set `logo.status` to `pending` when it is `true` and to `skipped` when it is `false`. The fixed Logo overlay zone remains part of every image prompt in both cases.
- Set `qa.requested` from `enable_qa`. Set `qa.status` to `skipped` when it is `false`; set it to `pending` when it is `true`, then update it to `passed` or `failed` after the review. A standalone `mode: qa` implies `enable_qa: true`.
- When `enable_qa: false`, treat a successful image-generation result as the chosen candidate. Do not visually inspect it to reject, regenerate, or rewrite its Prompt; only a missing file, finalizer failure, corrupt output, or placement failure is an execution error that may block delivery.
- Append, never overwrite, one attempt before every generation.
- Give each attempt an increasing integer `id`, the complete actual `prompt`, `status` (`pending`, `generated`, `rejected`, or `accepted`), `adjustment_reason`, optional `candidate_file`, and `logo` state. Set it to `pending` before generation, then update it after the generation result is known.
- Use `null` for a first-pass adjustment reason. Require an adjustment reason for every rejection or rework.
- Retain a rejected candidate PNG only when the user asks to compare it later; otherwise retain its manifest record but no rejected image file.
- When `enable_logo: true`, require Python 3.10+ and the pinned Pillow dependency, then run:

  ```bash
  python3 scripts/place_brand_wordmark.py <underlying-image> assets/logo/simplemkt-logo-demo.png <final-image> \
    --article-manifest <delivery_root>/assets/image/manifest.json \
    --image-id <figure-id> --attempt-id <attempt-id>
  ```

- Use that finalizer to create the fixed-contract final asset, atomically record its Logo geometry in the attempt, and set the top-level `logo.status` to `applied` after every final asset succeeds.
- When `enable_logo: false`, do not invoke the finalizer. Save the generated asset at its planned output path, set every attempt's `logo.status` to `skipped`, and retain top-level `logo.status: skipped`.
- Do not auto-install dependencies or substitute another compositor. Do not continue without the Logo record only when `enable_logo: true`.

#### 2.4 Place and accept

- In `article_package`, insert the cover immediately after the required H1 and insert each content image after its exact paragraph anchor using the idempotent placement rule.
- In `presentation_frames`, preserve source prose unchanged and verify the cover exists once at sequence `0`, followed by each content-image file once in approved narrative order.
- Use concise alt text that describes the image's explanatory role.
- After required finalization and placement, mark exactly one attempt per image as `accepted` and set `accepted_attempt` to that ID. Optional QA annotates that delivered result; it does not replace, regenerate, or unset the accepted attempt.
- Mark every rejected attempt with its adjustment reason.
- Re-read the saved source. In `article_package`, verify every planned path resolves once and appears once at its planned location. In `presentation_frames`, verify no image Markdown was added, the cover path resolves once, and every approved content-image path resolves once before reporting completion.

### 3. Optional QA and completion

`enable_qa` defaults to `false`. In that default, do not run a visual review or retry loop: after a successful image-generation result, complete only deterministic finalization, source placement or narrative-order checks, and the manifest record. Do not judge visual quality, source fidelity, information density, wording, style, or semantic fit in order to reject, regenerate, or rewrite a Prompt. Apply the exact Logo overlay when `enable_logo: true`, or record it as skipped when `enable_logo: false`, then set `qa.status: skipped`. Only a missing file, finalizer failure, corrupt output, or placement failure blocks delivery. Report that the images were delivered with QA skipped.

When `enable_qa: true` (or `mode: qa`), run one basic output check after finalization and placement. It can add review time and token use, but it is report-only: do not regenerate or repair automatically. Check only:

- **Source fidelity and grammar:** the cover matches its exact title; each content image answers its planned reader question or narrative beat, preserves `must_show`, and uses its selected grammar to make the source relationship legible.
- **Layout:** the shared type hierarchy, centered title band, Logo-safe zone, and invisible content stage hold.
- **Brand finalization:** when `enable_logo: true`, the fixed Logo result is applied; when `enable_logo: false`, the manifest records it as skipped. In both cases, no model-rendered duplicate wordmark remains.
- **Delivery:** each final asset has one resolving path at its required anchor or sequence, and a complete manifest attempt record.

Content-element selection, information density, paper treatment, and illustrative disclosure are generation-time requirements, not QA review criteria. When a QA check fails, record one observable source-fidelity, layout, brand, or delivery issue; do not regenerate or modify the delivered image unless the user explicitly requests a named rework. Do not accumulate broad exclusions or rewrite unrelated parts of the generation brief after the fact. Set `qa.status` to `passed` only after the basic check succeeds; otherwise set it to `failed` and report the observed issue.

Do not report delivery complete merely because image files exist. Complete when generation was explicitly requested, all final assets have been finalized and placed or ordered correctly, no planned image is missing or unrelated, and the manifest records whether the optional QA was `skipped`, `passed`, or `failed`. Image models are probabilistic, so this preserves the visual contract—not byte-identical pixels across model versions.
