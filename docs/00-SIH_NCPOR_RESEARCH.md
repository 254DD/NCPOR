# SIH26063 Research Brief

Sep 26, 2026 · @DD

The official SIH26063 brief is one sentence long, so the jury will reward the team that shows it understands NCPOR's actual bottleneck. The evidence points to publishing throughput, not missing software: NCPOR's expedition-updates page stopped in October 2022, and its public report archive ends at expedition 30 of 45. At least one rival team already pitches grounded AI with human review, so our edge has to come from real NCPOR data, government fit and measured results.

## 1. What the brief actually says

The full official description is one sentence: *"Develop a comprehensive outreach portal that archives expedition reports, scientific datasets, publications, photographs, videos and institutional activities while generating content for websites and social media."* The entry has no dataset link, no YouTube link and no contact ([official PS export, scraped 22 Aug 2026](https://github.com/NoBugNinja/Smart-India-Hackathon-SIH-2026-Problem-Statements)).

| Field | Value | Status |
| --- | --- | --- |
| PS number | SIH26063 | Verified |
| Organisation | Ministry of Earth Sciences (MoES) | Verified |
| Department | National Centre for Polar and Ocean Research (NCPOR) | Verified |
| Category | Software | Verified |
| Theme | "Space Technology" in the 22 Aug export; "Smart Education" in later catalogues | Conflict. The August export mislabels other NCPOR entries too (logistics under "Toys & Games"), so Smart Education is likely correct |
| Idea deadline | 20 Sep 2026 in the 22 Aug export; 30 Sep 2026 on a live tracker on 26 Sep | Conflict. Ideas were still arriving on 26 Sep, so an extension to 30 Sep is likely. Confirm on sih.gov.in |
| Ideas submitted | 28 of 500 as of 26 Sep | Third-party tracker |

All seven NCPOR statements (SIH26059 to SIH26065) are one-liners of 144 to 360 characters. Other MoES institutes wrote briefs of 1,000 to 7,000 characters. NCPOR left the interpretation to teams, so the jury will judge whose reading of the problem is most credible.

**Requirement split**

| Type | Requirement | Basis |
| --- | --- | --- |
| Explicit | Archive expedition reports | Brief text |
| Explicit | Archive scientific datasets and publications | Brief text |
| Explicit | Archive photographs and videos | Brief text |
| Explicit | Archive institutional activities | Brief text |
| Explicit | Generate content for websites and social media | Brief text |
| Strongly implied | Search and discovery across all content types | "Knowledge Repository" in the title |
| Strongly implied | An editor workflow: upload, review, publish | Someone at NCPOR must feed the archive and approve what goes out |
| Strongly implied | Link to NPDC rather than duplicate it | NPDC already holds dataset metadata |
| Our proposal | Map, school explainers, Hindi output, citation checking | Not in the text. Each is justified in section 6 |

The sibling statements show NCPOR's priorities in 2026: sea-ice navigation (26059), remote station management (26060), station energy (26061), expedition logistics (26062), seafloor sensors (26064) and ocean platforms (26065). Outreach is the only one aimed at the public.

## 2. Evidence of the problem

NCPOR produces a steady flow of scientific material, but its public channels are fragmented, partly stale and written for specialists. Each row below is something we checked on the page itself.

| Finding | What we saw | Confidence |
| --- | --- | --- |
| Publishing lapses | The [Expedition Updates page](https://ncpor.res.in/pages/view/247-expedition-updates) was last updated for the 42nd expedition in October 2022. Its newest entry gives both "22 October 2022" and "15–22 October 2021" | Verified |
| Report archive is behind | The [DSpace archive](http://14.139.119.23:8080/dspace/index.jsp) lists Antarctic reports 1 to 30. Reports 6 to 8 are marked "Not Published". The 45th expedition reached Maitri on 4 Nov 2025 | Verified |
| NCPOR's own link is out of date | [NCPOR's page](http://www.ncaor.gov.in/news/view/425) says the archive holds reports 1 to 24; the archive itself holds 1 to 30 | Verified |
| Archive server is fragile | DSpace runs on a raw IP at port 8080. It loaded on 26 Sep, then timed out on two later attempts the same morning | Verified (intermittent) |
| Content is written for scientists | The [15th Arctic Expedition Report 2024–25](http://ncpor.res.in//files/Indian_Arctic_Expedition-2024-25_Report_compressed.pdf) covers 45 projects (35 summer, 10 winter) in technical language | Verified |
| Reports mix science and institutional life | The same Arctic report includes Yoga Day, Independence Day, an ambassador visit and Onam: the "institutional activities" the brief names | Verified |
| Datasets sit in a researcher tool | [NPDC](https://npdc.ncpor.res.in) serves registered expedition members and general users searching datasets. Its manual names no metadata standard, API or DOI policy | Verified (manual) |
| Outreach is mostly physical | School visits, science fairs, Science on a Sphere sessions at Goa, and a Polar & Ocean Museum under development ([NCPOR outreach](https://ncpor.res.in/pages/view/409/), [PIB, 19 Mar 2026](https://www.moes.gov.in/static/uploads/2026/03/e60113076d48467ec1e261da616aa8bb.pdf)) | Verified |
| Indian research gets less online attention | 28.5% of Indian papers received social-media attention vs 46.7% globally (2016 papers, Altmetric) ([DST summary](https://dst.gov.in/research-connected-life-can-boost-social-media-visibility)) | Verified, but dated |

What we could not verify: who at NCPOR writes the posts today, how long one post takes, and current social-media follower counts. One 15-minute conversation with NCPOR's outreach cell would replace most of our assumptions.

## 3. Content and data inventory

Enough public NCPOR material exists to demo every content type in the brief. None of it has an open reuse licence, so the product must be framed as NCPOR's own tool.

| Brief item | Source | Format and access | What we found |
| --- | --- | --- | --- |
| Expedition reports (Antarctic) | [NCPOR DSpace](http://14.139.119.23:8080/dspace/index.jsp) | PDFs split per paper; browse by title, author, date | Reports 1–30, a Weddell Sea report, a 6.1 expedition volume. Report 1 has a text layer, with letter-spaced OCR in the foreword |
| Expedition reports (Arctic) | [NCPOR Reports page](https://ncpor.res.in/pages/display/452-reports) | PDF, clean text | 15th Arctic Expedition Report 2024–25 |
| Annual reports | [NCPOR Annual Reports](https://ncpor.res.in/annualreports) | PDF per year | 2003–04 to 2024–25 (21 years) |
| Publications | DSpace "NCAOR Publications" collection | PDF | Contents not yet checked |
| Photographs | DSpace "V3 Album"; figures inside reports | Unknown | Album contents not yet checked |
| Videos | [NCPOR YouTube](https://www.youtube.com/channel/UC1h2xM-VmB1opmtTa4IreQQ) | Embed | Channel exists; volume not checked |
| Institutional activities | [NCPOR news](http://www.ncaor.gov.in/news) + [RSS feed](http://www.ncaor.gov.in/upload/rssfeed/news.xml) | HTML, RSS | Post IDs run past 1,050; the cleanest automatic feed |
| Scientific datasets | [NPDC](https://npdc.ncpor.res.in) | Web portal; per-record XML at `xml_report.jsp?id=MF-…` | XML endpoint is indexed by search engines but returned HTTP 500 when we tried |
| Station weather data | [NCPOR met data portal](https://data.ncpor.res.in/newhtml/) | Download + request | Maitri: atmospheric, GPS, magnetometer. Bharati: atmospheric, magnetometer. Dakshin Gangotri: surface |
| Sea-ice context | [NSIDC Sea Ice Index v4](https://nsidc.org/data/g02135/versions/4) | Daily CSV, free | Arctic and Antarctic extent since Nov 1978 |

Reuse terms: NCPOR's [copyright page](http://www.ncaor.gov.in/pages/display/33-copyright-policy) reads only "All Rights Reserved". Cite and link every item in the demo and do not redistribute files in bulk.

Ingestion notes:

- Old reports need text cleanup, not OCR: collapse letter-spaced words, fix hyphenation, normalise author names (the contents page of report 1 prints "S. Z. Qasim" and "Q. Z. Qasim" for the same person).
- Store PDF page and printed page separately. Front matter uses Roman numerals, so a citation to printed "p. 191" must open the right PDF page.
- Mirror every ingested file locally. The archive server cannot be relied on during a live demo.

## 4. Users

The primary user is NCPOR's outreach and cooperation cell, because the brief's one active verb, "generating content", is work that cell does. Every other group consumes what that cell publishes.

| User | What they need from the portal | Evidence | Strength |
| --- | --- | --- | --- |
| NCPOR outreach cell | Turn reports, news and photos into web, social and school content quickly and accurately | The role exists: a Scientist-in-Charge, Outreach and Cooperation, signed the museum agreement ([report](https://www.illustrateddailynews.com/india/indias-first-polar-ocean-museum-to-come-up-in-goa-as-cmd-and-ncpor-sign-agreement-865985)). The updates page lapsed in 2022 | Strong for the role; workload not verified |
| NCPOR scientists | Show public engagement with little extra effort | DST's [SSR Guidelines 2022](https://www.indiascienceandtechnology.gov.in/featured-science/bridging-science-and-society-through-scientific-social-responsibility) ask knowledge workers for at least 10 working days a year of SSR activity, weighted in appraisal | Guideline verified; adoption at NCPOR not verified |
| School students and teachers | Polar science at class level, tied to Indian expeditions | NCPOR already runs school visits; Indian stations appear in Class 8 CBSE social-science Q&A material | Medium; no NCERT chapter mapping verified |
| Journalists | Recent, citable facts with a source link | NCPOR news posts are press notes; no media kit found | Assumption |
| Researchers | Plain summaries that point to NPDC datasets and DSpace reports | NPDC and DSpace are separate systems with separate search | Medium |
| General public | Discovery: "what does India do in Antarctica?" | Low social-media attention for Indian research (section 2) | Assumption |

One persona is enough for the pitch: **the outreach officer** who gets a 200-page report on Monday and must post about it by Friday. Build every demo step around that person.

## 5. Rival teams

Five public repos target SIH26063, and all five combine a repository with AI summaries. POLARIS already claims our core idea: grounded answers, claims split into atomic facts, and mandatory human review.

| Repo | Pitch | AI | Stack | Overlap with us |
| --- | --- | --- | --- | --- |
| [POLARIS](https://github.com/ompatil018/POLARIS-ncpor) | "From expedition to evidence": provenance chains, research timeline across expeditions | Gemini RAG with local fallback; refuses unsupported answers; drafts split into atomic facts; mandatory human review | FastAPI, React, PostgreSQL + pgvector, Leaflet | High: same trust story, same stack family |
| [PolarCross](https://github.com/Solstice-SIH26/SIH063-PolarCROSS) (NSUT) | Unified repository + "AI Outreach Studio" with editorial review | Audience-specific generation with source references | Not stated | High on outreach generation |
| [PolarConnect](https://github.com/doracoderr/PolarConnect) | Admin upload → auto summary + social caption → SEO public site | Summary service, model not named | React, Express, MongoDB, Cloudinary | Medium; no verification step |
| [PolarSetu / PolarVerse](https://github.com/SURAJPRAJAPATI9596/PolarVerse) | Centralised repository and discovery | Content generation and summarisation | React, Express, MongoDB | Medium |
| [Polar-India-Hub](https://github.com/prakash-saw/Polar-India-Hub) | Station map with telemetry, media catalogue | Gemini | React 19, Express, MongoDB | Low; PS number not stated |

What none of them shows publicly:

- Evidence that they ingested NCPOR's actual DSpace reports and handled their OCR problems.
- Any finding about NCPOR's publishing gap (the 2022 lapse, the 1–30 archive).
- Government deployment fit: GIGW 3.0, Bhashini, NIC hosting.
- A measured result, such as time per report or citation accuracy.

A repo shows what a team says, not what it demos. Treat this table as a floor on the competition, not its full shape.

## 6. Where we can still win

"Grounded AI with human review" is no longer a differentiator on its own. We win by proving it on NCPOR's real archive, fitting government deployment rules, and reviving the channels NCPOR has let lapse.

**Evidence-backed differentiators**

| Differentiator | Why it matters | Evidence |
| --- | --- | --- |
| Real NCPOR corpus, cleaned | Rivals claim "official corpus"; we show reports 1–30 ingested, with letter-spaced OCR fixed and printed-page citations | OCR defect seen in report 1 |
| Revive expedition updates | Auto-draft updates from the news RSS and the expedition calendar, so the page that stopped in 2022 stays current | Updates page last touched Oct 2022 |
| "On this day" drafts from the archive | NCPOR's X account already posts #OnThisDay history by hand, e.g. the first expedition landing in 1982 | [NCPOR on X](https://x.com/ncaor_goa) |
| Government fit | GIGW 3.0 accessibility and quality checks, Bhashini for Indian languages, deployable on NIC infrastructure | [GIGW 3.0](https://guidelines.india.gov.in/introduction/), [Bhashini API docs](https://bhashini.gitbook.io/bhashini-apis) |
| Measured results | Report the time per report and the share of sentences with a valid citation on a test set; no rival repo publishes numbers | Rival repos in section 5 |

**Proposed innovations** (sound ideas, not yet evidenced)

- **Scientist review that counts as SSR.** A scientist approving one explainer logs time toward the 10 SSR days in DST's guidelines. Adoption by MoES/NCPOR is not verified.
- **Topic threads across 45 years.** Link the same place or topic across reports, such as Schirmacher Oasis geology from report 1 onward. This is where the graph store earns its place.
- **All four regions.** Cover Antarctica, the Arctic, the Southern Ocean and the Himalaya (HIMANSH). Most rivals stop at the two poles.

**Change needed in our idea deck:** slide 2's "Why it's different" compares us with BAS, AAD, SCAR and NSIDC. That is true but beside the point, because the jury compares us with rival teams. Replace it with the real-corpus, revived-updates and government-fit points above.

## 7. Government fit

A ministry portal is judged on rules student teams rarely mention. Naming three of them shows we understand how NCPOR would actually deploy the tool.

| Rule or service | What it is | What it means for us | Status |
| --- | --- | --- | --- |
| [GIGW 3.0](https://guidelines.india.gov.in/introduction/) | Guidelines for Indian Government Websites and Apps from NIC with STQC and CERT-In. Sites can earn STQC's Certified Quality Website (CQW) mark | Design the public site for accessibility from day one: keyboard navigation, alt text on every image, contrast, bilingual pages | Verified. The intro page does not state it is mandatory for every central site, and no WCAG level was quoted there |
| [Bhashini](https://bhashini.gitbook.io/bhashini-apis) | MeitY's Indian-language AI: translation, speech-to-text, text-to-speech via a pipeline config + compute API | Hindi and regional-language explainers, plus audio for accessibility | Verified. Free use is for proof-of-concept only; production needs a paid plan. How to get API keys is not stated in the docs |
| [SSR Guidelines 2022](https://www.indiascienceandtechnology.gov.in/featured-science/bridging-science-and-society-through-scientific-social-responsibility) | DST, 11 May 2022: at least 10 working days a year of SSR per knowledge worker; institutions publish annual SSR reports | A reason for scientists to review content: it counts toward their SSR | Verified for DST's guidelines; MoES adoption not verified |
| [PRITHVI / REACHOUT](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1993366) | MoES umbrella scheme 2021–26 with an outreach sub-scheme | The funding line an outreach portal fits under | Verified; extension beyond 2026 not verified |

**Metadata standards.** DSpace records use Dublin Core by default, so we can adopt the same fields for reports and publications. NPDC's manual names no metadata standard. For datasets, keep a small set of fields that map to both Dublin Core and schema.org `Dataset`, so search engines can index the public pages. Whether NPDC uses DIF or ISO 19115 internally is not verified.

## 8. Map and GIS

A station map is cheap to build from free, verified sources, but NCPOR's own documents disagree on Maitri's position. Use one source and cite it on the map.

| Station | Region | Coordinates | Source |
| --- | --- | --- | --- |
| Maitri | Antarctica, Schirmacher Oasis | 70°45′01.65″S, 11°43′01.45″E | [NCPOR met data portal](https://data.ncpor.res.in/newhtml/) |
| Maitri (conflicting) | Same | 70°45′58″S, 11°43′56″E | [43-ISEA advertisement](https://ncpor.res.in/upload/recruitments/43-ISEA%20Webpage%20advertisment.PDF) |
| Bharati | Antarctica, Larsemann Hills | 69°24.41′S, 76°11.72′E | NCPOR met data portal |
| Dakshin Gangotri (historic) | Antarctica | 70°04′27″S, 12°00′12″E | NCPOR met data portal |
| Himadri | Arctic, Ny-Ålesund, Svalbard | Not verified from an NCPOR source | [NCPOR Arctic page](https://ncpor.res.in/arctics) |
| IndARC | Arctic, Kongsfjorden mooring at \~180 m depth | Not verified | [PACER summary](https://www.10pointer.com/current-affairs/polar-science-and-cryosphere-research-pacer-scheme) |
| HIMANSH | Himalaya, Spiti, above 4,000 m, opened 9 Oct 2016 | Not verified | [PIB](https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=151572&reg=48&lang=2) |

The two Maitri positions differ by about 1 minute of latitude, roughly 2 km. That is small on a continent map but worth a footnote.

**Basemaps and layers**

- **Antarctic basemap:** [SCAR Antarctic Digital Database](https://www.bas.ac.uk/project/add/). Coastline, contours and rock outcrop as GeoPackage or shapefile in EPSG:3031, updated every 6 months.
- **Web map in polar projection:** Leaflet with [Proj4Leaflet](https://kartena.github.io/Proj4Leaflet/). NASA GIBS publishes an [Antarctic EPSG:3031 Leaflet example](https://nasa-gibs.github.io/gibs-web-examples/examples/leaflet/antarctic-epsg3031.html); we could not read its tile settings, so check them before building.
- **Sea-ice layer:** [NSIDC Sea Ice Index](https://nsidc.org/data/seaice_index/data-and-image-archive), with monthly extent shapefiles and daily CSV values.
- **Arctic projection:** EPSG:3413 is the usual choice, but we have not verified a free Arctic tile source yet.

## 9. Risks and open questions

The biggest risk is looking identical to POLARIS and PolarCross. The biggest open question is the real deadline.

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Our pitch reads like rival "grounded RAG" portals | High | High | Lead with NCPOR-specific evidence (2022 lapse, archive 1–30) and measured results |
| Idea deadline is 20 Sep, not 30 Sep | Low | Fatal | Confirm on sih.gov.in today |
| DSpace server down during demo | Medium | High | Local mirror of all ingested files |
| AI states something the report does not | Medium | High | Per-sentence citation check; nothing publishes without an approver |
| Copyright challenge on NCPOR content | Low | Medium | Frame as NCPOR's internal tool; link every item to its source |
| Bhashini keys not granted in time | Medium | Low | Open-weight translation model as fallback; Bhashini named as the production route |
| Scope creep toward 30 features | High | Medium | Build the outreach-officer flow end to end first; everything else is future scope |

**Close before submission**

- [ ] Confirm the idea deadline and 2026 PPT template on sih.gov.in
- [ ] Check a report-30 PDF for a clean text layer (DSpace timed out during this research)
- [ ] Open the DSpace "V3 Album" and "NCAOR Publications" collections and note what they hold
- [ ] Revise deck slide 2 ("Why it's different") to the section 6 points
- [ ] Try to reach NCPOR outreach for one 15-minute call, or a past expedition member via the college network

**Open research questions**

- Who writes NCPOR's posts today, and how long does one take?
- Are Antarctic reports 31–45 published anywhere public?
- Does NPDC's per-record XML follow DIF or ISO 19115?
- Has MoES adopted DST's SSR guidelines for its institutes?

## Sources

Pages opened for this brief, 26 Sep 2026.

**Problem statement and competition**

- [SIH 2026 problem statements export (JSON, scraped 22 Aug 2026)](https://github.com/NoBugNinja/Smart-India-Hackathon-SIH-2026-Problem-Statements)
- [SIH26063 tracker, Zaid Sayyed](https://zaidsayyed.in/tools/sih-problem-statements/sih26063)
- [POLARIS](https://github.com/ompatil018/POLARIS-ncpor) · [PolarCross](https://github.com/Solstice-SIH26/SIH063-PolarCROSS) · [PolarConnect](https://github.com/doracoderr/PolarConnect) · [PolarVerse](https://github.com/SURAJPRAJAPATI9596/PolarVerse) · [Polar-India-Hub](https://github.com/prakash-saw/Polar-India-Hub)

**NCPOR content and data**

- [NCPOR DSpace archive](http://14.139.119.23:8080/dspace/index.jsp)
- [Report 1 introduction PDF](http://14.139.119.23:8080/dspace/bitstream/123456789/126/3/INTRODUCTION.pdf)
- [NCPOR page linking reports 1–24](http://www.ncaor.gov.in/news/view/425)
- [Expedition Updates page](https://ncpor.res.in/pages/view/247-expedition-updates)
- [15th Indian Arctic Expedition Report 2024–25](http://ncpor.res.in//files/Indian_Arctic_Expedition-2024-25_Report_compressed.pdf)
- [NCPOR Reports page](https://ncpor.res.in/pages/display/452-reports) · [Annual Reports](https://ncpor.res.in/annualreports)
- [NCPOR RSS feeds](http://www.ncaor.gov.in/rssfeeds) · [Copyright policy](http://www.ncaor.gov.in/pages/display/33-copyright-policy)
- [NPDC user manual](https://npdc.ncpor.res.in/user_manual/National_Polar_Data_Center.pdf)
- [NCPOR met data portal](https://data.ncpor.res.in/newhtml/)
- [NCPOR outreach programme](https://ncpor.res.in/pages/view/409/)
- [45th ISEA call for proposals](http://ncpor.res.in/news/view/815)

**Government and policy**

- [MoES/PIB parliament answer, 19 Mar 2026](https://www.moes.gov.in/static/uploads/2026/03/e60113076d48467ec1e261da616aa8bb.pdf)
- [PIB: PRITHVI scheme approval](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1993366)
- [PIB: HIMANSH opened](https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=151572&reg=48&lang=2)
- [GIGW 3.0 introduction](https://guidelines.india.gov.in/introduction/)
- [Bhashini API documentation](https://bhashini.gitbook.io/bhashini-apis)
- [SSR Guidelines 2022 (ISTI portal)](https://www.indiascienceandtechnology.gov.in/featured-science/bridging-science-and-society-through-scientific-social-responsibility)
- [DST: social-media visibility of Indian research](https://dst.gov.in/research-connected-life-can-boost-social-media-visibility)
- [Polar & Ocean Museum agreement](https://www.illustrateddailynews.com/india/indias-first-polar-ocean-museum-to-come-up-in-goa-as-cmd-and-ncpor-sign-agreement-865985)

**Maps and data**

- [SCAR Antarctic Digital Database](https://www.bas.ac.uk/project/add/)
- [NSIDC Sea Ice Index v4](https://nsidc.org/data/g02135/versions/4) · [Data and image archive](https://nsidc.org/data/seaice_index/data-and-image-archive)
- [Proj4Leaflet](https://kartena.github.io/Proj4Leaflet/) · [NASA GIBS Antarctic Leaflet example](https://nasa-gibs.github.io/gibs-web-examples/examples/leaflet/antarctic-epsg3031.html)
