---
name: "written-assignment"
description: "Draft university written assignments (essays, reports, reflection papers, case studies) in the user's simple B1 English voice with APA 7 citations. Use whenever the user asks to write, draft, plan, review, check, or improve any graded academic writing that is not a discussion forum post, including \"written assignment,\" \"essay,\" \"report,\" \"term paper,\" when they paste a rubric and assignment question, or when they paste their own draft and ask for feedback."
---

# University Written Assignment

Help the user with a university written assignment (essay/report style, not a discussion forum post). The output must sound like the user, follow the rubric, use APA 7 citations, and show real critical thinking.

There are two modes:
- **Mode A (Draft)**: write the assignment from the user's inputs.
- **Mode B (Review)**: the user pastes their own draft; check it and suggest improvements.

If the user pastes a draft and asks to check, review, grade, or improve it, use Mode B. If unclear, ask.

## Resource check first (hard gate, both modes)

Run this check before anything else, in both modes: before the rubric, the plan, a draft, or a review. The user wants every assignment to rest only on course material you have really read. An assignment built on a reading you could not open ends up with guessed claims and citations, and the marker checks them against the course material. So if even one course resource cannot be opened and read, tell the user and stop. A request to write directly skips the plan, not this check.

**What to check.** Every course resource the user gives or points to for this task:
- the topic knowledge: pasted readings, lecture notes, and slides;
- every file the user uploads or points to, of any type (PDF, Word, PowerPoint, image, and others), including a rubric, instructions, or a draft sent as a file;
- every link: readings, web pages, and videos;
- every reading or video that the assignment question or the instructions name for this task, even if the user did not supply it;
- in Mode B, every course reading that the draft cites.

A source is course material when the assignment question, the instructions, the topic knowledge, or the user name it as course material. Other sources are outside sources, and they are not part of this gate. A web page you find yourself follows "Outside information": if it will not open, use another page or cut the claim. An outside source that the user's draft cites is checked and flagged in the Mode B review, as usual.

**How to check.** Open each resource yourself and check all of it, not only the first page. Never mark a resource readable without opening it. Knowing the book, or seeing a search snippet, does not count.
- **Pasted text** passes when it is the reading itself, not only a title, author name, or reference entry. It fails if it is cut off, for example if it stops in the middle of a sentence or before the pages the task names.
- **A file** passes when it opens and every page or slide gives clear, normal text. If its content is shown in the chat, read it there. If only its path is listed, open it with your tools. If a page gives little or no text, it may be a scanned image, so look at the page as an image. If you still cannot read it, the file fails. For a long file, check that every page gives text (a short script can count the text on each page), then read closely the pages the task uses. A file also fails if it is empty, damaged, or locked with a password, or if the user mentions it but did not attach it.
- **A link** passes when web fetch returns the full reading. It fails on an error, an empty page, a login page (for example, the course site), a paywall or "subscribe to read" message, an "ask for access" page, only an abstract or a preview, text that stops before the part the task needs, or content that is not the named reading. It also fails if web fetch is not available in this chat or will not open the link.
- **A video or audio file** passes only with a full transcript that is pasted, uploaded, or opens as text. You cannot watch or listen, and the title and description of a video are not the video.
- **An image or screenshot** passes when all its text is sharp, complete, and not cut off at the edges.

Missing page numbers alone do not fail a resource. The citation rules handle them.

**If any resource fails, stop.** Check every resource first. Then report all the problems in one message, so the user can fix everything in one round:
1. The line **Resource check failed. I have not started [the plan / the draft / the review].**
2. A table with every resource, readable or not: Resource (short name and type) | Readable | Problem | What I need. Each failed resource gets the exact problem and one clear fix: paste the text with page numbers, upload the file, paste the transcript, or send a link that opens without a login.
3. Any other required input that is missing, such as the rubric, the assignment question, or the word count.
4. The closing line: "Send these, or tell me to leave a resource out, and I will check again before I start."

Example table:

| Resource | Readable | Problem | What I need |
|---|---|---|---|
| Textbook, Ch. 5 (PDF) | Yes | | |
| Unit 5 lecture video (link) | No | I cannot watch videos, and there is no transcript. | Paste the transcript. |
| Article on TCP, pp. 45-60 (link) | No | The link opens a login page. | Upload the PDF or paste pp. 45-60. |

