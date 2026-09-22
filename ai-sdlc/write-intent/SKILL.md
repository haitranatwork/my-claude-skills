---
name: write-intent
description: Turn a raw requirement into intent.md, the product-level artifact of the AI-Native SDLC Playbook, through a structured interview that pins down scope, out-of-scope, affected repositories, and cross-team dependencies before any planning happens. Use this whenever a new requirement, feature request, or epic arrives and needs to be scoped — including when the user says "new requirement", "scope this", "write the intent", "start an epic", "turn this into an intent", mentions intent.md or the knowledge-base repo, or pastes a requirement from a stakeholder and asks what to do with it. Use it even when the requirement looks small or obvious, because the value is in catching the hidden Core dependency and the unstated scope assumption. Do NOT use for spec.md, plan.md, or ticket generation — those are separate later stages.
---

# Write intent.md

`intent.md` is the single product-level artifact that sits above all code
repositories. One per epic. Everything downstream — `spec.md`, each repo's
`plan.md`, and the tickets — derives from it, so an unexamined assumption here
propagates into every ticket and gets discovered during implementation instead
of during scoping.

The output is a decision record, not a description. The test of a good
`intent.md` is that a developer who reads it cannot reasonably build the wrong
thing, and that the product owner can confirm it is done without asking anyone.

## Step 0 — Locate the knowledge base and the product

Do this silently before anything else. Don't narrate it.

**Repo root:** the `knowledge-base` directory among the session's working
directories — normally `<workspace>/knowledge-base`. If it is not in the
session, stop and tell the user to restart Claude Code with
`claude --add-dir <path>\knowledge-base`. Do not guess a path, and do not
proceed by writing artifacts somewhere else.

**Pick the product.** List the directories under `<kb>/products/`.

- One directory: use it, say nothing.
- Several, and `$ARGUMENTS` names one: use that.
- Several, and nothing names one: make this the first interview question, and
  the only one you ask before reading context.

**Read context, in this order:**

- `<kb>/context/` — org-wide: people, capacity, methodology
- `<kb>/products/<product>/context/` — this product: repositories, API
  landscape, conventions

The questions below depend on those files. If the product context directory is
missing or empty, say so plainly and ask the user to fill it in rather than
guessing at repo names and team boundaries.

## Where the file goes

```
<kb>/products/<product>/epics/<JIRA-KEY>-<epic-slug>/intent.md
```

Example: `products/titan-dms/epics/WM-1638-offline-mode-v1/intent.md`

The Jira key goes first so the folder resolves from a ticket without a lookup.
If the epic doesn't exist in Jira yet, use the slug alone and tell the user to
rename the folder once the key is assigned.

Never write `intent.md` into a code repository, and don't suggest it. These
documents outlive any single repo's lifecycle and belong to the product, not
the codebase. Developers reach them through `kb sync`.

## Workflow

### Phase 1 — Extract before asking

Read the requirement the user provided and extract everything it already
answers. This matters more than it sounds: the user has limited patience for
being asked things they already told you, and a skill that re-asks feels broken.

Then check for existing context:

- Search `<kb>/products/<product>/epics/` for related or superseding epics.
- Read `<kb>/products/<product>/domain/` and `architecture/` for anything
  bearing on this requirement.
- If the affected repos are in the session, look for code that already
  implements part of it.
- Check whether an existing `intent.md` covers this and should be amended
  rather than duplicated.

Present what you extracted as a short summary, then ask only about the genuine
gaps. If the requirement is rich enough to answer most of the checklist, say so
and ask two questions instead of six.

### Phase 2 — Interview

Ask one question at a time. Multiple questions in one message get answered
partially, and the unanswered ones quietly become assumptions.

Work through the checklist, skipping anything Phase 1 resolved.

**1. The user-visible outcome.** Not the feature name. What can a user of this
product do after this ships that they cannot do now? If the answer is phrased
in terms of screens or endpoints, the requirement is still solution language
and needs unwinding.

**2. Explicit out-of-scope.** What might a reasonable developer assume is
included that is not? This section prevents more rework than any other, because
scope creep here usually arrives as an assumption rather than a request.

**3. Affected repositories.** Which of this product's code repos, and why each
one. A repo listed without a stated reason usually means nobody has checked.

**4. External-system involvement.** Does any part of this need a change in a
system another team owns? Read `products/<product>/context/api-landscape.md`
for which systems those are. This is the most important question in the
interview: that work moves on another team's schedule, and absorbing it
silently is how a team ends up owning something it never agreed to own. If the
answer is yes or unclear, it becomes a cross-team dependency with a ticket to
raise on that team's project — never an unstated assumption.

**5. Product-level acceptance.** How does the product owner decide this is
done? If the answer requires asking a developer, it is not product-level
acceptance.

**6. Open questions with named owners.** Every unknown gets a person's name and
a yes/no on whether it blocks. An open question without an owner is not
tracked, it is just noted.

### Phase 3 — Write

Only when the user explicitly says to write it. Until then, keep interviewing
or summarising. Writing early is the main failure mode of this skill: the
document looks finished, the user stops interrogating it, and the assumptions
survive into the tickets.

Use `assets/intent-template.md` exactly. Create the epic directory if it
doesn't exist. Then report, in plain prose:

- Which sections are thin and why
- Which open questions block the spec stage and which do not
- Whether anything found in Phase 1 suggests this epic overlaps existing work

## Push back on these

Each one causes a specific downstream failure.

**Solution language in the requirement.** "Add a status dropdown to the vehicle
screen" is a solution. Ask what problem it solves. A spec built on a solution
inherits whatever was wrong with it.

**Dates or sprint commitments.** `intent.md` carries no dates. Near sprints are
commitment; anything further out is roadmap, and mixing the two in a scoping
document turns an estimate into a promise. `context/capacity.md` has the
calendar hazards worth naming when a requirement arrives with a date attached.

**Scope that quietly assumes the team absorbs another team's work.** See
question 4.

**Requirements that already exist.** If Phase 1 found code or an existing
intent covering part of this, say so before writing. Building against nameable
gaps means confirming the gap is real first.

**"Just make it like X."** Ask which properties of X matter. Usually two of
them do and the rest are incidental.

## What this skill does not do

Stop at `intent.md`. Do not draft the spec, propose an architecture, design API
contracts, estimate, or write tickets — even if the user seems ready and even
if the design feels obvious.

Those stages need the affected repositories read, and reading them is exactly
what has not happened yet. An architecture proposed at intent stage is
guesswork wearing a confident voice, and it anchors everything that follows.

When the intent is written and approved, say that the next stage is `spec.md`,
run at the workspace root with the affected repos added, and stop there.
