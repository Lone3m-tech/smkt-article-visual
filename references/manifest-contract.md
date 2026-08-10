# Page-centred manifest contract

`manifest.json` records each image page from plan through delivery. It is not a set of workflow buckets: top level contains package metadata only; all operational fields stay in the matching `pages[]` item.

## Top level

```json
{
  "schema_version": 9,
  "source_path": "article.md",
  "delivery_mode": "article_package | presentation_frames",
  "pages": []
}
```

Do not create top-level `plan`, `style`, `generate`, `logo`, `layout`, `placement`, `qa`, or global `stage` fields.

## Cover page

```json
{
  "id": "cover",
  "role": "cover",
  "status": "planned",
  "prompt_projection": "default",
  "plan": {
    "source_support": "article H1",
    "intent": "establish the article's reading promise",
    "title": "exact source H1",
    "layout_variant": "text_left_carrier_right",
    "core_promise": "...",
    "primary_carrier": "one abstract relationship carrier, never an entity or industry object",
    "visual_direction": "restrained_abstract_composition",
    "visual_progression": {"entry": "...", "development": "...", "resolution": "..."},
    "must_show": ["..."],
    "must_not_imply": ["..."],
    "editorial_treatment": {
      "title_units": [
        {"text": "first exact contiguous H1 unit", "emphasis": "none | selection_field"},
        {"text": "next exact contiguous H1 unit", "emphasis": "none | selection_field"}
      ],
      "trace": {"mode": "none | quiet_curve", "node_count": 0}
    },
    "colour_plan": {"mode": "brand_green_accent", "local_colours": [{"target": "the declared title selection field and one tiny abstract-carrier dry-brush accent", "colour_family": "brand green", "rationale": "editorial title emphasis with quiet carrier continuity"}], "limits": {"max_local_colours": 1, "gradients": "forbidden", "coverage": "small_detail_only"}},
    "scene_integrity": {"mode": "abstract", "rationale": "cover expresses the source promise through abstract spatial relationships only"},
    "annotation_plan": {"mode": "none", "items": [], "limits": {"max_items": 0, "max_text_items": 0}}
  }
}
```

`editorial_treatment` is required. `title_units` contains two or three ordered, contiguous strings whose exact concatenation equals `title`; each uses `none` or `selection_field`, and exactly one unit uses `selection_field`. All title characters remain deep ink; the selection field is the title-level brand-green emphasis, while the carrier may use one separate low-saturation dry-brush accent within at most 3% of its area. `trace.mode` is `none` or `quiet_curve`; `node_count` is 0–2 and must be 0 when the mode is `none`. The trace carries no text, arrow, metric, relation, direction, source fact, or claim.

Every cover requires `scene_integrity.mode: abstract`. Its `primary_carrier`, `visual_progression`, and `must_show` may describe only abstract spatial relationships—such as density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve—not a recognizable entity, object, scene, or industry symbol.

The cover never chooses a body grammar and never uses labels, leaders, connectors, directional lines, or notes.

`layout_variant` is optional for compatibility but should be selected explicitly for every new presentation cover. Valid cover values are `text_left_carrier_right`, `text_right_carrier_left`, `text_top_carrier_bottom`, and `text_centered`; omission resolves to `text_left_carrier_right`. The first three define a directional text/carrier split. `text_centered` centers the title and permits only a visibly secondary peripheral abstract echo, never a distinct carrier field.

## Presentation-only orientation and closing pages

`agenda` and `closing` are valid only when `delivery_mode` is `presentation_frames`. They are not body pages and never choose a body grammar.

### Agenda page

```json
{
  "id": "agenda",
  "role": "agenda",
  "status": "planned",
  "prompt_projection": "default",
  "plan": {
    "source_support": "ordered planned presentation beats",
    "intent": "orient the audience to the presentation sequence",
    "title": "目录",
    "layout_variant": "centered_list",
    "agenda_items": [
      {"title": "first planned beat", "source_support": "matching planned body beat"},
      {"title": "second planned beat", "source_support": "matching planned body beat"},
      {"title": "third planned beat", "source_support": "matching planned body beat"}
    ],
    "agenda_carrier": {
      "mode": "abstract_navigation",
      "description": "three uneven-density abstract clusters arranged along one quiet vertical rhythm",
      "placement": "lower_right"
    },
    "must_show": ["three to five ordered agenda items"],
    "must_not_imply": ["an unplanned section or claim"],
    "scene_integrity": {"mode": "abstract", "rationale": "a small navigation mark may support the ordered sequence"},
    "annotation_plan": {"mode": "none", "items": [], "limits": {"max_items": 0, "max_text_items": 0}}
  }
}
```

`agenda_items` contains three to five uniquely titled, ordered entries. Each entry names an already planned presentation beat or source section and records that support. The agenda follows the cover and precedes the first body page.

