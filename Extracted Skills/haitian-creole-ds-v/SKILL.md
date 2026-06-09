---
name: haitian-creole-ds-v
version: 1.2.0
description: >
  Use for Haitian Creole (Kreyòl Ayisyen) translation, writing, editing, checking, or analysis. Provides bilingual-quality HC↔English translation and authoritative orthography/grammar guidance based on AKA resolutions (2017, 2023), Freeman dictionaries, Fedexy grammar, and Zefi word-boundary analysis. Triggers: mentions of "Haiti", "Ayiti", "Creole", "Kreyòl", "Kreyol", "Pòtoprens"; translation requests with Creole/Haitian context; HC words/phrases (mwen, ou, bonjou, bonswa, mèsi, sak pase, n ap boule, etc.); requests to "check my Creole", "write in Creole", "edit Creole text", "check HC spelling"; word-boundary questions (e.g., "ontijan" vs "on ti jan"); bilingual forms/documents for Haitian audiences; HC grammar (TMA markers, articles, plurals, "se"/"ye", serial verbs); dialectal variation (Southern "pe" for "ap"); or any user message containing HC text. Default to using this skill when Haitian Creole involvement is ambiguous — false positives are acceptable; missed triggers are not.
---

# Haitian Creole Language Skill

Bilingual-quality translator and language advisor for Haitian Creole (Kreyòl Ayisyen), grounded in the official orthographic standards of the Akademi Kreyòl Ayisyen (AKA) and informed by the major dictionaries, grammars, and linguistic scholarship of the language.

## Citation Behavior

When making claims about HC rules, spelling, grammar, or linguistic structure, cite the source using the short codes from the Reference Key below. Format citations inline in parentheses after the claim: e.g., "HC does not have grammatical gender (AKA-100K, K84; Fedexy §14)." For orthographic rulings, always cite the specific Dispozisyon number. For contested points, cite sources on both sides. When translating (as opposed to explaining rules), citations are not needed on every sentence; cite only when a non-obvious translation choice warrants justification.

## Reference Key

| Code | Full Reference |
|---|---|
| AKA-2R | Akademi Kreyòl Ayisyen, *Dezyèm Rezolisyon sou Òtograf Lang Kreyòl Ayisyen*, September 2023 |
| AKA-1R | Akademi Kreyòl Ayisyen, *Premye Rezolisyon sou Òtograf Lang Kreyòl Ayisyen*, June 2017 |
| AKA-100K | Pierre Michel Chery, *100 Kesyon pou AKA*, AKA, June 2024 |
| Bernard | Institut Pédagogique National (IPN), *Circular on Haitian Creole Orthography*, January 31, 1980 |
| Zefi | Lemèt Zefi, "Kritè Fòmèl pou n Kole Mo Dekole Mo an Kreyòl," in Govain (dir.), *Le créole haïtien: description et analyse*, L'Harmattan, 2017/revised 2023 |
| Fedexy | Jockey Berde Fedexy, *Gramè Deskriptif Kreyòl Ayisyen an*, 2015 |
| Freeman-EH | Bryant C. Freeman, *English-Haitian Dictionary*, v2.4 |
| Freeman-HE | Bryant C. Freeman, *Haitian-English Dictionary*, 6th ed., Institute of Haitian Studies, University of Kansas, 2010/2011 |
| Valdman | Albert Valdman et al., *Haitian Creole-English Bilingual Dictionary*, Indiana University, 2007 |
| Lefebvre | Claire Lefebvre & Robert Fournier, "Les relatives en créole haïtien," *Cahier de linguistique*, 9, 1979 |
| CFPB | Consumer Financial Protection Bureau, *Haitian Creole-English Glossary of Financial Terms*, March 2024 |
| Nesifort | Fritz Nesifort, *Kou Kreyòl*, UNDH, February 2025 |
| Thelusma | Renord Thelusma, "Nesesite aksantegi nan sistèm grafik kreyòl ayisyen an," 2025 |

When the user's folder contains HC dictionaries or reference documents, read them for domain-specific vocabulary before translating specialized content.

## Core Translation Principles

### 1. Translate meaning, not words

HC and English have fundamentally different grammars. A word-for-word approach produces unnatural output in both directions. Target a text that reads as if it were originally written in the target language by a fluent native speaker.

### 2. Prefer idiomatic HC over Gallicisms

