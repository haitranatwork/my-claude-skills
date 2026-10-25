---
name: "forum-post"
description: "Draft or review university discussion forum posts in the user's simple B1 English voice with APA 7 citations. Use for any discussion post, forum post, initial post, classmate reply, or when the user pastes their own draft post and asks to review, check, or improve it before submitting."
---

# University Discussion Forum Post

Produce a complete, ready-to-edit draft of a university discussion forum post, or review the user's own draft before submission. The output must sound like the user, follow the rubric, use APA 7 citations, and show real critical thinking, not a generic summary.

There are three modes:
- **Mode A (Initial post)**: answer the discussion question at the top band of the rubric.
- **Mode B (Replies)**: respond to one or more classmate posts.
- **Mode C (Review)**: review a draft the user wrote (or edited) before they submit it.

The user will say which mode they want. If they don't, ask. Do not guess.

## Resource check first (hard gate, all modes)

Run this check before anything else, in every mode: before the rubric, a plan, a draft, or a review. The user wants every post to rest only on course material you have really read. A post built on a reading you could not open ends up with guessed claims and citations, and the grader checks them against the course material. So if even one course resource cannot be opened and read, tell the user and stop.

**What to check.** Every course resource the user gives or points to for this task:
- the topic knowledge: pasted readings, lecture notes, and slides;
- every file the user uploads or points to, of any type (PDF, Word, PowerPoint, image, and others), including a rubric, instructions, classmate posts, or a draft sent as a file;
- every link: readings, web pages, and videos;
- every reading or video that the discussion question or the instructions name for this task, even if the user did not supply it;
- in Mode C, every course reading that the draft cites.

A source is course material when the question, the instructions, the topic knowledge, or the user name it as course material. Other sources are outside sources, and they are not part of this gate. A web page you find yourself follows "Outside information": if it will not open, use another page or cut the claim. An outside source that the user's draft cites is checked and flagged in the Mode C review, as usual.

**How to check.** Open each resource yourself and check all of it, not only the first page. Never mark a resource readable without opening it. Knowing the book, or seeing a search snippet, does not count.
- **Pasted text** passes when it is the reading itself, not only a title, author name, or reference entry. It fails if it is cut off, for example if it stops in the middle of a sentence or before the pages the task names.
- **A file** passes when it opens and every page or slide gives clear, normal text. If its content is shown in the chat, read it there. If only its path is listed, open it with your tools. If a page gives little or no text, it may be a scanned image, so look at the page as an image. If you still cannot read it, the file fails. For a long file, check that every page gives text (a short script can count the text on each page), then read closely the pages the task uses. A file also fails if it is empty, damaged, or locked with a password, or if the user mentions it but did not attach it.
- **A link** passes when web fetch returns the full reading. It fails on an error, an empty page, a login page (for example, the course site), a paywall or "subscribe to read" message, an "ask for access" page, only an abstract or a preview, text that stops before the part the task needs, or content that is not the named reading. It also fails if web fetch is not available in this chat or will not open the link.
- **A video or audio file** passes only with a full transcript that is pasted, uploaded, or opens as text. You cannot watch or listen, and the title and description of a video are not the video.
- **An image or screenshot** passes when all its text is sharp, complete, and not cut off at the edges.

Missing page numbers alone do not fail a resource. The citation rules handle them.

**If any resource fails, stop.** Check every resource first. Then report all the problems in one message, so the user can fix everything in one round:
1. The line **Resource check failed. I have not started [the post / the replies / the review].**
2. A table with every resource, readable or not: Resource (short name and type) | Readable | Problem | What I need. Each failed resource gets the exact problem and one clear fix: paste the text with page numbers, upload the file, paste the transcript, or send a link that opens without a login.
3. Any other required input that is missing (see "Intake rules").
4. The closing line: "Send these, or tell me to leave a resource out, and I will check again before I start."

Example table:

| Resource | Readable | Problem | What I need |
|---|---|---|---|
| Textbook, Ch. 5 (PDF) | Yes | | |
| Unit 5 lecture video (link) | No | I cannot watch videos, and there is no transcript. | Paste the transcript. |
| Article on TCP, pp. 45-60 (link) | No | The link opens a login page. | Upload the PDF or paste pp. 45-60. |

End the reply there. Do not add a rubric analysis, a plan, an outline, or a partial draft, even from the resources that passed. Do not search for another copy or edition of a failed resource. Do not fill the gap from memory, general knowledge, a search snippet, or an abstract. This gate overrides every "proceed directly" rule in this skill and the user's general preference for a finished result over questions.

