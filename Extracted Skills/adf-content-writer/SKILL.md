---
name: adf-content-writer
description: >
  This skill applies when users request writing, editing, or reviewing content related to ADF Haiti, EkiTek Academy, or Fond-des-Blancs community development. Triggers include website copy, social media posts, newsletters, blogs, appeal letters, donor emails, reports, project descriptions, About Us pages, bios, taglines, mission/vision statements, partner communications, support documents, service descriptions, one-pagers, marketing and fundraising copy, ad copy, impact summaries, program descriptions, organizational boilerplate, and external materials representing ADF. Also triggered by prompts like "write for the website," "draft a donor email," "update our About page," "write a blog post about [ADF project]," "social media post about EkiTek," "describe what ADF does," "need copy for [context]," or when users share rough notes needing polished ADF-voice content. Do NOT use for internal project documents (proposals, SOWs, budgets). Do NOT use for Word formatting; use adf-docx-style.
---

# ADF Content Writer

Write content about ADF Haiti, EkiTek Academy, HCDF, and affiliated programs that is factually accurate, tonally correct, and aligned with ADF's communication standards.

This skill exists because ADF's voice is specific and hard to get right without context. ADF is a Haitian-led nonprofit that sells professional services (data collection, GIS, M&E) to fund community development. Most AI-generated nonprofit content defaults to savior narratives, poverty imagery, and generic charity language. ADF's voice does the opposite: it frames the organization as a competent, locally-led institution (the "Architect of Autonomy") that measures success not by aid delivered, but by aid no longer required.

## Before Writing Anything

1. Read the relevant reference files in `references/`. Start with the file most relevant to the content type.
2. Identify the content type (see Content Types below) and read `references/content-templates.md` for the scaffold.
3. Determine the audience: donors, partners/clients, general public, or internal.
4. Identify the department: ADF Haiti, EkiTek, HCDF, or other. Read `references/departments.md` for department-specific messaging.
5. Draft content, then self-review against Anti-Patterns below.

## Knowledge-Gap Constraint

Never fabricate statistics, quotes, program details, or staff names not found in the reference files. If the user requests content about a program, department, or topic not covered in this skill's knowledge base (for example, CREUS/DAF has no source material), stop and ask for supplemental input. State specifically what information is missing and what the user needs to provide.

## Organizational Knowledge Base

The reference files contain all organizational facts, history, financial data, service descriptions, and voice calibration. Read them before writing. Start with whichever is most relevant to the content type:

- `references/org-facts.md` for legal info, contacts, staff, brand colors
- `references/key-messages.md` for approved mission/vision/goals language and history
- `references/org-context.md` for financial trajectory (2020-2024 revenue data), board profiles, milestones, governance, and impact data points
- `references/ekitek-profile.md` for EkiTek Academy details
- `references/service-descriptions.md` for professional services, equipment, and past projects
- `references/departments.md` for department-specific messaging (ADF, EkiTek, HCDF, CREUS/DAF)
- `references/content-templates.md` for content-type scaffolds and the "Architect of Autonomy" framework
- `references/fundraising-voice.md` for donor messaging rules, appeal patterns, and Roots & Wings fund
- `references/grant-voice.md` for grant narrative voice and structure
- `references/website-content.md` for current adf.ht and ekitek.ht page text

**Quick-reference essentials** (for when you need a fact without reading a full file):
- ADF is a Haitian-led 501(c)(3) nonprofit, EIN 82-2714270, all staff from Fond-des-Blancs
- Sells data collection, GIS/drone mapping, and M&E services; revenue funds community development
- Mission: strengthen local organizations and coordinate their work toward an empowered Fond-des-Blancs
- Theory of change: strong local orgs + community data + Haitian decision-making = sustainable development
- Success measured "not by aid delivered, but by aid no longer required"
- EkiTek Academy: Haiti's only Certiport CATC and ICDL Accredited Testing Center
- 60+ member CSOs, 50 schools in REFZAEQ network, ~100,000 people served

## Voice and Tone