Freeman's dictionaries systematically flag French-influenced terms with [Fr.] and cross-reference less Gallicized alternatives with "cf." (Freeman-EH; Freeman-HE). When encountering a "cf." cross-reference, prefer the alternative: "koutim lontan" over "tradisyon," "jan li boule" over "atitid," "fè konnen" over "enfòme" (Freeman-EH).

HC is not "broken French" or a French dialect. It is an independent creole language with its own grammar, phonology, and orthographic system (AKA-100K, K96). Even though ~80% of HC vocabulary is French-derived, those words were transformed through HC's own phonological system and do not retain French pronunciation or spelling rules (AKA-100K, K82). Never use French spelling conventions when writing HC.

### 3. HC lacks adverbs; use structural equivalents

HC does not have a productive adverb category the way English does (Fedexy §18; Freeman-EH, introduction). Use "ak" + noun or "jan" + adjective/noun constructions instead: "carefully" → "ak atansyon," "quickly" → "vit" or "ak vitès," "honestly" → "ak onètete." Some adverbs ending in -man/-mman do exist from adjectives ending in -an/-em: aparamman, dezyèmman (Nesifort, p. 6).

### 4. Match register to context

HC does not have the formal/informal register split that French has (tu/vous). For formal English → HC, aim for clear, direct, professional HC prose. Do not make HC "sound formal" by inserting French-influenced syntax. Be aware of code-switching (boukantay kòd) vs. interference (entèferans): conscious alternation is common, but unconscious mixing of French syntax (the "sosyolèk ibrid") should be avoided in professional documents (AKA-100K, K80, K91-92).

### 5. Preserve communicative intent

When translating idioms, proverbs, or culturally loaded expressions, prioritize the communicative function over literal meaning. Use equivalent HC pwovèb when they exist (see `references/grammar.md` for common proverbs). When no equivalent exists, translate the underlying meaning.

### 6. Direction matters

**English to HC**: Avoid French-influenced calques. Think in HC structure first, then find the words. Use the "fè + noun" pattern extensively (Freeman-EH): fè konnen (inform), fè wè (show), fè lajan (earn money), fè dodo (sleep), fè fas ak (face/confront), fè bak (reverse), fè atansyon (be careful).

**HC to English**: Preserve the directness and economy of HC expression. HC sentences are often shorter and more direct than English equivalents; do not pad the English with unnecessary qualifiers. If the HC uses vulgar register (extensively documented in Freeman-HE), flag it but translate faithfully.

### 7. Handle phrasal verbs and serial verb constructions

HC makes heavy use of verb + preposition/particle combinations that change meaning significantly (Freeman-HE): rale kò (drag oneself), rale sou (draw on), rale monte (pull up); ranje kò (get ready), ranje zafè (settle affairs), ranje ak (reconcile with); rann kont (account for), rann sèvis (do a favor), rann vizit (visit).

Serial verb constructions (two+ verbs in sequence, no conjunction) are core HC grammar (Fedexy §21): "Li kouri ale" (He ran away), "Li pran liv la bay mwen" (He took the book and gave it to me).

## Quick Grammar Reference

### TMA (Tense-Mood-Aspect) Markers

HC verbs are invariant (no conjugation). All tense, mood, and aspect information is carried by pre-verbal particles (Fedexy §19).

| Marker | Function | Example | English |
|---|---|---|---|
| (none) | Present habitual / general truth | Li manje | He eats |
| te | Simple past | Li te manje | He ate |
| ap | Progressive | Li ap manje | He is eating |
| pral | Near future | Li pral manje | He is going to eat |
| ta | Conditional | Li ta manje | He would eat |
| t ap | Past progressive | Li t ap manje | He was eating |
| t a | Past conditional | Li t a manje | He would have eaten |

In the Southern dialect (Fond-des-Blancs / Sud), "pe" sometimes replaces "ap" as the progressive marker in oral speech. Both are correct; "ap" is the AKA standard and dominates in written communication. For detailed TMA behavior, serial verbs, copula system, and imperative patterns, see `references/grammar.md`.

### Definite Articles (Post-nominal)

HC definite articles come AFTER the noun. The form depends on the final sound of the word immediately preceding the article (Lefebvre; Fedexy §15).

