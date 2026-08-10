---
name: smkt-article-visual
description: "Turn a finished or near-finished narrative—Markdown, a local document export, or an authorized readable Feishu/Lark document normalized into local Markdown—into unified explanatory images, optionally adapting transferable high-level visual direction from a user-supplied reference without reproducing its distinctive content. Use when the request explicitly asks for 文章配图, 文章视觉包, 文章封面, 正文解释图, or 连续讲述图."
---

# smkt-article-visual

## Inputs

```yaml
source_path: ./source.md
source_origin: # optional original document path or authorized Feishu/Lark URL; provenance only
delivery_mode: article_package | presentation_frames
mode: plan | generate | qa
presentation_title:
presentation_output_root:
presentation_closing: 谢谢观看 # optional standard closing text override
enable_qa: false
existing_assets: []
style_reference_paths: [] # optional visual references for temporary high-level style extraction
style_direction:          # optional concise rendering direction that applies to this run only
```

## Outputs

```text
<article_root | presentation_root>/assets/image/
├── cover.png
├── <image-id>.png
└── manifest.json
```

## Boundaries

- Accept Markdown directly. For a local document export or an authorized readable Feishu/Lark document, first make a local Markdown working copy that preserves the source meaning, H1, and paragraph structure. `source_path`, source anchors, and `manifest.json` always point to that working copy; do not write back to the original document or remote service.
- Keep source prose unchanged. In `article_package`, insert only accepted image Markdown; `presentation_frames` never edits source prose.
- Generate with the host `image_gen` capability. Do not redraw generated artwork with another renderer. The packaged finalizer may add the Logo only.
- Generated illustrations are explanatory artwork, never authentic screenshots, source images, or factual evidence.
- A style reference may change only rendering treatment: line character, form abstraction, colour treatment, whitespace, and focal rhythm. Do not copy its subjects, characters, composition, text, signature, watermark, or distinctive identifying marks. It never changes source support, selected visual grammar, required content, or Logo handling.

## Page-centred manifest

Use [references/manifest-contract.md](references/manifest-contract.md) as the sole field and lifecycle contract. `manifest.json` is a page record, not a collection of workflow buckets: top level holds package metadata only, while every page owns its plan, Prompt, generation, finalization, placement, and QA state. Do not create top-level `plan`, `style`, `generate`, `logo`, `layout`, `placement`, `qa`, or global `stage` fields.

## Workflow

### 1. Plan the image system

Read the local Markdown working copy first. For every candidate body page, first copy one exact key source sentence (or the smallest contiguous source range that preserves one relationship) into `source_support`. This sentence is the page's semantic anchor: do not begin with a subject list, a desired scene, or a vague topic heading.

Before selecting a grammar, make one explanation contract from that support:

- `reader_block`: the one judgment the reader must gain from the source relationship;
- `core_judgment`: a short, source-faithful title for that judgment, never the proof itself;
- `must_show`: two to three reader-visible facts—states, positions, boundaries, connections, or ordered changes—that independently support the judgment; never a subject or prop inventory;
- `grammar_proof`: the corresponding visible evidence in the content stage, with every proof mapped to a `must_show` fact.

Hide `core_judgment` and `subtitle` mentally before choosing a grammar. If the remaining evidence cannot let a reader recover `reader_block`, revise the evidence, change grammar, or split the source relationship into separate pages. Do not generate a body page that relies on its title to explain its source support.

### Route source relationship to one visual grammar

| 原文呈现的关系 | 图法 | 不用来呈现 |
| --- | --- | --- |
| 组件之间的依赖、分支、合并、上下游如何共同组成一个系统 | `architecture` | 纯时间步骤、父子分类 |
| 父子、类别与子类、整体与部分、组织层级 | `hierarchy` | 条件选择、时间顺序、系统依赖 |
| 有明确先后的一次性步骤、输入到输出、状态转换 | `flow` | 没有顺序的并列概念、真实历史时间、反馈循环 |
| 反馈、迭代、优化、约束反复作用并回到前一状态 | `loop` | 一次性路线、装饰性圆箭头 |
| 明确的“如果／那么”条件，条件导致不同路径或结果 | `decision_tree` | 没有决策条件的组件依赖、普通分类 |
| 两个或多个方案、状态或处境的差异、取舍、前后对照 | `comparison` | 单一过程、只有名称不同而无可见结构差异 |
| 两个独立维度共同决定分类、定位或术语区分 | `matrix` | 单维分类、细致时间变化 |
| 共同部分与各自部分、交集、共存或冲突 | `overlap_map` | 互斥选项、顺序过程 |
| 什么属于、什么不属于、内外范围或边界 | `boundary_map` | 操作步骤、时间过程 |
| 原文已经给出的主张、依据、限制与结论如何互相支撑 | `argument_map` | 编造证据、无依据因果 |
| 历史、阶段、真实时间推进中的事件或变化 | `timeline` | 同时存在的系统结构、非时间渐变 |
| 非时间的成熟度、强度、位置或状态光谱 | `continuum` | 真实时间进程、二元对比 |
| 抽象层、系统层或包含层如何上下叠置 | `layer_stack` | 密集方向依赖、父子分类 |

