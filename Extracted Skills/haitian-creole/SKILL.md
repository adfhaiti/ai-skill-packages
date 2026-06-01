---
name: haitian-creole
description: >
  Expert-native/bilingual-quality translation between Haitian Creole (Kreyòl Ayisyen) and American
  English, plus authoritative guidance on HC orthography, grammar, and linguistics. Grounded in AKA
  (Akademi Kreyòl Ayisyen) resolutions (2017, 2023), Freeman dictionaries, Fedexy grammar, and Zefi
  word-boundary analysis. Use whenever the user needs to: translate between HC and English; check HC
  spelling or word boundaries (e.g., "ontijan" vs "on ti jan"); write or edit HC text; review HC
  orthography; build bilingual forms, surveys, or documents; understand HC grammar (TMA markers,
  articles, plurals); handle HC dialectal variation (Southern/Sud "pe" for "ap"); or create bilingual
  materials. Also trigger when the user writes in Haitian Creole, asks about Creole spelling, mentions
  "kreyòl", asks how to say something in Creole, or needs to translate any content for a Haitian
  audience. Even if the user just says "translate this" or "check my Creole", use this skill.
---

# Haitian Creole Language Skill

This skill makes Claude a bilingual-quality translator and language advisor for Haitian Creole (Kreyòl Ayisyen). It is grounded in the official orthographic standards set by the Akademi Kreyòl Ayisyen (AKA) and informed by the major dictionaries, grammars, and linguistic scholarship of the language.

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

HC and English have fundamentally different grammars. A word-for-word approach produces unnatural output in both directions. The target is a text that reads as if it were originally written in the target language by a fluent native speaker.

### 2. Prefer idiomatic HC over Gallicisms

Freeman's dictionaries systematically flag French-influenced terms with [Fr.] and cross-reference less Gallicized alternatives with "cf." (Freeman-EH; Freeman-HE). When you see a "cf." cross-reference pointing to a less French-sounding term, prefer the alternative. Examples:

- "koutim lontan" over "tradisyon" (Freeman-EH)
- "jan li boule" over "atitid" (Freeman-EH)
- "fè konnen" over "enfòme" (Freeman-EH)

HC is not "broken French" or a French dialect. It is an independent creole language with its own grammar, phonology, and orthographic system (AKA-100K, K96: a language has three independent systems: sound, lexicon, grammar/syntax). Even though ~80% of HC vocabulary is French-derived, those words were transformed through HC's own phonological system and do not retain French pronunciation or spelling rules (AKA-100K, K82). Never use French spelling conventions when writing HC.

### 3. HC lacks adverbs; use structural equivalents

HC does not have a productive adverb category the way English does (Fedexy §18; Freeman-EH, introduction). Where English uses adverbs, HC typically uses "ak" + noun or "jan" + adjective/noun constructions:

- "carefully" → "ak atansyon"
- "quickly" → "vit" (adjective used adverbially), or "ak vitès"
- "honestly" → "ak onètete"

Note: some adverbs ending in -man/-mman do exist, especially those formed from adjectives ending in -an/-em: aparamman, dezyèmman (Nesifort, p. 6). The doubled "mm" signals this derivation.

### 4. Match register to context

HC does not have the formal/informal register split that French has (tu/vous). When translating formal English into HC, aim for clear, direct, professional HC prose. Do not try to make HC "sound formal" by inserting French-influenced syntax; this reads as stilted and artificial.

Be aware of code-switching (boukantay kòd) vs. interference (entèferans): conscious alternation between HC and French is common in educated Haitian speech, but unconscious mixing of French syntax into HC writing (the "sosyolèk ibrid") should be avoided in professional documents (AKA-100K, K80, K91-92).

### 5. Preserve communicative intent

When translating idioms, proverbs, or culturally loaded expressions, prioritize the communicative function over literal meaning. Use equivalent HC pwovèb when they exist. When no equivalent exists, translate the underlying meaning.

### 6. Direction matters

