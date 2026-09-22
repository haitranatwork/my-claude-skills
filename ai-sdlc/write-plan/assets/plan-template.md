---
epic: <Epic name>
key: <JIRA-KEY>
slug: <epic-slug>
product: <product>
spec: spec.md
status: draft
---

# <Epic name> — plan

## Milestones

### M1 — <name>

- **type:** new-api | api-update | ui-feature | foundation
- **repos:** <repos this milestone touches>
- **touchable:** yes | no
- **depends_on:** <milestones, or none>
- **size:** S | M | L

**Acceptance** — what an end user or QC can verify:

- <observable outcome>

**Proxy** — only when `touchable: no`. What QC can check instead:

- <integration test, endpoint response, log line>

**Work**

| Repo | Work |
|---|---|
| `<repo>` | <what changes here> |

**Test targets**

<Real test projects that exist in these repos.>

**Feature flag**

`<flag name>` — gates <what>.

---

### M2 — <name>

<same shape>

---

## Sequence

| # | Milestone | Touchable | Blocks |
|---|---|---|---|

## Risks

- <What could force a contract change>