End the reply there. Do not add a rubric analysis, a plan, an outline, or a partial draft, even from the resources that passed. Do not search for another copy or edition of a failed resource. Do not fill the gap from memory, general knowledge, a search snippet, or an abstract. This gate overrides the user's general preference for direct execution over questions.

**When the user replies,** check the new or fixed resources the same way. Start the task only when every resource passes. If the user says to leave a resource out, drop it from the list. Run the check again whenever the user adds or replaces a resource later in the chat.

**If every resource passes,** start your first reply for the task with one line, then continue with the task in the same reply:
`Resource check: all [N] course resources open and readable ([short names]).`

## Mode A workflow (follow in order)

1. **Check resources, then inputs.** Run the resource check first (see "Resource check first"). If any resource fails, report it and stop there. Then read everything the user provided. If any critical input is missing, empty, or unclear (rubric, assignment question, word count, or sources), ask before writing. Do not guess anything, including what a reading says. If the user has not pasted the task content at all, point them to `assets/input-template.md` so they can fill it in.
2. **Parse the rubric for the top band.** Before planning, read the rubric closely (see "Aim for the highest rubric level" below). Identify, for each criterion, what the highest level demands and how it differs from the level below it. Those differences are the drafting targets.
3. **Split the question.** Break the assignment question into every part, including the small ones at the end ("…and why?", "…give an example," "…how does this apply in your field?"). Number them. Each part needs its own clear answer, in the order the question asks. Top marks are often lost to a missed part, not to weak thinking.
4. **Plan.** Once inputs are complete, give a short plan (3 to 6 bullets): the structure, the thesis, and, for each section, which rubric criterion it covers, **which top-band descriptor it will satisfy**, and which numbered question parts it answers. If the work needs a personal example and "My context" has none that fits, add at least 3 story ideas to the plan (see Personal examples). Wait for the user's confirmation before drafting. Skip this gate only if the user says to write directly.
5. **Draft.** After confirmation, write the two files in "Mode A deliverables": the assignment document and the review file.
6. **Self-grade before delivering.** Score the draft against the rubric yourself, criterion by criterion. If any criterion lands below the top level, revise the draft first, then deliver. Never deliver a draft you would grade below the top band without telling the user why (for example, a missing source the user must supply).

**Before drafting, always read `references/voice-sample.md`.** It holds the user's real writing. Mirror its sentence length, rhythm, formality, and hedging words.

## Language rules (strict: apply to every sentence)

The user writes at CEFR B1 level. This is the most important constraint. The draft must read like the user wrote it, so plain language always wins.

- **Vocabulary: B1 or below.** Use common, everyday words. Prefer *show, use, help, important, problem, idea, also, but, because, however*. Avoid AI-sounding or "elevated" words such as *delve, navigate, leverage, underscore, tapestry, multifaceted, paradigm, intricate, crucial, pivotal, foster*. If a B2+ word is a real technical term from the course, keep it.
- **Simple sentences.** Most sentences are one clause. Use some two-clause sentences joined by *and, but, because, so, when, if*. Avoid sentences with many commas, semicolons, or nested clauses.
- **Sentence length: 12 to 20 words on average.** Vary a little. Never write a sentence over 30 words.
- **One idea per sentence. One topic per paragraph.**
- **Active voice** almost everywhere. Use passive only when the actor does not matter.
- **Academic but plain tone.** No slang. No contractions ("do not", not "don't"). No rhetorical questions unless the assignment asks for them.
- **No filler phrases** such as "It is important to note that," "In today's society," or "Since the dawn of time."
- **Hedge uncertain claims** with "may," "suggests," or "one possible reason."

## Dashes and exact copying

**No dashes in new text.** Do not use an em dash (—) or an en dash (–) anywhere in new text. Do not use dashes inside sentences at all, including a hyphen with spaces around it ( - ). Split the sentence, or use a comma, colon, or brackets. Write ranges in sentences with words ("from 2021 to 2023", "12 to 18 words"). In citations and References, write page ranges with a hyphen (pp. 12-18). Hyphens inside words (well-known, two-way) are fine. The user's voice samples contain no dashes at all, so a dash does not sound like them.