### 选择与保存

1. 定义主关系
   - 只抽取原文实际陈述、且能解决 `reader_block` 的一个关系；
   - 多条独立关系：拆页，或只保留主关系。
2. 选择图法
   - 排除：命中表中“不用来呈现”的行；
   - 选择：额外假设最少的一种图法；
3. 保存并反推
   - 保存：一个主 `grammar`、两到三条作为可见证据的 `must_show`、`annotation_plan`、至少两条与证据对应的 `grammar_proof`；
   - 对比图：另写 `comparison_basis`；
   - 反推：遮住标题后仍不能复述 `reader_block`，回到第 1 步。

### 真实来源图

真实截图、论文图、数据图或 UI 图使用 `source_mode: annotated_source` 和可解析的 `source_asset`；它不是图法，仍须选择图法，只能做编辑标注，不得伪造证据。

After routing, read [references/visual-grammar.md](references/visual-grammar.md) only for the selected grammar's compiler contract: its topology, required visible proof, forbidden substitutions, and allowed encodings. Do not read or use the visual style to choose a grammar.

Create one planned page per selected image using the page schemas in [references/manifest-contract.md](references/manifest-contract.md). There are four image identities:

- `cover` establishes the article or presentation's reading promise. It never uses a body visual grammar.
- `body` explains one source-supported relationship. A titleless banner remains `body` with `render_text: false`; it is not a third identity.
- `agenda` exists only in `presentation_frames`. When the plan has three or more body beats, place one agenda after the cover; derive its three to five ordered items from already planned beats or source sections. It is an orientation page, never a body grammar.
- `closing` exists only in `presentation_frames`, after the final body page. Use the standard text `谢谢观看` unless `presentation_closing` supplies a replacement. It is standard presentation chrome, never a source claim, summary, promise, call to action, or body grammar.

Let the manifest contract define fields, encoding limits, projection mode, and lifecycle. Apply these rules:

- Keep `cover`, `body`, and `agenda` source-faithful: do not add causality, sequence, priority, containment, data, or conclusions absent from their declared support. `closing` may use only its standard closing text and must not add a source claim, summary, promise, or call to action.
- Explicitly declare `annotation_plan` for every body page. Use it for any source-supported relationship that objects alone cannot show; choose `mode: none` only when every required relationship remains legible without words.
- When a label needs a short explanation, declare a `note` for the same `target`: the label names the judgment and the note states one source-supported mechanism, condition, or scope. Use at most two such label-note clusters per body page; the note is one short line, shares the label's leader, and never becomes a card, caption block, or second argument.
- When `colour_plan` is omitted, use `brand_green_accent`. A cover reserves that single accent for its required title selection field; it never uses `brand_green_subject_fill`. An explicit existing `colour_plan` remains the page-level override within this rule. It never changes a selected grammar or adds gradients.
- Every cover uses `scene_integrity.mode: abstract`: its right-side carrier may express only source-supported abstract relationships such as density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve. Never plan or render a recognizable entity, product, object, scene, industry symbol, or body part.
- Every cover requires `editorial_treatment`: split the exact H1 into two or three contiguous title units, set exactly one to `selection_field`, and keep every title character deep ink. The selection field is the title-level brand-green emphasis; the abstract carrier may use only one separate tiny low-saturation brand-green dry-brush accent.
- For every presentation `cover`, `agenda`, and `closing`, select one explicit role-allowed `layout_variant` during planning. It changes only placement, whitespace, and visual balance; it never changes exact visible text, source support, scene integrity, page identity, shared style, or delivery rules. Existing plans without the field retain their role default.
- A presentation `agenda` may declare an optional `agenda_carrier` as one low-density abstract navigation rhythm derived from its already planned beats. It is orientation only: never an entity, scene, source claim, body grammar, card, badge, or decorative arrow. Omit it when an unadorned agenda is the intended result.
- A presentation `closing` chooses exactly one mutually exclusive treatment: `editorial_signoff` is an upper-left editorial closing with one tiny non-semantic lower-right end mark and no carrier; `baseline_signoff` is a lower-left formal closing anchored by one short broken baseline and no other mark or carrier; `echo_signoff` is a centered closing with one required low-density `closing_carrier` echoing the cover. A closing carrier is visual continuity only: never an entity, a scene, a source claim, a summary, or a call to action.
- For every representational page, use the existing `visual_solution` to state selectively observed details, a frontal/profile/lightly-oblique or flat-cutaway view with only shallow spatial cues, an allowable short/broad/skewed silhouette, one source-compatible memorable feature, one posture relation (tilt, opening, overlap, crop, or weight shift), one local directional fill gesture when colour is used, and an irregular cluster rhythm for its source-supported related objects. Do not put visual style in `must_show`.
- For every page, write `scene_integrity`: use `representational` for a person, animal, object, or embodied action; otherwise use `abstract` with a rationale. For representational pages, declare subject count, object continuity, required occlusion, and forbidden detached or duplicated parts. Split incompatible simultaneous actions into separate pages.
- For `article_package`, place each accepted body page at its source anchor. For `presentation_frames`, retain source prose and use narrative-frame sequencing.
- Keep a page `planned`, record `plan.issue`, and stop for clarification when source support cannot fill a required manifest field.

