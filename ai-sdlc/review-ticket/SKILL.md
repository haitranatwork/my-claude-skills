---
name: review-ticket
description: Review a completed ticket against its acceptance criteria and the epic's contracts before it is handed to QC. Use whenever a developer says "review WM-123", "review this ticket", "check my implementation", "is this ticket done", or asks for a code review on ticket work. Reviews against the spec and the ticket, not general code style. Do NOT use for planning, implementing, or reviewing a single unit mid-ticket.
---

# Review a ticket

Run this when every unit is done, before QC. Not per unit — review overhead
per unit swamps the work, and half-finished code cannot be judged against
acceptance criteria.

**Ideally a different developer than the one who implemented it.** An agent
reviewing its own session's work inherits the same assumptions that produced
it.

## Step 0 — Load

**Knowledge base:** among the session's working directories, or stop and say so.

**Ticket:** from `$ARGUMENTS`. Read from `epics/<epic>/tickets.yaml`:
acceptance criteria, `ai_context`, units.

Also read: `spec.md` and `contracts/`, `progress/<KEY>.md`, `handoff/<KEY>.md`,
the repo's `CLAUDE.md`, and the full diff for the ticket's commits.

The handoff's **Decisions** and **Ruled out** sections matter here. They record
choices that are not visible in the code, so a reviewer who skips them will
flag deliberate decisions as mistakes — and will suggest approaches that were
already tried and rejected.

If any unit is still `pending`, say so and stop. There is nothing to review.

## What to check

This is a scoped review. Four things, in order.

**1. Acceptance criteria, one at a time.** For each criterion: does the code
satisfy it, and how would QC verify it? Name the file and behaviour that proves
it. A criterion you cannot trace to code is a fail, not a maybe.

**2. Contract conformance.** Compare the implementation against
`contracts/openapi.yaml`, the shared types, and the event shapes — field names,
types, nullability, error shapes, status codes. This is the highest-value check
in the whole review: five repos code against these contracts, and a silent
divergence here surfaces as an integration failure weeks later.

**3. The `do_not`.** Did the implementation do the thing the ticket warned
against? This is the most commonly missed, because the wrong approach usually
looks natural in the surrounding code — which is exactly why it was written
down.

**4. Repo conventions.** Against `products/<product>/context/` and the repo's
`CLAUDE.md`. Money formats, error shapes, naming, auth. Not personal style
preference — only conventions that are written down somewhere.

## What not to check

Do not review general code quality, architecture you would have chosen
differently, or style the repo does not enforce. That turns a fifteen-minute
review into an argument and buries the four findings that matter.

If something genuinely concerning falls outside these four, say it once at the
end under "Outside scope" and move on.

## Output

A verdict per acceptance criterion — met, not met, or cannot verify — each with
the file that proves it. Then contract divergences, `do_not` violations, and
convention breaks, each with a file and line.

End with one of: **ready for QC**, **changes needed** (with the specific list),
or **blocked** (with what and why).

If the review finds the contract itself is wrong rather than the code, that is
a doc-request, not a change request. Say so and let the developer raise it.