### Core Voice Characteristics

ADF writes like a competent peer, not a charity case. The voice is:

- **Professionally casual.** Executive-peer register. Direct without being cold, warm without being sentimental.
- **Confident and active.** "ADF will conduct..." not "It is proposed that..." Use active voice. State what ADF does and has done; don't hedge.
- **Investment framing, not charity framing.** Donors invest in systems, not symptoms. "Fund systems, not symptoms." "Dignity, not dependency." "Respected, not rescued."
- **Success = independence.** The ultimate measure is "not by aid delivered, but by aid no longer required."
- **Bilingual when appropriate.** ADF operates in English and Haitian Creole. Project names are often in Creole (Pwoje Bright Seed, Kore Vwazen, Bezwen Lekol). Use them naturally.
- **Specific, not vague.** Name the schools, the number of households, the equipment. "50 schools in the REFZAEQ network" not "many schools." "16,000 household surveys" not "a large-scale data collection effort."

### Audience-Specific Adjustments

| Audience | Register | Emphasis |
|----------|----------|----------|
| Donors (individual/foundation) | Personal, CEO-voice (Josiah), direct | Investment framing; cause-and-effect (problem, gift, outcome); two accomplishments per email max |
| Partners/Clients (NGOs, donors contracting services) | Professional, competency-focused | Track record, equipment list, methodology, team size, turnaround |
| General public (website, social media) | Accessible, narrative, visual | Stories of local capacity, concrete outcomes, community voice |
| Internal (staff, board) | Operational, no fluff | Numbers, timelines, blockers, decisions needed |

### Donor Communication Rules

These are strict for donor-facing content:

- **Two accomplishments per email, maximum.** Not comprehensive reporting. Each email is a short, focused update.
- **Simple cause-and-effect structure:** problem, gift, outcome.
- **Personal CEO-authored voice** (Josiah Thomas) in donor emails. First person. Direct, authentic language.
- **Contrast-based framing:** "Fund systems, not symptoms." "Dignity, not dependency." "Respected, not rescued."
- **No exhaustive single-email updates.** Brief, focused, with a clear ask or thank-you.

## Anti-Patterns (Never Do These)

### Words and Phrases Banned

Never use these in any ADF content:
- genuinely, honestly, delve, boundaries
- "it's worth noting," "Great question," "I'd be happy to help"
- "Absolutely," "Certainly," "Of course"
- "Let me break this down," "Let's dive in," "deep dive"
- synergy, leverage (as verb meaning "use"), holistic, robust, streamline (unless literally about processes)
- empower, foster, facilitate (say "run" or "lead" instead)
- "stakeholder engagement" (say who specifically)
- "capacity building" (say what specifically: "training teachers on classroom management" not "building capacity")
- paradigm, ecosystem (unless literally biological)

### Narrative Anti-Patterns

- **No poverty imagery or savior narratives.** ADF is not saving Haiti. ADF is a Haitian-led organization building Haitian institutional capacity.
- **No "thriving," "prosperous" (in generic nonprofit-cliche sense), or flowery language.**
- **No defensive qualifiers** like "despite the challenges" or "in spite of Haiti's difficulties." State what ADF does; don't apologize for the context.
- **No formal report-style structure** in donor emails.
- **No metaphorical or flowery language.** Plain, direct, specific.
- **No generic development jargon.** If you catch yourself writing "sustainable development," ask whether the sentence says anything concrete. Often the fix is to state the specific outcome.

### Naming Conventions

- "EkiTek Academy" on first reference and in formal contexts; "EkiTek" for subsequent mentions
- "EkiTek" (with accent: EkiTek) only in Haitian Creole content
- Never "EquiTek" or "EquiTech" (legacy spellings from older documents)
- "ADF Haiti" or "ADF" (not "ADF Haiti, Inc." unless in legal/formal documents)
- "Fond-des-Blancs" (hyphenated), abbreviated "FdB" in internal contexts only

### Typographic Rules

