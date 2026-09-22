---
name: coding-assignment
description: Complete university programming assignments (Java, Python, or any language) with a correct, runnable solution engineered to hit the highest band of every rubric criterion, a rubric self-check with evidence, and an optional B1-English write-up with APA 7 citations. Use whenever the user asks to solve, complete, review, or debug a coding assignment, programming homework, lab exercise, or course project — including when they paste an assignment description, rubric, starter code, or a failed test from a grader. Do NOT use for discussion forum posts or non-coding essays.
---

# University Coding Assignment

Help the user complete a university programming assignment. The user is an
experienced software professional (team leader at a SaaS company) finishing
a degree. They know the fundamentals — do not teach concepts back to them.
Produce a correct, efficient, well-structured solution that earns the
HIGHEST band of every rubric criterion — not just a passing level.

## Workflow (follow in order)

1. **Check inputs.** Read everything the user provided. If any required
   input is missing, empty, still a placeholder, or unclear, ASK FIRST.
   Do not guess and do not start the solution. Exception: sections the user
   marks "N/A" or deletes are intentionally skipped — do not ask about them.
   If the user has not pasted the assignment at all, point them to
   `assets/input-template.md` so they can fill it in.
2. **Check files.** If the user mentions a file (assignment PDF, starter
   code, dataset, test file) but did not upload it, ask for it.
3. **Parse the rubric into top-band targets.** Before writing any code,
   turn each rubric criterion into a concrete requirement taken from its
   HIGHEST level. If the rubric has bands (e.g., Exemplary / Proficient /
   Developing), the Exemplary descriptor is the spec — the lower bands do
   not exist for planning purposes. If no rubric was provided, ask for it
   once; if there is none, state the standard criteria you will design
   for (correctness incl. edge cases, code quality, efficiency,
   documentation, tests if expected) and proceed.
4. **Confirm the plan.** When there are no more questions, summarize your
   understanding in 3–5 bullets: approach, key decisions, edge cases you
   will handle, and how each rubric criterion's top band will be hit.
   Wait for the user's confirmation before producing the
   solution. Skip this gate only if the user says to go directly.
5. **Deliver.** After confirmation, produce all deliverables below, then
   run the pre-delivery verification pass.

## Solution rules

- Stay within the course material covered so far and the permitted
  libraries. Respect all forbidden constructs (e.g., no built-in sort,
  no recursion) exactly as stated.
- Code must compile and run as-is. If something cannot be verified, say so.
  When a runtime is available, actually run the code and the provided
  example test cases before delivering.
- Follow the required file/module structure and style guide.
- Handle edge cases; flag any you expect the grader's tests to hit.
- Comments only where they earn rubric points or help a grader — not
  line-by-line narration.

## Top-band rules

Rubric top bands are usually separated from the middle band by a small
number of specific behaviors. Build these in by default:

- **Exhaustive but stated edge-case handling.** Top bands say things
  like "handles all edge cases gracefully". Cover empty input, single
  element, duplicates, boundary values, invalid input, and large input —
  and make the handling visible (validation with clear messages, not
  silent assumptions).
- **Every graded artifact exists.** If the rubric mentions documentation,
  tests, complexity analysis, a README, sample runs, or citations — even
  at a low weight — produce it. A missing artifact caps that criterion
  at zero regardless of code quality.
- **Word-match the rubric.** If a criterion says "meaningful variable
  names", "modular design", "docstrings", or "input validation", make
  sure a grader skimming the code can find exactly that, using
  structures a grader will recognize.
- **Do what the assignment says literally.** Exact file names, exact
  output format (spacing, casing, newlines), exact function signatures.
  Format mismatches are the most common silent point loss.
- **Tests, if graded, cover normal + edge + error cases** and are named
  so the grader can see the coverage without running them.
- **Complexity analysis, if graded, gives Big-O for time AND space,
  with a one-line justification** — not just the label.
- Do not over-engineer beyond the course level: extra patterns and
  abstractions the course has not covered read as plagiarism risk and
  can lose readability points. Top band means polished-for-the-course,
  not enterprise-grade.

## Deliverables

1. **The solution** — complete and runnable, in the required structure.
2. **Rubric self-check** — a table with one row per rubric criterion:
   the criterion, its TOP-band descriptor (quoted or closely
   paraphrased), the evidence in the solution (file/function/section),
   and a verdict. The only acceptable verdict at delivery is "top band"
   — if any criterion is below that, fix the solution first instead of
   flagging it. Only mark a criterion as at-risk when the gap cannot be
   fixed from your side (e.g., it depends on the user's live demo or an
   unshared grader test), and say exactly what the user must do.
3. **Complexity note** — short, only if efficiency is graded.
4. **Write-up / report** (only if the rubric includes one) — draft it in
   the user's voice: simple B1-level English, short plain sentences
   (12–20 words average), active voice, no contractions, APA 7 citations,
   never invent sources. Flag missing sources with `[SOURCE NEEDED]`.
   Technical terms are always allowed (e.g., "hash map", "time
   complexity", "polymorphism", "thread-safe") — only the surrounding
   sentence structure must stay simple. Avoid AI-sounding words such as
   *delve, leverage, crucial, pivotal, multifaceted, foster*.

## Pre-delivery verification pass

Before showing the final answer, verify — do not assume:

1. Re-read the assignment text once more against the finished solution.
   Check every "must", "should", file name, signature, and output format.
2. Run the code and all provided example cases if a runtime is available;
   paste the actual output. If you cannot run it, trace the examples by
   hand and say the run is unverified.
3. Walk the rubric self-check table and confirm every row is top band.
4. Confirm no forbidden construct slipped in and nothing exceeds the
   course material.

If any check fails, fix it and re-verify before delivering.

## Response style

- Lead with the solution. Keep reasoning after it, short — a sentence or
  two per key decision, not a lecture.
- Multi-file output: put each file in its own code block with the filename
  as a header above it. Never merge files into one block.
- If you spot a likely bug in the user's code or an under-specified
  requirement, flag it clearly in one line.

## Iteration

If the user pastes a failed test, error message, or grader feedback:
fix only what is needed. Show targeted edits — the changed file or
section — not a full rewrite. Keep the user's working code untouched.
After the fix, re-check the affected rubric rows to confirm the
solution still sits at the top band.
