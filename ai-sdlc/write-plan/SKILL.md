---
name: write-plan
description: Write plan.md for an epic that already has spec.md and contracts — an ordered list of milestones, each one a deliverable slice with acceptance criteria an end user or QC can actually touch. Use whenever the user says "write the plan", "plan this", "break it into milestones", "next stage" after a spec, or mentions plan.md or milestones for an epic. This is stage 3 of the AI-Native SDLC chain and requires spec.md to exist first. Do NOT use for scoping a requirement, writing the spec, generating tickets, or implementing anything.
---

# Write plan.md

One plan per epic. It splits the work into **milestones** — deliverable slices,
each one becoming one or more tickets. A milestone is not a repo and not a
layer: it is a thing that can be finished and looked at.

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

Then read `epics/<slug>/spec.md` and `contracts/`. If `spec.md` does not
exist, stop and say the epic needs `/write-spec` first.

Write to `epics/<slug>/plan.md` using `assets/plan-template.md`.

## Milestone types

| Type | Example |
|---|---|
| `new-api` | A new endpoint and its contract |
| `api-update` | Changing an existing endpoint |
| `ui-feature` | One feature, or a coherent set, in web or mobile |
| `foundation` | Schema, shared types, infrastructure |

A milestone spans whatever repos it needs. Group the work by repo **inside**
the milestone — do not make a milestone per repo, because then nothing is ever
finished until all of them are.

## Touchable acceptance is the rule

Every milestone's acceptance criteria should describe something an end user or
QC can **see, click, or verify for themselves**. Write them that way by
default.

When a milestone genuinely cannot be touched — a schema migration, a shared
type — it still needs a **proxy** QC can check: an integration test they can
run, an endpoint returning the new field, a log line, a health check. Never
leave a milestone with no verifiable outcome at all.

Two planning smells to raise rather than write around:

- **Three untouchable milestones in a row.** Stakeholders see nothing for weeks.
  Re-slice so a touchable one lands between them.
- **A milestone nobody can demo.** If you cannot write a sentence starting
  "after this, you can see…", it is not a milestone, it is a task inside one.

## Ordering

Order by dependency, then by how early something becomes touchable. The
contracts milestone comes first — it is what lets the other repos proceed in
parallel.

Mark dependencies between milestones explicitly. If most milestones depend on
most others, the slicing is wrong: say so instead of encoding it.

## Constraints

- **Reference real files** that exist in the repos. A plan naming files that
  are not there reads as researched and is worse than a gap.
- **Name real test projects** that exist, not ones you would create.
- **Assume the team as it is** — five full-stack developers, one mobile
  developer, one designer, two QC. Singleton roles mean a milestone needing
  both the designer and the mobile developer at once is a scheduling risk worth
  flagging.
- **No dates, no story points.** Sizes are S/M/L only.
- **No implementation code.**

## Finish

A table: milestone, type, repos, touchable yes/no, size, what blocks it. Then
say the next stage is `/write-tickets`.

If a milestone surfaced something that contradicts the spec — a contract that
cannot be implemented as written — raise it before the table. That is a signal
to revise `spec.md`, not to plan around it.
