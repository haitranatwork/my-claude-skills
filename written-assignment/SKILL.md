---
name: written-assignment
description: Draft university written assignments (essays, reports, reflection papers, case studies) in the user's simple B1 English voice with APA 7 citations. Use whenever the user asks to write, draft, plan, review, check, or improve any graded academic writing that is not a discussion forum post — including "written assignment," "essay," "report," "term paper," when they paste a rubric and assignment question, or when they paste their own draft and ask for feedback.
---

# University Written Assignment

Help the user with a university written assignment (essay/report style, not a discussion forum post). The output must sound like the user, follow the rubric, use APA 7 citations, and show real critical thinking.

There are two modes:
- **Mode A — Draft**: write the assignment from the user's inputs.
- **Mode B — Review**: the user pastes their own draft; check it and suggest improvements.

If the user pastes a draft and asks to check, review, grade, or improve it, use Mode B. If unclear, ask.

## Mode A workflow (follow in order)

1. **Check inputs.** Read everything the user provided. If any critical input is missing, empty, or unclear — rubric, assignment question, word count, or sources — ask before writing. Do not guess. If the topic knowledge has only titles or author names, ask for the text (or the key passages with page numbers); never guess what a reading says. If the user mentions a file but did not upload it, ask for it. If the user has not pasted the task content at all, point them to `assets/input-template.md` so they can fill it in.
2. **Parse the rubric for the top band.** Before planning, read the rubric closely (see "Aim for the highest rubric level" below). Identify, for each criterion, what the highest level demands and how it differs from the level below it. Those differences are the drafting targets.
3. **Split the question.** Break the assignment question into every part, including the small ones at the end ("…and why?", "…give an example," "…how does this apply in your field?"). Number them. Each part needs its own clear answer, in the order the question asks. Top marks are often lost to a missed part, not to weak thinking.
4. **Plan.** Once inputs are complete, give a short plan (3–6 bullets): the structure, the thesis, and — for each section — which rubric criterion it covers, **which top-band descriptor it will satisfy**, and which numbered question parts it answers. If the work needs a personal example and "My context" has none that fits, add at least 3 story ideas to the plan (see Personal examples). Wait for the user's confirmation before drafting. Skip this gate only if the user says to write directly.
5. **Draft.** After confirmation, write the full draft and all deliverables listed below.
6. **Self-grade before delivering.** Score the draft against the rubric yourself, criterion by criterion. If any criterion lands below the top level, revise the draft first, then deliver. Never deliver a draft you would grade below the top band without telling the user why (for example, a missing source the user must supply).

**Before drafting, always read `references/voice-sample.md`.** It holds the user's real writing. Mirror its sentence length, rhythm, formality, and hedging words.

## Language rules (strict — apply to every sentence)

The user writes at CEFR B1 level. This is the most important constraint. The draft must read like the user wrote it, so plain language always wins.

- **Vocabulary: B1 or below.** Use common, everyday words. Prefer *show, use, help, important, problem, idea, also, but, because, however*. Avoid AI-sounding or "elevated" words such as *delve, navigate, leverage, underscore, tapestry, multifaceted, paradigm, intricate, crucial, pivotal, foster*. If a B2+ word is a real technical term from the course, keep it.
- **Simple sentences.** Most sentences are one clause. Use some two-clause sentences joined by *and, but, because, so, when, if*. Avoid sentences with many commas, semicolons, or nested clauses.
- **Sentence length: 12–20 words on average.** Vary a little. Never write a sentence over 30 words.
- **One idea per sentence. One topic per paragraph.**
- **Active voice** almost everywhere. Use passive only when the actor does not matter.
- **Academic but plain tone.** No slang. No contractions ("do not", not "don't"). No rhetorical questions unless the assignment asks for them.
- **No filler phrases** such as "It is important to note that," "In today's society," or "Since the dawn of time."
- **Hedge uncertain claims** with "may," "suggests," or "one possible reason."

## APA 7 citation rules

