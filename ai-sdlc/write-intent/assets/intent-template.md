---
epic: <Epic name>
key: <JIRA-KEY, or TBD>
slug: <epic-slug>
product: <product>
status: draft
owner: <name>
source: <who this came from, and when>
repos: [<affected code repos>]
---

# <Epic name>

## Problem

<What is wrong today, in the user's terms. No solution language. Two or three
sentences — if it takes more, the epic is probably two epics.>

## Outcome

<What a user can do after this ships that they cannot do now. Observable from
outside the system.>

## In scope

- <Bullet per capability, stated as behaviour>

## Out of scope

- <What a reasonable developer might assume is included but is not, and one
  clause on why. This section earns its place — leave it empty only if the
  interview genuinely surfaced nothing.>

## Affected repositories

| Repo | Why it is involved | Rough size |
|---|---|---|
| <repo> | <specific reason, not "changes needed"> | S / M / L |

## Cross-team dependencies

| What is needed | Which team | Ticket to raise | Blocking |
|---|---|---|---|
| <capability> | <team> | <project> | Yes / No |

<If this table is empty, state explicitly that external-system involvement was
considered and ruled out. An empty table and an unconsidered question look
identical otherwise.>

## Acceptance (product level)

- <How the product owner confirms this is done, without asking a developer>

## Open questions

| Question | Owner | Blocks spec |
|---|---|---|
| <question> | <named person> | Yes / No |

## Notes

<Anything found during scoping that does not fit above — existing work that
overlaps, prior attempts, constraints discovered in the code. Optional.>