`layout_variant` is optional for compatibility but should be selected explicitly for every new presentation agenda. Valid agenda values are `centered_list`, `split_list`, `vertical_rail`, and `stepped_list`; omission resolves to `centered_list`. An `agenda_carrier` is allowed only with `centered_list`.

`agenda_carrier` is optional. When present, it uses only `mode: abstract_navigation`, a non-empty abstract `description`, and `placement: lower_right`. It is one low-density abstract rhythm of the already declared ordered beats; it may not render a recognizable entity, scene, source claim, body grammar, card, badge, or decorative arrow. Omit it for an intentionally unadorned agenda.

### Closing page

```json
{
  "id": "closing",
  "role": "closing",
  "status": "planned",
  "prompt_projection": "default",
  "plan": {
    "closing_text": "谢谢观看",
    "layout_variant": "editorial_signoff",
    "must_show": ["one standard closing message"],
    "must_not_imply": ["a new factual claim, summary, promise, or call to action"],
    "scene_integrity": {"mode": "abstract", "rationale": "a quiet standard closing requires no embodied subject"},
    "annotation_plan": {"mode": "none", "items": [], "limits": {"max_items": 0, "max_text_items": 0}}
  }
}
```

`closing_text` defaults to `谢谢观看` unless the presentation request supplies a replacement. A closing follows the final body page and is standard presentation chrome, not a source claim or a body grammar.

`layout_variant` is optional for compatibility but should be selected explicitly for every new presentation closing. Valid closing values are `editorial_signoff`, `baseline_signoff`, and `echo_signoff`; omission resolves to `editorial_signoff`.
- `editorial_signoff` is an upper-left editorial signoff: it forbids `closing_carrier` and allows exactly one tiny non-semantic lower-right end mark.
- `baseline_signoff` is a lower-left formal signoff: it forbids `closing_carrier` and uses exactly one short broken low-contrast baseline beneath the message, with no end mark, frame, arrow, or additional graphic.
- `echo_signoff` requires `closing_carrier`. It uses only `mode: abstract_echo`, a non-empty abstract `description`, and `placement: lower_right`; it is one low-density visual echo of the already planned cover carrier and may not render a recognizable entity, scene, source claim, summary, promise, or call to action.

## Body page

```json
{
  "id": "figure-1",
  "role": "body",
  "status": "planned",
  "prompt_projection": "default",
  "plan": {
    "source_support": "exact key source sentence, or the smallest contiguous source range preserving one relationship",
    "intent": "resolve one reader understanding block",
    "source_anchor": "exact supporting paragraph or contiguous range",
    "reader_block": "...",
    "source_relation": "...",
    "core_judgment": "...",
    "subtitle": "...",
    "grammar": "flow",
    "visual_solution": "source-specific objects, states, positions, boundaries, and connections",
    "must_show": ["..."],
    "must_not_imply": ["..."],
    "colour_plan": {"mode": "brand_green_accent", "local_colours": [{"target": "tiny semantic detail", "colour_family": "brand green", "rationale": "local reading emphasis"}], "limits": {"max_local_colours": 1, "gradients": "forbidden", "coverage": "small_detail_only"}},
    "grammar_proof": {"visible_evidence": ["visible fact that proves this grammar", "second visible fact that proves this grammar"]},
    "scene_integrity": {"mode": "representational", "subject_count": 1, "continuity_rules": ["..."], "forbidden": ["detached limb", "impossible occlusion", "duplicated actor"]},
    "annotation_plan": {
      "mode": "none | minimal | required",
      "items": [
        {
          "type": "label | leader | connector | directional_line | note",
          "target": "object or relationship in the page",
          "content": "exact short visible text when needed",
          "source_support": "the supporting source fact"
        }
      ],
      "limits": {"max_items": 4, "max_text_items": 4}
    }
  }
}
```

Every body plan must explicitly declare `annotation_plan`. Its required shape, item types, and limits are defined above; the compiler validates its conditional values against the selected grammar and style maxima. A `label` may be paired with a `note` on the same `target`: the label is the short judgment, while the note is one short source-supported mechanism, condition, or scope. Use no more than two paired notes per body page; they share one leader and are rendered as a single two-level callout, never as a card or detached caption. Every declared visible label or note is rendered exactly once, even when its target groups several source-supported objects or regions.

### Semantic proof contract

- `source_support` is the exact minimal source sentence or contiguous range that preserves one relationship; it is not a heading, topic, scene request, or object list.
- `reader_block` states the one judgment a reader must gain from that relationship. `core_judgment` may name that judgment for orientation, but cannot supply its proof.
- `must_show` contains two to three observable facts—states, positions, boundaries, connections, or ordered changes—that support `reader_block`. Do not write a subject, prop, or style inventory here.
- `grammar_proof.visible_evidence` records how those facts remain legible in the content stage. Each proof maps to a declared `must_show` fact and must remain readable when the core judgment and subtitle are hidden.