| Form | After... | Example |
|---|---|---|
| la | oral consonant (preceded by oral vowel) | tab la, bab la, kok la |
| a | oral vowel | papa a, kay a, lari a |
| an | nasal vowel | ban an, pen an, bonbon an |
| lan | oral consonant (preceded by nasal vowel) | tanp lan, tenb lan |
| nan | nasal consonant | pom nan, kizin nan, fanm nan |

Definite plural: "yo" (invariable) after the noun phrase. A noun takes the definite article only when the referent is "specified" through previous mention, situational presence, or shared cultural knowledge (Lefebvre). For the full article system, sentential "la," possessive paradigms, negation, and question formation, see `references/grammar.md`.

## Translation Workflow

1. **Read the full source text first** before translating.
2. **Identify domain vocabulary.** Check reference glossaries for technical terms.
3. **Draft in the target language's structure**: do not map word-by-word from source.
4. **Review for naturalness.** Would a fluent HC speaker actually say this? Would a fluent English speaker write it this way?
5. **Check orthography** against AKA rules: word boundaries, accents, article forms. See `references/orthography.md` and `references/word-boundaries.md`.
6. **Verify consistency.** Same English term → same HC term throughout a document.
7. **Check for Gallicisms.** Replace French-influenced terms with idiomatic HC alternatives (Freeman-EH). See `references/pitfalls.md`.
8. **Check clause-final articles.** Ensure sentential "la/a/an" is present where the context presupposes shared knowledge (Lefebvre).

## Reference Files

All reference files are in the `references/` directory. Read the relevant file(s) when detailed guidance on a topic is needed.

### Grammar and Usage

- **`references/grammar.md`**: Comprehensive HC grammar — sentence structure, verb system (bare verbs, serial verbs, copula, imperative), TMA markers deep dive, definite article system (phonological conditioning, two "la" particles, pragmatic conditions, sentential "la," determiner sharing), possessives, prepositions, conjunctions, relative clauses, reflexives, comparison, focus/emphasis, subordination, decreolization patterns, and common proverbs.

- **`references/pitfalls.md`**: Common translation pitfalls — false friends from French, structural traps (no grammatical gender, no verb conjugation, post-nominal articles, agglutinated French articles), English concepts without single HC equivalents, register and tone guidance for professional documents, and decreolization awareness.

### Orthography and Word Boundaries

- **`references/orthography.md`**: Complete orthographic reference — 32-grapheme alphabet, all 8 AKA orthographic rules (phonemic principle, apostrophe/hyphen rules, clitic short forms, grave accent, r/w before rounded vowels, country names, proper nouns, double consonants), particle "an," numbers (0-100+), and age/time conventions.

- **`references/word-boundaries.md`**: The most contested area of HC orthography — AKA Agglutination Theory (Dispozisyon 2-5, modifier insertion/split tests) vs. Zefi's Commutation Test, with agreement and disagreement tables, plus the complete "ontijan/on ti jan" analysis.

### Real-World Usage

- **`references/discourse-markers.md`**: High-frequency conversational expressions from the 2,551-message ADF Haiti WhatsApp corpus — core markers (tet chaje, mezanmi, monche, sa k pase, etc.), additional corpus-attested patterns, and register notes for formal vs. informal usage.

- **`references/real-world-examples.md`**: Annotated HC/English translation pairs from the WhatsApp corpus, organized by message type (scheduling, group coordination, status reports, reactions, directives). Each example includes grammatical notes on register, fusion, article choice, and code-switching.

- **`references/vocabulary-domains.md`**: Culturally rich HC vocabulary domains (coffee, food/agriculture, Vodou, kinship, weather, livestock) and the full dialectal awareness table comparing Standard (PaP) vs. Southern (Sud) features with corpus evidence from Fond-des-Blancs.

### External References (user's HC folder, if accessible)

Check for the user's Haitian Creole reference folder (often on a shared drive or local directory). Contents to look for:

- **Best Dictionaries/**: Freeman-EH v2.4; Freeman-HE 6th ed 2010. Read for vocabulary lookups.
- **Alternative Dictionaries/**: CFPB glossary; KreyolPale phrasebook. Consult for specialized vocabulary.
- **_Sort/**: AKA-1R and AKA-2R PDFs. Primary orthographic authorities.
- **English to French Dictionaries/**: Collins Robert; Langenscheidt. Useful for tracing HC etymology through French.

When uncertain about a specific word or construction, read the relevant dictionary pages before committing to a translation.
