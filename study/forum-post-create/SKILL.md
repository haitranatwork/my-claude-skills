---
name: forum-post-create
description: "Write the user's initial post for a university discussion forum, in their B1 voice with APA 7 citations. Use when asked to write, draft, or plan an initial post or answer a discussion question."
---

# Create an initial post

Write the user's **initial post**, their answer to the discussion question. The post reaches the top band of the rubric, sounds like the user, and lets the user check every claim before submitting.

Other forum tasks have their own skills: `forum-post-review` reviews the user's own draft, `forum-post-assessment` grades a classmate's initial post, and `forum-post-reply` writes replies. If the request is one of those, say which skill fits.

## Inputs

The user fills in `assets/input-template.md`, or pastes the same parts. If they have sent nothing yet, point them to the template.
- **Required:** the discussion question, the rubric, the assignment instructions (word count, citation minimum, formatting), and the course material.
- **Optional:** a real example from the user's work or life, and sample posts. Sample posts guide depth and structure only, never voice or wording.

Ask only when a required part is missing or empty. The user prefers a finished result over questions, so the plan in step 4 is the only planned stop.

## Steps

1. **Resource check.** Read `references/resource-check.md` and run it. Go on only when every item passes.
2. **Decode the rubric.** Read `references/rubric.md` and `references/strong-post.md`. For each criterion, note its weight, its top-band wording, its delta, and the concrete thing the post must contain. Also note the "on you" criteria and the word budget. This step is done when every criterion has a delta and a concrete target.
3. **Split the question.** Number every part of the question, including the small ones at the end ("...and why?", "...give an example," "...how does this apply in your field?"). Each part gets its own answer, in the order the question asks.
4. **Plan, then stop.** Read `references/sources.md`, `references/evidence-blocks.md`, and `references/personal-examples.md`. Show the plan:
   - the position, in one or two sentences;
   - the critical angle, and the criterion it serves;
   - each numbered question part, with the paragraph that will answer it;
   - the personal example: the user's real example, or at least 3 story ideas when the post needs one and the user gave none;
   - the sources (see "Sources in the plan" in `evidence-blocks.md`).

   Then wait for the user's reply. If the user said to write directly, skip the plan and go on.
5. **Draft.** Read `references/language.md`, `references/voice-sample.md`, and `references/apa7.md`. Write the title and the post from the approved plan, with the structure in `strong-post.md`, the word budget from step 2, and an evidence block under each paragraph (see `evidence-blocks.md`).
6. **Check and revise.**
   - Fix every hard gate below.
   - Build the rubric table (see "Deliverable"). Revise until every criterion reads Top band. If one cannot get there with the material given, say so plainly and name what is missing.
   - Check the depth ladder in `strong-post.md`: push weak claims up a level, and make sure the critical-angle paragraph reaches level 3.
   - Do one **strict-grader pass**: read the post as a tired grader looking for a reason to give the band below. For each criterion, ask whether this grader could argue that the delta is not clearly shown. If so, make it explicit: name the concept, name both sources in the same sentence, or state the judgment outright, then check again. Top-band evidence that a grader has to hunt for gets graded one band down.
7. **Deliver** as described below: the revised post, not a first attempt with a list of weaknesses.

## Hard gates

These cap the grade however good the writing is. Fix each one before delivering:
- The word count of the post text (without evidence blocks) is inside the target range.
- The post text holds no label, flag, or note; each one sits in an evidence block.
- The post meets the citation minimum.
- Every in-text citation appears in References, and every reference is cited in the text.
- References match the sources approved in the plan. A source added after the plan is named at the top of the chat reply.
- The title is present, and every formatting rule from the instructions is followed.
- The dash check in `language.md` passes.

## Deliverable

**The post file.** A Markdown file named from the course code and unit in the instructions, such as `CS2204-Unit5-initial-post.md`, or from a short topic name when the instructions give neither. It holds only what the user will submit, plus the evidence blocks: the title on the first line, the post with an evidence block under each paragraph, and the References list.

**The chat reply**, kept short, in this order:
1. **On you:** the criteria the post cannot earn by itself (deadline, replies, participation across the week), in one line.
2. **Checks:** the word count against the target; each numbered question part with the paragraph that answers it; and the language check from `language.md`.
3. **Rubric table:** criterion | the delta (what the top band needs beyond the band below) | the sentence or paragraph that earns it, quoted from the post | Top band / Not yet.
4. **Understanding check:** three short questions a classmate or the instructor could ask about this post. The user should be able to answer them without looking.
5. **Before you submit:** the list described in `evidence-blocks.md`.