**Copy exactly.** Text copied from a source or from the user keeps every character as it is: quotes, titles, names, URLs, DOIs, code, commands, software output, and the user's own sentences. Never turn a hyphen (-) into – or —, and never "clean up" any other character. A changed character breaks things: a quote can no longer be found with Ctrl+F; a URL, DOI, or piece of code stops working; and the user's text is changed without asking.

**Dash check before delivering.** Search the whole output for – and —. Each one must come from copied text that has it in the original. Rewrite or fix any other.

## APA 7 citation rules

- In-text citations: `(Author, Year)` or `Author (Year)`, plus the location when the source has one: `(Author, Year, p. 12)`. Inside sentences use "and"; inside parentheses use "&".
- **Name the author, not a pronoun.** Never refer to the author of a cited source with a pronoun ("he," "his," "him," "she," "her," or "they" for one author). Repeat the surname ("Dordal explains," "Dordal adds") or name the work ("the book explains," "the book's example," "the video shows"). This keeps the focus on the source and avoids guessing the author's gender.
- **Page numbers.** Add a page number to every citation when the source has one, for paraphrases too, not only quotes. If the source has no page numbers, use a paragraph number (`para. 4`), a section name, or a timestamp for videos. Never guess a page number. If it is missing, write the citation without it and add `[CHECK CITATION]` to the [EVIDENCE] block.
- **Web page dates.** For a source at a URL, use only the date parts that the page itself shows the reader, such as the byline or a "Published" or "Last updated" line. A full date shown gives (2024, March 5). A month and year give (2024, March). A year alone gives (2024). No date shown gives (n.d.) in References and (Author, n.d.) in the text. Never take a date from the page metadata (meta tags, structured data), the search result, the URL, or memory. The user cannot see those dates on the page, so they cannot check them, and neither can the marker. If the page shows a "last updated" date for the content, use it. Ignore a "last reviewed" date and the copyright year in the footer, because APA 7 does not treat them as publish dates. If the day and month order is unclear (05/03/2024), use the year only and add `[CHECK CITATION]` to the [EVIDENCE] block.
- **Direct quotes** in the text need quotation marks and a page number. Keep them short (under 40 words) and rare. Paraphrase when possible. This rule is about the assignment text. Quotes in [EVIDENCE] blocks are notes for the user and follow "Evidence blocks".
- **Paraphrase check.** Paraphrase in new words. Compare each cited sentence with the source text, and rewrite any sentence that keeps the source's wording or sentence pattern.
- **Cite what the user read.** If an original author's idea appears only through the textbook, use a secondary citation, such as `(Goleman, 1995, as cited in [Textbook Author], [Year])`, and list only the textbook in References.
- End with a **References** section: alphabetical by author surname, with a hanging indent. In a Word file, set the hanging indent. In a Markdown file, do not write a note about it in the assignment document; put the reminder in "Before you submit" in the review file. Sentence case for article and book titles; title case for journal names.
- Every reference must appear in-text, and every in-text citation must appear in the reference list.
- **Never invent sources, authors, years, page numbers, or DOIs.** Use the sources the user provides; outside sources, general knowledge included, follow "Source and evidence rules" below. If publication details are missing, flag them with `[CHECK CITATION]` in the [EVIDENCE] block. If a claim needs a source the user has not given, find an open web source (see "Outside information"). Flag it `[SOURCE NEEDED]` in the [EVIDENCE] block only when no open page supports it.

## Source and evidence rules

These rules decide what the draft may claim and where each claim comes from.

**Course material first.** Use this order: the question's wording, this unit's readings, other course readings, outside sources.

**The course version wins.** For definitions, terms, models, and formulas, use the course version. If another source says something different, name the difference in the text. Never contradict the readings silently, because graders check claims against the course material.

**General knowledge needs a source.** Never write a fact from memory, even when it seems widely known. Any factual claim that does not come from the course materials is outside information: background facts, definitions, numbers, dates, and study findings. It follows "Outside information" below and gets an in-text citation and a References entry. Key definitions still come from the course. The user's own experience and opinions are not outside information. Label them `[MY EXPERIENCE]` or `[MY OPINION]` in the [EVIDENCE] block, not in the text.

