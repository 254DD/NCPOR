# SIH26063: Research and Approach

29 Sep 2026 · builds on `SIH_NCPOR_RESEARCH.md` (26 Sep 2026)

Confidence tags: **[certain]** hard evidence opened today · **[likely]** strong inference or evidence from the 26 Sep brief not re-opened today · **[guess]** gap in evidence.

## 0. Blockers found today

| # | Finding | Confidence | Consequence |
| --- | --- | --- | --- |
| 1 | The national idea-submission deadline is 30 Sep 2026, which is tomorrow ([FirstVidya](https://firstvidya.com/sih-2026-guide/), [zaidsayyed tracker](https://zaidsayyed.in/tools/sih-problem-statements/sih26162)) | likely: sih.gov.in is blocked from this sandbox | The deck can't wait on a full working portal. Build a small demo that runs one real PDF end to end |
| 2 | There are now at least 10 public SIH26063 repos, not 5: DhruvGyani, Null2One, polar-science, ICEBOUND, a second PolarConnect and a second POLARIS join the 5 already known | certain (web search) | "Repository plus AI summaries" does not stand out. Only NCPOR-specific evidence and measured results do |
| 3 | The official SIH 2026 template sections are Title · Idea · Technical Approach · Feasibility and Viability · Impact and Benefits · Research and References, 6 slides max ([SIH template](https://www.sih.gov.in/letters/2026/SIH2026-IDEA-Presentation-Format.pptx)) | likely: the .pptx is blocked from this sandbox; section names come from search snippets of the official file | Third-party "6-slide guides" (e.g. tharsan1305/SIH-2026) use different titles. We follow the official ones |
| 4 | The `nemoire SIH26162` reference PDF and the NCPOR PDF to use as the demo database were not uploaded | certain | Deck content design and the demo corpus are blocked until they are uploaded |
| 5 | ncpor.res.in, ux4g.gov.in and sih.gov.in are blocked by this environment's network policy | certain | NCPOR PDFs have to be uploaded, not fetched |

## 1. What the problem actually is

The brief asks for an archive **plus** content generation. The evidence says NCPOR's bottleneck is **publishing throughput**, not storage:

- The Expedition Updates page stopped at the 42nd expedition (Oct 2022). The 45th expedition reached Maitri on 4 Nov 2025. **[likely]**: from the 26 Sep brief; the page is blocked from here
- The DSpace archive holds Antarctic reports 1–30 of 45, on a raw IP at port 8080 that timed out twice. **[likely]**: same source
- Reports are written for scientists. The 15th Arctic report has 45 projects in technical language, with Yoga Day, Onam and an ambassador visit mixed in. **[likely]**: same source
- Datasets live in NPDC, reports in DSpace, news in RSS, videos on YouTube. There are 4 separate systems and no shared search. **[likely]**

**Problem in one line:** NCPOR produces 45 years of expedition science but has no fast, trustworthy way to turn it into public content, so its public channels have gone quiet.

**Primary user:** the NCPOR outreach officer who receives a 200-page report on Monday and has to post about it by Friday. Every other audience (students, journalists, researchers, the public) receives what that person publishes.

## 2. How we address it

**Product concept: an outreach newsroom built on the archive.** The archive is table stakes. The newsroom is what makes the channels active again.

```
NCPOR PDF / RSS / media
      │
      ▼
[1] Ingest ─ clean OCR, keep PDF page ↔ printed page, Dublin Core metadata
      │
      ▼
[2] Archive ─ one searchable library linked by expedition, station and topic
      │
      ▼
[3] Draft ─ web article · X thread · Instagram captions · Class-8 explainer · Hindi (Bhashini)
      │        every sentence carries a [p. N] citation back to the source page
      ▼
[4] Verify ─ citation checker flags sentences the source does not support
      │
      ▼
[5] Approve ─ scientist or outreach-officer sign-off (can count toward SSR hours)
      │
      ▼
[6] Publish ─ GIGW 3.0 / UX4G public portal + social-ready exports
```

### Requirement coverage

| Brief item | Where it is covered |
| --- | --- |
| Expedition reports | Steps 1–2, with printed-page citations |
| Scientific datasets | Linked from NPDC records, not copied |
| Publications | Steps 1–2, using Dublin Core fields (the DSpace default) |
| Photographs and videos | Media library with mandatory alt text and captions (a GIGW requirement), with YouTube embeds |
| Institutional activities | News RSS ingest, plus activity sections extracted from reports |
| Content for websites and social media | Steps 3–6 |

### Where we differ from the 10+ rival repos

| Differentiator | Why a rival can't claim it easily | Confidence |
| --- | --- | --- |
| **Revive a stale channel:** auto-drafts restart the Expedition Updates page that stopped in 2022 | Needs our finding about NCPOR's publishing gap. No rival repo mentions it | likely |
| **Real corpus handled properly:** letter-spaced OCR fixed, PDF page vs printed page (Roman-numeral front matter) | Rivals describe an "official corpus"; none shows the cleanup | likely |
| **Measured, not claimed:** minutes per report and % of sentences with a valid citation on a test set | No rival repo publishes numbers | likely |
| **Deployable by government:** GIGW 3.0 checklist, UX4G 3.0 components, Bhashini, NIC hosting | Rivals use generic React UI kits | certain for UX4G (npm `ux4g-web-components@3.0.0`, published 27 Sep 2026) |
| **"On this day" drafts** from the 45-year archive (NCPOR's X account already posts these by hand) | Needs the archive-date index | likely |

## 3. Design rules

**Portal (demo):** GIGW 3.0 and UX4G 3.0. This is non-negotiable for a MoES deployment.

UX4G 3.0 tokens, taken from the npm package **[certain]**:

| Token | Value |
| --- | --- |
| Primary (brand purple) 600 / 700 / 50 | `#4A2BC2` / `#3D239F` / `#F2EFFF` |
| Secondary (saffron) 400 / 600 / 50 | `#E89C30` / `#A46800` / `#FFF5EA` |
| Neutral 900 / 600 / 200 / 50 | `#171717` / `#525252` / `#E5E5E5` / `#FAFAFA` |
| Type | Noto Sans (body) · Noto Sans Display (headings); Noto covers Devanagari |
| Type scale (rem) | 0.75 · 0.875 · 1 · 1.125 · 1.25 · 1.5 · 2 · 2.5 · 3 |

GIGW 3.0 checkpoints we build in from day one: keyboard navigation, alt text on every image, captions or transcripts for video, text contrast AA, bilingual (Hindi/English) switch, colour never the only signal, a skip-to-content link, and a last-updated date on every page.

**Deck:** the official SIH 2026 frame and section order, with the content-design pattern taken from the `nemoire SIH26162` PDF once it is uploaded. It uses the same UX4G palette and Noto type, so the deck and demo look like one product.

Of the skills you named, `design-dna`, `apple-design-system`, `motion-design` and `genjutsu-paint` are not installed here, and none appears in `affaan-m/ecc`, `leonxlnx/taste-skill` or `voltagent/awesome-design-md`. I apply their stated intent (palette and type, spacing and hierarchy, transition timing, visual identity) using the Vercel guidelines, taste-skill and the ECC `frontend-slides` and `design-system` skills.

## 4. Demo scope (fits the deadline)

We build one vertical slice, not 30 features:

1. Upload one NCPOR PDF (proposed: the 15th Arctic Expedition Report 2024–25, because it covers both science and institutional activities)
2. Search it, with every answer citing a page
3. Click **Generate outreach pack**: web article, X thread, Class-8 explainer and Hindi version, each with citations
4. The citation checker flags any unsupported sentence
5. Approve and publish to a GIGW/UX4G public page

## 5. Sources opened today

- [SIH26063 rival repos (web search)](https://github.com/Mudavath-Giri-Naik/DhruvGyani) · [Null2One](https://github.com/ezhilarasu-dev-hub/Null2One-1_Polar_Repository) · [polar-science](https://github.com/SanjayGoffl/polar-science) · [ICEBOUND](https://github.com/Nikhilkumar-creator/SIH) · [PolarConnect (2)](https://github.com/mishrapari210607-bit/PolarConnect) · [POLARIS (2)](https://github.com/anuvarshini276-eng/POLARIS)
- [SIH 2026 template (official, blocked here)](https://www.sih.gov.in/letters/2026/SIH2026-IDEA-Presentation-Format.pptx) · [tharsan1305/SIH-2026 guide](https://github.com/tharsan1305/SIH-2026/blob/main/SIH2026_PPT_Submission_Template.md)
- [SIH 2026 timeline (FirstVidya)](https://firstvidya.com/sih-2026-guide/)
- [UX4G (NeGD)](https://negd.gov.in/our_projects/ux4g/) · npm `ux4g-web-components@3.0.0`
- [GIGW 3.0](https://guidelines.india.gov.in/gigw3/) · [UXDT on GIGW](https://www.uxdt.nic.in/guidelines/technical-considerations/gigw-guidelines-for-indian-government-websites/)
- [45th ISEA call](http://ncpor.res.in/news/view/815)
- [affaan-m/ecc](https://github.com/affaan-m/ecc) skills used: `frontend-slides`, `design-system`, `deep-research`