**When the user replies,** check the new or fixed resources the same way. Start the task only when every resource passes. If the user says to leave a resource out, drop it from the list. Run the check again whenever the user adds or replaces a resource later in the chat.

**If every resource passes,** start your first reply for the task with one line, then do the task in the same reply:
`Resource check: all [N] course resources open and readable ([short names]).`

## How the user provides the task

The user supplies the variable parts each time, usually as a filled-in copy of `assets/input-template.md`. Expect some or all of:
- a quick-fill header (mode, word count target, replies needed, minimum citations, discipline)
- the rubric
- the assignment instructions (word count, number of replies, deadline, formatting rules)
- topic knowledge / course material: this unit's readings first, pasted as text with page numbers, not just titles (concepts, authors, definitions, data, quotes)
- the exact discussion question
- for Mode B: the full classmate post(s), labeled Classmate 1, Classmate 2, etc.
- for Mode C: the user's own draft
- optional sample posts (use only for depth and structure, never to copy voice or wording)
- optional: the user's real example (see Personal examples), and for Mode B the user's own initial post

If the user hasn't pasted this content, point them to `assets/input-template.md` so they can fill it in.

**Intake rules:**
- A file the user mentions but did not attach, topic knowledge with only titles or author names, and any resource you cannot open or read are handled by "Resource check first" above. Never guess what a reading says.
- If a required part is empty (quick-fill header, rubric, assignment instructions, topic knowledge, or discussion question), ask the user to update it.
- If the user says they will run a mode later, run the resource check, confirm that everything is ready, and wait. Do not execute any mode until they say which one to run.
- Check the output against the quick-fill header numbers. Report the actual word count of the post text only (without [EVIDENCE] blocks) in the deliverable.

**Before drafting, always read `references/voice-sample.md`.** It holds the user's real writing. Mirror its sentence length, rhythm, formality, hedging words, and how the user opens and closes posts.

Only ask a clarifying question if something critical is missing: no rubric, no discussion question, no classmate post in Mode B, no draft in Mode C, a resource that fails the resource check, or missing citation details. Otherwise proceed directly, because the user prefers a finished result over questions.

## Language rules (strict: apply to every sentence)

The user writes at CEFR B1 level. This is the most important constraint. The draft must read like the user wrote it, so plain language always wins.

- **Vocabulary: B1 or below.** Use common, everyday words. Prefer *show, use, help, important, problem, idea, also, but, because, however*. Avoid "elevated" synonyms and AI-sounding words such as *delve, navigate, leverage, underscore, tapestry, multifaceted, paradigm, intricate*. If a B2+ word is a real technical term from the course, keep it, but do not reach for fancy words.
- **Simple sentences.** Most sentences are one clause. Use some two-clause sentences joined by *and, but, because, so, when, if*. Avoid long sentences with many commas, semicolons, or nested clauses.
- **Sentence length 12 to 18 words on average.** Vary a little. Never write a sentence over 30 words.
- **One idea per sentence. One topic per paragraph.**
- **Active voice** almost everywhere. Use passive only when the actor does not matter.
- **No filler phrases** such as "It is important to note that," "In today's society," or "Since the dawn of time."

## Dashes and exact copying

**No dashes in new text.** Do not use an em dash (—) or an en dash (–) anywhere in new text. Do not use dashes inside sentences at all, including a hyphen with spaces around it ( - ). Split the sentence, or use a comma, colon, or brackets. Write ranges in sentences with words ("from 2021 to 2023", "12 to 18 words"). In citations and References, write page ranges with a hyphen (pp. 12-18). Hyphens inside words (well-known, two-way) are fine. The user's voice samples contain no dashes at all, so a dash does not sound like them.

**Copy exactly.** Text copied from a source or from the user keeps every character as it is: quotes, titles, names, URLs, DOIs, code, commands, software output, and the user's own sentences. Never turn a hyphen (-) into – or —, and never "clean up" any other character. A changed character breaks things: a quote can no longer be found with Ctrl+F; a URL, DOI, or piece of code stops working; and the user's text is changed without asking.

**Dash check before delivering.** Search the whole output for – and —. Each one must come from copied text that has it in the original. Rewrite or fix any other.

## APA 7 citation rules

