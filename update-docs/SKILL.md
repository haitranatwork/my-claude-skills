---
name: update-docs
description: Sync CLAUDE.md and the docs/ knowledge base with code changes since the last documentation update. Use whenever the user asks to update docs, refresh documentation, sync docs with recent commits, check if docs are stale, or after merging changes — including phrases like "update the docs", "are the docs up to date", "sync documentation with the latest commits", or when the user names a specific commit range or PR to document.
---

# Update Docs

Detect code changes since the last documentation sync and update CLAUDE.md / docs/ accordingly. This is a two-phase workflow: **propose → confirm → apply**. Never modify docs before the user confirms.

## Step 1 — Find the baseline

Determine the last commit where docs were in sync, in this priority order:

1. **User-specified range**: if the user names a commit, tag, or PR (e.g. "diff from abc1234", "only PR #456"), use that and skip auto-detection.
2. **Marker file**: if `docs/.last-sync` exists, read the commit hash from it.
3. **Fallback**: last commit that touched docs/:

   ```bash
   git log --oneline -1 -- docs/ CLAUDE.md
   ```

## Step 2 — Collect changes since the baseline

```bash
git diff <baseline>..HEAD --stat -- ':!docs' ':!CLAUDE.md'
git log --oneline <baseline>..HEAD -- ':!docs' ':!CLAUDE.md'
```

If there are no changes, tell the user the docs are already up to date and stop.

## Step 3 — Assess staleness

For each changed area, check whether the relevant docs/ file or CLAUDE.md is now stale. Look for:

- Renamed/moved/deleted classes, projects, or files that docs reference by path
- Changed workflows, request pipelines, background jobs
- New or removed endpoints, integrations, configuration keys
- New projects/modules with no corresponding doc
- Changed build/test commands or conventions in CLAUDE.md
- **Stale paths in docs/code-map.md**: verify every entry-point path in the table still exists (`ls` or `git ls-files`); fix moved/renamed paths and add rows for new domain concepts introduced since the baseline
- **docs/data-model.md**: new/removed/renamed core entities or changed relationships (check changes under entity/domain folders and migrations)
- **docs/integrations.md**: new or removed external integrations, changed protocols/auth, changed job schedules
- **docs/decisions.md**: if the diff shows a significant new technical choice (new library, new pattern, architectural exception), propose a dated entry and ask the user to confirm the reasoning
- **docs/glossary.md / docs/gotchas.md**: only flag if changed code contradicts an existing entry; never invent new gotchas from the diff alone — ask the user instead

Ignore trivial changes: formatting, minor refactors that don't change behavior or structure, dependency bumps without API impact.

## Step 4 — Propose, then apply

1. Present a list of proposed doc updates: which file, what changes, and which commits caused them. **STOP and wait for confirmation.**
2. After confirmation, apply the updates.
3. For newly inferred business logic, flag assumptions with `<!-- VERIFY -->` comments, same as initial generation.
4. Update `docs/README.md` (the index) if files were added or removed.
5. Write the current HEAD hash to `docs/.last-sync`:

   ```bash
   git rev-parse HEAD > docs/.last-sync
   ```

6. Include `docs/.last-sync` in the same commit as the doc updates, so the baseline only advances on a real sync.

## Notes

- The `.last-sync` marker makes the baseline robust against typo-fix commits in docs/ that would otherwise skip undocumented code changes.
- If `docs/` does not exist at all, tell the user to run the create-docs skill first.
