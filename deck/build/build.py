"""Builds deck/Nemoire_SIH26063.pptx from the official SIH 2026 template.

Template rule (slide 7 of the template): only the provided template may be used, and the
idea-detail pointers must not change. So this script only fills values in, swaps the
decorative bulb art for our polar visual, and never touches headers, logos, footers or
pointer text.

Run: python3 build.py
"""
import copy
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template" / "SIH2026-IDEA-Presentation-Format.pptx"
ASSETS = ROOT / "assets"
OUT = ROOT / "Nemoire_SIH26063.pptx"

TEAM_NAME = "Nemoire"
TEAM_ID = "170341"

# Polar palette (design/MASTER.md). Used only inside content areas.
NIGHT_900 = RGBColor(0x0B, 0x1F, 0x33)
ICE_100 = RGBColor(0xDC, 0xEB, 0xF3)
SLATE_600 = RGBColor(0x4A, 0x5B, 0x6B)


def shape(slide, name):
    return next(s for s in slide.shapes if s.name == name)


def set_alt(pic, text):
    pic._element.nvPicPr.cNvPr.set("descr", text)


def append_value(paragraph, value, size):
    """Keep the template's bold label run; add the value as a regular-weight run."""
    label = paragraph.runs[0]
    label.font.size = Pt(size)
    run = copy.deepcopy(label._r)
    paragraph._p.append(run)
    new = paragraph.runs[-1]
    new.text = " " + value
    new.font.bold = False
    new.font.size = Pt(size)


def solid_fill(sp, rgb):
    """Replace a shape's fill with a solid colour, leaving its geometry and outline alone."""
    spPr = sp._element.spPr
    for tag in ("a:solidFill", "a:noFill", "a:gradFill", "a:pattFill", "a:blipFill"):
        for el in spPr.findall(qn(tag)):
            spPr.remove(el)
    fill = etree.SubElement(spPr, qn("a:solidFill"))
    etree.SubElement(fill, qn("a:srgbClr"), val=str(rgb))
    # a:solidFill must come right after the geometry element.
    geom = spPr.find(qn("a:custGeom"))
    if geom is None:
        geom = spPr.find(qn("a:prstGeom"))
    geom.addnext(fill)


def fill_title_slide(s):
    fields = shape(s, "TextBox 9").text_frame
    values = {
        "Problem Statement ID": "SIH26063",
        "Problem Statement Title": "Integrated Polar Science Outreach, Knowledge Repository and Media Dissemination Portal",
        "Theme": "Smart Education",
        "PS Category": None,  # resolved in place: "Software/Hardware" → "Software"
        "Team ID": TEAM_ID,
        "Team Name": "- " + TEAM_NAME,
    }
    for p in fields.paragraphs:
        if not p.runs:
            continue
        p.line_spacing = 1.0
        p.space_before = Pt(12)
        p.alignment = PP_ALIGN.LEFT
        key = next((k for k in values if p.text.startswith(k)), None)
        if key == "PS Category":
            p.runs[0].text = "PS Category-"
            append_value(p, "Software", 20)
        elif key:
            append_value(p, values[key], 20)

    # Template hexagon → pale ice tint (hexagon = ice-crystal motif); bulb art → globe.
    # Kept light: the template's "TITLE PAGE" text overlaps the hexagon ring.
    solid_fill(shape(s, "Freeform: Shape 26"), ICE_100)
    bulb = shape(s, "Picture 4")
    bulb._element.getparent().remove(bulb._element)

    size = Inches(4.6)
    globe = s.shapes.add_picture(str(ASSETS / "globe-title.png"), Inches(6.83), Inches(1.76), size, size)
    globe.name = "Polar globe"
    set_alt(globe, "Globe centred on the Indian Ocean showing expedition routes from NCPOR Goa "
                   "to India's Antarctic stations Maitri and Bharati.")

    cap = s.shapes.add_textbox(Inches(7.0), Inches(6.72), Inches(4.3), Inches(0.3)).text_frame
    cap.margin_left = cap.margin_right = 0
    cap.text = "Station coordinates: NCPOR met-data portal. Globe: Three.js render, Natural Earth land."
    for r in cap.paragraphs[0].runs:
        r.font.size, r.font.name, r.font.color.rgb = Pt(8), "Arial", SLATE_600


def fill_team_badge(s):
    """'Your Team Name' oval on slides 2–6."""
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.replace("\n", " ").strip() == "Your Team Name":
            p = sh.text_frame.paragraphs[0]
            p.runs[0].text = TEAM_NAME
            for extra in p.runs[1:]:
                extra._r.getparent().remove(extra._r)
            for extra in sh.text_frame.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)


def drop_slide(prs, index):
    sldIdLst = prs.slides._sldIdLst
    sld = sldIdLst[index]
    prs.part.drop_rel(sld.rId)
    sldIdLst.remove(sld)


def main():
    prs = Presentation(str(TEMPLATE))
    slides = list(prs.slides)
    fill_title_slide(slides[0])
    for s in slides[1:6]:
        fill_team_badge(s)
    drop_slide(prs, 6)  # "Important Instructions": the template says to delete it before upload
    prs.save(str(OUT))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