**Outside information.** Use it only when the question asks for it or it adds something the readings do not. Do not use it at all if the assignment or rubric allows only course materials. When you use it, find the source yourself with these steps. Do not stop to ask first.
1. **Search.** Find a page with web search. Prefer credible open pages: official documentation, standards bodies, government and university sites, and open-access journals.
2. **Open the full page** with web fetch. A search snippet is not enough.
3. **Check that it is open.** The user must be able to read the full page for free. Do not use a page that fails to load, needs a login, needs payment or a subscription, or shows only an abstract or a preview. Do not use private pages, such as course forums, shared drives, or intranets. Treat words like "subscribe to read," "members only," or "sign in to continue" in the fetched text as a paywall. If the user cannot open the page, they cannot check the claim, and neither can the marker.
4. **Write only what the page says.** Base each sentence on the fetched text. Do not add facts from memory, even true ones. If the page does not support the sentence, change the sentence or find another page.
5. **Cite what you opened.** Use the exact URL you opened. Take the author, title, and date from what the page shows (see "Web page dates").

If no open page supports a claim, cut the claim or stay within the course materials. Mark it `[SOURCE NEEDED]` in the [EVIDENCE] block only if the answer cannot work without it. If web search or web fetch is not available, do not use outside information, and tell the user why. Mark each outside source `[VERIFY]` in its first [EVIDENCE] entry until the user has opened it. Web sources get [EVIDENCE] entries like any other source.

**Recency (computer science).** For outside computer science sources on fast-changing topics, prefer the last 1 to 3 years and stay within 5 years. Foundational topics (for example algorithms, OOP principles, protocol standards, digital logic) may use older classic sources. Course readings are exempt, and a recency rule in the rubric overrides this one. Judge recency only by the date the page shows. A page with no date cannot show that it is recent, so prefer pages that show one.

**Numbers.** Never do statistics or arithmetic in your head. Use the user's own software output, or run the calculation with code. Show the inputs in the [EVIDENCE] block, and mark anything unverified there with `[CHECK NUMBER]`.

## Evidence blocks (Mode A)

Under each paragraph of a draft, add an `[EVIDENCE]` block so the user can check every claim. For each sentence, or group of sentences with one idea, give the source, the location (page number, or paragraph, section, table, slide, or timestamp), and a direct quote: the exact words in the source that support it. The user checks a claim by finding the quote in the source with Ctrl+F. A location alone, such as "opening paragraph" or "SMALLINT and INT rows", makes the user read the whole part and guess which words support the sentence. So every source in every entry gets a quote.

**What to quote.** Find the smallest part of the source that supports the sentence. Then:
- **A sentence, or part of one:** quote the words that carry the claim, usually one sentence or less.
- **A longer part** (a paragraph, a section, a list, a slide, or a stretch of a transcript): quote its first words and its last words with ` ... ` between them, about 5 to 8 words at each end. The user then sees exactly where the part starts and where it ends. If the part is short enough to quote whole, quote it whole.
- **A table:** name the table and the row, and quote the row: its first cell ` ... ` the cell with the fact the sentence uses. Quote every row the sentence uses.
- **A figure or image:** quote its caption or the words on it.

**Quote rules.**
- Every source in an entry gets its own location and quote. When one entry names two sources, both get a quote.
- Copy each quoted part exactly (see "Copy exactly"), so Ctrl+F finds it. The ` ... ` is the only new text inside the quotation marks.
- Quotes come only from text the user pasted or uploaded (such as course material) or the full text you fetched from a link. Never quote a search snippet or from memory.
- If you cannot find words in the source that support the sentence, the sentence has no support. Change it to say what the source says, find a source that says it, or cut it. Never deliver an entry with a location and no quote, except under the web page limit below.
- **Web page limit.** Text you fetch from a link (an outside web page, or a course reading given only as a link) falls under the copyright rules for web content: you may quote each page only once in the whole reply, in under 15 words. This skill cannot change that. A ` ... ` quote counts as that one quote, so keep both ends short. Put the quote on the entry where the page matters most. If the assignment text itself quotes the page, that is its one quote. Every other entry for the page gets the URL, an exact location (the heading the page shows plus the paragraph number under it, or the table name and row), and the tag `no quote (web page limit)`. "Before you submit" lists these entries. If the user also pasted or uploaded the same reading, quote from that copy instead: short quotes from text the user supplied are fine.
- Web sources also get the URL. The first entry for a web source also gives the date exactly as the page shows it, such as `date on page: "Updated March 5, 2024"`, or `date on page: none` for (n.d.). The user can then find it on the page with Ctrl+F.
- Label sentences with no source as `[MY EXPERIENCE]`, `[MY OPINION]`, or `[INVENTED - NEED TO VERIFY]`. They need no quote. Do not use a `[GENERAL KNOWLEDGE]` label. A general fact needs a web source (see "Outside information"), or `[SOURCE NEEDED]` if no open page supports it.