- In-text citations in APA 7 format: `(Author, Year)` or `Author (Year)`, plus the location when the source has one: `(Author, Year, p. 12)`.
- **Name the author, not a pronoun.** Never refer to the author of a cited source with a pronoun ("he," "his," "him," "she," "her," or "they" for one author). Repeat the surname ("Dordal explains," "Dordal adds") or name the work ("the book explains," "the book's example," "the video shows"). This keeps the focus on the source and avoids guessing the author's gender.
- **Page numbers.** Add a page number to every citation when the source has one, for paraphrases too, not only quotes. If the source has no page numbers, use a paragraph number (`para. 4`), a section name, or a timestamp for videos. Never guess a page number. If it is missing, write the citation without it and add `[CHECK CITATION]` to the [EVIDENCE] block.
- **Web page dates.** For a source at a URL, use only the date parts that the page itself shows the reader, such as the byline or a "Published" or "Last updated" line. A full date shown gives (2024, March 5). A month and year give (2024, March). A year alone gives (2024). No date shown gives (n.d.) in References and (Author, n.d.) in the text. Never take a date from the page metadata (meta tags, structured data), the search result, the URL, or memory. The user cannot see those dates on the page, so they cannot check them, and neither can the grader. If the page shows a "last updated" date for the content, use it. Ignore a "last reviewed" date and the copyright year in the footer, because APA 7 does not treat them as publish dates. If the day and month order is unclear (05/03/2024), use the year only and add `[CHECK CITATION]` to the [EVIDENCE] block.
- **Direct quotes** in the post need quotation marks and a page number. Keep them short (under 40 words) and rare. Paraphrase when possible. This rule is about the post text. Quotes in [EVIDENCE] blocks are notes for the user and follow "Evidence blocks".
- **Paraphrase check.** Paraphrase in new words. Compare each cited sentence with the source text, and rewrite any sentence that keeps the source's wording or sentence pattern.
- **Cite what the user read.** If an original author's idea appears only through the textbook, use a secondary citation, such as `(Goleman, 1995, as cited in [Textbook Author], [Year])`, and list only the textbook in References.
- End the post with a **References** section in APA 7 format: hanging indent style, alphabetical by author surname.
- If a source is missing publication details, flag it with `[CHECK CITATION]` in the [EVIDENCE] block. Never invent author names, years, or page numbers.
- **Source whitelist.** Cite sources from the topic knowledge. Outside sources, general knowledge included, follow "Source and evidence rules" below. Never add them silently.

## Source and evidence rules

These rules decide what the draft may claim and where each claim comes from.

**Course material first.** Use this order: the question's wording, this unit's readings, other course readings, outside sources.

**The course version wins.** For definitions, terms, models, and formulas, use the course version. If another source says something different, name the difference in the text. Never contradict the readings silently, because graders check claims against the course material.

**General knowledge needs a source.** Never write a fact from memory, even when it seems widely known. Any factual claim that does not come from the course materials is outside information: background facts, definitions, numbers, dates, and study findings. It follows "Outside information" below and gets an in-text citation and a References entry. Key definitions still come from the course. The user's own experience and opinions are not outside information. Label them `[MY EXPERIENCE]` or `[MY OPINION]` in the [EVIDENCE] block, not in the text.

**Outside information.** Use it only when the question asks for it or it adds something the readings do not. Do not use it at all if the assignment or rubric allows only course materials. When you use it, find the source yourself with these steps. Do not stop to ask first.
1. **Search.** Find a page with web search. Prefer credible open pages: official documentation, standards bodies, government and university sites, and open-access journals.
2. **Open the full page** with web fetch. A search snippet is not enough.
3. **Check that it is open.** The user must be able to read the full page for free. Do not use a page that fails to load, needs a login, needs payment or a subscription, or shows only an abstract or a preview. Do not use private pages, such as course forums, shared drives, or intranets. Treat words like "subscribe to read," "members only," or "sign in to continue" in the fetched text as a paywall. If the user cannot open the page, they cannot check the claim, and neither can the grader.
4. **Write only what the page says.** Base each sentence on the fetched text. Do not add facts from memory, even true ones. If the page does not support the sentence, change the sentence or find another page.
5. **Cite what you opened.** Use the exact URL you opened. Take the author, title, and date from what the page shows (see "Web page dates").

If no open page supports a claim, cut the claim or stay within the course materials. Mark it `[SOURCE NEEDED]` in the [EVIDENCE] block only if the answer cannot work without it. If web search or web fetch is not available, do not use outside information, and tell the user why. Mark each outside source `[VERIFY]` in its first [EVIDENCE] entry until the user has opened it. Web sources get [EVIDENCE] entries like any other source.

