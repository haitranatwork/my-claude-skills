---
name: implement
description: Implement one unit of a ticket from the knowledge base, commit it, and write a handoff file so any future session can resume cold without re-reading the docs or scanning the repo. Use whenever a developer says "implement WM-123", "continue", "next unit", "keep going", "carry on with the ticket", or asks to pick up where they left off. This is the developer-facing execution skill for the AI-Native SDLC chain and reads tickets.yaml from the knowledge base, not Jira. Do NOT use for planning, writing specs, or generating tickets.
---

# Implement a unit

One invocation does **one unit**, commits it, and writes a handoff. "Continue"
does the next one.

The handoff is what makes this work across sessions, machines, and accounts.
Nothing lives in a chat history or a model's memory — a session three weeks
later on a different account reads the handoff and continues without scanning
anything.

## Step 0 — Locate

**Knowledge base:** the `knowledge-base` directory among the session's working
directories. If it is not there, stop and tell the developer to restart with
`claude --add-dir <path>\knowledge-base`. Do not guess.

**Ticket:** from `$ARGUMENTS` (e.g. `WM-1741`). If no key is given, look for an
in-progress ticket in `epics/*/progress/` whose repo matches the current working
directory. If several, ask. Never guess from recency.

## Step 1 — Cold start

**If `epics/<epic>/handoff/<KEY>.md` exists, read it first and follow it.**

It tells you what was built, what was decided, and — in its "Read these" section
— the exact files to open. Open those and nothing more. Do not scan the repo,
do not re-read the full spec, do not re-derive decisions already recorded.
That section exists so this step costs a few thousand tokens instead of a
context window.

Then read only what the handoff does not already cover: the current unit's
entry in `tickets.yaml`, and the specific contract section it implements.

**If there is no handoff**, this is the first unit. Read `tickets.yaml` (the
ticket, its `ai_context`, its units), the `contracts/` section named in
`ai_context`, `plan.md` for the milestone, `products/<product>/context/` for
conventions, and the repo's `CLAUDE.md`.

## Step 2 — Safety checks

Every time, before writing anything.

**Has the repo moved?** Compare the handoff's `last_commit` against the current
branch. If other commits landed since, say so and re-verify that the files
named in "Read these" still exist and still look as described. A handoff
written against code that has since changed is the main way this goes wrong.

**Is the knowledge base current?** If `kb.lock` is older than the epic's last
commit, say so and ask whether to continue.

**Do the unit's `touches` paths exist?** If files moved since planning, stop.
Report what changed and let the developer decide whether the unit still makes
sense. Do not adapt silently.

**Is the working tree clean?** Uncommitted changes mean something was left
half-done. Report and stop.

## Step 3 — Work one unit

Take the first unit with `status: pending`. Only that one.

Follow the conventions in `products/<product>/context/` and the repo's
`CLAUDE.md`, not the ones you would choose. Honour the ticket's `do_not`.

Verify `done_when` yourself — run the build, run the named test. If it fails,
do not commit. Report and stop.

## Step 4 — Commit

```
<KEY> <unit id>: <goal>

<what changed and why, two or three lines>
```

Commit only. **Never push.** The developer reviews and pushes.

## Step 5 — Write the handoff

Rewrite `epics/<epic>/handoff/<KEY>.md` from `assets/handoff-template.md`.

**Rewrite it, never append.** This file is a briefing, not a log. Completed
units collapse to one line each. Decisions get merged. Anything no longer
relevant comes out. If it passes roughly 200 lines, compact harder — a handoff
too expensive to read is a handoff nobody reads.

Write it for someone with no memory of this session and no access to it. Assume
a different person, on a different machine, three weeks later.

The section that matters most is **"Read these, nothing else"**: the exact file
list the next unit needs, each with one line on why. Getting this right is what
removes the repo scan. Getting it wrong — listing everything, or listing too
little — is the difference between a five-minute resume and a full re-derivation.

Record in **Decisions** anything chosen that is not visible from the code or
stated in the spec. A fresh session cannot tell a deliberate choice from an
accident, and will otherwise re-litigate it or quietly reverse it.

Record in **Ruled out** what was tried and rejected, with the reason. Without
it the next session tries the same thing.

Then update `epics/<epic>/progress/<KEY>.md`: tick the unit, record the commit
hash and date. One file per ticket, so two developers in the same epic never
conflict.

Commit both.

## Step 6 — Report and stop

Say what was done, what the next unit is, and its `context` size so the
developer can judge whether to continue. Then **stop**.

Run more than one unit only if the developer explicitly asked for a number
("do three"). Even then, stop early at any doc-request or failed `done_when`,
and write the handoff before stopping.

## When the plan is wrong

**A contract change is never a code change.** If the OpenAPI contract, a shared
type, or an event shape cannot be implemented as written — stop. Do not adapt
the code to a different shape. Other repos are coding against that contract.

**Write a doc-request, don't fix the docs.** Only the knowledge base owner edits
`spec.md`, `plan.md`, `contracts/`, `context/`, `architecture/`, or `domain/`.
When something there is wrong or missing, create:

```
epics/<epic>/doc-requests/<KEY>-<unit>-<YYYY-MM-DD>.md
```

from `../apply-doc-updates/assets/doc-request-template.md`. Include the
evidence — file path and line — and **the proposed replacement text**. The
owner reviews; they should not have to author it.

Note it in the handoff's Open threads, commit, tell the developer to raise it
with the knowledge base owner, and stop. Do not continue to the next unit on a
contract question.

Progress and handoff files are the exception: developers write those directly.
