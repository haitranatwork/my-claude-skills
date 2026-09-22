---
ticket: <KEY>
epic: <epic-slug>
milestone: M1
repo: <repo>
branch: <branch>
last_unit: <KEY>-U3
last_commit: <hash>
next_unit: <KEY>-U4
updated: <YYYY-MM-DD>
---

# <KEY> — handoff

Written for a session with no memory of this work. Read this, open the files in
"Read these", and continue. Do not scan the repo.

## Where this is

<Two or three sentences. What the ticket builds, what is done, what is next.>

## Read these, nothing else

| File | Why |
|---|---|
| `<repo>/<path>` | <what it is and why the next unit needs it> |
| `epics/<slug>/spec.md#<anchor>` | <the contract section being implemented> |

<Everything the next unit needs, and nothing it does not. Too long and this
file costs as much as scanning; too short and the next session re-derives.>

## Built so far

<One or two lines per completed unit. The shape of what exists, not a diff.>

- U1 — <what it produced, and where>
- U2 — <what it produced, and where; note anything deliberately left out>

## Decisions

<Choices made that are not visible in the code and not stated in the spec. A
fresh session cannot tell a deliberate choice from an accident.>

- <decision, and the reason>

## Ruled out

<What was tried and rejected, with why. Without this the next session tries it
again.>

- <approach> — rejected because <reason>

## Open threads

<Work deliberately deferred, unanswered questions, raised doc-requests.>

- <thread, and which unit picks it up>

## Environment

<Anything non-obvious about building or testing this repo that was discovered
the hard way.>

- <command, dependency, or gotcha>