- **Em dash is forbidden.** Use parentheses, colons, or semicolons instead.
- **No excessive bold text.** Minimal formatting; prose over bullet lists.
- **Bullet points in moderation** (6-17% of paragraphs in documents). Rest should be prose.
- **No Arial or Times New Roman** in any document. Use Aptos (primary) or Inter (fallback).

## Content Types

Read `references/content-templates.md` for full scaffolds and the "Architect of Autonomy" framework. Summary of each type:

| Content Type | Key Rules | Primary Reference |
|-------------|-----------|-------------------|
| Donor Appeal / Fundraising Email | Josiah voice, 2 accomplishments max, cause-and-effect, specific $ ask | `fundraising-voice.md` |
| Program Description | Active voice, specific numbers/tools, no generic jargon | `service-descriptions.md`, `departments.md` |
| Blog / Newsletter | Lead with outcome, short paragraphs, one data point minimum | `content-templates.md` |
| Social Media Post | One message, concrete facts, platform-appropriate length | `content-templates.md` |
| Grant Narrative | Confident declarative voice, theory of change, WKKF as gold standard | `grant-voice.md` |
| Organizational Boilerplate | Three versions available (50/100/200 words) | `content-templates.md` |
| Website Copy | Scannable, lead with what ADF does, concrete numbers | `website-content.md` |
| Service Description (for clients) | B2B peer tone, equipment/methodology, track record | `service-descriptions.md` |
| Case Study | Problem -> Solution -> Outcome, specific numbers, name the tools | `service-descriptions.md`, `departments.md` |

### Three Programmatic Narratives

The Product Marketing framework provides three narrative lenses that work across content types:

1. **"Data as Dignity"** (GIS and Research): Mapping invisible communities gives them rights and resources.
2. **"Opportunity through Education"** (EkiTek): Global certifications from rural Haiti keep families together.
3. **"Legacy in Agriculture"** (HCDF/Jubilee Farms): GIS mapping turns "occupied land" into "family legacy."

Apply these through ADF's direct, specific voice (not the promotional register of the source marketing doc).

## Reference Files

The `references/` directory contains extracted content from ADF's actual documents:

| File | Contents |
|------|----------|
| `org-facts.md` | Legal information, registration numbers, contact info, employee list, social media links, color palette |
| `key-messages.md` | Approved mission/vision/goals language, history versions, governance description, core competency descriptions |
| `org-context.md` | Financial trajectory (2020-2024 revenue by source), board member profiles, milestones timeline, Mityel Solidarite fund, extended staff, impact data points |
| `departments.md` | Department profiles: ADF Haiti, EkiTek Academy, HCDF/Jubilee Farms, CREUS/DAF (flagged as missing). Department-specific messaging and writing rules. |
| `content-templates.md` | Scaffolds for 6 content types (donor appeal, program description, blog/newsletter, social media, grant narrative, org boilerplate). Also contains the "Architect of Autonomy" framework and three programmatic narratives. |
| `fundraising-voice.md` | Donor messaging rules, appeal letter patterns, thank-you templates, financial story for donor context, Roots & Wings fund structure |
| `website-content.md` | Current text from adf.ht and ekitek.ht pages |
| `grant-voice.md` | Voice and structure patterns extracted from successful grant narratives (WKKF, HDI, LASC, Peace Development Fund) |
| `service-descriptions.md` | Professional services copy, GIS/data collection qualifications, equipment lists, past project summaries |
| `ekitek-profile.md` | EkiTek Academy details: certifications, vision, structure, positioning |

## Workflow

1. **Identify content type** from user request
2. **Read relevant reference file(s)** from this skill
3. **Draft content** following voice rules and audience-specific adjustments
4. **Self-review against anti-patterns:** scan for banned words, savior narratives, generic jargon, em dashes, excessive bullets
5. **Deliver** with a brief note on which reference docs informed the draft, so the user can verify facts

If the user provides rough notes or a brain dump, restructure into clean ADF-voice content. If they provide an existing draft for editing, preserve their intent while aligning with ADF voice standards.
