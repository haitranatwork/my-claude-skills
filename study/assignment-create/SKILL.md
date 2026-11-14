---
name: assignment-create
description: "Write the user's written assignment (essay, report, reflection paper, case study) in their B1 voice with APA 7 citations. Use when asked to write, draft, or plan an essay, report, or paper."
---

# Create a written assignment

Write the user's **written assignment**: an essay, a report, a reflection paper, or a case study. The assignment reaches the top band of the rubric, sounds like the user, and lets the user check every claim before submitting.

Other tasks have their own skills: `assignment-review` reviews a draft the user wrote, and the `forum-post` skills handle discussion forum posts. If the request is one of those, say which skill fits.

## Inputs

The user fills in `assets/input-template.md`, or pastes the same parts. If they have sent nothing yet, point them to the template.
- **Required:** the assignment question, the rubric, the assignment instructions (word count, minimum number of sources, formatting), and the course material.
- **Optional:** the output format (Markdown or Word), a real example from the user's work or life, and extra notes.

Ask only when a required part is missing or empty. When the rubric is missing, ask for it before the plan, and follow "No rubric" in `references/rubric.md` if the user answers that there is none. The user prefers a finished result over questions, so the plan in step 4 is the only planned stop.

## Steps

1. **Resource check.** Read `references/resource-check.md` and run it. Go on only when every item passes.
2. **Decode the rubric.** Read `references/rubric.md` and `references/strong-assignment.md`. For each criterion, note its weight, its top-band wording, its delta, and the concrete thing the assignment must contain. Also note the "on you" criteria and the word budget. This step is done when every criterion has a delta and a concrete target.
3. **Split the question.** Number every part of the question, including the small ones at the end ("...and why?", "...give an example," "...how does this apply in your field?"). Each part gets its own answer, in the order the question asks.
4. **Plan, then stop.** Read `references/sources.md`, `references/evidence-blocks.md`, and `references/personal-examples.md`. Show the plan:
   - the thesis, in one or two sentences;
   - the sections in order, each with its heading if it has one, the numbered question parts it answers, the criterion and delta it earns, and its word budget;
   - the critical angle: what the assignment will weigh or judge, and the section that does it;
   - the personal example: the user's real example, or at least 3 story ideas when the assignment needs one and the user gave none;
   - the sources (see "Sources in the plan" in `evidence-blocks.md`);
   - the output format, for the user to confirm: the format the user named, or the question "Markdown or Word?" when they named none.

   Then wait for the user's reply. If the user said to write directly, skip the plan and go on. If they also named no output format, ask that one question first.
5. **Draft.** Read `references/language.md`, `references/voice-sample.md`, and `references/apa7.md`. Write the title and the assignment from the approved plan, with the structure in `strong-assignment.md`, the word budget from step 2, and an evidence block under each paragraph (see `evidence-blocks.md`).
6. **Check and revise.**
   - Fix every hard gate below.
   - Build the rubric table (see "Deliverable"). Revise until every criterion reads Top band. If one cannot get there with the material given, say so plainly and name what is missing.
   - Check the depth ladder in `strong-assignment.md`: push weak claims up a level, and make sure every section that answers an analysis, evaluation, or application criterion reaches level 3.
   - Do one **strict-grader pass**: read the assignment as a tired grader looking for a reason to give the band below. For each criterion, ask whether this grader could argue that the delta is not clearly shown. If so, make it explicit: name the concept, name both sources in the same sentence, or state the judgment outright, then check again. Top-band evidence that a grader has to hunt for gets graded one band down.
7. **Deliver** as described below: the revised assignment, not a first attempt with a list of weaknesses.

## Hard gates

These cap the grade however good the writing is. Fix each one before delivering:
- The word count is inside the target range (see "Word count" in `strong-assignment.md`).
- The assignment text holds no label, flag, or note; each one sits in an evidence block.
- The assignment meets the minimum number of sources.
- Every in-text citation appears in References, and every reference is cited in the text.
- References match the sources approved in the plan. A source added after the plan is named under "Changes from the plan" in the check file.
- The title is present, and every formatting rule from the instructions is followed.
- The tone rules and the dash check in `language.md` pass.

## Deliverable

Two files, named as a pair from the course code and unit in the instructions, such as `CS2204-Unit3-assignment.md` and `CS2204-Unit3-checks.md`, or from a short topic name when the instructions give neither.

**The assignment document**, in the format the user confirmed. It holds only what the user will submit, plus the evidence blocks: it starts at the title and ends at the last References entry, with the headings the assignment needs and an evidence block under each paragraph. A Word file gives the title and headings their APA 7 format and each References entry a real hanging indent (see `apa7.md`). If a Word file cannot be made in this chat, say so and deliver Markdown.

**The check file**, in Markdown, with these parts in this order:
1. **On you:** the criteria the assignment cannot earn by itself, such as submitting by the deadline, in one line.
2. **Rubric table:** criterion | the delta (what the top band needs beyond the band below) | the sentence that earns it, quoted from the assignment, with its section | Top band / Not yet.
3. **Question parts:** each numbered part of the question, with the section or paragraph that answers it.
4. **Word count and citations:** the word count against the target; whether citations and References match both ways; and "Changes from the plan," which names every source or section that differs from the approved plan, or says "None."
5. **Language check:** as `language.md` describes it.
6. **Understanding check:** three short questions a classmate or the instructor could ask about this assignment. The user should be able to answer them without looking.
7. **Before you submit:** the list described in `evidence-blocks.md`.

**The chat reply**, kept short: present the two files, and name in one or two sentences what the user must act on first, such as an open flag or a criterion that reads Not yet. The check file is not repeated in the chat. If files cannot be created, give the two parts as two clearly separated blocks, headed "Assignment document" and "Check file."