**Recency (computer science).** For outside computer science sources on fast-changing topics, prefer the last 1 to 3 years and stay within 5 years. Foundational topics (for example algorithms, OOP principles, protocol standards, digital logic) may use older classic sources. Course readings are exempt, and a recency rule in the rubric overrides this one. Judge recency only by the date the page shows. A page with no date cannot show that it is recent, so prefer pages that show one.

**Numbers.** Never do statistics or arithmetic in your head. Use the user's own software output, or run the calculation with code. Show the inputs in the [EVIDENCE] block, and mark anything unverified there with `[CHECK NUMBER]`.

## Evidence blocks (Modes A and B)

Under each paragraph of a draft, add an `[EVIDENCE]` block so the user can check every claim. For each sentence, or group of sentences with one idea, give the source, the location (page number, or paragraph, section, table, slide, or timestamp), and a direct quote: the exact words in the source that support it. The user checks a claim by finding the quote in the source with Ctrl+F. A location alone, such as "opening paragraph" or "SMALLINT and INT rows", makes the user read the whole part and guess which words support the sentence. So every source in every entry gets a quote.

**What to quote.** Find the smallest part of the source that supports the sentence. Then:
- **A sentence, or part of one:** quote the words that carry the claim, usually one sentence or less.
- **A longer part** (a paragraph, a section, a list, a slide, or a stretch of a transcript): quote its first words and its last words with ` ... ` between them, about 5 to 8 words at each end. The user then sees exactly where the part starts and where it ends. If the part is short enough to quote whole, quote it whole.
- **A table:** name the table and the row, and quote the row: its first cell ` ... ` the cell with the fact the sentence uses. Quote every row the sentence uses.
- **A figure or image:** quote its caption or the words on it.

**Quote rules.**
- Every source in an entry gets its own location and quote. When one entry names two sources, both get a quote.
- Copy each quoted part exactly (see "Copy exactly"), so Ctrl+F finds it. The ` ... ` is the only new text inside the quotation marks.
- Quotes come only from text the user pasted or uploaded (course material and classmate posts) or the full text you fetched from a link. Never quote a search snippet or from memory.
- If you cannot find words in the source that support the sentence, the sentence has no support. Change it to say what the source says, find a source that says it, or cut it. Never deliver an entry with a location and no quote, except under the web page limit below.
- **Web page limit.** Text you fetch from a link (an outside web page, or a course reading given only as a link) falls under the copyright rules for web content: you may quote each page only once in the whole reply, in under 15 words. This skill cannot change that. A ` ... ` quote counts as that one quote, so keep both ends short. Put the quote on the entry where the page matters most. If the post text itself quotes the page, that is its one quote. Every other entry for the page gets the URL, an exact location (the heading the page shows plus the paragraph number under it, or the table name and row), and the tag `no quote (web page limit)`. "Before you submit" lists these entries. If the user also pasted or uploaded the same reading, quote from that copy instead: short quotes from text the user supplied are fine.
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

Deliver one version only: the draft with its [EVIDENCE] blocks. Do not add a clean copy. Word counts and language checks cover the text only, without the [EVIDENCE] blocks.

## Before you submit (end of every draft in Modes A and B)

End the deliverable with this list, so nothing unchecked reaches the submission. For each flag and story, say where it is (for example, paragraph 3, S2) so the user can find it fast:
- the references the user must open. For each web source, check that the page opens for free, says what the sentence claims, and shows the date used;
- each evidence entry tagged `no quote (web page limit)`: open the page, find the part by its location, and check it. To get quotes for these entries, the user can paste the page text or upload the page as a PDF and ask for the evidence again;
- each `[INVENTED - NEED TO VERIFY]` story: keep it only if it matches what really happened, with the details fixed; otherwise replace it or cut it;
- every open flag in the [EVIDENCE] blocks, with what to fix: `[SOURCE NEEDED]`, `[VERIFY]`, `[CHECK NUMBER]`, `[CHECK CITATION]`, `[ADD YOUR EXAMPLE]`;
- the last step: delete every [EVIDENCE] block. When the items above are done, what is left is ready to submit.

## Personal examples (do not invent silently)