Format (S1, S2… are the sentence numbers inside that paragraph):

```
[EVIDENCE]
- S1-S2 (main idea in a few words): Author (Year), p. 12, "exact words that support the claim"
- S3 (main idea): Author (Year), p. 14, para. 2, "first 5 to 8 words of the paragraph ... last 5 to 8 words of the paragraph"
- S4 (main idea): Author A (Year), p. 7, "exact words"; Author B (Year), p. 20, Table 3, INT row, "INT ... the cell with the fact used"
- S5 (main idea): Author (Year), Heading Name section, para. 1, URL, "one quote from this page, under 15 words", date on page: "March 5, 2024" [VERIFY]
- S6 (main idea): Author (Year), Heading Name section, para. 4, URL, no quote (web page limit)
- S7 (main idea): Author (Year), Section Name, "exact words" [CHECK CITATION: no page number in the pasted text]
- S8: [MY EXPERIENCE]
- S9: [MY OPINION]
- After S9: [ADD YOUR EXAMPLE: a time your team had to choose between two tools]
```

**Keep the text clean.** The user deletes the [EVIDENCE] blocks and submits what is left. So everything outside the blocks must be text the user will submit, from the title to the References list.
- No tag, flag, or note to the user ever goes in the text. Each one goes in the [EVIDENCE] block under its paragraph, on the entry for the sentence it is about. This covers:
  - labels about where a sentence comes from: `[MY EXPERIENCE]`, `[MY OPINION]`, `[INVENTED - NEED TO VERIFY]`, `[VERIFY]`;
  - flags for a gap the user must fix before submitting: `[CHECK CITATION]`, `[SOURCE NEEDED]`, `[CHECK NUMBER]`, `[ADD YOUR EXAMPLE]`. After a colon, each flag says in a few words what to fix, such as `[CHECK CITATION: no page number in the pasted text]`.
- No gap marks in the text either, such as "p. ?" or "XX". When a page number is missing, the citation is (Author, Year), and the flag goes in the [EVIDENCE] block.
- A flag about a References entry, such as a missing date or publisher, goes on the first [EVIDENCE] entry that cites that source.
- An `[ADD YOUR EXAMPLE]` entry says where the example goes, such as "After S3". Write the paragraph so it still reads well before the user adds the example.
- Start each block with the line `[EVIDENCE]`, leave a blank line before and after it, and put only its entries inside. The user can then delete each block in one step.
- "Before you submit" lists every flag with where it is, so none is missed.

Deliver one version only: the assignment document with its [EVIDENCE] blocks. Do not add a clean copy. Word counts and language checks cover the text only, without the [EVIDENCE] blocks.

## Before you submit (end of the review file)

End the review file with this list, so nothing unchecked reaches the submission. For each flag and story, say where it is (for example, paragraph 3, S2) so the user can find it fast:
- the references the user must open. For each web source (`[VERIFY]`), check that the page opens for free, says what the sentence claims, and shows the date used;
- each evidence entry tagged `no quote (web page limit)`: open the page, find the part by its location, and check it. To get quotes for these entries, the user can paste the page text or upload the page as a PDF and ask for the evidence again;
- each `[INVENTED - NEED TO VERIFY]` story: keep it only if it matches what really happened, with the details fixed; otherwise replace it or cut it;
- every open flag in the [EVIDENCE] blocks, with what to fix: `[SOURCE NEEDED]`, `[CHECK NUMBER]`, `[CHECK CITATION]`, `[ADD YOUR EXAMPLE]`. Under each `[ADD YOUR EXAMPLE]`, give the story ideas for it (see "Personal examples");
- for a Markdown assignment document, a reminder to set a hanging indent on the References entries;
- the last step: delete every [EVIDENCE] block. When the items above are done, what is left is ready to submit.

