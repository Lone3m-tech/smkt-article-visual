# SimpleMkt editorial style

This is the single, direct-text visual-style source for article visuals. The compiler injects **shared + page role**, and adds **annotation** only when the page has a non-empty annotation plan.

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

- Use one calm, continuous left-to-right editorial-poster composition: a clean left title field and one resolved right-side focal area;
- Let the right-side artwork carry most of the illustrative spatial area, with a diagonal growth from upper-right to lower-left or lower-right to upper-left when it helps the source promise;
- Keep the title visually stronger and darker than the artwork;
- The right-side carrier must turn the article's core judgment into one abstract editorial relationship. Use only density, interval, porosity, layering, dispersion, convergence, fracture, containment, or a non-directional curve to make up to two source-supported states perceptible;
- Never render a recognizable person, animal, product, tool, vehicle, building, landscape, plant, body part, industry object, or any other representational entity; the cover is an abstract composition, not an illustration of its topic;
- A sparse, nonessential edge of the right-side carrier may lightly enter the left whitespace, but never the title-safe field;
- Do not use montage, scattered top-and-bottom composition, multiple preview panels, multiple paper props, decorative scenery, or any representational subject.

### Cover typography

- Use a high-contrast Songti-like editorial serif, semibold, and deep ink (#1A1A1A) for the cover title;
- Keep the cover title left-aligned and vertically centered in its continuous white title field, with no more than two lines;
- Use the required `editorial_treatment.title_units` to set two or three contiguous title units as an intentionally uneven but continuous title composition; their concatenation remains the exact H1 and they still occupy the same two-line title block;
- Exactly one declared title unit uses a pale brand-green selection field with a thin green outline and up to two small terminal dots; its characters remain deep ink. It is the only brand-green area on the cover and is an editorial emphasis, never a text box, cursor, toolbar, or interface;
- When a cover plan declares `editorial_treatment.trace.mode: quiet_curve`, use one hairline deep-ink or restrained-gray curve with the declared zero to two small dots only in non-title whitespace; it gives viewing rhythm, never direction, topology, a metric, an arrow, a label, or a claim;
- Do not add secondary typographic treatments, decorative labels, ornamental text, or undeclared curves.

### Cover abstract treatment

- Keep the right-side abstract carrier primarily white with loose fine deep-ink and restrained-gray marks; use no brand green in the carrier;
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

### Body typography

- When a page renders a title and subtitle, use a high-contrast Songti-like editorial serif, semibold, and brand green (#1A6B3A) for the core judgment;
- When a page renders a title and subtitle, use regular neutral gray (#6B6B6B) for the subtitle;
- When a page renders a title and subtitle, keep the core judgment and subtitle centered as one typographic block;
- Keep the title region free of artwork, frame, and divider;
- When declared in the annotation plan, use dark-gray, medium-weight structural labels; restrained gray-green, regular labels; and small, italic, gray disclosure notes.

### Body visual exclusions

- Do not use landscape, trees, plants, animals, people, or architecture as filler;
- Do not use unsupported visual noise such as generic dashboards, analytics-panel styling, placeholders, dashed boxes, frames, or badges;
- Do not use photography, realistic texture, studio lighting, glossy 3D, or cinematic shading.
<!-- /smkt-style:body -->

## Agenda visual language

<!-- smkt-style:agenda -->
### Agenda composition

- Use one calm, centered agenda title and a single ordered vertical sequence of three to five short items;
- Keep every agenda item compact, evenly separated, and clearly subordinate to the title;
- Use one small abstract navigation mark only when it supports the sequence; do not add cards, badges, decorative arrows, or unrelated illustrations.

### Agenda typography

- Render only the exact title and exact agenda item titles declared by the page plan;
- Use restrained gray numbering and deep-ink or brand-green title emphasis; do not use hand-lettering, paragraph copy, or extra labels.
<!-- /smkt-style:agenda -->

## Closing visual language

<!-- smkt-style:closing -->
### Closing composition

- Use one calm, centered standard closing message with generous white space and, at most, one small quiet end mark;
- Do not repeat the cover, summarize the article, add a call to action, or introduce any factual claim.

### Closing typography

- Render only the exact closing message declared by the page plan, once, in high-contrast Songti-like editorial serif with restrained brand-green emphasis;
- Do not add a subtitle, secondary text, decorative label, or ornamental typography.
<!-- /smkt-style:closing -->

## Annotation visual language

<!-- smkt-style:annotation -->
### Visible text

- Render only the exact labels or notes declared by this page’s annotation plan.

### Attachment

- Use adjacent short labels, local leaders, and low-contrast gray hairlines;
- Attach every label or note to its target;
- Keep every annotation subordinate to the illustrated relation.

### Green relation line

- Allow one equally thin, local brand-green connector, directional line, arrow, or route only when the page declares one source-supported key relationship;
- Keep all other structural lines gray.

### Annotation exclusions

- Treat annotations as meaning-bearing encoding, never decoration;
- Do not add detached captions, decorative arrows, badges, extra labels, source-support wording, field names, coordinates, colour codes, limits, or planning metadata.
<!-- /smkt-style:annotation -->
