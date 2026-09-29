# Deck design system: "Polar Ice on the SIH template"

## Hard constraints from the official SIH 2026 template (slide 7)

1. At most 6 slides, including the title slide.
2. Use only the provided template, and do not change the idea-detail pointers.
3. Submit as a **PDF only**. PPT, Word and other formats are rejected.
4. Use points, diagrams, infographics and pictures instead of paragraphs.

Consequences:
- The header, SIH logo, slide titles, team-name oval, blue footer bar, page numbers and pointer text stay exactly as they are. We fill in content under each pointer and replace only decorative art.
- **PowerPoint animations and transitions are dropped** because a PDF cannot play them. Motion design is used only to stage stills, such as the Three.js renders. Transitions can be added later if the team presents live at the finale.
- Typography follows the template: Times New Roman or Garamond for titles (the template's own), and **Arial** for everything we add. We don't use Noto in the deck, because the final PDF will be exported from PowerPoint, which has Arial but may not have Noto.

## Theses (genjutsu)

- **Visual thesis:** Polar ice on a white government template. Pale ice-blue hexagons (ice crystals, reusing the template's own hexagon) frame one dark polar visual per slide. Saffron is used only for India's stations, routes and one key number per slide.
- **Interaction thesis:** None in the PDF. Each still is framed as if paused mid-drift: the globe is lit from the upper left and routes arc gently.

## Colour (content areas only; template colours untouched)

| Token | Hex | Role |
| --- | --- | --- |
| `night-900` | `0B1F33` | Dark polar visuals and diagram nodes |
| `ocean-700` | `12395C` | Sub-headings we add |
| `glacier-400` | `5FB8D6` | Secondary: halos, data series, icons |
| `ice-100` | `DCEBF3` | Hexagon motif fill, card backgrounds |
| `ink-900` | `0E1A26` | Body text we add |
| `slate-600` | `4A5B6B` | Captions and sources (8 pt) |
| `saffron-400` | `E89C30` | The only accent (UX4G secondary-400) |
| `saffron-600` | `A46800` | Saffron text on white (AA) |

## Type sizes for added content (Arial)

- Values on the title page: 20 pt. Body points: 14–16 pt. Diagram labels: 11–12 pt. Sources: 8 pt, `slate-600`.
- Bold is reserved for the template's pointer labels. Values we add are regular weight.

## Visuals

- Three.js and GSAP scenes are rendered to transparent PNGs by `build/visuals/render.js`.
- Every picture gets alt text, and every factual claim gets an 8 pt source line.
- There are no accent bars, no title underlines and no stock iceberg photos.

## The portal (demo), separately

The portal follows GIGW 3.0 and the UX4G 3.0 tokens: Noto Sans, primary `#4A2BC2`, saffron `#E89C30`. See `docs/01-research-and-approach.md` §3.