The user's posts often use a real personal or work example. Never invent one and present it as the user's without telling them. If a personal example would strengthen the post and none was given:
1. Add `[ADD YOUR EXAMPLE: what kind of example fits here]` to the [EVIDENCE] block of the paragraph where the example fits, with where it goes (for example, "After S3"), not to the post text, and
2. Below the draft, suggest at least 3 story ideas based on the user's profile and memory. Give each in a line or two: the situation, and the main idea it would show. The user can answer with a real example, "idea X happened" plus the real details, or "invent."

If the user says invent, or chooses invent for an idea, write the story in first person as the user's experience. Draw on their profile and memory; if neither is available, use their background (software team leader at a SaaS company building a dealership management system). Mark it `[INVENTED - NEED TO VERIFY]`. Do not ask again. Write it.

Use the hypothetical style ("Imagine a team that…") only when the user asks for it.

In the [EVIDENCE] block, label invented sentences `[INVENTED - NEED TO VERIFY]` (never in the post text), and list the story under "Before you submit".

## What makes a strong post (all modes)

- **Take a clear position** in the first one or two sentences.
- **Name the course material specifically**: the concept, author, or study. Do not write "the readings showed."
- **Show critical thinking**: ask a question, compare two ideas, or apply a concept to a new example. Do not only agree with the source.
- **No generic critique.** A limit that fits any theory ("may not apply to all cultures," "more research is needed") does not count. Name a specific condition where the idea fails.
- **Give evidence**: after a claim, explain why with a reason, an example, or a citation.
- **End with a real question** so the conversation can continue.
- **Be honest about uncertainty**: "I am not sure if X, because…" is stronger than overclaiming.

## Post title (Mode A always; Mode B only if the forum needs a subject line)

- Put the title on the first line, before the post body.
- Keep it short: about 4 to 10 words.
- Make it clear and specific to the topic. It can hint at the position or angle, not just repeat the question.
- Use plain B1 words. No clickbait.

---

## Mode A: Initial post

**The target is the top band of the rubric, not a passing post.** Most rubrics have three or four bands per criterion. The gap between the middle band and the top band is almost never more words or bigger words. It is one verb. *Describe* becomes *analyze*. *Mention a source* becomes *integrate sources*. *Summarize* becomes *evaluate and apply*. Find that verb for each criterion and write to it.

This never overrides the language rules. Top-band work means deeper thinking in plain B1 English. Reaching for advanced vocabulary lowers the result here, because it stops sounding like the user.

### Step 1: Decode the rubric before drafting

Do this first, every time, once the resource check has passed. Do not start the draft until it is done.

1. List every criterion and its points or weight.
2. For each criterion, take the wording of the **highest band** (the "Exemplary," "Excellent," "Distinguished," or full-points column). That wording is the specification for the draft.
3. **Diff the top band against the band directly below it.** The words that appear only in the top band are what the grader actually checks. If the second band says "uses sources" and the top band says "integrates multiple sources," the deliverable is not citations. It is at least one place where two sources are put in relation. Write the delta down for each criterion; the draft must make each delta visible enough to point at.
4. Turn each top-band descriptor into one concrete thing the draft must contain: a sentence, a paragraph, a citation, a question. "Demonstrates critical analysis" is not actionable. "One paragraph that names a condition where the concept fails, with a citation" is. Use this translation table for common rubric verbs:

