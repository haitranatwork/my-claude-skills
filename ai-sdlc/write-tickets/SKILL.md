---
name: write-tickets
description: Generate tickets.yaml from an epic's milestones — one or more tickets per milestone, each split into small resumable implementation units so a developer can run as many as their context budget allows. Use whenever the user says "write the tickets", "break the milestones into tickets", "generate the backlog", "next stage" after a plan, or mentions tickets.yaml or implementation units. Requires plan.md to exist first. This skill NEVER touches Jira. Do NOT use for scoping, specs, plans, or implementing.
---

# Write tickets.yaml

`tickets.yaml` is the developer's source of truth. It is what `/implement`
reads. Jira is a mirror for company-wide visibility, not the working copy.

## Step 0 — Locate the knowledge base

Do this silently. Don't narrate it.

**Repo root:** the `knowledge-base` directory among the session's working
directories — normally `<workspace>/knowledge-base`. If it is not in the
session, stop and tell the user to restart Claude Code with
`claude --add-dir <path>\knowledge-base`. Do not guess a path, and do not
proceed by writing artifacts somewhere else.

**Product:** one directory under `<kb>/products/` means use it silently.
Several means take it from `$ARGUMENTS` or ask.

**Read context:** `<kb>/products/<product>/context/` — repositories, api-landscape,
conventions. If missing, say so rather than guessing at repo names.

Then read `intent.md`, `spec.md`, `contracts/`, and `plan.md`. If `plan.md`
does not exist, stop and say the epic needs `/write-plan` first.

Write to `epics/<slug>/tickets.yaml` using `assets/tickets-template.yaml`.

## Structure

- **One Epic**, from `intent.md`.
- **One or more tickets per milestone.** Split a milestone when it spans repos
  that different people will own, or when one ticket would exceed roughly eight
  units. Never merge two milestones into one ticket.
- **Each ticket carries an `ai_context` block and a list of units.**
- **Cross-team items become tickets on the DEV project**, never absorbed
  silently into a WM ticket.

## Units — the part that matters most

A unit is one resumable step. A developer runs one, reviews the commit, and
either continues or stops for the day. That only works if every unit obeys one
rule:

> **Every unit must leave the repository compiling, passing its existing
> tests, and safe to commit.**

A unit that ends mid-refactor strands the developer with a context window that
is gone and a branch that does not build. If a piece of work cannot be split
without breaking this rule, make it one larger unit and mark it `context: L` —
do not split it badly.

Each unit needs:

| Field | Purpose |
|---|---|
| `id` | `<TICKET-KEY>-U<n>` |
| `goal` | One sentence, verb-first |
| `touches` | Real file paths, so staleness can be detected later |
| `done_when` | Verifiable without the full feature — compiles, test X passes |
| `context` | S / M / L — how much context window this will need |
| `status` | `pending` |

`context` is what lets a developer plan their session. Estimate it from how
many files must be read and held, not from how much code gets written.

Aim for three to eight units per ticket. One unit means the ticket is a unit.
More than ten means the ticket is a milestone.

**Write U1 assuming nothing.** Every later unit starts from a handoff file
written by the one before it, but the first unit has none — so its `goal` and
`touches` must be specific enough to act on from the ticket alone.

## Acceptance criteria

Inherit the milestone's touchable criteria. Describe behaviour, never
implementation — if a criterion names a class or a file, rewrite it. QC should
be able to read the ticket and test it without opening the spec.

## ai_context

Mandatory on every ticket. It is why this file exists: a developer's agent must
land on the original solution without re-deriving it.

Fill `do_not` with the wrong-but-tempting approach for that specific ticket —
what an agent reading only the surrounding code would reasonably try. If you
cannot name one, leave it empty rather than inventing a generic warning.

## Rules

- **`depends_on` only for genuine blocking.** If most tickets have
  dependencies, the slicing is wrong — stop and say so.
- **T-shirt sizes only. No story points, no sprint assignment.** Those happen in
  refinement with the team.
- **Unknowns become a Spike with a timebox**, not a Story with a guess.
- **Write the file. Do not create anything in Jira.**

## Finish

Total tickets, units per ticket, count per repo, and the critical path. Then
say the file is ready to review, and that `/sync-tickets` mirrors it to Jira
once they are happy.
