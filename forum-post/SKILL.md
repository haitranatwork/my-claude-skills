---
name: forum-post
description: Draft or review university discussion forum posts in the user's simple B1 English voice with APA 7 citations. Use for any discussion post, forum post, initial post, classmate reply, or when the user pastes their own draft post and asks to review, check, or improve it before submitting.
---

# University Discussion Forum Post

Produce a complete, ready-to-edit draft of a university discussion forum post, or review the user's own draft before submission. The output must sound like the user, follow the rubric, use APA 7 citations, and show real critical thinking — not a generic summary.

There are three modes:
- **Mode A — Initial post**: answer the discussion question at the top band of the rubric.
- **Mode B — Replies**: respond to one or more classmate posts.
- **Mode C — Review**: review a draft the user wrote (or edited) before they submit it.

The user will say which mode they want. If they don't, ask — do not guess.

## How the user provides the task

The user supplies the variable parts each time, usually as a filled-in copy of `assets/input-template.md`. Expect some or all of:
- a quick-fill header (mode, word count target, replies needed, minimum citations, discipline)
- the rubric
- the assignment instructions (word count, number of replies, deadline, formatting rules)
- topic knowledge / course material (concepts, authors, definitions, data, quotes with page numbers)
- the exact discussion question
- for Mode B: the full classmate post(s), labeled Classmate 1, Classmate 2, etc.
- for Mode C: the user's own draft
- optional sample posts (use only for depth and structure, never to copy voice or wording)

If the user hasn't pasted this content, point them to `assets/input-template.md` so they can fill it in.

**Intake rules:**
- If the user mentions file uploads but forgot to attach them, ask for the files before doing anything.
- If a required part is empty (quick-fill header, rubric, assignment instructions, topic knowledge, or discussion question), ask the user to update it.
- If the user says they will run a mode later, confirm that everything is ready and wait. Do not execute any mode until they say which one to run.
- Check the output against the quick-fill header numbers. Report the actual word count in the deliverable.

**Before drafting, always read `references/voice-sample.md`.** It holds the user's real writing. Mirror its sentence length, rhythm, formality, hedging words, and how the user opens and closes posts.

Only ask a clarifying question if something critical is missing: no rubric, no discussion question, no classmate post in Mode B, no draft in Mode C, or missing citation details. Otherwise proceed directly — the user prefers a finished result over questions.

## Language rules (strict — apply to every sentence)

The user writes at CEFR B1 level. This is the most important constraint. The draft must read like the user wrote it, so plain language always wins.

- **Vocabulary: B1 or below.** Use common, everyday words. Prefer *show, use, help, important, problem, idea, also, but, because, however*. Avoid "elevated" synonyms and AI-sounding words such as *delve, navigate, leverage, underscore, tapestry, multifaceted, paradigm, intricate*. If a B2+ word is a real technical term from the course, keep it — but do not reach for fancy words.
- **Simple sentences.** Most sentences are one clause. Use some two-clause sentences joined by *and, but, because, so, when, if*. Avoid long sentences with many commas, semicolons, or nested clauses.
- **Sentence length 12–18 words on average.** Vary a little. Never write a sentence over 30 words.
- **One idea per sentence. One topic per paragraph.**
- **Active voice** almost everywhere. Use passive only when the actor does not matter.
- **No filler phrases** such as "It is important to note that," "In today's society," or "Since the dawn of time."

## APA 7 citation rules

- In-text citations in APA 7 format: `(Author, Year)` or `Author (Year)`.
- For a direct quote, add the page number: `(Author, Year, p. 12)`. Keep quotes short (under 40 words) and rare. Paraphrase when possible.
- End the post with a **References** section in APA 7 format: hanging indent style, alphabetical by author surname.
- If a source is missing publication details, flag it with `[CHECK CITATION]`. Never invent author names, years, or page numbers.
- **Source whitelist.** Only cite sources listed in the topic knowledge. If 1–2 outside sources would make the post stronger, do not add them silently — ask the user first and wait for confirmation.

## Personal examples (do not invent silently)

The user's posts often use a real personal or work example. Never invent one and present it as the user's without telling them. If a personal example would strengthen the post and none was given:
1. Insert `[ADD YOUR EXAMPLE: what kind of example fits here]` in the draft, and
2. Ask the user: do they want to supply a real example, or should you invent one for them to adapt?

If they say invent, write a realistic example that fits their background (software team leader at a SaaS company building a dealership management system) and mark it `[INVENTED — check and adjust details]`.

## What makes a strong post (all modes)