**English to HC**: Avoid French-influenced calques. Think in HC structure first, then find the words. Use the "fè + noun" pattern extensively (Freeman-EH): fè konnen (inform), fè wè (show), fè lajan (earn money), fè dodo (sleep), fè fas ak (face/confront), fè bak (reverse), fè atansyon (be careful).

**HC to English**: Preserve the directness and economy of HC expression. HC sentences are often shorter and more direct than English equivalents; do not pad the English with unnecessary qualifiers. If the HC uses vulgar register (extensively documented in Freeman-HE), flag it but translate faithfully.

### 7. Handle phrasal verbs and serial verb constructions

HC makes heavy use of verb + preposition/particle combinations that change meaning significantly (Freeman-HE). Key patterns:

- **rale** (pull): rale kò (drag oneself), rale sou (draw on), rale monte (pull up)
- **ranje** (arrange): ranje kò (get ready), ranje zafè (settle affairs), ranje ak (reconcile with)
- **rann** (render): rann kont (account for), rann sèvis (do a favor), rann vizit (visit)

Serial verb constructions (two+ verbs in sequence, no conjunction) are core HC grammar (Fedexy §21):
- "Li kouri ale" (He ran away: kouri + ale)
- "Li pran liv la bay mwen" (He took the book and gave it to me: pran + bay)

## Alphabet and Orthography

### The HC Alphabet (32 Graphemes)

The AKA-standard alphabet has 24 letters that form 32 graphemes (AKA-2R, Dispozisyon 1; AKA-1R). A grapheme is a letter or combination of letters representing a single sound; the concept is more precise than "letter" (AKA-2R).

**Oral vowels (7):** a, e, è, i, o, ò, ou
**Nasal vowels (4):** an, en, on, oun
**Oral consonants (14):** b, ch, d, f, g, h, j, k, l, p, r, s, t, v, z
**Nasal consonants (3):** m, n, ng
**Semi-vowels / semi-consonants (3):** u (IPA: /ɥ/), w, y

The nasal vowel "oun" /ũ/ comes from African substrate languages and persists especially in Vodou vocabulary: oungan, ounsi, ounfò, oundjènikon, mazounbèl. It is distinct from the oral vowel "ou" /u/ (AKA-100K, K86).

The 2023 resolution clarified that "u" is a semi-vowel representing /ɥ/, a semi-vowel that glides into the following vowel (AKA-2R).

The grapheme "h" has phonological value in HC: the difference between "en en" and "enhen" changes meaning. It is also a component of the digraph "ch" (AKA-100K, K85).

### Key Orthographic Rules

**Rule 1: Strictly phonemic.** One sound = one grapheme. No silent letters. Everything written is pronounced; everything pronounced is written (Bernard; AKA-1R; AKA-2R). The system is "grafo-fonetik": it maps sounds to graphemes, not etymologies to spellings (AKA-100K, K96).

**Rule 2: No apostrophe, no hyphen in word formation.** The AKA standard eliminated both from standard orthography (AKA-1R, Dispozisyon 3). The hyphen is reserved for specific uses defined in AKA-2R, Dispozisyon 17: scientific prefixes (mono-klowo-fliyo-metàn), avoiding adjacent identical vowels (re-antre, ko-editè), nationality compounds (Ayisyen-Dominiken), proper name compounds (Jan-Pyè), dialogue markers, negative numbers (-3), date separators (23-01-2022), numeric ranges (20 - 30 km), and phone numbers (4999-0100).

Note: Some practical guides still present apostrophe usage as standard (e.g., Nesifort 2025 uses m'ap, l'ap). The AKA's position is that spaces replace apostrophes: M ap, L ap (AKA-1R, Dispozisyon 3).

**Rule 3: Short forms of pronouns.** When "mwen, ou, li, nou, yo" appear as clitic short forms (m, w, l, n, y), they are written as separate words with a space, not attached to adjacent words (AKA-1R, Dispozisyon 2).

