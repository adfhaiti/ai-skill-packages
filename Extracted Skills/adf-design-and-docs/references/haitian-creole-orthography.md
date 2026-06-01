# Haitian Creole and French Diacritics

ADF documents written in Haitian Creole (Kreyol Ayisyen) or French must carry correct
diacritics. Stripping accents to plain ASCII is a defect, not a simplification. The
`haitian-creole` skill is the authoritative reference for orthography (AKA resolutions 2017,
2023); this file is the operational rule for document and design output.

## Rule

When generating or editing any ADF deliverable that contains Haitian Creole or French text:
render the required accented characters. Never substitute an unaccented letter for an
accented one, and never "correct" a properly accented Creole term back to ASCII.

## Haitian Creole accented characters

Haitian Creole uses three accented vowels plus the digraph `ou`. The accents are not optional;
they distinguish meaning and pronunciation.

| Character | Name | Example word | Meaning |
|---|---|---|---|
| `è` | e grave | `lekòl` uses `ò`; `mèsi` | thank you |
| `ò` | o grave | `kòmanse`, `pòt`, `lekòl` | begin, door, school |
| `à` | a grave | `vwala`, `là` | there |
| `é` | e acute (loanwords/French) | `Devlòpman` (Creole) vs `Développement` (French) | development |

Common ADF terms with required accents: `Devlòpman` (Creole), `lekòl` (school), `kominote`
(community, no accent), `evalyasyon` (evaluation, no accent), `bezwen` (need, no accent),
`kòmantè` (comment), `siyati` (signature, no accent), `paj` (page, no accent).

Do not add accents where the word does not take one. Add them only where the correct
orthography requires (`è`, `ò`, `à`, and `é` in French loan spellings).

## French

ADF's legal name is `Association pour le Développement de Fond-des-Blancs` (note `é` in
Développement). French text uses `é è ê à â ç ô î û` as required. Render them; do not flatten.

## Encoding

Write files as UTF-8. In python-docx, pass accented strings directly as Python `str` (the
library encodes UTF-8). In docx-js / HTML, ensure the document declares UTF-8. When extracting
or round-tripping existing text, preserve the original bytes; do not normalize away accents.

## Verification

After generating a Creole or French document, scan the output for words that should carry
accents but appear in ASCII (for example `lekol` instead of `lekòl`, `Developpement` instead
of `Développement`). Correct any that were flattened.