- **Take a clear position** in the first one or two sentences.
- **Name the course material specifically** — the concept, author, or study. Do not write "the readings showed."
- **Show critical thinking**: ask a question, compare two ideas, or apply a concept to a new example. Do not only agree with the source.
- **Give evidence**: after a claim, explain why with a reason, an example, or a citation.
- **End with a real question** so the conversation can continue.
- **Be honest about uncertainty**: "I am not sure if X, because…" is stronger than overclaiming.

## Post title (Mode A always; Mode B only if the forum needs a subject line)

- Put the title on the first line, before the post body.
- Keep it short: about 4–10 words.
- Make it clear and specific to the topic. It can hint at the position or angle, not just repeat the question.
- Use plain B1 words. No clickbait.

---

## Mode A — Initial post

**The target is the top band of the rubric, not a passing post.** Most rubrics have three or four bands per criterion. The gap between the middle band and the top band is almost never more words or bigger words — it is one verb. *Describe* becomes *analyze*. *Mention a source* becomes *integrate sources*. *Summarize* becomes *evaluate and apply*. Find that verb for each criterion and write to it.

This never overrides the language rules. Top-band work means deeper thinking in plain B1 English. Reaching for advanced vocabulary lowers the result here, because it stops sounding like the user.

### Step 1 — Decode the rubric before drafting

Do this first, every time. Do not start the draft until it is done.

1. List every criterion and its points or weight.
2. For each criterion, take the wording of the **highest band** — the "Exemplary," "Excellent," "Distinguished," or full-points column. That wording is the specification for the draft.
3. **Diff the top band against the band directly below it.** The words that appear only in the top band are what the grader actually checks. If the second band says "uses sources" and the top band says "integrates multiple sources," the deliverable is not citations — it is at least one place where two sources are put in relation. Write the delta down for each criterion; the draft must make each delta visible enough to point at.
4. Turn each top-band descriptor into one concrete thing the draft must contain: a sentence, a paragraph, a citation, a question. "Demonstrates critical analysis" is not actionable. "One paragraph that names a condition where the concept fails, with a citation" is. Use this translation table for common rubric verbs:

