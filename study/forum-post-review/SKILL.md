---
name: forum-post-review
description: "Review the user's own draft of a discussion forum initial post, with a rubric check and numbered edits in their B1 voice. Use when asked to review, check, or improve their initial post."
---

# Review my initial post

Review the user's own **initial post** before they submit it, and suggest the smallest edits that lift it to the top band. The goal is to improve the user's draft, not to replace it.

Other forum tasks have their own skills: `forum-post-create` writes a new initial post, `forum-post-assessment` grades a classmate's initial post, and `forum-post-reply` writes replies and reviews replies the user wrote. If the request is one of those, say which skill fits.

## Inputs

The user fills in `assets/input-template.md`, or pastes the same parts.
- **Required:** the user's draft (the full post, with References), the discussion question, the rubric, and the course material the draft uses.
- **Optional:** the assignment instructions (word count, citation minimum, formatting).

Inputs carry over within a chat: the user often runs `forum-post-create` first and asks for the review later in the same chat. Reuse every input the user already sent in this chat for this discussion: the question, the instructions, the rubric (or the answer that there is none), the course material, and the user's copy of any outside source. When the user sends no new draft, review the latest version of the initial post in the chat, such as the post file from `forum-post-create`. Right after the resource check line, list in one line what you took from earlier in the chat, including the draft if it came from there, so the user can correct it.

If the draft or the question is still missing, ask for it. For a missing rubric, follow "No rubric" in `rubric.md`.

## Steps

1. **Resource check.** Read `references/resource-check.md` and run it. Also check every course material the draft cites. Outside sources the draft cites are checked in step 3, not here.
2. **Read the standards.** Read `references/rubric.md`, `references/strong-post.md`, `references/language.md`, `references/voice-sample.md`, `references/apa7.md`, and `references/sources.md`. Decode the rubric: the top band and the delta for each criterion.
3. **Review the draft** in this order. If the draft still holds evidence blocks, review the text only, and remind the user to delete the blocks before submitting.
   1. **Rubric:** mark each criterion Met, Weak, or Missing against its delta, with a one-line reason.
   2. **Requirements:** the word count, the citation minimum, the title, and the formatting rules in the instructions.
   3. **Question coverage:** number the parts of the question, and name any part that is missing or thin.
   4. **Language:** the language check in `language.md`, plus words that sound like AI writing and anything that does not match the voice sample.
   5. **Citations and sources:** APA 7 format in the text and in References, including page numbers, "as cited in," and DOI URLs; whether each source really supports the sentence it is attached to; sentences that copy the source's wording too closely; claims that contradict the course material without saying so; facts from outside the course material with no source; and pronouns used for a cited author. For a source with a user's copy, use that copy alone (see `resource-check.md`). Open each other web source and DOI URL, or say that you could not. Report a page that does not load, needs a login, or needs payment, a DOI URL that leads to a different work, a claim the page does not make, and a date the page does not show. Report a source you cannot verify as unverified, never as confirmed.
   6. **Critical thinking:** a position in the first sentences, course material named specifically, one angle that is not obvious, specific critique, and claims that reach level 3 of the depth ladder where the rubric asks for it.
4. **Write the suggestions.** Number them 1, 2, 3, and so on, in order of grade impact. Each one gives the exact sentence from the draft, the fixed sentence, and a short reason.
   - Make targeted edits. Rewrite a whole paragraph only when it fails the rubric and small edits cannot fix it.
   - A fixed sentence is clean text the user can paste straight in, in the user's voice at B1. Any flag, such as `[CHECK CITATION: ...]`, goes in the reason.
   - Add a new idea or source only to fix a Missing criterion, and then only the smallest addition, from the course material given.
   - If the draft is already good, say so briefly and stop. An honest short review beats invented problems.
5. **Deliver** as described below.
6. **Apply the accepted edits.** When the user names the numbers they accept (for example, "apply 1, 3, 4"), return the full corrected post in a Markdown file named from the course code and unit (such as `CS2204-Unit5-initial-post.md`), or from a short topic name. Apply only those edits, and copy every other character of the draft exactly (see "Exact copying" in `language.md`). In the chat, list the numbers you applied.
7. **Second pass.** When the user pastes a revised draft, check again only the criteria marked Weak or Missing and the sentences that had suggestions. Deliver in the same format.

## Deliverable

In the chat, in this order:
1. **Verdict:** Ready to submit, Ready after small edits, or Needs one more pass, in one or two sentences that name the biggest risk to the grade.
2. **Rubric table:** criterion | Met / Weak / Missing | one-line reason.
3. **Suggestions:** the numbered list from step 4.
4. **Checks:** the word count against the target; each question part with where the draft answers it; the language check; and the citation and source check.
5. The closing line: "Reply with the numbers you accept, and I will return the corrected post."