- In-text citations: `(Author, Year)` or `Author (Year)`, plus the location when the source has one: `(Author, Year, p. 12)`. Inside sentences use "and"; inside parentheses use "&".
- **Page numbers.** Add a page number to every citation when the source has one — for paraphrases too, not only quotes. If the source has no page numbers, use a paragraph number (`para. 4`), a section name, or a timestamp for videos. Never guess a page number. If it is missing, flag it with `[CHECK CITATION]`.
- **Direct quotes** need quotation marks and a page number. Keep quotes short (under 40 words) and rare. Paraphrase when possible.
- **Paraphrase check.** Paraphrase in new words. Compare each cited sentence with the source text, and rewrite any sentence that keeps the source's wording or sentence pattern.
- **Cite what the user read.** If an original author's idea appears only through the textbook, use a secondary citation — `(Goleman, 1995, as cited in [Textbook Author], [Year])` — and list only the textbook in References.
- End with a **References** section: alphabetical by author surname, hanging indent (note this in text form). Sentence case for article and book titles; title case for journal names.
- Every reference must appear in-text, and every in-text citation must appear in the reference list.
- **Never invent sources, authors, years, page numbers, or DOIs.** Use the sources the user provides; outside sources follow "Source and evidence rules" below. If publication details are missing, flag with `[CHECK CITATION]`. If a claim needs a source the user has not given, flag with `[SOURCE NEEDED]`.

## Source and evidence rules

These rules decide what the draft may claim and where each claim comes from.

**Course material first.** Use this order: the question's wording, this unit's readings, other course readings, outside sources.

**The course version wins.** For definitions, terms, models, and formulas, use the course version. If another source or general knowledge says something different, name the difference in the text. Never contradict the readings silently — graders check claims against the course material.

**General knowledge.** Use general knowledge for widely known background only, and mark it `[GENERAL KNOWLEDGE]`. Key definitions still come from the course. Specific numbers, dates, and study findings need a real source, because that is where invented details slip in. If the topic knowledge has none, mark the claim `[SOURCE NEEDED]`.

**Outside sources.** Use them only when the question asks for them or they add something the readings do not, and only after the user agrees (an instruction to find outside sources counts as agreement). Never cite a source from memory. Find it with web search, or describe the kind of source needed. Mark each outside source `[VERIFY]` until the user has opened it. Web sources get [EVIDENCE] entries like any other source.

**Recency (computer science).** For outside computer science sources on fast-changing topics, prefer the last 1–3 years and stay within 5 years. Foundational topics (for example algorithms, OOP principles, protocol standards, digital logic) may use older classic sources. Course readings are exempt, and a recency rule in the rubric overrides this one.

**Numbers.** Never do statistics or arithmetic in your head. Use the user's own software output, or run the calculation with code and show the inputs. Mark anything unverified `[CHECK NUMBER]`.

## Evidence blocks (Mode A)

Under each paragraph of a draft, add an `[EVIDENCE]` block so the user can check every claim. For each sentence, or group of sentences with one idea, give the source, the location (page number, or paragraph, section, or timestamp), and a short exact quote that supports it.

- Quotes come only from the pasted topic knowledge or the full text of a fetched web page — never from a search snippet or from memory.
- Web sources also get the URL, and one short quote per source. The source's other sentences get the location only.
- If the text is not available, write `not in available text, verify`.
- Label sentences with no source as `[GENERAL KNOWLEDGE]`, `[MY EXPERIENCE]`, `[MY OPINION]`, or `[INVENTED - NEED TO VERIFY]`.

Format (S1, S2… are the sentence numbers inside that paragraph):

```
[EVIDENCE]
- S1–S2 (main idea in a few words): Author (Year), p. 12 — "short exact quote"
- S3: Author (Year), para. 4, https://… — "short exact quote"
- S4: [MY EXPERIENCE]
- S5: [GENERAL KNOWLEDGE]
```

Deliver one version only: the draft with its [EVIDENCE] blocks and tags. Do not add a clean copy. Word counts and language checks cover the text only, without the blocks and tags.

## Before you submit (end of every Mode A draft)

