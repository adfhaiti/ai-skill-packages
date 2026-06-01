# ADF Haiti Design System

Association pour le Développement de Fond-des-Blancs (ADF Haiti). Haitian-led US 501(c)(3)
nonprofit, Fond-des-Blancs, Sud, Haiti, 10-12 staff. ADF sells data collection, GIS/drone
mapping, and program evaluation services; revenue funds community development. ADF also runs
EkiTek Academy, an ICDL/Certiport-certified testing center.

This file governs visual/design output: HTML artifacts and prototypes, Power BI dashboards,
Excel workbook styling, presentations, and web/digital assets. For Word documents, use
`references/word-standards.md` and `references/python-docx-helpers.py` instead.

## Bundled assets

| Asset | Path |
|---|---|
| Color + type tokens (CSS custom properties) | `assets/colors_and_type.css` |
| Poppins (5 weights), Gotham (Medium, Bold) | `assets/fonts/` |
| Logo (icon, dark bg) | `assets/logo-icon-dark-bg.png` |
| Logo (full name, dark bg) | `assets/logo-full-dark-bg.png` |
| Logo (icon, color circle) | `assets/logo-icon-color.png` |
| Brand blurred background | `assets/brand-background-blurred.png` |
| Favicon | `assets/favicon-96.png` |
| Letterhead / cover header images | `assets/docx-cover-header.png`, `assets/docx-letterhead-*.png` |
| Document UI kit (proposal/SOW/report layout) | `assets/ui_kits/document/index.html` |
| Power BI dashboard UI kit | `assets/ui_kits/powerbi/index.html` |

When building visual artifacts (slides, mocks, prototypes), copy the needed assets out and
build static HTML for the user to view. For production code, read the tokens here and import
`assets/colors_and_type.css`.

## Voice and tone

Professionally casual, executive-peer. Write as a peer addressing a senior NGO director or
donor, not a supplicant. Direct, no hedging: "ADF will conduct baseline surveys," not "It is
proposed that surveys may be conducted." Active voice throughout. Investment framing for
fundraising ("Fund systems, not symptoms"); donors are investors, communities are partners.
No poverty imagery or savior narratives; ADF is a technical peer enabling Haitian-led solutions.

Casing: title case for headings and proper nouns; sentence case for body and bullets. No em
dashes (use parentheses, colons, semicolons). Oxford comma always. Spell out one through nine;
numerals for 10+. No emoji in professional deliverables.

Prohibited words: synergy, leverage (verb), holistic, robust, empower, transformative,
capacity building (filler), stakeholder (prefer "partners" or name the group), impactful,
genuinely, delve, foster, spearhead, cutting-edge, game-changing, state-of-the-art.

Language: English is primary for client deliverables; French and Haitian Creole appear in
field materials. Render Creole/French diacritics correctly (see haitian-creole-orthography.md).
Proper names: "Fond-des-Blancs" (hyphenated), "EkiTek Academy" (camelCase), "ADF Haiti" or
"ADF".

## Color system

| Name | Hex | Role |
|---|---|---|
| Raisin Black | `#231f20` | Body text, primary headings |
| Davy Grey | `#58585b` | Secondary text, subheadings |
| Prussian Blue | `#0a3d50` | Primary accent: table headers, cover pages, heading bars |
| Smooth Green | `#3eac7a` | Secondary accent: highlights, status, positive values |
| Light Sea Green | `#41aaa3` | Tertiary accent: chart series, tab colors |
| Neptune Cyan | `#6eb7b2` | Light accent: borders, dividers |
| Pale Blue Lily | `#d8e7e6` | Background fill: row banding, shaded sections |
| Off-white | `#f5f8f8` | Page background tint |

Vibe: cool and grounded. Deep teal-navy anchors authority; the green family signals growth and
environmental credibility. No warm reds or oranges in the palette. Chart series order:
Prussian Blue, Smooth Green, Light Sea Green, Neptune Cyan, Davy Grey.

## Typography

Documents/Office: Aptos SemiBold headings, Aptos Regular 11pt body. Never Arial or Times New
Roman. Web/brand display: Gotham (headlines, wordmark area); Poppins (body, labels, UI).
Fallback chain `'Aptos', 'Poppins', 'Inter', sans-serif`. Minimum sizes: 11pt / 14.7px body;
9pt captions; 24px+ slide titles. Headings always Prussian Blue; body Raisin Black; secondary
Davy Grey.

## Backgrounds and texture

Brand background: softly blurred gradient (cyan to green to off-white) from the logo mark; used
on cover pages and presentation title slides (`assets/brand-background-blurred.png`). Page
backgrounds: near-white (`#f5f8f8`) or white; no dark mode. Table banding: Pale Blue Lily
alternating rows; Prussian Blue header with white text. No photographic backgrounds in
documents; presentations may use the brand blur as a subtle panel.

## Logo system

Mark only (icon): round globe motif with diagonal bands in Prussian Blue, Smooth Green, Light
Sea Green; used as favicon and app icon. Horizontal lockup: mark plus the full org name in Davy
Grey / Poppins Regular. Dark-background variant: white wordmark on Prussian Blue
(`assets/logo-*-dark-bg.png`). Minimum clear space: half the mark height on all sides. Do not
recolor or distort the mark.

## Spacing, radii, shadows

8px base grid; tokens 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64px. Documents: 0.75" margins
all sides (matches word-standards.md); header/footer zones ~1.25cm. Radii: 3px badges/chips, 6px
cards/panels, 999px pills; no large "bubbly" radii. Shadows are Prussian Blue tinted, never pure
black: card `0 1px 4px rgba(10,61,80,0.10)`; raised panel `0 4px 12px rgba(10,61,80,0.12)`;
modal `0 12px 32px rgba(10,61,80,0.18)`.

## Motion and states

Minimal, functional transitions only (200-300ms ease-out). No bouncing, spinning, or
decorative motion. Fade plus slight upward translate for modals/toasts. Hover: darken
background 8-12% or shift links to Smooth Green. Press: darken a further 8%, scale to 0.98 on
buttons. No opacity-only hover.

## Iconography and imagery

No proprietary icon font. Favicon/app icons: the ADF globe mark at standard sizes. Word/Excel:
built-in Office symbols. Power BI: built-in icon visuals. Web/digital: Lucide (stroke-based,
1.5px) via `https://unpkg.com/lucide@latest`. No emoji in proposals, reports, or dashboards.
Imagery: cool natural tones (teals, greens, earth tones); real photography of Haitian
landscapes, community, or field work. No stock-photo cliches. Captions required on figures.

## Power BI

Star schema data models preferred. PBIR format. Brand colors on all visuals (series 1 Prussian
Blue, series 2 Smooth Green, and so on). Use `assets/ui_kits/powerbi/index.html` as the layout
reference. For DAX, modeling, and PBIR mechanics, pair with the `powerbi-pbir` skill.

## Excel

Visual styling only here; for structure and code mechanics pair with the `excel-style` and
public `xlsx` skills. Every data range a proper Excel Table with a built-in Table Style; Aptos
11pt; Prussian Blue header with white text; Pale Blue Lily banding; Total row over manual sums.
