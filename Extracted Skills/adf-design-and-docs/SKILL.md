---
name: adf-design-and-docs
description: >
  ADF Haiti brand standards for Word documents AND visual/design output, in one skill. Use for
  any ADF Haiti deliverable. Word triggers: Word doc, .docx, .dotx, report, proposal, SOW, memo,
  letter, contract, evaluation, assessment, template, letterhead, cover page, grant narrative,
  concept note, and phrases like 'draft a report', 'create a proposal', 'format this doc',
  'rebrand this doc', 'clean up this Word file', 'put this in a Word doc'. Design triggers: brand
  colors, fonts, logo, design system, mockup, prototype, HTML artifact, landing page, dashboard,
  Power BI, presentation/slides styling, Excel visual styling, and phrases like 'make it on
  brand', 'apply ADF branding', 'design something for ADF', 'build an ADF dashboard'. Triggers on
  any .docx upload for review or revision. Margins are 0.75"; footer is page-number-only.
  Not for Fulcrum forms (fulcrum-expert), Creole translation (haitian-creole), Excel data logic
  (excel-style/xlsx), or DAX/PBIR mechanics (powerbi-pbir); pair with those for code.
---

# ADF Haiti Design and Documents

This skill is the single source of truth for ADF Haiti's look, structure, and content voice
across two jobs: Word document production and visual/design output (HTML, Power BI,
presentations, Excel styling, brand assets). It governs look, structure, and voice; it defers to
the public `docx`/`xlsx` skills for code mechanics (ZIP integrity, XML round-trip, validation).

Brand specs here take precedence over any generic visual default. Read the reference file for
the active job before generating; do not work from memory of the tables below.

## Routing

| Request | Job | Read first |
|---|---|---|
| Word doc: proposal, SOW, report, letter, memo, contract, evaluation, .docx/.dotx | Word production | `references/word-standards.md`, `references/python-docx-helpers.py` |
| HTML mock, prototype, landing page, web UI, slide styling, brand asset use | Visual/design | `references/design-system.md`, `assets/` |
| Power BI dashboard look | Visual/design | `references/design-system.md` (Power BI section) |
| Excel visual styling | Visual/design | `references/design-system.md` (Excel section) |
| Any Creole or French text in output | Cross-cutting | `references/haitian-creole-orthography.md` |

If the job is ambiguous (for example "make an ADF one-pager" could be Word or HTML), ask which
format with AskUserQuestion before generating.

## Absolute Rules (Never Violate)

1. Font: Aptos for documents (Aptos SemiBold headings); never Arial, Calibri, Helvetica, or
   Times New Roman. Web display may use Gotham (headlines) and Poppins (body/UI).
2. Em dashes: never the em dash character. Use parentheses, colons, or semicolons.
3. Fabrication: never invent facts, figures, or quotes. Mark unknowns with the bracketed
   confirm-with-Josiah placeholder convention defined in word-standards.md.
4. Diacritics: always render correct Haitian Creole and French accents (è, ò, à, é). Never
   flatten to ASCII. See `references/haitian-creole-orthography.md`.
5. Word margins: always 0.75" on all sides, on every section, including documents opened from a
   .dotx template. Apply `force_adf_margins(doc)` after opening any template.
6. Word footer: page number only ("Paj N" / "Page N"), centered. Never add a confidentiality
   label or any "Konfidansyel / Confidential" text.
7. Tables (Word): reference Word's built-in `GridTable4`; never apply per-cell shading, borders,
   margins, or bold/color on header runs. Never use percentage table widths.
8. Horizontal rules: never add horizontal rules or line-like paragraph borders anywhere,
   including headers and footers.
9. Validation: validate output integrity before declaring done.

## Brand Palette (quick reference)