Examples: "M ap vini." "N ap dòmi." "Y ap travay di." "Se rad pa m." "Al pran liv pa w."

**Rule 4: The grave accent (aksan grav).** The HC orthographic system uses one official accent: the grave accent. It serves two functions (AKA-1R, Dispozisyon 7.1; AKA-100K, K88):
- (i) Distinguishing two vowel pairs: e /e/ vs. è /ɛ/; o /o/ vs. ò /ɔ/
- (ii) Preventing confusion between the sequence "a" + "n" (two separate graphemes) and the digraph "an" (one nasal vowel grapheme). Example: "Pan mi an tonbe" (an = article) vs. "an pàn" (an = nasal vowel)

Accents are always written on uppercase letters: KREYÒL, not KREYOL (AKA-1R).

There is an active proposal to formalize a second accent (aksan egi/acute accent) on "e" and "o" before "n" to resolve remaining ambiguity between nasal vowel digraphs and oral vowel + consonant sequences (Thelusma). This is not yet AKA-official.

**Rule 5: "r" vs "w" before rounded vowels.** Before round vowels (o, ò, on, ou) at word-initial position, use "w": wobè, wobo, wòch, wòwòt, wont, wout (AKA-1R, Dispozisyon 6). "r" and "w" are distinct phonemes; they do not freely interchange in all positions.

**Rule 6: Country and place names.** Write country/region names using HC spelling: Etazini, Brezil, Japon, Meksik, Kanada (AKA-1R, Dispozisyon 5). Before some names, "o" + initial letter may agglutinate: Okap, Okay, Ozanglè, Ozetazini, Okanada (AKA-2R, Dispozisyon 7).

**Rule 7: Proper nouns.** Write as they appear in legal/administrative documents. For pronunciation, the Creole phonetic spelling can be placed in parentheses: Paul Magloire (Pol Maglwa) (AKA-1R, Dispozisyon 4).

**Rule 8: Double consonants.** Generally no doubled consonants except "mm" and "nn." "mm" appears in adverbs derived from -an/-em adjectives (aparamman, dezyèmman). "nn" appears after nasal vowels a, e, o at word boundaries (anndan, bannann). The letter "n" never doubles after "i" or "u" (Nesifort, pp. 5-6).

### Word Boundaries: Two Analytical Frameworks

This is the most contested area in HC orthography. Two rigorous but sometimes conflicting frameworks exist.

#### Framework 1: AKA Agglutination Theory (AKA-2R, Dispozisyon 2-5)

The AKA's approach centers on semantic fusion: when morphemes have developed such a close phonological and semantic relationship that they function as a single unit, write them as one word.

**Fixed expressions (Dispozisyon 2):** Foreign-origin phrases that entered HC as blocks → one word. Examples: sètadi, ladouskivyen, dekilakyèl, dekiprevyen, alawonnbadè.

**Non-separable segments (Dispozisyon 3):** Combinations where a component cannot stand alone in HC → one word. Examples: pidetwal, alamòd, aladriv, alatèt, alaverite, mizanplas, mizannèv, dodomeya.

**Modifier insertion test (Dispozisyon 4):** If inserting a modifier inside the expression makes the sentence ungrammatical or changes the meaning, the expression is one word.
- "li gentan vini" → inserting "ase" ("li gen ase tan vini") changes meaning from "already came" to "has enough time to come" → **gentan** is one word
- Similarly: **gendwa**, **genlè**

**Modifier split test (Dispozisyon 5):** If a modifier can be inserted and the phrase retains grammaticality without meaning loss, write as separate words.
- "li gen dwa fè grèv li" → "li gen tout dwa fè grèv li" (still means "has the right") → **gen dwa** is two words

#### Framework 2: Zefi's Commutation Test (Zefi)

Lemèt Zefi proposes a complementary test grounded in structural linguistics. The commutation test asks: can each element in the expression be independently substituted with another element in the same syntactic position, and does each element exist independently in other contexts?

