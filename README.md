# smkt-article-visual

> Turn every key judgment into a visual people can understand.

[中文](README.zh-CN.md)

Turn a structured narrative—an article, talk, report, proposal, or workshop outline—into coherent explanatory images. It decides what needs to be shown, selects the right visual grammar, and delivers a traceable image package in the SimpleMkt editorial style.

![smkt-article-visual opening banner](examples/readme-visuals/hero-banner.png)

[View the complete demo](examples/demo-article/article.md) · [Read the runtime contract](SKILL.md)

## Install

```bash
npx skills add Lone3m-tech/smkt-article-visual \
  --skill smkt-article-visual \
  --global \
  --agent codex \
  --copy
```

Manual installation:

```bash
git clone --depth 1 https://github.com/Lone3m-tech/smkt-article-visual.git
mkdir -p ~/.codex/skills
cp -R smkt-article-visual ~/.codex/skills/smkt-article-visual
```

Remove `--global` for a project installation. For Claude Code, replace `--agent codex` with `--agent claude-code`.

## Start in 30 seconds

Give it a local Markdown source and choose a delivery mode:

```yaml
source_path: ./article.md
delivery_mode: article_package
mode: plan
```

Use `article_package` to place a cover and explanatory figures back into an article. Use `presentation_frames` when a speech, report, proposal, or workshop outline needs independent visual frames:

```yaml
source_path: ./talk.md
delivery_mode: presentation_frames
mode: plan
```

Review the visual plan first, then use `mode: generate`. When direct generation is already intended, say so in the request.

## From text to a visual people can follow

An attractive image is not enough when the audience needs to understand a process, comparison, hierarchy, boundary, or key judgment. The Skill starts from the narrative: it identifies the point that needs explaining, chooses a grammar, generates the image, and records the prompt, revisions, and QA in one manifest.

## Where it helps

| Scenario | Input | What it delivers |
| --- | --- | --- |
| Article or report | A finished Markdown article or research report | A cover and explanatory figures placed at their exact reading anchors. |
| Talk or keynote | A speech script or presentation outline | One standalone explanation frame for each key judgment worth showing. |
| Consulting proposal | A strategy narrative or proposal | Clear frames that make a mechanism, option, or recommendation easier to present. |
| Internal alignment | A strategy memo or retrospective | Shared pictures of decisions, boundaries, systems, and handoffs. |
| Workshop or course | A teaching outline or lesson script | Memorable teaching visuals that turn abstract concepts into a visible relationship. |

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

## Output modes

| Mode | Best for | What you get |
| --- | --- | --- |
| `article_package` | Articles and reports | `cover.png`, explanatory body figures, Markdown placement, and one manifest. |
| `presentation_frames` | Talks, proposals, workshops, and teaching scripts | One ordered standalone frame per accepted key judgment, plus one manifest. The source prose remains unchanged. |

```text
source.md
assets/image/
├── cover.png                       # article_package only
├── <figure-or-frame-id>.png
└── manifest.json
```

`manifest.json` appends every generation attempt; `accepted_attempt` identifies the current accepted version. The Skill never rewrites source prose.

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

The demo article, “Open-source illustration Skill: images are part of the explanation,” includes one cover and six explanatory body figures.

[Open the demo article](examples/demo-article/article.md)

## Default visual direction and boundaries

The default is the SimpleMkt editorial style: a pure-white canvas, clear type hierarchy, fine relations, restrained material, and a consistent Logo. Generated images are never presented as authentic screenshots or factual evidence; non-factual examples carry an explicit note.

## License

Released under the [MIT License](LICENSE).
