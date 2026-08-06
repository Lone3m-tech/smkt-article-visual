# Narrative Visual Planning Judgment

Use this reference only during [Workflow → Plan the visual framework](../SKILL.md#1-plan-the-visual-framework) to decide whether the source needs an image, what it must clarify, and which visual grammar fits. Use the canonical `visual_plan` format, field requirements, disclosure rule, delivery contract, and completion checks from [SKILL.md](../SKILL.md); do not reproduce them here.

## Scan order

1. Read the title and opening to identify the narrative's central question.
2. Read every first- and second-level section, or every speaking beat, to extract the argument path.
3. Mark understanding obstacles: abstract mechanisms, terminology, boundaries, counterintuitive judgments, and missing links between claims.
4. Mark supplied screenshots, paper figures, data charts, or framework diagrams.
5. In `article_package`, mark existing images and their current Markdown locations.
6. Plan one cover and only the content images that make a key judgment or relation easier to understand.

## Must consider a content image

- The source enlarges one stage, branch, or mechanism within a larger system.
- The passage explains a process such as training, retrieval, tool use, or a feedback loop.
- A concept is likely to be misunderstood from prose alone.
- Several similar concepts require a comparison or boundary distinction.
- A supplied external figure needs its topology explained or restyled.
- A section needs its conclusion compressed into a structure.

## Usually skip a content image

- The paragraph is a transition or emotional setup.
- A short list or table already explains the point clearly.
- The image would repeat the heading without increasing understanding.
- The explanation requires dense exact text and should remain a table or use deterministic layout.
- No credible source exists for a requested factual, data, or screenshot claim.

## Select the cover

- Identify the one promise the title and concise visual direction must make together. That direction may be a vivid metaphor or a restrained abstract composition; it must not become a complex scene.
- In `article_package`, make the cover identify the document and invite reading.
- In `presentation_frames`, make the cover establish the premise the following sequence will unfold.
- Leave title handling, layout, Logo, and delivery fields to the contracts in `SKILL.md`.

## Select each content image

For every candidate, answer these questions before adding it to the plan:

- Which exact passage, speaking beat, or supplied source material supports it?
- What can the reader or audience not confidently infer from prose alone?
- What one conclusion should become easier to understand?
- What relationship must be visible, and which visual grammar expresses it most directly?
- Which concrete source details must remain visible so the image does not become generic?
- Why is an image better than leaving the content as prose, a list, or a table?
- Which nearby grammars were rejected, and why?

Flag any non-factual illustrative content so `SKILL.md` can apply its disclosure contract. Do not turn an illustrative example into a quote, source, screenshot, or factual claim.

## Apply the selected mode's judgment

### Article package

- Anchor each content image to one exact paragraph and its local reading obstacle.
- Offload the part that is harder to understand in prose; do not restate what the reader has just consumed.
- Place the image where it resolves that obstacle with the least interruption.

### Presentation frames

- Choose content images as narrative beats such as hook, tension, mechanism, reframe, and resolution.
- State what each image receives from the previous image and what it makes possible next.
- Ensure every image can communicate its intended judgment when shown on its own.
- Make the ordered sequence form one spoken argument: introduce the cover promise, avoid unjustified repetition, and resolve the promise at the end.
- Combine multiple source paragraphs only when they form one supported narrative slice; do not introduce a new claim.

After making these judgments, fill and validate the sole canonical `visual_plan` in `SKILL.md`.