In `mode: plan`, show only the manifest-required planned-page table, then stop before generation.

### 2. Generate pages one by one

For the next planned page only, use `assets/simplemkt-editorial-style.md`, [references/visual-grammar.md](references/visual-grammar.md), [references/prompt-templates.md](references/prompt-templates.md), and [references/manifest-contract.md](references/manifest-contract.md). Select `cover-v1`, `body-v1`, `agenda-v1`, or `closing-v1` for the matching role.

Compile the Prompt deterministically before calling `image_gen`:

```bash
python3 scripts/compile_page_prompt.py \
  --manifest <delivery_root>/assets/image/manifest.json \
  --image-id <image-id>
```

The compiler validates the page and writes its exact `prompt`; do not hand-write, shorten, or override `page.prompt.text`.

### Delivery layout contract

- Deliver every page as an opaque 1200×675, 16:9 PNG on a pure-white canvas;
- Keep at least a 5% safe margin for visible text and local annotations;
- Keep the upper-right 144×60 Logo reserve (x=1056, y=0) free of title, subtitle, label, connector, essential diagram content, placeholder, dashed outline, border, frame, and badge;
- Render no Logo, wordmark, brand name, seal, signature, or watermark; the packaged transparent Logo is the only permitted post-generation branding.

When `render_text: false`, retain the body's semantic fields as plan metadata; the compiler uses the body template's no-rendered-text branch and the body title-color rule does not apply.

Use `image_gen` with the compiler-written `page.prompt.text`. Record only that page's `generation` status and candidate file; on failure, record its issue, do not retry automatically, and do not change another page.

### 3. QA generated pages (optional; off by default)

`enable_qa: false` is the default. It writes `page.qa = {"status": "skipped"}` for generated pages and proceeds to delivery.

When `enable_qa: true` or `mode: qa`, inspect each generated page before any Logo is applied or source prose is changed. Apply the acceptance criteria below, record observable checks and issues in `page.qa`, and set only that page to `qa_passed` or `qa_failed`.

A failed page never reaches Logo finalization or placement. `mode: qa` checks existing generated pages and finalizes only pages that pass.

### Coarse QA acceptance

QA is an optional hard-failure gate, not a design review. When enabled, reject a page only when one of these is clearly true:

- 核心关系缺失、画反，或出现与来源直接矛盾的新主张。
- 出现模型擅自生成的来源文字、Logo、品牌名、签名或水印，或必要文字已无法阅读。
- 人物、动物或物体页出现明显断肢、重复主体、无法成立的遮挡或动作。

Do not QA visual style, line character, whitespace, colour, layout balance, fine annotation accuracy, Logo-reserve measurements, or every individual `must_show` / `grammar_proof` item. The finalizer, not QA, normalizes the delivery PNG. If no hard failure is obvious, pass the page; when `enable_qa: false`, record `qa_skipped` and proceed directly to finalization and placement.

### 4. Deliver accepted pages

For every generated page whose QA passed or was skipped, run the finalizer. It preserves artwork and text, normalizes delivery size, overlays the packaged transparent Logo when present, writes only that page's `final`, and moves it to `finalized`. Do not ask the model to render a Logo.

```bash
python3 scripts/place_brand_wordmark.py <generated-image> <same-final-path> \
  --manifest <delivery_root>/assets/image/manifest.json \
  --image-id <image-id>
```

After finalization, place only accepted pages. In `article_package`, put the cover immediately after the H1 and each body page at its declared insertion anchor; a titleless body banner may instead go immediately before that same anchor. Re-read the article and record placement according to the manifest contract. In `presentation_frames`, leave source prose unchanged and record the accepted sequence: cover, agenda when planned, body pages, then closing. Set only that page to `placed`.

The package is complete only when every planned page is placed and has `qa_passed` or `qa_skipped`; derive this from `pages[]`, never from a global workflow stage.
