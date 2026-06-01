# Software Adviser: Output Template Reference

This file provides the canonical output format for software comparison deliverables.
Copy this structure exactly; adapt only the content.

## Full Example

```markdown
# Modern Alternatives to HashCheck Shell Extension

**Category:** File Hashing / Checksum Verification (Windows Shell Extensions)
**Date:** 2026-04-06
**Platform:** Windows 11 (Dell XPS 8950)

| Software | Platform | Pricing | Key Features | Reviews | Homepage |
|----------|----------|---------|--------------|---------|----------|
| **OpenHashTab** | Win 7+ (x86, x64, ARM64) | Free, Open Source (GPL-3) | 28 algorithms (SHA-256, MD5, CRC32, BLAKE3), VirusTotal integration, shell extension in file Properties tab, batch multi-file hashing, high DPI support. Actively maintained. | [AlternativeTo](https://alternativeto.net/software/openhashtab/) | [GitHub](https://github.com/namazso/OpenHashTab) |
| **HashMyFiles** (NirSoft) | Win 2000-11 | Free | MD5, SHA1, SHA256, SHA384, SHA512, CRC32. Portable (no install), drag-and-drop, shell integration, export to HTML/XML/CSV/text, CLI. | [AlternativeTo](https://alternativeto.net/software/hashmyfiles/) | [NirSoft](https://www.nirsoft.net/utils/hash_my_files.html) |
| **RapidCRC Unicode** | Win | Free, Open Source | CRC32, MD5, SHA1, SHA256, SHA512. Explorer integration, batch processing, SFV/MD5/SHA file creation and verification, Unicode filename support, portable option. | [AlternativeTo](https://alternativeto.net/software/rapidcrc-unicode/) | [GitHub](https://github.com/OV2/RapidCRC-Unicode) |

## Summary

**OpenHashTab is the clear winner**: it integrates into the same file Properties dialog as HashCheck, supports 28 algorithms (including modern BLAKE3), has VirusTotal checking built in, and is actively maintained. **HashMyFiles** is the best portable/USB-drive option. **RapidCRC Unicode** is the go-to for SFV verification workflows.

Install via: `winget install namazso.OpenHashTab`
```

## Column formatting rules

### Software column
- Bold the product name: `**OpenHashTab**`
- Add developer in parentheses for lesser-known tools: `**HashMyFiles** (NirSoft)`
- Do not include version numbers in the name

### Platform column
- Use abbreviations: Win, macOS, Linux, Web, iOS, Android
- Specify version range if relevant: `Win 7+`, `Win 10/11`
- Note architecture support if relevant: `x64, ARM64`

### Pricing column
- Lead with the model, then the price
- Examples of correct formatting:
  - `Free, Open Source (MIT)`
  - `Free, Open Source (GPL-3)`
  - `Free`
  - `Freemium (free tier: 3 projects; Pro $9/mo)`
  - `One-time $79`
  - `One-time $49.99 (Win), $29.99 (Android)`
  - `$12/mo or $99/yr (no perpetual option)`
  - `$15/mo; nonprofit: 50% off`
  - `Perpetual $199 + optional $49/yr maintenance`

### Key Features column
- 3-5 features as comma-separated sentence fragments
- Lead with the features most relevant to the user's stated requirements
- End with maintenance status if notable: "Actively maintained" or "Last updated 2024"
- Do not use bullet points inside table cells; use commas and periods

### Reviews column
- Default source: AlternativeTo
- Fallback sources (in order): G2, Capterra, TrustRadius, SourceForge
- Format: `[AlternativeTo](https://alternativeto.net/software/[slug]/)`
- Do not fabricate review URLs; verify they resolve

### Homepage column
- Link to official product page, not a download page
- For open-source tools, link to GitHub/GitLab repo
- Format: `[Homepage](https://example.com)` or `[GitHub](https://github.com/org/repo)`

## Summary section rules

1. Name the top pick in bold with a colon, then the reason
2. Name each alternative with its best use case in bold
3. Include `winget install <id>` for the top pick if available
4. 2-4 sentences maximum; no hedging, no "it depends on your needs"

## File naming convention

Save to: `/mnt/user-data/outputs/[category-slug]-comparison.md`

Examples:
- `hashcheck-alternatives.md`
- `pdf-editors-comparison.md`
- `subscription-managers-comparison.md`
- `markdown-editors-comparison.md`
- `file-converters-comparison.md`

## Anti-patterns (do not do these)

- Do not include tools the user already has in their stack
- Do not re-recommend previously rejected tools (Rocket Money, Monarch Money, etc.)
- Do not use em dashes; use colons, semicolons, or parentheses
- Do not pad with generic "consider your needs" advice
- Do not include more than 5 options unless the user explicitly asks for more
- Do not fabricate URLs, version numbers, or pricing
- Do not include tools last updated before 2023
- Do not write an introduction paragraph before the table; the table header IS the intro
