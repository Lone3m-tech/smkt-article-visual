# SimpleMkt editorial style

This is the single, direct-text visual-style source for article visuals. The compiler injects **shared + page role**, and adds **annotation** only when the page has a non-empty annotation plan.

<!-- smkt-presentation-typography -->
| role | family | weight | color | size_px | line_height_px | max_lines | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cover_title | 简宋衬线体 | semibold | #1A1A1A | 64 | 78 | 2 | local |
| body_title | 简宋衬线体 | semibold | #1A6B3A | 48 | 60 | 1 | center |
| body_subtitle | 简宋衬线体 | regular | #6B6B6B | 28 | 36 | 1 | center |
| agenda_title | 简宋衬线体 | semibold | #1A6B3A | 48 | 60 | 1 | local |
| agenda_item | 简宋衬线体 | regular | #1A1A1A | 28 | 36 | 1 | local |
| closing_message | 简宋衬线体 | semibold | #1A6B3A | 52 | 64 | 1 | local |
| label | 微软雅黑（细） | regular | #515151 | 22 | 28 | 1 | local |
| note | 微软雅黑（细） | regular italic | #6B6B6B | 17 | 23 | 1 | local |
<!-- /smkt-presentation-typography -->

## Shared visual language

<!-- smkt-style:shared -->
### Form and line

- Draw recognizable people, animals, food, plants, products, natural materials, and other real-world entities as small, characterful iconic hand-drawn ink forms;
- When a source-required person, animal, or embodied object appears, use one readable asymmetric posture, gaze, or action direction to make its source-supported state or role clear; do not add a second decorative actor or an unsupported gesture;
- Give every primary real-world object one memorable, source-compatible signature feature—an opening, bend, lift, loose edge, overlap, or weight shift—rather than presenting it as a neutral specimen;
- Retain only selectively observed details that make a real-world object recognizable and characterful; omit the rest instead of fully specifying the product, but do not impose a fixed part or plane count;
- Prefer frontal, profile, lightly oblique, or flat cutaway views; allow shallow front/back overlap, tilt, visible edge thickness, and a deliberately short, broad, skewed, or mildly off-balance silhouette, but never correct them into precise perspective;
- Let related source-supported objects or states lean, overlap, open, crop, or sit at unequal heights when that preserves their relationship; do not present them as evenly spaced inventory;
- Omit seams, mesh, mechanical construction, realistic material detail, and precise foreshortening only when they do not carry the object's recognizable observed character or the source relationship;
- Use predominantly fine, visibly variable, occasionally broken deep-ink contours with sparse marks and generous white space; allow one or two short, imperfect retraced strokes where an observed edge, fold, lace, opening, or overlap deserves attention;
- Let line weight gather and release naturally around those observed details; leave one or two intentional open joins or dry breaks rather than closing and smoothing every contour;
- Use loose fine-to-medium deep-ink contours with modest pressure variation, slight wobble, occasional retracing, open joins, and imperfect turns; never derive them from perfect geometry or resolve the object as a polished product drawing;
- Keep structural connectors hairline-thin, calm, and low-contrast gray, except one declared local brand-green relation line;
- Never use line weight to encode hierarchy;
- Do not use a thick arrow, thick green route, double-weight connector, mixed connector widths, dense engraving, woodcut texture, scientific-plate or technical pen linework, dense crosshatching, repeated parallel shading, uniform vector contour, or marker-like cartoon border.

### Fill and colour