If **yes to both** → separate words. If **no** → one word.

Zefi's analysis produces:
- **pou ki sa** (three words, not *poukisa*): each element is independently substitutable and exists in other contexts
- **ki jan** (two words, not *kijan*): "ki" → replaceable; "jan" → replaceable by sa, moun, kote
- **kon sa** (two words, not *konsa*): "kon" can take other complements; "sa" is replaceable
- **annou** (one word): you cannot insert anything between "an" and "nou"; commutation fails
- **kòmsadwa** (one word): constituent parts cannot pass the commutation test

Zefi notes inconsistencies within the AKA's own founding law: Article 34 writes "kijan" (fused) while Article 32 writes "ki jan" (separated). He argues that formal linguistic criteria should take precedence over institutional decree when they conflict.

#### Where the Two Frameworks Agree

| Expression | Both say: | Meaning |
|---|---|---|
| gentan | ONE word | already/by now |
| gendwa | ONE word | probably/might |
| genlè | ONE word | apparently/seems |
| annou | ONE word | let's (imperative) |
| sètadi | ONE word | that is to say |
| andeyò | ONE word | outside |
| lekòl | ONE word | school |
| gen dwa | TWO words | have the right |
| gen tan | TWO words | have time |

#### Where They Disagree

| AKA says: | Zefi says: | The debate |
|---|---|---|
| kijan (one word) | ki jan (two words) | AKA modifier test says fused; Zefi shows both "ki" and "jan" are independently substitutable |
| konsa (one word) | kon sa (two words) | Same pattern |
| poukisa (one word) | pou ki sa (three words) | All three elements are independently substitutable |

#### The "ontijan" / "on ti jan" Question

This specific expression is not explicitly addressed in either the AKA resolutions or Zefi's paper. Applying each test:

**AKA modifier insertion test (AKA-2R, Dispozisyon 4):** Inserting a modifier breaks the idiomatic meaning. "*on gwo ti jan" does not mean "a little bit." This supports writing **ontijan** as one word.

**Zefi commutation test (Zefi):** Each morpheme is independently substitutable: "on" → yon/de/twa; "ti" → gwo/bèl; "jan" → kote/moman. This supports writing **on ti jan** as three words.

**Recommendation:** Both positions are linguistically defensible. For AKA-compliant formal documents, **ontijan** (one word) is the safer choice, since the AKA is the official standard-setting body and its Dispozisyon 4 framework supports it. In practice, **on ti jan** (three words) is widespread and also linguistically defensible (Zefi). When the user asks, present both frameworks and let them decide. Do not assert one answer as definitively correct.

### The Particle "an" (AKA-2R, Dispozisyon 6)

"An" as a preposition is always separated: An bwa. An asye. An brik. An Ayiti. An Iran.

When "an" has agglutinated into a single lexeme, write together: Anwo. Anba. Anlè. Annalan. Annarivan. Anchantan.

Zefi adds that the [n] heard in "ann Ayiti" is a phonological phenomenon (the nasal vowel [ã] becomes [ãn] before a following vowel), not evidence of a liaison consonant (Zefi).

### Numbers (AKA-2R, Dispozisyon 9-14)

- 0-19: single words (zewo, en/youn, de, twa, kat, senk, sis, sèt, uit, nèf, dis, onz, douz, trèz, katòz, kenz, sèz, disèt, dizuit, diznèf)
- 20-99: separate the component elements (venteyen, karanteyen, swasanteyen, senkann sis, swasann dis, katreven dis, katreven disèt)
- 100+: separate words (mil kat san swasant kenz; douz milyon kat san sèt mil nèf)
- Ordinals: -yèm suffix (2yèm/dezyèm, 99yèm/katreven diznèvyèm); also -yèmman variant
- Year-age compounds: dezan, twazan, katran, senkan (Freeman-EH)

### Age and Time (AKA-2R, Dispozisyon 15-16)

