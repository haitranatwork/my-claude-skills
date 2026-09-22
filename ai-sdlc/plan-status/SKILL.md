---
name: plan-status
description: Report progress across a whole epic — milestones, tickets, units done, what is blocked, and which doc-requests are waiting. Use whenever the user asks "where are we", "what's the status", "how is the epic going", "progress on WM-1740", "what's blocked", or asks for a rollup before sprint planning or a status report. Reads the knowledge base, not Jira. Do NOT use for planning, implementing, or reviewing.
---

# Report plan status

Reads the plan and every progress file and renders one picture. The knowledge
base is the source of truth; Jira is the mirror.

## Step 0 — Load

**Knowledge base:** among the session's working directories, or stop and say so.

**Epic:** from `$ARGUMENTS`. If absent, list the epic folders under
`products/<product>/epics/` and ask which — or, if the user asked about
everything, report across all epics with at least one progress file.

Read `plan.md`, `tickets.yaml`, every file in `progress/`, and every file in
`doc-requests/`.

Do **not** read `handoff/`. Those files are implementation briefings for
`/implement`, and pulling them into a rollup costs a great deal for information
this report does not use. The one exception is checking whether a handoff's
`last_commit` is still in the branch history — read the front matter only.

## Output

**Rollup first.** Milestones complete out of total, tickets complete out of
total, units complete out of total. Three numbers, one line.

**Then milestones**, in plan order:

| Milestone | Type | Touchable | Tickets | Units | State |
|---|---|---|---|---|---|

State is one of: not started, in progress, complete, blocked.

**Then attention items**, which is the part that earns the report:

- **Blocked** — what, why, and who can unblock it
- **Pending doc-requests** — each one is a developer waiting, or working around
  something wrong
- **Stale** — a ticket in progress whose last commit is more than five working
  days old. Usually means the developer moved to something else and nobody
  said so
- **Orphaned handoffs** — a handoff whose `last_commit` is no longer in the
  branch history, meaning the branch was rebased or force-pushed. The next
  `/implement` on that ticket will be working from a description of code that
  no longer exists
- **Contract questions** — any doc-request touching `contracts/`, called out
  separately because these block more than one repo

**Then what is demoable.** Which completed milestones have touchable acceptance
criteria that QC or a stakeholder could see today. This is the number Robert
actually wants.

## Rules

- **Report what the files say.** If a progress file is stale or contradicts a
  commit history, report the discrepancy rather than resolving it silently.
- **No estimates, no completion dates.** Units done out of units planned is a
  measurement. Extrapolating it into a date is not.
- **Do not update Jira.** This skill reads. `/sync-tickets` writes.