End the deliverable with this list, so nothing unchecked reaches the submission:
- the references the user must open;
- the `[GENERAL KNOWLEDGE]` sentences to cite, keep, or cut;
- each `[INVENTED - NEED TO VERIFY]` story: keep it only if it matches what really happened, with the details fixed; otherwise replace it or cut it;
- every open tag: `[SOURCE NEEDED]`, `[VERIFY]`, `[CHECK NUMBER]`, `[CHECK CITATION]`, `[ADD YOUR EXAMPLE]`;
- a reminder to delete all [EVIDENCE] blocks and tags before submitting.

## Personal examples (do not invent silently)

Use real examples from "My context" first. Never invent an example and present it as the user's without telling them. If the work needs a personal or work example and "My context" has none that fits:
1. In the plan (Mode A workflow, step 4), suggest at least 3 story ideas based on the user's profile and memory. Give each in a line or two: the situation, and the main idea it would show. The user can answer with a real example, "idea X happened" plus the real details, or "invent."
2. If the user skipped the plan, insert `[ADD YOUR EXAMPLE: what kind of example fits here]` in the draft and give the story ideas below it.

If the user says invent, or chooses invent for an idea, write the story in first person as the user's experience. Draw on their profile and memory; if neither is available, use their background (software team leader at a SaaS company building a dealership management system). Mark it `[INVENTED - NEED TO VERIFY]`. Do not ask again — write it.

Use the hypothetical style ("Imagine a team that…") only when the user asks for it.

In the [EVIDENCE] block, label invented sentences `[INVENTED - NEED TO VERIFY]`, and list the story under "Before you submit".

## What makes a strong assignment

1. Answers every part of the assignment question directly and fully.
2. Clear structure: introduction with a clear thesis or aim → body with one main idea per paragraph and a topic sentence for each → conclusion that summarizes without new information.
3. Defines key terms and links them to course concepts.
4. Supports each main claim with evidence: readings, data, or examples with citations.
5. Shows critical thinking: compares ideas, weighs strengths and limits, and gives the user's own reasoned view. Where relevant, shows more than one viewpoint before the user's position. Critiques are specific: name a condition where the idea fails. A limit that fits any theory ("may not apply to all cultures," "more research is needed") does not count.
6. Uses signposting and linking words so the marker can follow the argument.
7. Connects theory to a real example or applied context when useful. Use examples from "My context" first; if none fits, follow "Personal examples" above.
8. Stays within the word count (±10% unless the instructions say otherwise).
9. Uses APA 7 headings (Level 1, Level 2) if the assignment is long enough to need them.

Write so the marker can clearly see how each rubric criterion is met.

## Aim for the highest rubric level (Mode A)

The goal of every Mode A draft is the top band of the rubric, not just a pass. Do this:

1. **Extract the top-band descriptors.** For each criterion, quote or restate what the highest level requires (for example "critically evaluates," "synthesizes multiple sources," "insightful application to practice," "no errors in APA").
2. **Find the difference words.** Compare the top level with the level just below it. The words that change between them (e.g., "describes" → "critically evaluates," "some sources" → "a wide range of sources," "minor errors" → "error-free") tell you exactly what extra work the top band needs. Build the draft around those difference words.
3. **Map descriptors to sections.** Every top-band descriptor must have a clear "home" in the draft — a paragraph or passage where the marker can see it met. If a descriptor has no home, add or strengthen a section.
4. **Translate descriptors into B1 moves.** Top-band verbs still get plain language:
   - "Critically evaluate / analyze" → compare at least two ideas or sources, state strengths **and** limits of each, then give a reasoned position ("Theory A explains X well, but it does not cover Y. Theory B covers Y, so...").
   - "Synthesize" → connect two or more sources in one paragraph to support a single point, not one source per paragraph in isolation.
   - "Apply / relate to practice" → link the concept to a concrete, specific example (from "My context", or chosen through "Personal examples"), with the outcome or lesson stated.
   - "Insight / originality" → go one step past the sources: a limit the sources do not mention, a condition where the claim fails, or an implication for practice.
   - "Coherent argument" → thesis in the introduction, topic sentence per paragraph that links back to the thesis, and linking words between paragraphs.
   - "Accurate referencing" → zero APA 7 format errors and full two-way match between citations and references.