If the declared evidence cannot support `reader_block` without the title, revise the page plan, select another grammar, or split the source relationship before compilation.

### Conditional body plan fields

- `comparison_basis` is required only when `grammar` is `comparison`. It is an array of at least two source-supported conditions that make the alternatives visibly different in object, position, connection, sequence, or boundary; labels alone do not satisfy it.

```json
{
  "grammar": "comparison",
  "comparison_basis": ["visible condition on one alternative", "visible condition on another alternative"]
}
```

- `source_mode` is omitted for a generated illustration. Set it to `annotated_source` only when the page annotates a supplied real screenshot, paper figure, data chart, or UI image; then `source_asset` is required and records its resolvable source-asset locator. This material mode does not replace the page's `grammar` or turn the result into fabricated evidence.

```json
{
  "source_mode": "annotated_source",
  "source_asset": "path-or-source-identifier-for-the-supplied-asset"
}
```

### Optional page colour plan

`colour_plan` is optional. When omitted, the compiler records `brand_green_accent`. For a cover, that single accent is reserved for the required title selection field; `brand_green_subject_fill` is not valid for covers. When supplied, it remains the page-specific override and records one local colour entry when applicable with its required limits.

```json
{
  "colour_plan": {
    "mode": "brand_green_accent | brand_green_subject_fill | small_optional_spot | source_factual | monochrome_exception",
    "local_colours": [
      {
        "target": "tiny secondary detail, never a hero or main object",
        "colour_family": "brand green or one restrained non-brand spot family",
        "rationale": "local reading reason; not a factual colour claim"
      }
    ],
    "limits": {"max_local_colours": 1, "gradients": "forbidden", "coverage": "small_detail_only | primary_subject_partial_fill"}
  }
}
```

`brand_green_accent` and `small_optional_spot` use one entry with `rationale` and `coverage: small_detail_only`; `source_factual` uses one entry with `source_support`; `monochrome_exception` uses no entries and a non-empty `rationale`.

`brand_green_subject_fill` is a declared stylistic exception for one representational primary subject. It uses exactly one `colour_family: brand green` entry with `rationale` and `coverage: primary_subject_partial_fill`. Fill only one or two connected local regions with translucent uneven dry-brush or wax-pencil marks, retain substantial paper white and dominant ink contours, and do not use a green relation line, second green subject, or secondary green detail on that page.

Use the existing `visual_solution` to bind the drawing treatment for representational pages: state selectively observed details, a frontal/profile/lightly-oblique or flat-cutaway view with shallow spatial cues, an allowed short/broad/skewed silhouette, one source-compatible memorable feature, one posture relation (tilt, opening, overlap, crop, or weight shift), one local directional fill gesture when colour is used, and irregular arrangement of the source-supported related objects. Do not add a style-only object to `must_show` or a decorative object to the page. Gray may support structure, sparse texture, or shallow separation, never continuous tonal volume. At most two quiet gray graphic punctuation marks may support whitespace, but they never name, prove, or imply a source claim.

### Visible grammar proof and scene integrity

Every body page requires at least two non-empty `grammar_proof.visible_evidence` statements. Every page requires `scene_integrity`; its mode determines which fields apply.

```json
{
  "grammar_proof": {
    "visible_evidence": ["...", "..."]
  },
  "scene_integrity": {
    "mode": "representational | abstract",
    "subject_count": 1,
    "continuity_rules": ["every visible limb belongs to a complete, connected subject"],
    "forbidden": ["detached limb", "impossible occlusion", "duplicated actor"]
  }
}
```

For `article_package`, use `source_anchor`. For `presentation_frames`, use `source_slice`, `beat`, `previous_handoff`, and `next_bridge` instead.

## Prompt projection

Set `prompt_projection` per page before compilation:

| Value | Compiled style projection | Use |
| --- | --- | --- |
| `default` | shared editorial language + page identity + selected grammar + declared annotations | Formal production default |
| `expanded` | `default` plus every relevant natural-language style explanation selected by the style source | Strengthen an unstable style render |
| `full_diagnostic` | `default` plus the entire style Markdown as invisible guidance | Test and compare only; never the normal production default |

The compiler stores the resolved choice at `page.prompt.projection_mode`; it never changes the page plan. `page.prompt.deduplicated_style_sections` records any role-style subsections omitted only because an equivalent template or page projection already emits their rule. It is a trace of final-Prompt de-duplication, never a deletion from the canonical style source.

## Per-page lifecycle

Use only `planned`, `prompt_ready`, `generated`, `finalized`, `placed`, `qa_passed`, `qa_failed`, and `qa_skipped`. A rework replaces only that page's `prompt`, `generation`, `final`, and later fields unless a history is explicitly requested.

`prompt` stores the exact compiled text and its sources. `generation` records the model candidate. `final` records size normalization and deterministic Logo application. `placement` records source position or frame sequence. `qa` is optional and defaults to skipped when QA is disabled.