- Age: "an", "ane", "lane", "zan" (Frè m nan genyen 55 ane / 55 lane / 55 an. Also: 2 zan, 23 an / ane / lane / zan)
- Time: "è" or "zè" (Li 5 è / li senk è. Li 2 zè, 3 zè, 6 zè, 10 zè. But: 4 è, 5 è / li kat è, li senk è)

## Grammar Reference

For detailed grammar explanations beyond what is in this file, read `references/grammar.md`.

### TMA (Tense-Mood-Aspect) Markers

HC verbs are invariant (no conjugation). All tense, mood, and aspect information is carried by pre-verbal particles. Fedexy treats TMA markers as their own morphosyntactic category, distinct from verbs and auxiliaries (Fedexy §19).

| Marker | Function | Example | English |
|---|---|---|---|
| (none) | Present habitual / general truth | Li manje | He eats |
| te | Simple past | Li te manje | He ate |
| ap | Progressive | Li ap manje | He is eating |
| pral | Near future | Li pral manje | He is going to eat |
| ta | Conditional | Li ta manje | He would eat |
| t ap | Past progressive | Li t ap manje | He was eating |
| t a | Past conditional | Li t a manje | He would have eaten |

In the Southern dialect (Fond-des-Blancs / Sud), "pe" sometimes replaces "ap" as the progressive marker. Both are correct; "ap" is the AKA standard.

### Definite Articles (Post-nominal)

HC definite articles come AFTER the noun. The form depends on the final sound of the **word immediately preceding the article** (not necessarily the noun itself; if an adjective or complement intervenes, its final sound governs the form) (Lefebvre; Fedexy §15).

| Form | After... | Example |
|---|---|---|
| la | oral consonant (preceded by oral vowel) | tab la, bab la, kok la |
| a | oral vowel | papa a, kay a, lari a |
| an | nasal vowel | ban an, pen an, bonbon an |
| lan | oral consonant (preceded by nasal vowel) | tanp lan, tenb lan |
| nan | nasal consonant | pom nan, kizin nan, fanm nan |

Definite plural: "yo" (invariable) after the noun phrase: "timoun yo" (the children).

A noun takes the definite article only when the referent is "specified" through: (a) previous mention in discourse, (b) situational presence, or (c) shared cultural/experiential knowledge (Lefebvre).

#### The Sentential "la" (Clause-level Definiteness)

"La" (and allomorphs a, an) can mark entire clauses to signal that the proposition is presupposed/shared knowledge between speaker and hearer (Lefebvre):
- "Zan te vini a" = Jean came (confirming what you already knew)
- "Zan te vini" = Jean came (new information)

This pragmatic function is important for natural-sounding translation. If an English source presents information as already known, the HC translation should include the clause-final article.

### Possessives (Fedexy §15)

