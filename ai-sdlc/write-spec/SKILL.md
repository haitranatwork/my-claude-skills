---
name: write-spec
description: Write spec.md and the API contracts for an epic that already has an approved intent.md, after reading the affected repositories with one subagent per repo. Use whenever the user says "write the spec", "spec this out", "next stage", "move to spec", mentions spec.md or contracts or OpenAPI for an epic, or asks what the API should look like for a scoped requirement. This is stage 2 of the AI-Native SDLC chain and requires intent.md to exist first — if it does not, say so and point to /write-intent instead. Do NOT use for scoping a raw requirement, for per-repo plans, or for tickets.
---

# Write spec.md

`spec.md` is the single product-level specification for an epic. Its contracts
section is the point of the document: it is what lets a backend, web, and
mobile developer start the same day without talking to each other. Everything
else is supporting material.

## Step 0 — Locate the knowledge base, product, and epic

Do this silently. Don't narrate it.

**Repo root:** the `knowledge-base` directory among the session's working
directories — normally `<workspace>/knowledge-base`. If it is not in the
session, stop and tell the user to restart Claude Code with
`claude --add-dir <path>\knowledge-base`. Do not guess a path, and do not
proceed by writing artifacts somewhere else.

**Product:** one directory under `<kb>/products/` means use it silently.
Several means take it from `$ARGUMENTS` or ask.

**Epic:** take the slug from `$ARGUMENTS`. If absent, list the epic folders
under `<kb>/products/<product>/epics/` and ask which one. Never guess from
recency.

**Read context:** `<kb>/context/` (people, capacity, methodology) and
`<kb>/products/<product>/context/` (repositories, api-landscape, conventions).
The instructions below depend on those files. If they are missing, say so
rather than guessing at repo names and team boundaries.

Then read `<kb>/products/<product>/epics/<slug>/intent.md`. If it does not
exist, stop and say the epic needs `/write-intent` first. If its status is
still `draft` and open questions are marked as blocking, say which ones and
ask whether to proceed anyway.

## Phase 1 — Reconnaissance

Dispatch **one subagent per affected repo**, using the repo list in
`intent.md`. Do not read all repos in the main context; they will not fit and
quality degrades as it fills.

Each subagent reports back this and nothing more:

- Existing endpoints, DTOs, and events this change touches
- The conventions actually used in that repo — naming, error shape, pagination,
  auth, versioning — quoting real examples from the code
- Every integration point with the other repos
- Anything already built that makes part of the requirement unnecessary

## Phase 2 — Report, then stop

Show a consolidated findings summary and **stop**. Include:

- Contradictions between repos, where conventions disagree
- Anything in `intent.md` the code says is already solved
- Anything in `intent.md` the code says is harder than assumed
- Whether any `WebAPI` endpoint is in scope, and therefore whether the
  fix-in-place versus move-to-`TitanWebAPI` decision is open

Wait for the user. This stop exists because the reconnaissance regularly
changes the intent, and changing it after the spec is written is expensive.

## Phase 3 — Write

Only after the user approves the findings. Use `assets/spec-template.md`.
Write `spec.md` and the `contracts/` directory in the epic folder.

Rules that matter more than the template:

- **Attribute every claim about existing behaviour to a file path.** If you did
  not read it, say you did not read it.
- **Match conventions found in the code, not conventions you would design.**
  Where repos disagree, present both and ask. Do not pick.
- **Never invent Core behaviour.** If Core is unknown, it goes in Core
  dependencies as an open item, not an assumption dressed as fact.
- **No dates and no estimates**, at any point in this document.
- **List every assumption you made** in its own section, so they can be killed
  individually.

Finish by naming which contracts are firm and which depend on an unanswered
question, then say the next stage is `/write-plan`.
