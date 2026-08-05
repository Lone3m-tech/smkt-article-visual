<p align="center">
  <img src="examples/readme-visuals/hero-banner.png" alt="smkt-article-visual opening banner" width="100%">
</p>

<div align="center">

# smkt-article-visual

**Turn every key judgment into a visual people can understand.**

Turn a structured narrative—an article, talk, report, proposal, or workshop outline—into either an **article package** or a sequence of **presentation frames**. It decides what needs to be shown, selects the right visual grammar, and delivers a traceable image package in the SimpleMkt editorial style.

[SimpleMkt](https://simplemkt.cc) · [X](https://x.com/AlchemistZhou) · [Xiaohongshu](https://www.xiaohongshu.com/user/profile/65a0ecb4000000002201219c) · [Douyin](https://www.douyin.com/user/MS4wLjABAAAArV0uXvsSYl6pD-p5nr-5OFlZED5cEUnb7r2K6j9u4tA)

[View the complete demo](examples/demo-article/article.md) · [Read the runtime contract](SKILL.md)

**English | [简体中文](README.zh-CN.md)**

</div>

## Install

Copy either command to your Agent or run it in a terminal. Prefer `npx`; use `git clone` when `npx` is unavailable.

### npx (recommended)

```bash
npx skills add Lone3m-tech/smkt-article-visual \
  --skill smkt-article-visual \
  --global \
  --agent codex \
  --copy
```

### git clone

```bash
mkdir -p ~/.codex/skills
git clone --depth 1 https://github.com/Lone3m-tech/smkt-article-visual.git \
  ~/.codex/skills/smkt-article-visual
```

Remove `--global` for a project installation. For Claude Code, replace `--agent codex` with `--agent claude-code` and use `~/.claude/skills/smkt-article-visual` as the clone destination.

## Shared workflow

Every delivery follows these three stages. They are workflow stages, not the two output choices below.

| Mode | What the Skill does | What it does not do yet |
| --- | --- | --- |
| `plan` | Finds the audience obstacle, selects one visual grammar, names the required source details, placement, and what must not be drawn. | Generate artwork or alter the source. |
| `generate` | Creates the accepted cover, figures, or frames; records the actual prompt and every revision; places article figures at their approved anchors. | Rewrite the source prose. |
| `qa` | Checks meaning, grammar topology, type hierarchy, Logo reserve, disclosure, file placement, and manifest acceptance. | Call a generated image finished merely because it exists. |

The normal sequence is `plan → generate → qa`. A direct-generation request may skip plan acceptance, but it still creates a plan before producing assets.

## Choose your delivery

Use `article_package` when readers will follow the content independently. Use `presentation_frames` when a presenter leads the audience through the same judgments in sequence.

| Question | `article_package` | `presentation_frames` |
| --- | --- | --- |
| How the audience receives it | Reads an article or report, with a figure at the relevant passage. | Follows a speaker, proposal, workshop, or lesson in narrative order. |
| Image unit | One cover, then explanatory body figures. | Frame 01, Frame 02, Frame 03 … each carrying one accepted judgment. |
| Delivery is complete when | The cover and figures resolve once at their exact reading anchors in the Markdown source. | Every approved frame resolves once in the agreed sequence; the source prose remains untouched. |
| Best input | Finished Markdown article or report. | Speech script, proposal outline, workshop, or teaching script. |

![Article package and presentation-frame delivery modes](examples/readme-visuals/delivery-modes.png)

## From text to a visual people can follow

An attractive image is not enough when the audience needs to understand a process, comparison, hierarchy, boundary, or key judgment. The Skill starts from the narrative: it identifies the point that needs explaining, chooses a grammar, generates the image, and records the prompt, revisions, and QA in one manifest.

## Where it helps

| Scenario | Input | Delivery | What it delivers |
| --- | --- | --- | --- |
| Article or report | A finished Markdown article or research report | `article_package` | A cover and explanatory figures placed at their exact reading anchors. |
| Talk or keynote | A speech script or presentation outline | `presentation_frames` | One standalone explanation frame for each key judgment worth showing. |
| Consulting proposal | A strategy narrative or proposal | `presentation_frames` | Clear frames that make a mechanism, option, or recommendation easier to present. |
| Internal alignment | A strategy memo or retrospective | Either, based on whether people read or are led through it | Shared pictures of decisions, boundaries, systems, and handoffs. |
| Workshop or course | A teaching outline or lesson script | `presentation_frames` | Memorable teaching visuals that turn abstract concepts into a visible relationship. |

![Five narrative use cases](examples/readme-visuals/usage-scenarios.png)

## What it explains

| Reading or speaking obstacle | What it does |
| --- | --- |
| A process is hard to follow | Preserves steps, order, and handoffs with a flow figure. |
| Two approaches are hard to compare | Places the difference in one reading path. |
| A system relation is abstract | Preserves structure with a hierarchy, boundary, or relation figure. |
| Text and images have drifted apart | Places the figure at its exact article anchor or delivers it as a self-contained presentation frame. |

## Who it is for

- Creators and speakers who need a complex judgment to land quickly with an audience.
- Content teams, consultants, researchers, and educators producing consistent explanatory visuals.
- Authors or presenters who already have a narrative argument and need images to explain it—not a rewrite.

## Who it is not for

- A standalone poster, mood image, or social-media cover with no explanatory task.
- Article writing, publishing, logo design, or a full PPTX / slide-deck production workflow.
- Fabricating screenshots, charts, or factual evidence.

![Audience-fit boundary](examples/readme-visuals/audience-fit.png)

## Core capabilities

### Confirm what the figure must explain

Not every heading or spoken paragraph deserves a figure. The Skill first creates a visual plan that states the reader or audience obstacle, grammar, output mode, placement or frame order, and what must not be drawn.

![Confirm the visual plan before generation](examples/demo-article/assets/image/plan-before-generation.png)

### Translate narrative relationships into the right grammar

Narrative structure decides what needs explaining. Visual grammar makes flow, comparison, hierarchy, or boundaries legible. The editorial master keeps a package or frame series visually coherent.

![Article structure, grammar, and editorial master](examples/demo-article/assets/image/content-grammar-style.png)

### Deliver image, placement, and record together

For articles, each figure is placed after its corresponding paragraph. For talks and proposals, each frame is delivered as a standalone asset in narrative order. A manifest records every attempt, adjustment reason, Logo result, and accepted version. Generation is not complete until the selected delivery mode and QA pass.

![Traceable illustration delivery](examples/demo-article/assets/image/traceable-delivery.png)

## Visual grammar library

Choose one primary grammar for each figure. Start with the relationship an audience needs to understand, then select the structure; a shared visual style must not flatten different questions into one layout.

| Grammar | Example |
| --- | --- |
| Architecture | <img src="examples/visual-grammar/architecture.png" alt="Architecture visual grammar example" width="520"> |
| Flow | <img src="examples/visual-grammar/flow.png" alt="Flow visual grammar example" width="520"> |
| Loop | <img src="examples/visual-grammar/loop.png" alt="Loop visual grammar example" width="520"> |
| Decision tree | <img src="examples/visual-grammar/decision-tree.png" alt="Decision tree visual grammar example" width="520"> |
| Comparison | <img src="examples/visual-grammar/comparison.png" alt="Comparison visual grammar example" width="520"> |
| Matrix | <img src="examples/visual-grammar/matrix.png" alt="Matrix visual grammar example" width="520"> |
| Overlap map | <img src="examples/visual-grammar/overlap-map.png" alt="Overlap map visual grammar example" width="520"> |
| Boundary map | <img src="examples/visual-grammar/boundary-map.png" alt="Boundary map visual grammar example" width="520"> |
| Argument map | <img src="examples/visual-grammar/argument-map.png" alt="Argument map visual grammar example" width="520"> |
| Timeline | <img src="examples/visual-grammar/timeline.png" alt="Timeline visual grammar example" width="520"> |
| Continuum | <img src="examples/visual-grammar/continuum.png" alt="Continuum visual grammar example" width="520"> |
| Layer stack | <img src="examples/visual-grammar/layer-stack.png" alt="Layer stack visual grammar example" width="520"> |
| Annotated source | <img src="examples/visual-grammar/annotated-source.png" alt="Annotated source visual grammar example" width="520"> |

## Complete demo

The bundled demo shows `article_package`: “Open-source illustration Skill: images are part of the explanation,” with one cover and six explanatory body figures.

[Open the demo article](examples/demo-article/article.md)

## Default visual style

This release uses one editorial visual system across every cover, figure, and presentation frame. It keeps a series coherent without forcing every relationship into the same layout.

![Typography hierarchy](examples/readme-visuals/typography-hierarchy.png)

- **Cover and body figures have different jobs.** The cover is a quiet PPT cover: the article H1 is preserved character-for-character, supported by one dominant visual metaphor. A body figure is an explanation: centered core judgment, one short subtitle, then one dominant relationship.
- **Type has a reading order.** Body titles stay smaller than cover titles, are centered in one fixed upper band, and never compete with the top-right Logo reserve. Chinese uses one editorial serif family; English identifiers use a restrained companion face; handwritten semantic text is rejected.
- **Elements carry meaning before labels do.** Source and claim use an excerpt sheet, stages and outputs use narrow paper strips, decisions and boundaries use cut-paper fields, and positions or changes use direct ink, hatch, or anchors. Empty paper cards with a label are not enough.
- **Sketching must explain.** An engraving or pencil-sketch subject is allowed only when it comes from the article's actual relation or source detail, then receives direct labels and hairline leaders. It never defaults to plants, generic objects, icons, or decorative metaphors.
- **The finish stays editorial, not UI-like.** Pure white canvas, fine low-contrast lines, one faint paper elevation, restrained forest-green emphasis, and no dashboard cards, heavy arrows, decorative grids, crop marks, or floating ornament.
- **The Logo is deterministic.** The packaged wordmark is placed after generation in a protected white reserve. No model-rendered Logo, title, label, or connector may enter that area.
- **The style protects meaning and trust.** No heading automatically earns a figure; one figure answers one primary question with one primary grammar. Article prose stays intact and every accepted image path appears once at its approved anchor. Non-factual examples carry the lower-left disclosure `图中示例仅为解释用途，并非事实`; generated work is never presented as a real screenshot, source, or fact.

## License

Released under the [MIT License](LICENSE).
