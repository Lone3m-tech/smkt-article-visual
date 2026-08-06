# Narrative Visual Plan

Use this reference to decide whether a passage needs an image and what the image must clarify. It does not choose the fixed editorial-diagram style. Apply the article-specific placement rules only in `article_package`; use the `presentation_frames` framework in `SKILL.md` for talks, reports, proposals, and workshop outlines.

## Scan order

1. Read the title and opening to identify the narrative's central question.
2. Read every first- and second-level section, or every speaking beat, to extract the argument path.
3. Mark reader or audience obstacles: abstract mechanisms, terminology, boundaries, and counterintuitive judgments.
4. Mark supplied screenshots, paper figures, data charts, or framework diagrams.
5. In `article_package`, mark existing images and their current Markdown locations.
6. In `article_package`, plan one cover and only the body figures that improve reader understanding. In `presentation_frames`, plan one cover followed by the standalone frames that improve audience understanding and together form a spoken narrative.

## Must consider a figure

- The article enlarges one stage, branch, or mechanism within a larger system.
- The passage explains a process such as training, retrieval, tool use, or a feedback loop.
- A concept is likely to be misunderstood from prose alone.
- Several similar concepts require a comparison or boundary distinction.
- A supplied external figure needs its topology explained or restyled.
- A section needs its conclusion compressed into a structure.

## Usually skip a figure

- The paragraph is a transition or emotional setup.
- A short list or table already explains the point clearly.
- The image would repeat the heading without increasing understanding.
- The explanation requires dense exact text and should remain a table or use deterministic layout.
- No credible source exists for a requested factual, data, or screenshot claim.

## Outputs for article_package

Use the canonical `article_package` `visual_plan` structure in [SKILL.md](../SKILL.md#required-framework-first). Generate exactly one `cover` immediately after the H1, plus only the `body_figures` that clarify a reader obstacle. A body figure's paragraph anchor, reader problem, and visual grammar determine its purpose and placement; do not create a second output category for opening maps, summaries, comparisons, or source restyles.

While filling that canonical structure, use this reference only to decide whether a figure belongs in the plan and to provide its `reader_problem`, `visual_grammar`, `why_this_grammar`, `rejected_grammars`, `why_needed`, and `must_preserve`. Do not add `must_have`, `reason`, or `skip_if`: every selected item is already required, and a skipped item does not belong in the final plan.

`visual_explanation_contract.visible_title` is the figure's core judgment: it must be able to stand alone as the reader's first conclusion, not merely restate a section name.

When a figure needs detailed explanatory content, record the concrete chain in `source_detail_anchors`; the final figure must keep those anchors visibly linked through one selected visual grammar. If it uses any non-factual illustrative example, record the exact lower-left small-gray-italic note `图中示例仅为解释用途，并非事实`.

## Outputs for presentation_frames

Use the canonical `presentation_frames` `visual_plan` structure in [SKILL.md](../SKILL.md#required-framework-first). Use the source H1 verbatim for the cover title; if the source has no H1, require an explicit `presentation_title`. Generate one presentation cover at sequence `0`, then use one ordered standalone frame only for a key judgment that helps an audience follow the narrative. Do not modify the source Markdown.

While filling that canonical structure, use this reference only to decide the cover's `narrative_promise` and `visual_metaphor`, and each frame's `source_anchor`, `audience_problem`, `key_judgment`, `narrative_beat`, `transition_from_previous`, `visual_grammar`, `why_this_grammar`, `rejected_grammars`, and `must_preserve`. Do not add `must_have`: every selected frame is already required.

Each frame must be self-contained enough to show while speaking: it carries one core judgment, the relationship that explains it, and the planned audience takeaway. The ordered sequence must make a complete presentation argument, not merely a gallery of explanatory images: the first frame must receive the cover promise, adjacent frames must not repeat a judgment or grammar without reason, and the final frame must resolve the promise. Record the cover and every frame's sequence explicitly in the manifest; never infer their order from filenames. Keep the same source-detail and non-factual-example rules as article figures.
