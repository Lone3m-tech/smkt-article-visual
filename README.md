# smkt-article-visual

> Make every article image explain, not decorate.

[中文](README.zh-CN.md)

Turn a finished or near-finished Markdown article into a coherent package of a cover and explanatory body figures that serve reading.

![Cover for “Open-source illustration Skill: images are part of the explanation”](examples/demo-article/assets/image/cover.png)

[View the complete demo](examples/demo-article/article.md) · [Read the runtime contract](SKILL.md)

## Images are not a last-five-minutes decoration task

When an article needs to explain a process, comparison, hierarchy, boundary, or key judgment, a visually pleasing image is not enough. SMKT Article Visual starts from the article: it decides what deserves a figure, selects a grammar, places the figure after the paragraph it serves, then records prompts, revisions, and QA in one manifest.

## Who it is for

- Individual creators writing long-form Markdown who want complex judgments to be easier to understand.
- Content teams, consultants, and researchers producing consistent illustrated articles.
- Authors who already have an article argument and need explanation figures—not a rewrite.

## Who it is not for

- A standalone poster, mood image, or social-media cover.
- Article writing, publishing, logo design, or a full deck.
- Fabricating screenshots, charts, or factual evidence.

![Audience-fit boundary](examples/readme-visuals/audience-fit.png)

## Where it helps

| Reading obstacle | What it does |
| --- | --- |
| A process is hard to follow | Preserves steps, order, and handoffs with a flow figure. |
| Two approaches are hard to compare | Places the difference in one reading path. |
| A system relation is abstract | Preserves structure with a hierarchy, boundary, or relation figure. |
| Text and images have drifted apart | Places the figure immediately after its paragraph and checks the final location. |

![Four common use cases](examples/readme-visuals/usage-scenarios.png)

## Visual grammar library

Choose one primary grammar for each body figure. Start with the relationship a reader needs to understand, then select the structure; a shared visual style must not flatten different questions into one layout.

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

## Core capabilities

### Confirm what the figure must explain

Not every heading deserves a figure. The Skill first creates a visual plan that states the reader obstacle, grammar, placement, and what must not be drawn.

![Confirm the visual plan before generation](examples/demo-article/assets/image/plan-before-generation.png)

### Translate article relationships into the right grammar

Article structure decides what needs explaining. Visual grammar makes flow, comparison, hierarchy, or boundaries legible. The editorial master keeps the series visually coherent.

![Article structure, grammar, and editorial master](examples/demo-article/assets/image/content-grammar-style.png)

### Deliver image, placement, and record together

Each figure is placed after its corresponding paragraph. A manifest records every attempt, adjustment reason, Logo result, and accepted version. Generation is not complete until placement and QA pass.

![Traceable illustration delivery](examples/demo-article/assets/image/traceable-delivery.png)

## Install

Recommended:

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

## Get started

After installation, provide an article path in an Agent host that can read and write local Markdown and invoke `image_gen`:

```yaml
article_path: ./article.md
mode: plan
```

Review the visual plan first, then use `mode: generate`. When direct generation is already intended, say so in the request.

## What you get

```text
article.md
assets/image/
├── cover.png
├── <figure-id>.png
└── manifest.json
```

`manifest.json` appends every generation attempt; `accepted_attempt` identifies the current accepted version. The Skill only adds image Markdown references and does not rewrite article prose.

## Complete demo

The demo article, “Open-source illustration Skill: images are part of the explanation,” includes one cover and six explanatory body figures.

[Open the demo article](examples/demo-article/article.md)

## Default visual direction and boundaries

The default is the SimpleMkt editorial style: a pure-white canvas, clear type hierarchy, fine relations, restrained material, and a consistent Logo. Generated images are never presented as authentic screenshots or factual evidence; non-factual examples carry an explicit note.

## License

Released under the [MIT License](LICENSE).
