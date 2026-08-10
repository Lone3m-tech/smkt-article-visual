<div align="center">

# smkt-article-visual

**Turn the relationships already present in a narrative into a visual package that can be reviewed, placed, and used for a continuous explanation.**

</div>

<p align="justify">
It does not write the article or add decorative filler. It compiles relationships already present in articles, talks, reports, proposals, and workshop outlines into reviewable image decisions, then delivers a coherent cover and content-image system. <code>article_package</code> places explanatory images where readers need them; <code>presentation_frames</code> turns the same decisions into a continuous explanation.
</p>

<div align="center">

Designed for Codex and Agents with image-generation capability.

[SimpleMkt](https://simplemkt.cc) · [X](https://x.com/AlchemistZhou) · [Xiaohongshu](https://www.xiaohongshu.com/user/profile/65a0ecb4000000002201219c) · [Douyin](https://www.douyin.com/user/MS4wLjABAAAArV0uXvsSYl6pD-p5nr-5OFlZED5cEUnb7r2K6j9u4tA)

[Official repository](https://github.com/Lone3m-tech/smkt-article-visual) · [View releases](https://github.com/Lone3m-tech/smkt-article-visual/releases)

[View the 13 visual-grammar demos](#visual-grammar-reference) · [View the Skill runtime contract](SKILL.md)

**[简体中文](README.md) | English**

</div>

## Why this Skill

A normal image prompt answers “make me an image.” This Skill answers “what should a reader understand from this passage, and how should that relationship become visible?” The former leaves semantic decisions to manual work; the latter records source support, reader block, grammar, visible proof, and placement in one page-centred manifest.

| Product strength | What it means in use |
| --- | --- |
| **Relationship before image** | Find the comprehension obstacle before selecting one primary grammar and declaring a body page's `annotation_plan`; do not generate an image first and invent its explanation afterward. |
| **Two delivery strategies** | `article_package` supports local reading comprehension; `presentation_frames` turns selected narrative slices into a continuous explanation. |
| **Reviewable delivery** | Prompts, generated assets, Logo handling, placement, and QA state live in one manifest; the model does not fabricate source evidence, and QA never rewrites prose or reworks output automatically. |

The shared purpose is simple: reduce cognitive load for readers or audiences, so the creator can communicate what is already present in the narrative more clearly.

## Install

These are public candidate installation paths for Codex. A successful installation only means the files are in place; completing the workflow still depends on the host's local-file permissions, image-generation capability, and the dependencies below.

```bash
npx skills add Lone3m-tech/smkt-article-visual \
  --skill smkt-article-visual \
  --global \
  --agent codex \
  --copy
```

Or clone it into Codex's global Skill directory:

```bash
mkdir -p ~/.codex/skills
git clone --depth 1 https://github.com/Lone3m-tech/smkt-article-visual.git \
  ~/.codex/skills/smkt-article-visual
```

Remove `--global` for a project installation. Another Agent host can complete the workflow only when it can read and write local files, invoke an equivalent image-generation capability, and satisfy the dependencies below; this README does not claim universal host compatibility.

## Verified Agent hosts

The following hosts have completed an actual run of this Skill. This support is limited to local file access, page-level Prompt compilation, image generation, and finalization; it does not imply co-publication, partnership, or compatibility with untested hosts.

| Agent | Test status | Verified scope |
| --- | --- | --- |
| <img src="examples/readme-visual/codex-openai-wordmark.webp" alt="OpenAI logo representing Codex" width="128"><br>**Codex** | Tested | Can complete this Skill's local workflow. |
| <img src="examples/readme-visual/doubao-logo.png" alt="Doubao logo" width="72"><br>**Doubao** | Tested | Can complete this Skill's local workflow. |

The Logos belong to OpenAI and Doubao respectively and appear only to identify the tested Agents; they do not imply endorsement or partnership.

## Start

Give the Agent an accessible narrative and delivery goal. Markdown can be used directly; a local document export or an authorized readable Feishu/Lark document must first be normalized into a local Markdown working copy. Start in planning mode:

```yaml
source_path: ./article.md
delivery_mode: article_package
mode: plan
existing_assets: []
```

`source_path` always points to the local Markdown working copy used for execution. The original source may be a Word / Docs export or a Feishu/Lark document; normalization preserves the traceable prose, H1, and paragraph anchors, does not rewrite meaning, and never writes back to the remote document.

Example request:

> Create an article visual package for `article.md`. Show the plan first, then generate only after approval. Do not rewrite the prose.

After plan approval:

```yaml
source_path: ./article.md
delivery_mode: article_package
mode: generate
enable_qa: false
```

### Minimum success criteria

A successful run is not simply a set of attractive images. Each body page explains one source-supported relationship; the relationship remains readable from objects, position, and necessary annotations with the title hidden; and every accepted image is placed once at its approved anchor without rewriting the prose.

## Bundled example

![Bundled example cover: Why should freshly cleaned sneakers not be dried directly against a radiator?](examples/demo-article/assets/image/cover.png)

[“Why should freshly cleaned sneakers not be dried directly against a radiator?”](examples/demo-article/article.md)

## How it works

The body visuals, tested-Agent marks, and companion manifest used by this README live in [`examples/readme-visual/`](examples/readme-visual/). They are documentation display assets, not `assets/image/` output from a Skill run.

Input can be accessible Markdown, an exportable local document, or an authorized readable Feishu/Lark document, plus optional real source assets. Normalize non-Markdown sources into a local Markdown working copy before using its anchors and `source_path`. The output is a cover, necessary explanatory images, and `assets/image/manifest.json`. Article mode writes at the article root, while presentation mode writes at `presentation_output_root`; the Skill's static grammar gallery lives in [`examples/visual-grammar/`](examples/visual-grammar/) and is not output from an individual run.

| Mode | Default and input condition | Delivery boundary |
| --- | --- | --- |
| `article_package` | Default; the source needs an H1. | Place the cover after the H1 and each approved figure once after its source anchor; do not rewrite the prose. |
| `presentation_frames` | Use only for an explicit presentation, slides, deck, or PPT request; supply `presentation_title` if the source has no H1. | Store a cover and ordered narrative frames; leave the source unchanged. |
| `plan` / `generate` / `qa` | `plan` is default; `generate` compiles a Prompt and generates one page at a time; `qa` inspects existing generated pages. | Write planning, grammar, each body page's `annotation_plan`, actual Prompts, generation, QA, and delivery state to one manifest; do not create separate plan or run files. |

There are only four page identities: `cover` establishes a reading promise; `body` explains one source-supported relationship; `agenda` exists only in `presentation_frames` to orient three or more body beats; and `closing` is the standard presentation signoff. A cover is not a body grammar, and neither `agenda` nor `closing` carries a new source claim.

Logo needs no setting. The finalizer detects only the regular PNG in `assets/logo/` whose name matches the style contract: it applies that asset when present and skips it when missing or symlinked. The model must not render a Logo, brand name, or watermark. `enable_qa` is off by default: disabled QA sends generated images directly to finalization and placement; enabled QA permits only passing images to receive the Logo and placement. QA never redraws, rewrites prompts, or changes prose automatically.

## Demo: presentation layouts

These layout demos show only page identity and whitespace organization for `presentation_frames`; they do not carry article facts. A real page is still compiled from planned source support, exact visible text, and the selected `layout_variant`.

### Cover

| `text_left_carrier_right` | `text_right_carrier_left` |
| --- | --- |
| ![Cover: left title with right abstract carrier](examples/demo-cover/text-left-carrier-right.png) | ![Cover: right title with left abstract carrier](examples/demo-cover/text-right-carrier-left.png) |

| `text_top_carrier_bottom` | `text_centered` |
| --- | --- |
| ![Cover: top title with bottom abstract carrier](examples/demo-cover/text-top-carrier-bottom.png) | ![Cover: centered title with low-density peripheral echo](examples/demo-cover/text-centered.png) |

### Agenda

| `centered_list` | `split_list` |
| --- | --- |
| ![Agenda: centered list](examples/demo-agenda/centered-list.png) | ![Agenda: split list](examples/demo-agenda/split-list.png) |

| `vertical_rail` | `stepped_list` |
| --- | --- |
| ![Agenda: vertical rail](examples/demo-agenda/vertical-rail.png) | ![Agenda: stepped list](examples/demo-agenda/stepped-list.png) |

### Closing

| `editorial_signoff` | `baseline_signoff` | `echo_signoff` |
| --- | --- | --- |
| ![Closing: editorial signoff](examples/demo-closing/editorial-signoff.png) | ![Closing: baseline signoff](examples/demo-closing/baseline-signoff.png) | ![Closing: echo signoff](examples/demo-closing/echo-signoff.png) |

## Controlled boundaries

- Each body page explains one source-supported relationship; a grammar cannot add data, causality, or conclusions.
- A `comparison` needs visibly different structure; real screenshots, paper figures, data charts, and UI images are handled only as explicitly supplied source assets.
- An accepted article image appears once at its approved anchor. Detailed selection, Prompt-compilation, and QA contracts live in [references/visual-grammar.md](references/visual-grammar.md), [references/manifest-contract.md](references/manifest-contract.md), and [SKILL.md](SKILL.md).

## Where it helps

| User and task | Output | Why it fits |
| --- | --- | --- |
| Long-form writers and content teams | An article package with a cover and explanatory images at source anchors | It turns relationships the reader would otherwise have to infer into visible judgments without rewriting the article. |
| Strategy, consulting, and research practitioners | Narrative frames for a talk or proposal | It makes differences, mechanisms, and boundaries legible beyond spoken explanation without pretending to be an editable PPTX. |
| Trainers and workshop facilitators | Explanation pages that follow a teaching sequence | It turns abstract steps, feedback, or hierarchy into a visual structure an audience can follow. |

## Who it is not for

- Standalone posters, mood images, or social-only covers.
- Article writing, CMS-brief management, publishing, platform upload, or outcome guarantees.
- A complete deck, editable PPTX, or presentation-software implementation.
- Fabricated screenshots, source images, data, or unlicensed third-party material.

## Demo: body visual grammars

These 13 body-page images show only the structural relationship each grammar is designed to organize. Their files live in [`examples/visual-grammar/`](examples/visual-grammar/); they are not facts or data. A real delivery must still be determined by source support, the reader question, and `must_show`.

| Grammar | Reference |
| --- | --- |
| Architecture (`architecture`) | ![Architecture grammar: components, branches, and convergence](examples/visual-grammar/architecture.png) |
| Hierarchy (`hierarchy`) | ![Hierarchy grammar: parent-child relationships](examples/visual-grammar/hierarchy.png) |
| Flow (`flow`) | ![Flow grammar: input to output](examples/visual-grammar/flow.png) |
| Loop (`loop`) | ![Loop grammar: feedback iteration](examples/visual-grammar/loop.png) |
| Decision tree (`decision_tree`) | ![Decision tree grammar: conditional paths](examples/visual-grammar/decision_tree.png) |
| Comparison (`comparison`) | ![Comparison grammar: visibly different structures](examples/visual-grammar/comparison.png) |
| Matrix (`matrix`) | ![Matrix grammar: two-dimensional placement](examples/visual-grammar/matrix.png) |
| Overlap map (`overlap_map`) | ![Overlap grammar: shared and distinct areas](examples/visual-grammar/overlap_map.png) |
| Boundary map (`boundary_map`) | ![Boundary grammar: inside and outside scope](examples/visual-grammar/boundary_map.png) |
| Argument map (`argument_map`) | ![Argument grammar: evidence, constraint, and conclusion](examples/visual-grammar/argument_map.png) |
| Timeline (`timeline`) | ![Timeline grammar: staged progression](examples/visual-grammar/timeline.png) |
| Continuum (`continuum`) | ![Continuum grammar: non-temporal gradual position](examples/visual-grammar/continuum.png) |
| Layer stack (`layer_stack`) | ![Layer stack grammar: system layers](examples/visual-grammar/layer_stack.png) |

## Requirements and limitations

- Requires an Agent host with local file read/write access and `image_gen` or an equivalent capability.
- Logo finalization requires Python 3.10+ and Pillow from [`scripts/requirements.txt`](scripts/requirements.txt). The Skill does not install dependencies or repair generated work with another renderer.
- Successful installation alone does not prove end-to-end image behavior; that depends on the host image capability.
- The package includes an `examples/demo-article/` outcome example aligned to the current manifest contract. It demonstrates input, page planning, and image-delivery shape; it does not replace isolated cross-host verification.
- The latest isolated product test remains `blocked` because its retained trace exposes a host-internal generated-image path. Until that issue is resolved, it is not evidence of complete cross-host or end-to-end acceptance.
- Each user remains responsible for input rights, third-party image-model terms, and redistribution permission.

## License

[MIT License](LICENSE)
