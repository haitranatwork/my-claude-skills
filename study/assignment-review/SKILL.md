---
name: assignment-review
description: "Review the user's own draft of a written assignment (essay, report, paper), with a rubric check and numbered edits in their B1 voice. Use when asked to review, check, or improve an essay or report."
---

# Review my written assignment

Review a **written assignment** the user wrote, before they submit it, and suggest the smallest edits that lift it to the top band. The goal is to improve the user's draft, not to replace it.

Other tasks have their own skills: `assignment-create` writes a new assignment, and the `forum-post` skills handle discussion forum posts. If the request is one of those, say which skill fits. Grading a classmate's assignment is outside this skill: say so and stop.

## Inputs

The user fills in `assets/input-template.md`, or pastes the same parts.
- **Required:** the user's draft (the full assignment, with References), the assignment question, the rubric, and the course material the draft uses.
- **Optional:** the assignment instructions (word count, minimum number of sources, formatting), and the output format for the corrected assignment (Markdown or Word).

If the draft or the question is missing, ask for it. If the rubric is missing, ask for it too, and follow "No rubric" in `rubric.md` when the user answers that there is none.

## Steps

1. **Resource check.** Read `references/resource-check.md` and run it. Also check every course material the draft cites. Outside sources the draft cites are checked in step 3, not here.
2. **Read the standards.** Read `references/rubric.md`, `references/strong-assignment.md`, `references/language.md`, `references/voice-sample.md`, `references/apa7.md`, and `references/sources.md`. Decode the rubric: the top band and the delta for each criterion.
3. **Review the draft** in this order. If the draft still holds evidence blocks, review the text only, and remind the user to delete the blocks before submitting.
   1. **Rubric:** mark each criterion Met, Weak, or Missing against its delta, with a one-line reason.
   2. **Requirements:** the word count, the minimum number of sources, the title and headings, and the formatting rules in the instructions.
   3. **Question coverage:** number the parts of the question, and name any part that is missing or thin.
   4. **Structure:** the thesis, the topic sentences, the conclusion, and the signposting, against `strong-assignment.md`.
   5. **Language:** the language check in `language.md`, plus words that sound like AI writing and anything that does not match the voice sample.
   6. **Citations and sources:** APA 7 format in the text, in References, and in the headings, including page numbers, "as cited in," "and" against "&," and DOI URLs; whether each source really supports the sentence it is attached to; sentences that copy the source's wording too closely; claims that contradict the course material without saying so; facts from outside the course material with no source; and pronouns used for a cited author. For a source with a user's copy, use that copy alone (see `resource-check.md`). Open each other web source and DOI URL, or say that you could not. Report a page that does not load, needs a login, or needs payment, a DOI URL that leads to a different work, a claim the page does not make, and a date the page does not show. Report a source you cannot verify as unverified, never as confirmed.
   7. **Critical thinking:** ideas or sources compared, specific critique, the user's own reasoned position, and claims that reach level 3 of the depth ladder where the rubric asks for it.
4. **Write the suggestions.** Number them 1, 2, 3, and so on, in order of grade impact. Each one gives its location (the section and the paragraph), the exact sentence from the draft, the fixed sentence, and a short reason.
   - Make targeted edits. Rewrite a whole paragraph only when it fails the rubric and small edits cannot fix it.
   - A bigger fix, such as a new paragraph, a paragraph to move, or a passage to cut, is a numbered suggestion too: it gives the full new text and says exactly where it goes.
   - A fixed sentence is clean text the user can paste straight in, in the user's voice. Any flag, such as `[CHECK CITATION: ...]`, goes in the reason.
   - Add a new idea or source only to fix a Missing criterion, and then only the smallest addition, from the course material given.
   - What only the user can fix goes in the "For you to fix" list (see "Deliverable"), not in a suggestion.
   - When the user asks for a rewrite, give this review. Applying every suggestion is the most this skill changes, and a fresh version is the task of `assignment-create`.
   - If the draft is already good, say so briefly and stop. An honest short review beats invented problems.
5. **Deliver** as described below.
6. **Apply the accepted suggestions.** When the user names the numbers they accept (for example, "apply 1, 3, 4"), return the full corrected assignment in one file, in the format the user confirmed, named from the course code and unit (such as `CS2204-Unit3-assignment.md`), or from a short topic name. Apply only those suggestions, and copy every other character of the draft exactly (see "Exact copying" in `language.md`). For a Word draft returned as Word, make the edits in a copy of the user's file, so its formatting stays. If the user named no format, use the format the draft came in and say so. In the chat, list the numbers you applied and the flags still open.
7. **Second pass.** When the user pastes a revised draft, check again only the criteria marked Weak or Missing and the sentences that had suggestions. Deliver in the same format.

## Deliverable

In the chat, in this order:
1. **Verdict:** Ready to submit, Ready after small edits, or Needs one more pass, in one or two sentences that name the biggest risk to the grade.
2. **Rubric table:** criterion | Met / Weak / Missing | one-line reason.
3. **Suggestions:** the numbered list from step 4.
4. **For you to fix:** what only the user can fix, such as their own example, a page number, or a source to find. Each item gives its location and a flag: `[CHECK CITATION: ...]`, `[SOURCE NEEDED: ...]`, `[CHECK NUMBER: ...]`, or `[ADD YOUR EXAMPLE: ...]`. Write "Nothing" when the list is empty.
5. **Checks:** the word count against the target; each question part with where the draft answers it; the language check; and the citation and source check.
6. The closing line: "Reply with the numbers you accept and the format you want, Markdown or Word, and I will return the corrected assignment." When the user already named the format, name it in this line instead of asking.
