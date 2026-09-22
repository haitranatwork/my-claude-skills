---
name: apply-doc-updates
description: Review and apply pending doc-requests that developers raised during implementation — proposed corrections to spec.md, contracts, plan.md, or the context and architecture docs. Use whenever the user says "apply doc updates", "any doc requests", "process the doc requests", "what did the developers flag", or asks to review proposed knowledge base corrections. Only the knowledge base owner runs this. Do NOT use for implementing or for writing new artifacts.
---

# Apply doc-requests

Developers write doc-requests when implementation reveals the knowledge base is
wrong. They never edit the authored documents themselves. This skill is how
those corrections get reviewed and applied.

Every change is approved individually. Batch approval defeats the point of
single-owner control.

## Step 0 — Load

**Knowledge base:** among the session's working directories, or stop and say so.

Find every file under `products/*/epics/*/doc-requests/` without an
`applied:` field in its front matter. If none, say so and stop.

## For each request, in order

Oldest first — a stale correction can be superseded by a later one, and applying
them out of order reintroduces the old text.

Present four things together, so the decision can be made without opening
files:

1. **What the developer claims is wrong**, and which KB file
2. **The evidence** — the file path and line in the code they found it in
3. **The current KB text**, quoted exactly
4. **The proposed replacement**, quoted exactly

Then ask: apply, edit, or skip. Wait.

- **Apply** — write it, then mark the request applied.
- **Edit** — take the owner's wording, not the developer's. Apply that.
- **Skip** — leave the request unapplied and record why in the request file.
  A skipped request is a decision, and the next person to read it should see
  the reasoning rather than raise it again.

## Marking applied

Add to the request's front matter:

```yaml
applied: 2026-09-16
applied_by: <owner>
outcome: applied | edited | skipped
note: <one line, required when skipped or edited>
```

Never delete a request. The history of what was wrong and what was decided is
worth more than a tidy folder.

## Contract changes are different

A request touching `contracts/` — OpenAPI, shared types, event shapes — affects
every repo coding against it. Before applying one:

- Say which repos and which tickets are working against the current contract
- Check `progress/` for tickets already in progress that would be invalidated
- Say plainly that applying it means notifying those developers

Then ask separately whether to apply. A contract change made quietly is how five
repos end up implementing three different versions of the same interface.

## Finish

List what was applied, edited, and skipped. Flag anything that needs a
downstream action: a ticket to regenerate, a developer to notify, a spec
section now inconsistent with a contract.

If any applied change alters `spec.md` or `plan.md` materially, say that
`/write-tickets` should be rerun for that epic — it is idempotent on tickets
that already have keys, so regenerating is safe.