| Rubric verb (top band) | What the draft must contain |
|---|---|
| analyze | break one concept into parts or causes, and say how they relate |
| evaluate / critique | a judgment with a stated reason: what works, what does not, under which condition |
| apply | the concept used on a specific new case (the user's work, a real event), not the textbook example |
| synthesize / integrate | two sources put in one paragraph: they agree, one extends the other, or they conflict — and the draft says which |
| compare / contrast | both sides named, plus one sentence on which fits when |
| justify / support | every claim followed by a reason, example, or citation — no bare claims |
| stimulate discussion | a closing question a classmate can actually answer with the readings |
| connect to practice / real world | one concrete example from the user's own work or life, tied back to a named concept |

5. **Separate criteria writing can earn from criteria it cannot.** Timeliness, posting by a deadline, number of replies, and netiquette across the week cannot be earned inside the draft. List them for the user at the top of the deliverable as "on you," so no top-band points are lost to logistics.
6. Allocate the word budget by points. A criterion worth 40% of the grade gets roughly 40% of the words. If "critical thinking" outweighs "summary of readings," the critical paragraphs must be the longest ones — a post that spends most words summarizing has its budget backwards.

If the rubric has no bands — a checklist or a single description per criterion — skip the diff in point 3 and treat every listed requirement as top-band wording. If the user gave no rubric, ask for it once — the top band cannot be targeted blind. If they do not have one, use `references/top-band-standard.md` and say at the top of the deliverable that this default standard was used.

### Step 2 — Split the discussion question

Top marks on content are usually lost to coverage, not to thinking. The prompt had three parts and the post answered two.

Break the question into every part, including the small ones buried at the end ("…and why?", "…give an example," "…how does this apply in your field?"). Number them. Each part needs its own clear answer, in the order the question asks. Carry the numbered list into the self-check.

### Step 3 — Hard gates

These cap the grade no matter how good the writing is. Check them before handing anything over, and fix them rather than flagging them:
- Word count inside the target range.
- At least the minimum number of citations.
- Every in-text citation appears in References, and every reference is cited in the text.
- Title present, and any formatting rule from the assignment followed.

### Structure (cover all four, but keep it natural)
1. **Position** — the answer to the question in the first one or two sentences. Graders look for the position early. A post that builds up to it over three paragraphs reads as unfocused.
2. **Support** — 2–3 short paragraphs that answer the parts of the question, each with evidence and APA 7 citations. Use at least two sources, and at least once put two of them together: they agree, one extends the other, or they pull in different directions. One source per paragraph, each sitting alone, reads as summary and stays in the middle band.
3. **Critical angle** — one paragraph the readings do not hand you. Pick one: a condition where the concept does not hold, a real case from the user's work or study, a tension between two sources, or a trade-off the readings skip. Keep a citation in this paragraph too, since an unsupported opinion scores below a supported one.
4. **Open question** — one genuine, open question. Not yes/no, not rhetorical, and not one the post already answered.

### The depth ladder
Every claim sits at one of three levels. The top band lives at level 3.
- **Level 1 — repeat.** "Scarbrough (2023) lists five conflict styles."
- **Level 2 — explain.** "Collaboration takes more time, because both sides have to agree on the problem first."
- **Level 3 — apply and judge.** "In my team, collaboration worked for the deadline conflict. It would have failed if we had needed a decision the same day. The style has to fit the time available, not only the relationship."

Scan the draft before delivering. If most claims stop at level 1 or 2, the post is not top band yet. Push the weakest ones up. **The critical-angle paragraph must reach level 3** — if it only explains, it is a support paragraph wearing the wrong label.

### Audience and originality
The audience is classmates and the instructor, who have done the readings. Do not over-explain basics. Include at least one angle that is not obvious from the readings.

### Step 4 — Self-check, grade adversarially, revise, then deliver

Build the rubric table from the deliverable list below. If any criterion is not yet at the top band, revise the draft and rebuild the table. Repeat until every criterion reads Top band — or until one genuinely cannot be met with the material provided, and then say so plainly and name what is missing.

Then do one **strict-grader pass**: read the finished draft as a tired grader who wants a reason to give the second band, not the first. For each criterion, ask "could this grader argue the delta from Step 1.3 is not clearly shown?" If yes for any criterion, the evidence is too implicit — make it explicit in the draft (name the concept, name both sources in the same sentence, state the judgment outright) and re-check. Top-band evidence a grader has to hunt for gets graded one band down.

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
3. The draft post, formatted as the user would submit it, with APA 7 in-text citations and a References list.
4. The actual word count, checked against the target.
5. **A rubric table** — one row per criterion: criterion | what the top band requires *beyond the band below* (the Step 1.3 delta) | the sentence or paragraph in the draft that earns it | Top band / Not yet. Quote the draft; do not describe it.
6. A coverage check — the numbered parts of the question from Step 2, each marked answered, with where.
7. A language check — flag any word above B1 with a simpler replacement, and flag any sentence over 20 words.
8. 2–3 alternative opening lines.
9. One follow-up question the user could use later, when classmates reply to them.

---

## Mode B — Replies to classmates

A strong reply is not "I agree." Each reply must do **at least two** of these five moves:
- **Extend** — add a new point, example, or source that builds on what they said.
- **Question** — ask an open, genuine question about an assumption, a gap, or an unclear point. Ask to understand and to deepen the dialogue, not to correct or grade.
- **Connect** — link their idea to another reading, concept, or to the user's own initial post.
- **Apply** — take their idea and apply it to a different context or real case.
- **Synthesize** — point out where their view agrees or disagrees with another classmate or a source.

If a reply cannot be labeled as two of these five moves, it is too soft. Rewrite it.

### Meaningful peer reply guidelines (course standard)
These come from the course "Guidelines for Meaningful Peer Replies." Apply them to every reply. The goal is to grow the conversation, not to judge the post.
- **Acknowledge and connect.** Start by naming a specific point from their post that stood out or made you think differently. Do not summarize their whole post back to them.
- **Add to the discussion — do not grade it.** Share a new idea, perspective, or real example that builds on their point. Avoid judging whether their post is correct or good. Leave assessment and grading to the instructor. This is the key rule: replies are non-evaluative.
- **Ask thoughtful, open questions.** Pose open-ended questions that invite deeper thinking and critical discussion. Avoid yes/no questions.
- **Share experience or sources.** If you have related knowledge, a personal example, or a useful resource, add it. If you cite a source, give a short APA 7 citation (and a link if it is online) so others can explore it.
- **Be supportive and inclusive.** Use a friendly, professional tone that keeps the discussion respectful. Respect different opinions, backgrounds, and ways of writing.
- **Be clear and concise.** Plain B1 language, easy to follow. Use normal paragraphs and punctuation.
- **Keep the conversation going.** End in a way that invites a reply, and approach any reply received with curiosity, not defensiveness.

### Tone rules for replies
- **Respectful and specific.** Name what they said before responding: "You said that X. I think…"
- **No empty praise.** Skip "Great post!" and "I really enjoyed reading this." Get to the substance in the first sentence.
- **Disagree kindly.** Offer a different view as your own perspective, not as a verdict on their post. Use phrases like "I see this a little differently," "I am not sure I agree, because…," or "That made me think, but I wonder if…"
- **Stay shorter than the initial post** unless the rubric says otherwise. Replies are usually 100–200 words.

### Structure for each reply
1. One-sentence acknowledgement of a specific point they made (not the whole post).
2. The response — extend, question, connect, apply, or synthesize. Use course material and APA 7 citations where useful.
3. A question back to them (see exception below).

### Replying to multiple classmates
- Write one reply per classmate, clearly labeled.
- Make each reply different. Do not recycle the same point. If two classmates said similar things, take a different angle in each, or use one reply to *connect* their two posts.
- Not every reply needs to end with a question. If replying to three classmates in a row, it is fine to let one or two replies end as a statement, so they do not all feel the same.

### Mode B deliverable
1. A subject line for each reply, but only if the forum needs one (see Post title). Otherwise skip it.
2. One labeled reply per classmate, in the user's voice, with APA 7 citations where used.
3. For each reply, state which move(s) it makes (Extend / Question / Connect / Apply / Synthesize).
4. The actual word count per reply, checked against the target.
5. A language check — flag any word above B1, and flag any sentence over 20 words.
6. A short self-check confirming each reply meets the rubric, is *not* empty agreement, and stays non-evaluative (it adds to the discussion and does not grade or judge the classmate's post).

---

## Mode C — Review the user's draft

The user pastes their own draft (initial post or reply) for review before submitting.

### How to review
Review the draft against everything above. Check, in this order:
1. **Rubric** — go through each criterion one by one. Mark it Met / Weak / Missing, with one line of reason.
2. **Requirements** — word count, number of citations, title if required, and any formatting rules from the assignment.
3. **Language level** — flag every word above B1 with a simpler replacement. Flag every sentence over 20 words and show a shorter split.
4. **Citations** — check APA 7 format for in-text citations and the References list. Flag anything that looks invented or incomplete with `[CHECK CITATION]`. Do not confirm a source is real if it cannot be verified — say so.
5. **Critical thinking** — does the draft take a position, use course material by name, and add one non-obvious angle? For a reply: does it make at least two of the five moves, and is it non-evaluative?
6. **AI-sounding language** — flag any phrase from the Avoid list or anything that does not match the voice sample.

### Review rules
- **Suggest targeted edits, not a rewrite.** Quote the exact sentence, then show the fixed version. Only rewrite a full paragraph if it fails the rubric and cannot be fixed with small edits.
- **Keep the user's voice.** Fixes must stay at B1 level and match the voice sample. Do not "upgrade" the writing.
- **Do not add new ideas or sources** unless a rubric criterion is Missing — then suggest the smallest addition that fixes it, using only the topic knowledge provided.
- **Be honest.** If the draft is already good, say so briefly and stop. Do not invent problems to look thorough.

### Second pass (iteration loop)
After applying the edits, the user may paste the revision back. On a second pass, only re-check the items previously marked Weak or Missing, plus any sentence flagged for fixing. Do not re-review the whole draft from scratch. End with the same verdict format.

### Mode C deliverable
1. A rubric table: each criterion marked Met / Weak / Missing with a one-line reason.
2. A numbered list of targeted edits: exact original sentence → fixed sentence, with a short reason.
3. A language check — words above B1 and sentences over 20 words, with fixes.
4. A citation check result, with `[CHECK CITATION]` flags where needed.
5. The actual word count, checked against the target.
6. A final verdict: **Ready to submit** / **Ready after small edits** / **Needs one more pass**, in one or two sentences.

---

## Always avoid (all modes)

AI-sounding phrases ("delve into," "tapestry," "navigate the complexities"), bullet-point lists where prose is expected, empty agreement, restating the question back, and inventing sources or page numbers.

**Anti-template rhythm.** Do not use "Firstly / Secondly / Finally" or "In conclusion." Vary how paragraphs open — do not start every paragraph the same way. Not every paragraph needs a citation. Paragraphs can have different lengths. The post should read like a person thinking, not a filled-in template.

After drafting, check the draft against each rubric criterion before handing it over. In Mode A, fix what is weak and re-check (Step 4). In Modes B and C, flag it.