## Personal examples (do not invent silently)

Use real examples from "My context" first. Never invent an example and present it as the user's without telling them. If the work needs a personal or work example and "My context" has none that fits:
1. In the plan (Mode A workflow, step 4), suggest at least 3 story ideas based on the user's profile and memory. Give each in a line or two: the situation, and the main idea it would show. The user can answer with a real example, "idea X happened" plus the real details, or "invent."
2. If the user skipped the plan, add `[ADD YOUR EXAMPLE: what kind of example fits here]` to the [EVIDENCE] block of the paragraph where the example fits, with where it goes (for example, "After S3"), not to the text. Give the story ideas in the review file under "Before you submit", not in the assignment document.

If the user says invent, or chooses invent for an idea, write the story in first person as the user's experience. Draw on their profile and memory; if neither is available, use their background (software team leader at a SaaS company building a dealership management system). Mark it `[INVENTED - NEED TO VERIFY]`. Do not ask again. Write it.

Use the hypothetical style ("Imagine a team that…") only when the user asks for it.

In the [EVIDENCE] block, label invented sentences `[INVENTED - NEED TO VERIFY]` (never in the text), and list the story under "Before you submit" in the review file.

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
3. **Map descriptors to sections.** Every top-band descriptor must have a clear "home" in the draft: a paragraph or passage where the marker can see it met. If a descriptor has no home, add or strengthen a section.
4. **Translate descriptors into B1 moves.** Top-band verbs still get plain language:
   - "Critically evaluate / analyze" → compare at least two ideas or sources, state strengths **and** limits of each, then give a reasoned position ("Theory A explains X well, but it does not cover Y. Theory B covers Y, so...").
   - "Synthesize" → connect two or more sources in one paragraph to support a single point, not one source per paragraph in isolation.
   - "Apply / relate to practice" → link the concept to a concrete, specific example (from "My context", or chosen through "Personal examples"), with the outcome or lesson stated.
   - "Insight / originality" → go one step past the sources: a limit the sources do not mention, a condition where the claim fails, or an implication for practice.
   - "Coherent argument" → thesis in the introduction, topic sentence per paragraph that links back to the thesis, and linking words between paragraphs.
   - "Accurate referencing" → zero APA 7 format errors and full two-way match between citations and references.
5. **Self-grade honestly.** After drafting, assign each criterion the level the draft actually earns and say why in one line, in the review file's Rubric check. Fix anything below the top level before delivering. If the top level cannot be reached with the inputs given (for example the rubric asks for 6+ sources and the user gave 3), say so plainly and tell the user exactly what to add. Do not invent material to close the gap.
6. **No rubric provided?** Ask for it once. If the user says there is none, use the "What makes a strong assignment" list above as the rubric and target its strongest form.

Top-band quality must never break the language rules: depth comes from ideas, structure, and evidence, not from complex vocabulary or long sentences.

## Mode A deliverables: two separate files (after the plan is confirmed)

Deliver two separate files, never one. The assignment document holds only what the user will submit, plus the [EVIDENCE] blocks. Every other part goes in the review file. The test: once any open flag is fixed, the user deletes every [EVIDENCE] block and the assignment document is ready to submit.

Use Markdown unless the user asks for another format, such as Word. Name the two files so they pair up, for example `CS2204-Unit3-assignment.md` and `CS2204-Unit3-review.md`.

**File 1: the assignment document**
- The title and headings the assignment needs, the full text with APA 7 in-text citations, and the References list, all exactly as they will be submitted.
- An [EVIDENCE] block under each paragraph (see "Evidence blocks"). Every tag and note sits in these blocks, none in the text. One version only, with no clean copy.
- Nothing else: no plan, notes, comments to the user, word count, rubric table, or "Draft" label, and no text before the submission starts or after the References list.

**File 2: the review file**, with these sections in this order:
1. **Rubric check**: for each rubric criterion, the section that covers it, the level the draft earns, and a one-line reason. Every criterion should show the top level. If one does not, explain the gap and what the user must add.
2. **Question parts**: each numbered part of the question (workflow step 3) and where the draft answers it.
3. **Word count and citations**: the word count of the text only (without [EVIDENCE] blocks) against the target, and a check that citations and references match both ways.
4. **Language check** on the text only: flag any word above B1 with a simpler replacement, flag any sentence over 25 words, and confirm the dash check (see "Dashes and exact copying").
5. **Why I made these choices** (about 100 to 150 words): the structure, which sources were used where, and any assumptions made.
6. **Understanding check**: three short questions a classmate or the instructor could ask about this work. The user should be able to answer them without looking.
7. **Before you submit**: the list described in "Before you submit".