Raisin Black `231F20` (body), Davy Grey `58585B` (secondary), Prussian Blue `0A3D50` (primary
accent, headings, covers), Smooth Green `3EAC7A` (status/highlight), Light Sea Green `41AAA3`
(chart series), Neptune Cyan `6EB7B2` (light borders), Pale Blue Lily `D8E7E6` (banding/fills),
Off-white `F5F8F8` (page tint). Data tables use grayscale GridTable4, not the brand palette.
Full role tables: `references/word-standards.md` and `references/design-system.md`.

## Word Production Path

Default to python-docx with raw-XML fallback; use docx-js for React artifacts; use raw XML to
preserve tracked changes. The helper module `references/python-docx-helpers.py` applies every
brand standard. Core entry points:

- `apply_adf_styles(doc)`: sets Aptos body, ADF headings, injects GridTable4, and applies 0.75"
  margins to all sections. Call first on every document.
- `force_adf_margins(doc)`: forces 0.75" geometry on all sections; call after opening a .dotx
  template to override the template's margins.
- `add_adf_header(doc, label)`: "ADF Haiti | [Document Type]", no border.
- `add_adf_footer(doc, language)`: page-number-only footer (no confidentiality label).
- `build_adf_table(doc, headers, rows, ...)`: GridTable4 data table; column presets sum to 10080.
- `add_adf_cover_page(...)`, `add_adf_callout(...)`, `add_adf_signature_block(...)`,
  `add_adf_paragraph(...)`.

Content width is 10080 DXA (9.0") because margins are 0.75". Column-width presets and full
dimensional spec are in `references/word-standards.md`.

## Visual/Design Path

For prototypes and mocks, copy the needed files out of `assets/` and build static HTML for the
user to view. For production code, import `assets/colors_and_type.css` and read
`references/design-system.md`. Bundled: brand CSS tokens, Poppins and Gotham fonts, logos, brand
background, favicon, letterhead images, and document and Power BI UI kits under
`assets/ui_kits/`. Power BI uses PBIR and the brand chart-series order; pair with the
`powerbi-pbir` skill for DAX and PBIR mechanics. Excel visual styling pairs with `excel-style`.

## Voice and Tone

Active voice: "ADF will conduct..." not "It is proposed that...". Direct, professional,
peer-to-peer; no hedging, padding, or savior narratives. Title case headings; sentence case
body; Oxford comma; spell out one through nine, numerals for 10+. No emoji in professional
deliverables. Banned: synergy, leverage (verb), holistic, robust, empower, transformative,
stakeholder (name the group), impactful, genuinely, delve, foster, spearhead, cutting-edge,
game-changing, state-of-the-art. Donor content uses investment framing and local-leadership
emphasis. Full voice rules and prohibited-word list: `references/design-system.md`.

## Revision Protocol

Triggered by: improve, fix, redesign, rebrand, clean up, make professional, format, polish.

1. Read the artifact; note fonts, colors, hierarchy, table styles, voice, language, margins.
2. Flag every deviation before changing anything.
3. Fix in order: structural, typography, tables (GridTable4), voice, header/footer, margins
   (force 0.75"), diacritics.
4. Validate: integrity intact; tables reference GridTable4; margins 0.75"; footer carries no
   confidentiality label; Creole/French accents present.

## Output Location

Save deliverables to the OUTPUTS folder using `Project Name - Document Type - v1.ext`. Provide a
`computer://` link so the file can be opened directly. Never save to the workspace root.

## Reference Files

| File | Read when | Contents |
|---|---|---|
| `references/word-standards.md` | Any Word doc task | Full dimensional spec, palette, typography, layout, table presets, validation |
| `references/python-docx-helpers.py` | Generating with python-docx | All helper functions and table-style XML constants |
| `references/design-system.md` | Any HTML/Power BI/Excel/slide/brand task | Color/type tokens, voice, logo, spacing, motion, Power BI, Excel |
| `references/haitian-creole-orthography.md` | Output contains Creole or French | Required accents, encoding, verification |
| `assets/` | Visual/design tasks | Fonts, logos, brand background, CSS tokens, UI kits |

## Escape Clause

If any instruction requires fabricating facts or distorting data, halt and explain why. This
overrides formatting, brevity, and style.