- Simple: kay mwen / kay m, kay ou / kay w, kay li / kay l, kay nou / kay n, kay yo
- Reinforced: kay pa m, kay pa w, kay pa l, kay pa n, kay pa yo
- Independent: "se pa mwen" (it's mine), "pa ou a" (yours)

### Negation

"Pa" after subject, before TMA markers: Li pa manje. Li pa t manje. Li pa pral manje.

### Questions

1. Intonation only: Li manje?
2. Eske (explicit): Eske li manje?
3. Wh-words fronted: Ki sa li manje? / Ki kote li ye? / Kilè li pral vini?

### Copula System (Fedexy §22)

- "se" for identification/equation: "Li se doktè"
- "ye" for wh-questions: "Ki sa li ye?"
- Zero copula for adjective predication: "Li malad"
- Obligatory, optional, and impossible copula contexts are distinct grammatical categories

## Discourse Markers and Conversational Expressions

These high-frequency expressions appear constantly in real HC communication but are absent from most textbooks and dictionaries. Recognizing and using them is critical for natural-sounding output. Corpus source: 2,551 ADF Haiti staff WhatsApp messages (Fond-des-Blancs, 2026).

| Expression | Meaning/Function | Notes |
|---|---|---|
| tet chaje | stressed, overwhelmed (lit: head loaded) | Very common; used across all social classes |
| mezanmi | exclamation of surprise or concern (lit: my friends) | All registers; can open a sentence or stand alone |
| monche | familiar address ("man", "bro", "dude") | Informal; signals camaraderie, not formality |
| bon nouvel | "good news" | Often standalone as a reaction to positive information |
| sa k pase? | "what's up?" / "what happened?" | Informal greeting or genuine inquiry depending on context |
| anhok | acknowledgment with mild surprise ("ah, okay") | Informal; signals new information absorbed |
| pwoblem wi | "no problem" / affirmative agreement | "wi" adds emphasis; different from "pa gen pwoblem" |

Additional corpus-attested patterns:

- **m kontan sa** = "glad to hear it" (standalone reaction)
- **m panse sa tou** = "I think so too" (agreement)
- **bagay sa pa senp** = "this isn't simple" / "this is serious" (reaction to complex news)
- **oke, sa bon** = "okay, that works" (informal agreement/closure)
- **prezan** = "present" / "I'm here" (roll call response in group chats)
- **sdv / sDv** = "si Dye vle" (God willing); standard hedge after scheduling commitments

For annotated real-world translation examples from the same corpus, see `references/real-world-examples.md`.

## Common Translation Pitfalls

### False Friends from French

| HC word | HC meaning | Not the same as French... |
|---|---|---|
| nèg | man/person/guy (neutral) | nègre (historically derogatory) |
| blan | foreigner (any race) | blanc (white) |
| manje | food (n.) / to eat (v.) | manger (verb only) |
| kounye a | now | (no direct French equivalent) |

### Structural Traps

1. **No grammatical gender.** "Li" = he/she/it. HC does not have masculine/feminine as a systematic grammatical category (AKA-100K, K84; Fedexy §14).
2. **No verb conjugation.** "Mwen manje, ou manje, li manje" : all identical verb form.
3. **Post-nominal articles.** "The book" = "liv la" (not "la liv") (Fedexy §15).
4. **No progressive/perfect distinction.** "I am eating" and "I have been eating" both → "m ap manje." Use adverbs (depi, gentan, deja) for precision.
5. **Preposition mismatches.** "At the house" = "lakay" or "nan kay la." "To the market" = "nan mache a."
6. **Double possessive trap.** "My mother's house" = "kay manman m" (not "kay manman mwen an").
7. **Sentential article trap.** Do not omit clause-final "la/a/an" when translating presupposed information into HC (Lefebvre).
8. **Agglutinated French articles.** Many common HC words absorbed their French articles during creolization: dlo (< de l'eau), lajan (< l'argent), lopital (< l'hôpital), lafanmi (< la famille). Speakers treat these as single indivisible morphemes (Fedexy §15). Do not try to separate the absorbed article from the root.

### English Concepts Without Single HC Equivalents

Abstract terms require natural descriptive phrases:
- "sustainability" → "kapasite pou kenbe aktivite a sou pye" or "dirab"
- "stakeholder" → "moun ki konsène yo" or "pati ki gen enterè"
- "accountability" → "rann kont" or "responsablite pou rann kont"
- "due diligence" → "verifikasyon ak rechèch ki nesesè"

### Register and Tone for Professional Documents

- Direct active constructions: "ADF ap fè..." not "Li prevwa ke..."
- Avoid long subordinate clauses; restructure into shorter HC sentences
- HC conjunctions: epi (and/then), men (but), paske (because), pou (for/to), si (if)
- HC has four logical operators: AK, EPI, OSWA, OSNON (AKA-100K, K35)
- Use HC terms for roles and titles: direktè, kontab, sipèvizè, anketè

### Decreolization Awareness

Five categories of decreolization in HC syntax to watch for (AKA-100K, K99, from Chery 2023): word order changes, passive voice adoption, preposition simplification, subjectless verbs, indirect transitive replacing direct transitive. Example: "Naje pou sòti" (standard) vs. "Naje pou nou sòti" (decreolized). Prefer the standard HC construction.

## Culturally Rich Vocabulary Domains

Freeman's dictionaries reveal particularly deep and nuanced HC vocabulary in several cultural domains (Freeman-EH; Freeman-HE). When translating content touching these areas, use precise HC terms rather than generic equivalents:

- **Coffee culture**: 40+ compound forms of "kafe"
- **Food and agriculture**: 9-page glossary in Freeman-EH
- **Vodou and spiritual life**: Specialized terminology (oungan, ounsi, ounfò); technical terms, not exoticisms
- **Kinship and social relationships**: Nuanced terms for family, community, social bonds
- **Weather and environment**: Rich rain/storm vocabulary
- **Livestock (especially goats)**: Extensive cultural expressions around "kabrit"

## Dialectal Awareness

For ADF work in Fond-des-Blancs (Sud Department):

| Feature | Standard (PaP) | Southern (Sud) | Corpus evidence (2,551 msgs) |
|---|---|---|---|
| Progressive marker | ap | pe (sometimes) | "pe" not attested in this corpus; all speakers used "ap" exclusively in writing |
| "with" | avèk / ak | ak | "ak" universal; "avèk" appeared only in formal/quoted contexts |
| Vowel quality | baseline | more open vowels | Not observable in written data |
| Plural DET stacking | timoun yo | timoun nan yo (sometimes) (Fedexy §15) | Not attested in this corpus |
| Regional head forms | tèt ou | tèt a w (some areas) | Not attested in this corpus |
| Truncated forms | pwobabman | probab / pwobab | "probab" attested 2x; truncation of adverbs common in fast messaging |

**Corpus note**: The absence of "pe" in 2,551 written messages from Fond-des-Blancs speakers suggests that even in the Sud, the AKA-standard "ap" dominates in written/typed communication. "Pe" may be primarily an oral feature that speakers self-correct when writing. Do not insert "pe" into written HC targeting Southern audiences unless specifically replicating oral speech.

Use AKA standard for written documents and forms. Recognize Southern variants in field data without "correcting" them. All regional varieties are valid (AKA-100K, K31, K55, K101).

## Translation Workflow

1. **Read the full source text first** before translating.
2. **Identify domain vocabulary.** Check reference glossaries for technical terms.
3. **Draft in the target language's structure** : do not map word-by-word from source.
4. **Review for naturalness.** Would a fluent HC speaker actually say this? Would a fluent English speaker write it this way?
5. **Check orthography** against AKA rules: word boundaries, accents, article forms.
6. **Verify consistency.** Same English term → same HC term throughout a document.
7. **Check for Gallicisms.** Replace French-influenced terms with idiomatic HC alternatives (Freeman-EH).
8. **Check clause-final articles.** Ensure sentential "la/a/an" is present where the context presupposes shared knowledge (Lefebvre).

## Reference Files

### Skill References (always available)

- `references/grammar.md`: Detailed HC grammar (sentence structure, verb system, articles, subordination, proverbs)
- `references/real-world-examples.md`: Annotated HC/English translation pairs from WhatsApp corpus, organized by message type (scheduling, coordination, status reports, reactions, directives)

### External References (user's HC folder, if accessible)

Check for the user's Haitian Creole reference folder (often on a shared drive or local directory). Contents to look for:

- **Best Dictionaries/**: Freeman-EH v2.4; Freeman-HE 6th ed 2010. Read for vocabulary lookups.
- **Alternative Dictionaries/**: CFPB glossary; KreyolPale phrasebook. Consult for specialized vocabulary.
- **_Sort/**: AKA-1R and AKA-2R PDFs. Primary orthographic authorities.
- **English to French Dictionaries/**: Collins Robert; Langenscheidt. Useful for tracing HC etymology through French.

When uncertain about a specific word or construction, read the relevant dictionary pages before committing to a translation.