In the chat reply, present both files and keep the message short. In one or two sentences, name only what the user must act on first, such as an open flag or a criterion below the top band. Do not repeat the review file in chat. If files cannot be created, give the two parts as two clearly separated blocks, headed "Assignment document" and "Review file".

## Mode B: Review the user's own draft

The user pastes their draft (and, ideally, the rubric, assignment question, and word count). The goal is to improve the draft, not replace it. **Do not rewrite the whole draft unless the user asks.** Keep the user's original wording wherever it works. Make targeted edits only.

### Mode B workflow
1. Run the resource check (see "Resource check first"). If any resource fails, report it and stop there.
2. Read `references/voice-sample.md` so suggested wording stays in the user's voice and at B1 level.
3. If the rubric or assignment question is missing, ask for them once. If the user says to review without them, check structure, language, and APA 7 only, and say the rubric check was skipped.
4. Review the draft against every check below.

### What to check
- **Question coverage**: does the draft answer every part of the assignment question? Name any part that is missing or thin.
- **Rubric**: map each criterion to where the draft meets it. Flag weak or missing criteria first; these matter most for the grade.
- **Structure**: clear thesis in the introduction, one main idea per body paragraph with a topic sentence, conclusion with no new information, signposting between sections.
- **Argument**: claims supported by evidence and citations; critical thinking shown, not only summary; critiques specific, not generic; no claims that contradict the readings without saying so; hedging on uncertain claims.
- **Language**: flag any word above B1 with a simpler replacement, any sentence over 25 words, passive voice where active is better, contractions, filler phrases, and any en dash, em dash, or hyphen used as a dash. Also flag AI-sounding words if any appear.
- **APA 7 and sources**: in-text format, page numbers where the source has them, "as cited in" for ideas met only through the textbook, reference list order and case, and that citations and references match both ways. Check that each source supports the sentence it is attached to, not only that the format is right. Flag sentences that copy the source's wording too closely. Flag suspicious details with `[CHECK CITATION]`; never "fix" a citation by inventing details. For web sources, open each URL, or say that you could not. Flag a page that does not load, needs a login, or needs payment, a claim the page does not make, and a date the page does not show (see "Web page dates"). Also flag facts from outside the course materials that have no source, and any pronoun used for a cited author (suggest the surname or the work instead).
- **Word count**: count the draft and compare to the target (±10%).

### Mode B deliverables
1. **Verdict** in 2 or 3 sentences: is the draft ready to submit, close, or needs work, and the single biggest risk to the grade.
2. **Priority fixes**: the issues to fix first, ordered by grade impact. For each: the problem, where it is, and a concrete suggested fix in the user's B1 voice.
3. **Line edits**: specific before → after suggestions for weak sentences. Small and targeted. Do not restyle sentences that are already fine. The "after" sentence is clean text the user can paste in, so put any flag, such as `[CHECK CITATION]`, in a note beside it, never in the sentence.
4. **Checks summary**: short results for rubric coverage, question coverage, language, APA 7 and sources, and word count.
5. Offer to apply the fixes and produce a corrected version, but only after the user agrees with the suggestions. Deliver it with the same split as Mode A: the corrected text alone in the assignment document, and a short list of what changed in a separate review file. Any open flag goes in that review file with where it is, never in the corrected text.

## Always avoid

AI-sounding phrases ("delve into," "navigate the complexities," "tapestry"), bullet-point lists where prose is expected, restating the question back as filler, starting any work before every course resource passes the resource check, stereotypes or non-inclusive language, copied strings of words from sources, inventing sources or details, evidence entries with a location but no quote (outside the web page limit), outside facts written from memory, web sources that are paid, private, or will not open, web dates the page does not show, generic critiques that fit any theory, specific numbers or findings with no source, pronouns such as "he" or "she" for a cited author, tags or notes in the assignment text, and dashes in new text.