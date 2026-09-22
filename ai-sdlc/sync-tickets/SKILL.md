---
name: sync-tickets
description: Push a reviewed tickets.yaml into Jira via the Atlassian MCP server, then write the assigned keys back into the file. Run only when the user explicitly invokes it — this skill creates real issues in a real backlog. Requires an existing tickets.yaml from /write-tickets and a connected Atlassian MCP server.
disable-model-invocation: true
---

# Sync tickets.yaml to Jira

This skill has side effects in a shared backlog that other people are working
from. Everything below is built around making a mistake recoverable and a rerun
harmless.

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

Then read `epics/<slug>/tickets.yaml`. If it does not exist, stop and point to
`/write-tickets`.

Confirm the Atlassian MCP server is connected before doing anything else. If it
is not, say so and stop — do not fall back to describing what you would have
created.

## Idempotency

Every ticket in the file has a `key` field, null until it exists in Jira.

- `key: null` → create it, then write the assigned key back into the file.
- `key` present → the ticket already exists. Do not create it again. Compare
  the file against Jira and report differences; do not silently update.

This is what makes rerunning safe. An epic's tickets get regenerated whenever
the spec changes, and the second run must not duplicate the first.

## Sequence

**1. Dry run.** Before creating anything, show what will happen: how many
issues, of what types, in which projects, with which parent links and which
dependency links. Show the epic and the Contracts story explicitly, since
everything else hangs off them. Then stop and wait.

**2. Create in dependency order.** Epic first. Then the Contracts story. Then
the remaining sub-tickets. A ticket whose `depends_on` target does not exist
yet is a signal to stop, not to skip the link.

**3. Link.** Apply `depends_on` as Jira issue links after all issues exist.

**4. Write back.** Update `tickets.yaml` with every assigned key. Do this even
if a later step failed — an unrecorded created ticket is the one failure mode
that makes the next run duplicate work.

**5. Report.** Every key created, grouped by repo, plus anything that failed and
why.

## Do not

- **Do not assign a sprint or story points.** Those belong to refinement with
  the team.
- **Do not transition status.** Everything lands in the default state.
- **Do not create anything not in the file.** If a ticket seems obviously
  missing, say so after the run and let the user regenerate the file.
- **Do not proceed past a failure.** Stop, report what exists so far, and let
  the user decide. A half-created epic that reports success is worse than one
  that stops loudly.
