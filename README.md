# SIH26063: NCPOR Polar Outreach Portal (Team Nemoire, 170341)

Smart India Hackathon 2026 · MoES / NCPOR · Software · Smart Education

- `docs/00-SIH_NCPOR_RESEARCH.md`: problem research brief (26 Sep 2026)
- `docs/01-research-and-approach.md`: updated findings, solution approach, design rules, demo scope
- `deck/template/`: official SIH 2026 idea-presentation template
- `deck/Nemoire_SIH26063.pptx`: the deck, generated from the template by `deck/build/build.py`
- `deck/design/MASTER.md`: deck design system and template constraints

## Build the deck

```bash
cd deck/build
npm install                     # three, d3-geo, world-atlas, playwright (for the visuals)
node visuals/render.js globe.html ../assets/globe-title.png "lat=-37&lon=56&ls=2.0"
python3 build.py                # needs python-pptx
```

Export the final PDF from PowerPoint, not LibreOffice, so the template's Garamond header renders with correct widths.