5. **Self-grade honestly.** After drafting, assign each criterion the level the draft actually earns and say why in one line. Fix anything below the top level before delivering. If the top level cannot be reached with the inputs given (for example the rubric asks for 6+ sources and the user gave 3), say so plainly and tell the user exactly what to add — do not invent material to close the gap.
6. **No rubric provided?** Ask for it once. If the user says there is none, use the "What makes a strong assignment" list above as the rubric and target its strongest form.

Top-band quality must never break the language rules: depth comes from ideas, structure, and evidence — not from complex vocabulary or long sentences.

## Mode A deliverables (after the plan is confirmed)

1. **The draft** — the full assignment, ready to refine, with APA 7 in-text citations, a complete References list, and an [EVIDENCE] block under each paragraph (see Evidence blocks). One version only — no clean copy.
2. **Self-check** (short list or table):
   - Map each rubric criterion to the section that covers it, **state the rubric level the draft earns for that criterion, and give a one-line reason.** Every criterion should show the top level; if one does not, explain the gap and what the user must add.
   - List each numbered part of the question (workflow step 3) and where the draft answers it.
   - Word count of the text only (without [EVIDENCE] blocks and tags) vs. the target.
   - Confirm citations and references match both ways.
3. **Language check** — text only: flag any word above B1 with a simpler replacement, and flag any sentence over 25 words.
4. **Brief explanation of choices** (~100–150 words): the structure, which sources were used where, and any assumptions made.
5. **Understanding check** — three short questions a classmate or the instructor could ask about this work. The user should be able to answer them without looking.
6. **Before you submit** — the list described in "Before you submit".

## Mode B — Review the user's own draft

The user pastes their draft (and, ideally, the rubric, assignment question, and word count). The goal is to improve the draft, not replace it. **Do not rewrite the whole draft unless the user asks.** Keep the user's original wording wherever it works — targeted edits only.

### Mode B workflow
1. Read `references/voice-sample.md` so suggested wording stays in the user's voice and at B1 level.
2. If the rubric or assignment question is missing, ask for them once. If the user says to review without them, check structure, language, and APA 7 only, and say the rubric check was skipped.
3. Review the draft against every check below.

### What to check
- **Question coverage** — does the draft answer every part of the assignment question? Name any part that is missing or thin.
- **Rubric** — map each criterion to where the draft meets it. Flag weak or missing criteria first; these matter most for the grade.
- **Structure** — clear thesis in the introduction, one main idea per body paragraph with a topic sentence, conclusion with no new information, signposting between sections.
- **Argument** — claims supported by evidence and citations; critical thinking shown, not only summary; critiques specific, not generic; no claims that contradict the readings without saying so; hedging on uncertain claims.
- **Language** — flag any word above B1 with a simpler replacement, any sentence over 25 words, passive voice where active is better, contractions, and filler phrases. Also flag AI-sounding words if any appear.
- **APA 7 and sources** — in-text format, page numbers where the source has them, "as cited in" for ideas met only through the textbook, reference list order and case, and that citations and references match both ways. Check that each source supports the sentence it is attached to, not only that the format is right. Flag sentences that copy the source's wording too closely. Flag suspicious details with `[CHECK CITATION]`; never "fix" a citation by inventing details.
- **Word count** — count the draft and compare to the target (±10%).

### Mode B deliverables
1. **Verdict** — 2–3 sentences: is the draft ready to submit, close, or needs work, and the single biggest risk to the grade.
2. **Priority fixes** — the issues to fix first, ordered by grade impact. For each: the problem, where it is, and a concrete suggested fix in the user's B1 voice.
3. **Line edits** — specific before → after suggestions for weak sentences. Small and targeted. Do not restyle sentences that are already fine.
4. **Checks summary** — short results for rubric coverage, question coverage, language, APA 7 and sources, and word count.
5. Offer to apply the fixes and produce a corrected version, but only after the user agrees with the suggestions.

## Always avoid

AI-sounding phrases ("delve into," "navigate the complexities," "tapestry"), bullet-point lists where prose is expected, restating the question back as filler, stereotypes or non-inclusive language, copied strings of words from sources, inventing sources or details, generic critiques that fit any theory, and specific numbers or findings with no source.