- Use pure white, deep ink, restrained gray (#7E8581, #6B6B6B, #8C8C8C), and one small concentrated brand-green (#1A6B3A) semantic accent as the default palette;
- Use very light local dry-brush or wax-pencil fills that deliberately leave paper visible;
- Keep each local fill loose, partially open, and beneath the ink contour;
- Treat every local colour as one loose directional hand gesture in a selected local region, entering unevenly and stopping early; it may cross an internal structural line but stays inside the outer silhouette, and never becomes tidy area colouring, technical highlighting, shadow, or material description;
- Establish visual focus through expressive contour, intentional whitespace, one declared local-colour fill, or one declared partial primary-subject fill; restrained gray may support structure, sparse texture, or a shallow separation, never continuous tonal volume;
- Use brand green only for one approved state, relationship, focus field, tiny object detail, short underline, or one source-supported local connector, directional arrow, or route; when `brand_green_subject_fill` is explicitly declared, use it instead on one primary subject only;
- For a declared primary-subject fill, use one or two connected local regions of that one subject in translucent, uneven green dry-brush or wax-pencil strokes, with substantial white paper still visible and the black contour always dominant;
- Do not use brand green as a real entity’s default body colour, contour, hatching, repeated connector system, ordinary label colour, large background block, or fully opaque object fill; do not add a green relation line, second green subject, or green decorative detail when a primary-subject fill is declared;
- Use a non-brand colour only when the page explicitly declares one tiny secondary detail; never use it for an animal, box, product, or other main semantic object;
- Use no large background colour field, solid-black anchor fill, fully opaque object body, gradient, reflection, airbrush, realistic material colour, gray wash, continuous tonal shading, or realistic colour modelling.

### Surface and texture

- Allow a small number of short, dry, direction-consistent wax-pencil or crayon strokes inside a declared local fill;
- Let those strokes remain gestural and leave visible gaps of white paper; they may lightly suggest an edge turn or shallow separation, but never a continuous light source, curved tonal volume, or material finish;
- Keep the surface neutral white and flat;
- At most two quiet graphite or restrained-gray graphic punctuation marks may support the rhythm of otherwise empty space; they are never labels, symbols of a claim, extra objects, or decoration competing with the source relationship;
- Do not use cream paper, beige or warm cast, weathering, stains, damage, faux-aged filter, ornamental collage, decorative retro motifs, cast shadow, ground shadow, studio lighting, glossy 3D, cinematic depth, photographic rendering, realistic fur, cardboard texture, pencil modelling, realistic anatomy, precise perspective, dense tonal volume, or light modelling.

### Global visual exclusions

- Do not render a polished product illustration: no commercial-product refinement, merchandising silhouette, catalogue-ready detailing, precision product-design drawing, corrected perspective, or product volume resolved through tonal gray;
- Do not render landscape photography, realistic or photographic subjects, product-studio lighting, glossy 3D rendering, cinematic soft shadow, pale-green outer frame, tinted paper, warm colour cast, generic SVG, or wireframe treatment;
- Do not add unrelated visual metaphor, large shaded illustration, multiple detached paper objects, or magnifying-glass/clipboard/folded-page combinations.
<!-- /smkt-style:shared -->

## Cover visual language

<!-- smkt-style:cover -->
### Cover composition

- Apply the selected `layout_variant` as the cover's only geometry decision; it may vary title placement and abstract-carrier balance, but may not change the exact title, abstract-only scene integrity, or single-carrier principle;
- Keep the title in one continuous pure-white safe field and the abstract carrier in a separate non-title field; never let either invade the Logo reserve;
- Keep the title visually stronger and darker than the artwork;
- The selected carrier must turn the article's core judgment into one abstract editorial relationship. Use only density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve to make up to two source-supported states perceptible;
- Never render a recognizable person, animal, product, tool, vehicle, building, landscape, plant, body part, industry object, or any other representational entity; the cover is an abstract composition, not an illustration of its topic;
- A sparse, nonessential edge of the carrier may lightly enter unused whitespace, but never the title-safe field;
- Do not use montage, scattered top-and-bottom composition, multiple preview panels, multiple paper props, decorative scenery, or any representational subject.

### Cover typography

- Let the selected layout variant determine the cover title's alignment and placement inside its continuous white title field; keep it to no more than two lines;
- Use the required `editorial_treatment.title_units` to set two or three contiguous title units as an intentionally uneven but continuous title composition; their concatenation remains the exact H1 and they still occupy the same two-line title block;
- Exactly one declared title unit uses a pale brand-green selection field with a thin green outline and up to two small terminal dots; its characters remain deep ink. It is the title-level brand-green emphasis, never a text box, cursor, toolbar, or interface;
- When a cover plan declares `editorial_treatment.trace.mode: quiet_curve`, use one hairline deep-ink or restrained-gray curve with the declared zero to two small dots only in non-title whitespace; it gives viewing rhythm, never direction, topology, a metric, an arrow, a label, or a claim;
- Do not add secondary typographic treatments, decorative labels, ornamental text, or undeclared curves.

### Cover abstract treatment

- Keep the selected abstract carrier primarily white with loose fine deep-ink and restrained-gray marks; allow one separate, low-saturation brand-green dry-brush accent or short path within at most 3% of the carrier area. It must not become a second title field, a large fill, a green contour system, or an interface element;
- Do not use collage, faux-aged material, product photography, glossy 3D, cinematic lighting, or any outline that resolves into a recognizable real-world thing.
<!-- /smkt-style:cover -->

## Body visual language

<!-- smkt-style:body -->
### Body composition

- Use one calm, asymmetric semantic object cluster with 68–78% quiet space;
- Use one primary object plus two to four source-supported related objects, states, or parts; every element must map to a visible proof, annotation, or source constraint;
- Make their scale, spacing, and vertical placement an intentional irregular object-cluster rhythm; use uneven, non-grid placement rather than a row, mirrored pair, card wall, or equal-weight constellation;
- Let one meaningful near-overlap, unequal gap, or partial crop create tension inside the cluster; preserve enough separation that each source relationship remains readable;
- Keep the full artwork cluster within 44% of the content-stage width and 44% of its height. Treat it as a small editorial vignette: leave a clear white-paper margin on all four sides, and do not let any one object occupy more than two thirds of the cluster;
- When detail would require enlarging the main object, simplify it or split the explanation into another page; never enlarge one cutaway object to fill the lower content stage;
- Do not use unrelated decoration, oversized objects, repeated cards, summary tables, dashboard layouts, or a separate narrative scene.

- Keep the core judgment and subtitle centered as one typographic block; labels and notes are a separate local annotation hierarchy;
- Keep label and note text compact: label above note when they share a target, with the note visibly subordinate;
- Keep the title region free of artwork, frame, and divider;
- Do not apply this body scale to the cover, agenda, or closing roles.

### Body visual exclusions

- Do not use landscape, trees, plants, animals, people, or architecture as filler;
- Do not use unsupported visual noise such as generic dashboards, analytics-panel styling, placeholders, dashed boxes, frames, or badges;
- Do not use photography, realistic texture, studio lighting, glossy 3D, or cinematic shading.
<!-- /smkt-style:body -->

## Agenda visual language

<!-- smkt-style:agenda -->
### Agenda composition

- Apply the selected `layout_variant` as the agenda's only geometry decision; it may vary the title and sequence placement, but must retain one ordered sequence of three to five short exact items;
- Keep every agenda item compact, evenly separated, and clearly subordinate to the title;
- When a page declares `agenda_carrier`, use it only with `centered_list`: render exactly one low-density abstract navigation rhythm in the lower-right whitespace, within 18% of the canvas, subordinate to the title and sequence;
- An agenda carrier is never a recognizable entity, object, scene, plant, animal, vehicle, building, landscape, body part, industry symbol, card, badge, or decorative arrow;
- When no `agenda_carrier` is declared, use at most one small quiet abstract navigation mark; do not add cards, badges, decorative arrows, or unrelated illustrations.

### Agenda typography

- Render only the exact title and exact agenda item titles declared by the page plan;
- Do not use hand-lettering, paragraph copy, or extra labels.
<!-- /smkt-style:agenda -->

## Closing visual language

<!-- smkt-style:closing -->
### Closing composition

- `editorial_signoff` places the closing message in the upper-left title-safe field and renders exactly one tiny non-semantic dry-ink end mark in lower-right non-Logo whitespace; it never uses a carrier;
- `baseline_signoff` places the closing message in the lower-left safe field and anchors it with exactly one short, broken, low-contrast dry-ink baseline beneath it; it never uses a carrier, end mark, frame, arrow, or extra graphic;
- `echo_signoff` centers the closing message and requires exactly one low-density abstract `closing_carrier` echo in lower-right whitespace. Keep it within 18% of the canvas, subordinate to the message, and use only density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve;
- A closing carrier is never a recognizable entity, object, scene, plant, animal, vehicle, building, landscape, body part, or industry symbol;
- Do not repeat the cover, summarize the article, add a call to action, or introduce any factual claim.

### Closing typography

- Render only the exact closing message declared by the page plan, once;
- Do not add a subtitle, secondary text, decorative label, or ornamental typography.
<!-- /smkt-style:closing -->

## Annotation visual language

<!-- smkt-style:annotation -->
### Visible text

- Render only the exact labels or notes declared by this page’s annotation plan, each exactly once.
- When a label and note share the same target, render the label as the compact judgment and the note directly beneath it as one smaller, lighter gray line; they remain one callout, not two captions.

### Attachment

- Use adjacent short labels, local leaders, and low-contrast gray hairlines;
- Attach every label or note to its target;
- A paired label and note share one leader; do not add a second leader, frame, card, or badge for the note;
- Keep every annotation subordinate to the illustrated relation.

### Green relation line

- Allow one equally thin, local brand-green connector, directional line, arrow, or route only when the page declares one source-supported key relationship;
- Keep all other structural lines gray.

### Annotation exclusions

- Treat annotations as meaning-bearing encoding, never decoration;
- Do not add detached captions, decorative arrows, badges, extra labels, source-support wording, field names, coordinates, colour codes, limits, or planning metadata.
<!-- /smkt-style:annotation -->