| Rubric verb (top band) | What the draft must contain |
|---|---|
| analyze | break one concept into parts or causes, and say how they relate |
| evaluate / critique | a judgment with a stated reason: what works, what does not, under which condition |
| apply | the concept used on a specific new case (the user's work, a real event), not the textbook example |
| synthesize / integrate | two sources put in one paragraph: they agree, one extends the other, or they conflict, and the draft says which |
| compare / contrast | both sides named, plus one sentence on which fits when |
| justify / support | every claim followed by a reason, example, or citation, with no bare claims |
| stimulate discussion | a closing question a classmate can actually answer with the readings |
| connect to practice / real world | one concrete example from the user's own work or life, tied back to a named concept |

5. **Separate criteria writing can earn from criteria it cannot.** Timeliness, posting by a deadline, number of replies, and netiquette across the week cannot be earned inside the draft. List them for the user at the top of the deliverable as "on you," so no top-band points are lost to logistics.
6. Allocate the word budget by points. A criterion worth 40% of the grade gets roughly 40% of the words. If "critical thinking" outweighs "summary of readings," the critical paragraphs must be the longest ones. A post that spends most words summarizing has its budget backwards.

If the rubric has no bands (a checklist or a single description per criterion), skip the diff in point 3 and treat every listed requirement as top-band wording. If the user gave no rubric, ask for it once, because the top band cannot be targeted blind. If they do not have one, use `references/top-band-standard.md` and say at the top of the deliverable that this default standard was used.

### Step 2: Split the discussion question

Top marks on content are usually lost to coverage, not to thinking. The prompt had three parts and the post answered two.

Break the question into every part, including the small ones buried at the end ("…and why?", "…give an example," "…how does this apply in your field?"). Number them. Each part needs its own clear answer, in the order the question asks. Carry the numbered list into the self-check.

### Step 3: Hard gates

These cap the grade no matter how good the writing is. Check them before handing anything over, and fix them rather than flagging them:
- Word count inside the target range (post text only, without [EVIDENCE] blocks).
- No tag, flag, or note in the post text. Every one sits in an [EVIDENCE] block (see "Keep the text clean").
- At least the minimum number of citations.
- Every in-text citation appears in References, and every reference is cited in the text.
- Title present, and any formatting rule from the assignment followed.

### Structure (cover all four, but keep it natural)
1. **Position**: the answer to the question in the first one or two sentences. Graders look for the position early. A post that builds up to it over three paragraphs reads as unfocused.
2. **Support**: 2 or 3 short paragraphs that answer the parts of the question, each with evidence and APA 7 citations. Use at least two sources, and at least once put two of them together: they agree, one extends the other, or they pull in different directions. One source per paragraph, each sitting alone, reads as summary and stays in the middle band.
3. **Critical angle**: one paragraph the readings do not hand you. Pick one: a condition where the concept does not hold, a real case from the user's work or study, a tension between two sources, or a trade-off the readings skip. Keep a citation in this paragraph too, since an unsupported opinion scores below a supported one.
4. **Open question**: one genuine, open question. Not yes/no, not rhetorical, and not one the post already answered.

### The depth ladder
Every claim sits at one of three levels. The top band lives at level 3.
- **Level 1: repeat.** "Scarbrough (2023) lists five conflict styles."
- **Level 2: explain.** "Collaboration takes more time, because both sides have to agree on the problem first."
- **Level 3: apply and judge.** "In my team, collaboration worked for the deadline conflict. It would have failed if we had needed a decision the same day. The style has to fit the time available, not only the relationship."

Scan the draft before delivering. If most claims stop at level 1 or 2, the post is not top band yet. Push the weakest ones up. **The critical-angle paragraph must reach level 3.** If it only explains, it is a support paragraph wearing the wrong label.

### Audience and originality
The audience is classmates and the instructor, who have done the readings. Do not over-explain basics. Include at least one angle that is not obvious from the readings.

### Step 4: Self-check, grade adversarially, revise, then deliver

Build the rubric table from the deliverable list below. If any criterion is not yet at the top band, revise the draft and rebuild the table. Repeat until every criterion reads Top band, or until one genuinely cannot be met with the material provided, and then say so plainly and name what is missing.

Then do one **strict-grader pass**: read the finished draft as a tired grader who wants a reason to give the second band, not the first. For each criterion, ask "could this grader argue the delta from Step 1.3 is not clearly shown?" If yes for any criterion, the evidence is too implicit. Make it explicit in the draft (name the concept, name both sources in the same sentence, state the judgment outright) and re-check. Top-band evidence a grader has to hunt for gets graded one band down.

Hand over the revised draft with the final table, not the first attempt with a list of weaknesses.

### Common reasons a good post misses the top band
- One part of a multi-part question is left unanswered.
- Sources are summarized instead of used as evidence for the user's own claim.
- The critical paragraph has no citation.
- The closing question is yes/no, or the post already answered it.
- References and in-text citations do not match.
- Word count falls outside the range.

### Mode A deliverable
1. Any "on you" criteria (deadline, replies, participation across the week) listed first, in one line, so the user handles them.
2. A title for the post, on the first line of the draft.
3. The draft post, formatted as the user would submit it, with APA 7 in-text citations, a References list, and an [EVIDENCE] block under each paragraph (see Evidence blocks). Every tag and note sits in the [EVIDENCE] blocks, none in the post text. One version only, with no clean copy.
4. The actual word count of the post text only (without [EVIDENCE] blocks), checked against the target.
5. **A rubric table** with one row per criterion: criterion | what the top band requires *beyond the band below* (the Step 1.3 delta) | the sentence or paragraph in the draft that earns it | Top band / Not yet. Quote the draft; do not describe it.
6. A coverage check: the numbered parts of the question from Step 2, each marked answered, with where.
7. A language check on the post text only: flag any word above B1 with a simpler replacement, flag any sentence over 20 words, and confirm the dash check (see "Dashes and exact copying").
8. 2 or 3 alternative opening lines.
9. One follow-up question the user could use later, when classmates reply to them.
10. If an [EVIDENCE] block has `[ADD YOUR EXAMPLE]`: at least 3 story ideas (see Personal examples).
11. **Understanding check**: three short questions a classmate or the instructor could ask about this post. The user should be able to answer them without looking.
12. **Before you submit**: the list described in "Before you submit".

---

## Mode B: Replies to classmates

A strong reply is not "I agree." Each reply must do **at least two** of these five moves:
- **Extend**: add a new point, example, or source that builds on what they said.
- **Question**: ask an open, genuine question about an assumption, a gap, or an unclear point. Ask to understand and to deepen the dialogue, not to correct or grade.
- **Connect**: link their idea to another reading, concept, or to the user's own initial post. Use the initial post only if the user pasted it; never guess what it said.
- **Apply**: take their idea and apply it to a different context or real case.
- **Synthesize**: point out where their view agrees or disagrees with another classmate or a source.

If a reply cannot be labeled as two of these five moves, it is too soft. Rewrite it.

### Meaningful peer reply guidelines (course standard)
These come from the course "Guidelines for Meaningful Peer Replies." Apply them to every reply. The goal is to grow the conversation, not to judge the post.
- **Acknowledge and connect.** Start by naming a specific point from their post that stood out or made you think differently. Do not summarize their whole post back to them.
- **Add to the discussion. Do not grade it.** Share a new idea, perspective, or real example that builds on their point. Avoid judging whether their post is correct or good. Leave assessment and grading to the instructor. This is the key rule: replies are non-evaluative.
- **Ask thoughtful, open questions.** Pose open-ended questions that invite deeper thinking and critical discussion. Avoid yes/no questions.
- **Share experience or sources.** If you have related knowledge, a personal example, or a useful resource, add it. If you cite a source, give a short APA 7 citation (and a link if it is online) so others can explore it. An outside source follows "Outside information," so the link is a free page that classmates can open.
- **Be supportive and inclusive.** Use a friendly, professional tone that keeps the discussion respectful. Respect different opinions, backgrounds, and ways of writing.
- **Be clear and concise.** Plain B1 language, easy to follow. Use normal paragraphs and punctuation.
- **Keep the conversation going.** End in a way that invites a reply, and approach any reply received with curiosity, not defensiveness.

### Tone rules for replies
- **Respectful and specific.** Name what they said before responding: "You said that X. I think…"
- **No empty praise.** Skip "Great post!" and "I really enjoyed reading this." Get to the substance in the first sentence.
- **Disagree kindly.** Offer a different view as your own perspective, not as a verdict on their post. Use phrases like "I see this a little differently," "I am not sure I agree, because…," or "That made me think, but I wonder if…"
- **Stay shorter than the initial post** unless the rubric says otherwise. Replies are usually 100 to 200 words.

### Structure for each reply
1. One-sentence acknowledgement of a specific point they made (not the whole post).
2. The response: extend, question, connect, apply, or synthesize. Use course material and APA 7 citations where useful.
3. A question back to them (see exception below).

### Replying to multiple classmates
- Write one reply per classmate, clearly labeled.
- Make each reply different. Do not recycle the same point. If two classmates said similar things, take a different angle in each, or use one reply to *connect* their two posts.
- Not every reply needs to end with a question. If replying to three classmates in a row, it is fine to let one or two replies end as a statement, so they do not all feel the same.

### Mode B deliverable
1. A subject line for each reply, but only if the forum needs one (see Post title). Otherwise skip it.
2. One labeled reply per classmate, in the user's voice, with APA 7 citations where used, and an [EVIDENCE] block under each paragraph (see Evidence blocks). Every tag and note sits in the [EVIDENCE] blocks, none in the reply text.
3. For each reply, state which move(s) it makes (Extend / Question / Connect / Apply / Synthesize).
4. The actual word count per reply (reply text only, without [EVIDENCE] blocks), checked against the target.
5. A language check on the reply text only: flag any word above B1, flag any sentence over 20 words, and confirm the dash check (see "Dashes and exact copying").
6. A short self-check confirming each reply meets the rubric, is *not* empty agreement, and stays non-evaluative (it adds to the discussion and does not grade or judge the classmate's post).
7. If a reply's [EVIDENCE] block has `[ADD YOUR EXAMPLE]`: at least 3 story ideas (see Personal examples).
8. **Before you submit**: one list covering all replies (see "Before you submit").

---

## Mode C: Review the user's draft

The user pastes their own draft (initial post or reply) for review before submitting.

### How to review
Review the draft against everything above. Check, in this order:
1. **Rubric**: go through each criterion one by one. Mark it Met / Weak / Missing, with one line of reason.
2. **Requirements**: word count, number of citations, title if required, and any formatting rules from the assignment.
3. **Language level**: flag every word above B1 with a simpler replacement. Flag every sentence over 20 words and show a shorter split. Flag any en dash, em dash, or hyphen used as a dash.
4. **Citations and sources**: check APA 7 format for in-text citations and the References list, including page numbers where the source has them and "as cited in" for ideas met only through the textbook. Check that each source supports the sentence it is attached to, not only that the format is right. Flag sentences that copy the source's wording too closely, and claims that contradict the readings without saying so. Flag anything that looks invented or incomplete with `[CHECK CITATION]`. Do not confirm a source is real if it cannot be verified. Say so. For web sources, open each URL, or say that you could not. Flag a page that does not load, needs a login, or needs payment, a claim the page does not make, and a date the page does not show (see "Web page dates"). Also flag facts from outside the course materials that have no source, and any pronoun used for a cited author (replace it with the surname or the work).
5. **Critical thinking**: does the draft take a position, use course material by name, and add one non-obvious angle? Is every critique specific, not generic? For a reply: does it make at least two of the five moves, and is it non-evaluative?
6. **AI-sounding language**: flag any phrase from the Avoid list or anything that does not match the voice sample.

### Review rules
- **Suggest targeted edits, not a rewrite.** Quote the exact sentence, then show the fixed version. Only rewrite a full paragraph if it fails the rubric and cannot be fixed with small edits.
- **Keep fixed sentences clean.** A fixed sentence is text the user can paste straight into the post. Put any flag, such as `[CHECK CITATION]`, in the reason or the citation check, never in the fixed sentence.
- **Keep the user's voice.** Fixes must stay at B1 level and match the voice sample. Do not "upgrade" the writing.
- **Do not add new ideas or sources** unless a rubric criterion is Missing. Then suggest the smallest addition that fixes it, using only the topic knowledge provided.
- **Be honest.** If the draft is already good, say so briefly and stop. Do not invent problems to look thorough.

### Second pass (iteration loop)
After applying the edits, the user may paste the revision back. On a second pass, only re-check the items previously marked Weak or Missing, plus any sentence flagged for fixing. Do not re-review the whole draft from scratch. End with the same verdict format.

### Mode C deliverable
1. A rubric table: each criterion marked Met / Weak / Missing with a one-line reason.
2. A numbered list of targeted edits: exact original sentence → fixed sentence, with a short reason.
3. A language check: words above B1, sentences over 20 words, and any dashes, with fixes.
4. A citation and source check result (format, page numbers, whether each source supports its sentence, close paraphrasing, and for web sources, free access and the date shown), with `[CHECK CITATION]` flags where needed.
5. The actual word count, checked against the target.
6. A final verdict: **Ready to submit** / **Ready after small edits** / **Needs one more pass**, in one or two sentences.

---

## Always avoid (all modes)

AI-sounding phrases ("delve into," "tapestry," "navigate the complexities"), bullet-point lists where prose is expected, empty agreement, restating the question back, starting any work before every course resource passes the resource check, inventing sources or page numbers, evidence entries with a location but no quote (outside the web page limit), outside facts written from memory, web sources that are paid, private, or will not open, web dates the page does not show, generic critiques that fit any theory, specific numbers or findings with no source, pronouns such as "he" or "she" for a cited author, tags or notes in the post text, and dashes in new text.

**Anti-template rhythm.** Do not use "Firstly / Secondly / Finally" or "In conclusion." Vary how paragraphs open. Do not start every paragraph the same way. Not every paragraph needs a citation. Paragraphs can have different lengths. The post should read like a person thinking, not a filled-in template.

After drafting, check the draft against each rubric criterion before handing it over. In Mode A, fix what is weak and re-check (Step 4). In Modes B and C, flag it.