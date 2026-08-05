# Article Visual Plan

Use this reference to decide whether a passage needs an image and what the image must clarify. It does not choose the fixed editorial-diagram style.

## Scan order

1. Read the title and opening to identify the article's central question.
2. Read every first- and second-level section to extract the argument path.
3. Mark reader obstacles: abstract mechanisms, terminology, boundaries, and counterintuitive judgments.
4. Mark supplied screenshots, paper figures, data charts, or framework diagrams.
5. Mark existing images and their current Markdown locations.
6. Plan one cover and only the body figures that improve reader understanding.

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

## Outputs

Generate exactly one `cover` immediately after the H1, plus only the `body_figures` that clarify a reader obstacle. A body figure's paragraph anchor, reader problem, and visual grammar determine its purpose and placement; do not create a second output category for opening maps, summaries, comparisons, or source restyles.

```yaml
cover:
  article_judgment:
  visual_metaphor:
  title: exact_article_h1
  presentation: ppt_cover
  title_breaks: deliberate_for_readability
  title_safe_zone:
  output_path: assets/image/cover.png
  placement: after_h1
body_figures:
  - id:
    paragraph_anchor:
    reader_problem:
    visual_grammar:
    why_this_grammar:
    rejected_grammars: []
    must_have: true
    reason:
    skip_if:
```

`visual_explanation_contract.visible_title` is the figure's core judgment: it must be able to stand alone as the reader's first conclusion, not merely restate a section name.

When a figure needs detailed explanatory content, record the concrete chain in `source_detail_anchors`; the final figure must keep those anchors visibly linked through one selected visual grammar. If it uses any non-factual illustrative example, record the exact lower-left small-gray-italic note `图中示例仅为解释用途，并非事实`.
