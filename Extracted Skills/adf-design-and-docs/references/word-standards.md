# ADF Word Document Standards (Full Dimensional Spec)

Authoritative dimensions extracted from ADF's production .dotx templates (Custom 13 theme,
Nov 2025) with the May 2026 layout changes applied (0.75" margins, page-number-only footer).
These override the public docx skill's visual defaults; the public docx skill still governs
code mechanics (ZIP integrity, XML round-trip, pandoc extraction, validation).

## Absolute Rules (Never Violate)

1. Font: NEVER Arial, Calibri, Helvetica, or Times New Roman. Aptos only; Inter as rendering
   fallback only when Aptos is genuinely unavailable.
2. Em dashes: NEVER the em dash character. Use parentheses, colons, or semicolons.
3. Fabrication: NEVER fabricate content. Insert `[TODO: confirm with Josiah]` for unknowns.
4. Tables: NEVER apply per-cell formatting (shading, borders, margins, bold/color on header
   runs) to data tables. Reference `GridTable4` via XML; the style handles visuals.
5. Table widths: NEVER percentage widths. Use `auto` or explicit DXA.
6. Bullets: NEVER unicode bullet characters directly in TextRun content.
7. Horizontal rules / borders: NEVER add horizontal rules, paragraph borders, or line-like
   separators anywhere, including headers and footers. No exceptions.
8. Header/footer tables: NEVER put tables inside headers or footers. Use tab stops.
9. Table row height: NEVER reduce row height below 0.22" (317 DXA). Set AT_LEAST.
10. Margins: ALWAYS 0.75" on all sides, on every section, including documents opened from a
    .dotx template. Call `force_adf_margins(doc)` after opening any template.
11. Footer: page number only ("Paj N" / "Page N"). NEVER add a confidentiality label.
12. Diacritics: ALWAYS render correct Haitian Creole and French accents (see
    haitian-creole-orthography.md). NEVER strip accents to plain ASCII.
13. Validation: Before declaring done, validate the DOCX ZIP structure is intact.

## Brand Color Palette (Custom 13 Theme)

| Role | Name | Hex | Usage |
|---|---|---|---|
| Body text | Raisin Black | `231F20` | Paragraph text, doc-wide default |
| Secondary text | Davy Grey | `58585B` | Subtitles, captions, H3, footer, metadata |
| Primary accent | Prussian Blue | `0A3D50` | H1, H2, cover bg, header border |
| Secondary accent | Smooth Green | `3EAC7A` | Status indicators, success |
| Tertiary accent | Light Sea Green | `41AAA3` | Chart series, callout borders |
| Light accent | Neptune Cyan | `6EB7B2` | (legacy footer border; footers now have no border) |
| Background fill | Pale Blue Lily | `D8E7E6` | Info box backgrounds |
| Theme dark 1 | Dark Grey | `363636` | GridTable4 header fill (via theme) |
| Inverse | White | `FFFFFF` | Cover page title on Prussian Blue |

Data tables use Word's built-in grayscale `GridTable4` (`363636` header, `D6D6D6` banding) and
are intentionally excluded from the brand palette.

Status scale: Smooth Green `3EAC7A` (on track), Amber `FFC107` (at risk), Orange `FF9800`
(behind), Red `F44336` (critical), Dark Red `B71C1C` (severe).

## Typography

| Element | Font | Points | Weight | Color | Space before/after (DXA) |
|---|---|---|---|---|---|
| Cover title | Aptos | 24-36 | SemiBold | White `FFFFFF` | n/a |
| Title | Aptos SemiBold | 28 | SemiBold | Prussian Blue `0A3D50` | 240 / 0 |
| Subtitle | Aptos | 14 | Regular | Davy Grey `58585B` | 0 / 200 |
| Heading 1 | Aptos SemiBold | 16 | SemiBold | Prussian Blue `0A3D50` | 40 / 0 |
| Heading 2 | Aptos SemiBold | 12 | SemiBold | Prussian Blue `0A3D50` | 40 / 0 |
| Heading 3 | Aptos SemiBold | 11 | SemiBold | Davy Grey `58585B` | 40 / 0 |
| Body (Normal) | Aptos | 11 | Regular | Raisin Black `231F20` | 0 / 80 |
| Table header | Aptos | 10 | (GridTable4) | (GridTable4) | n/a |
| Table body | Aptos | 10 | Regular | Raisin Black `231F20` | n/a |
| Header bar | Aptos | 9 | Mixed | Prussian Blue / Davy Grey | n/a |
| Footer | Aptos | 8 | Regular | Davy Grey `58585B` | n/a |
| Caption | Aptos | 9 | Italic | Davy Grey `58585B` | 60 / 200 |

Line spacing: 1.15x (276 twips) body; single (240 twips) headings. Headings use the "Aptos
SemiBold" font face, NOT Aptos with the bold flag. Do not set `w:b` / `font.bold` on headings.
Table cells: set only `rFonts` (Aptos) and `sz` (20 half-pts); GridTable4 handles header
formatting.

## Page Layout (0.75" margins, May 2026)

| Property | DXA | Inches |
|---|---|---|
| Page width | 12240 | 8.5" |
| Page height | 15840 | 11" |
| Top margin | 1080 | 0.75" |
| Bottom margin | 1080 | 0.75" |
| Left margin | 1080 | 0.75" |
| Right margin | 1080 | 0.75" |
| Header distance | 720 | 0.5" |
| Footer distance | 432 | 0.3" |
| Content width | 10080 | 9.0" |

Apply to every section, including template-opened documents, via `force_adf_margins(doc)`.

## Header Pattern

```
ADF Haiti  |  [Document Type]
```

"ADF Haiti": Aptos 9pt Bold Prussian Blue `0A3D50`. " | " and document type: Aptos 9pt Regular
Davy Grey `58585B`. No border line.

## Footer Pattern (page number only)

```
              Paj [N]
```

Centered, Aptos 8pt Regular Davy Grey `58585B`, no border. Localized label only: "Paj " (ht),
"Page " (en/fr), "Página " (es), followed by the PAGE field. No confidentiality label.

## Table Design (GridTable4)

All data tables reference Word's built-in `GridTable4`. Inject `TableNormal` and `GridTable4`
into styles.xml if missing (helpers do this in `apply_adf_styles`). Required tblPr:

```xml
<w:tblPr>
  <w:tblStyle w:val="GridTable4"/>
  <w:tblW w:w="0" w:type="auto"/>
  <w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0"
             w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
</w:tblPr>
```

Row height >= 0.22" (317 DXA), `hRule="atLeast"`. Forbidden inside cells: `<w:shd>`,
`<w:tcBorders>`, `<w:tcMar>` on `<w:tc>`; `<w:b>`, `<w:bCs>`, `<w:color>` on `<w:r>`. Only
`<w:rFonts>` (Aptos) and `<w:sz>`/`<w:szCs>` (20 half-pts).

### Column width presets (sum to 10080)

| Type | Widths |
|---|---|
| 2-col label + value | 3780 + 6300 |
| 2-col equal | 5040 + 5040 |
| 3-col label + rating + notes | 4600 + 1280 + 4200 |
| 4-col KPI | 3440 + 2240 + 2240 + 2160 |
| 5-col budget | 3440 + 1300 + 1300 + 1900 + 2140 |

Use `GridTable1Light` for minimal lookup tables, `PlainTable1` for layout-only tables.

## Lists and Bullets

Level 0: indent left 720, hanging 360 DXA. Level 1: indent left 1440, hanging 360 DXA. Usage
6-17% of paragraphs; every section opens with prose before bullets. Max depth: level 1.

## Document Structure Defaults

| Type | Cover? | Header/footer? |
|---|---|---|
| Client Proposal | Yes | Yes |
| Grant Narrative | No | Page number only |
| SOW | No | Yes |
| Evaluation Report | Yes | Yes |
| Performance Review | No | No |
| Internal Memo | No | No |
| Client Letter | No | Letterhead header |
| Technical Report | Yes | Yes |

## Revision Protocol

Triggered by: improve, fix, redesign, rebrand, clean up, make professional, format, polish.

1. Read the document; note fonts, colors, heading hierarchy, table styles, voice, language.
2. Flag every deviation before changing anything.
3. Fix in order: structural, typography, tables (GridTable4), voice, header/footer, margins
   (force 0.75"), diacritics.
4. Validate: ZIP integrity, no repair dialog, all tables reference GridTable4, margins 0.75",
   footer carries no confidentiality label.

## Generation Path Selection

Default: python-docx with raw-XML fallback. Use docx-js for React artifacts. Use raw XML
editing to preserve tracked changes or reach features beyond python-docx.

## Output Location

Save to OUTPUTS: `Project Name - Document Type - v1.docx`. Provide a `computer://` link.
