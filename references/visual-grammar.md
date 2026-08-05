# Visual Grammar

Choose the diagram grammar from the relationship the narrative needs a reader or audience to understand. The fixed editorial-diagram style may change only presentation; it must not invent or change relationships.

| Grammar | Use for | Do not use for |
| --- | --- | --- |
| `architecture` | Components, dependencies, branches, merges, and upstream/downstream relationships | Purely chronological steps |
| `flow` | Ordered steps and input-to-output processing | Parallel concepts without sequence |
| `loop` | Feedback, iteration, optimization, constraints, and repeated cycles | A one-time route |
| `decision_tree` | Conditional choices, if/then rules, and diverging paths | Component dependencies without a decision rule |
| `comparison` | Trade-offs or differences between two or more alternatives | A single process |
| `matrix` | Crossed dimensions, classifications, and terminology distinctions | Detailed time change |
| `overlap_map` | Shared parts, differences, intersections, and conflicts | Mutually exclusive alternatives or a sequential process |
| `boundary_map` | What belongs inside/outside a concept and what it is not | Operational sequence |
| `argument_map` | A supplied claim, its stated basis, caveat, and conclusion | Inventing evidence or asserting unsupported causality |
| `timeline` | History, phases, and temporal progression | Simultaneous system structure |
| `continuum` | Gradual position, maturity, intensity, or a spectrum | Real chronological progression |
| `layer_stack` | Abstraction levels, system layers, and containment | Dense directional dependencies |
| `annotated_source` | A supplied screenshot, paper figure, or UI image | A concept with no authentic source image |

## Selection and preservation

- Preserve an architecture as `architecture`; do not turn it into a pipeline, staircase, route map, or card grid.
- Use `flow` for “first A, then B, then C” and `loop` for “generate, evaluate, update, repeat.”
- Use `decision_tree` only when a stated condition selects a path; otherwise preserve dependencies as `architecture`.
- Use `comparison` for differences or trade-offs between alternatives. Use `matrix` only when two independent dimensions classify or position the same objects; without two dimensions, do not use `matrix`.
- Use `overlap_map` for intersection or coexistence; use `comparison` when alternatives are being weighed against each other.
- Use `argument_map` only to organize claims, stated bases, caveats, and conclusions already present in the article or supplied source; never invent support.
- Use `timeline` for temporal progression; use `flow` for a one-time sequence; use `loop` for repeated feedback.
- Use `continuum` for a non-temporal spectrum such as maturity or intensity; do not imply time passing unless the article states it.
- Select one primary reader question and one grammar per figure. Record the nearest rejected grammar when it could plausibly be confused with the selected one.
- Use `boundary_map` when the value is “this is not that.”
- Use `annotated_source` only with a supplied real asset. Label it as an editorial annotation; do not fabricate a screenshot or source.
- Do not convert every concept into circles and arrows, add decorative causality, or force distinct concepts into one layout template.

## Required image-spec fields

```yaml
visual_grammar: flow
why_this_grammar: The passage describes an ordered transformation.
rejected_grammars: []
must_preserve:
  - input-to-output order
forbidden_transformations:
  - Do not imply feedback that the article does not claim.
deterministic_layout_required: false
```

Set `deterministic_layout_required: true` when exact text, code, tabular data, or precise geometry is necessary. Keep the requirement visible in the image specification; this Skill must not introduce a local HTML, SVG, Python, or second-renderer fallback because the original result contract generates final artwork through `image_gen`.
