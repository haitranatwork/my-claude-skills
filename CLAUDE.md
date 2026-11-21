# my-claude-skills

A personal collection of Claude skills. This file maps the skills the user created here: where each group lives, where it runs, and what it is for. For what one skill does, read the `description` in its `SKILL.md`: that is the source of truth.

| Location | Where it runs | Purpose |
|---|---|---|
| `study/` | claude.ai (uploaded as zips) | University coursework done in the user's own voice |
| `ai-sdlc/` | Claude Code, in a workspace that includes the `knowledge-base` repo | The AI-Native SDLC chain, from a raw requirement to a reviewed ticket |
| `create-docs/`, `update-docs/` | Any code repository | `create-docs` generates a `CLAUDE.md` and a `docs/` knowledge base; `update-docs` syncs them with later code changes |

These folders hold the source. To see or change what a skill does, read and edit its files here: a skill of the same name offered in the session is the installed copy, which can be older.

## `study/`

- **Forum family** (discussion forum posts): `forum-post-create` writes the user's initial post, `forum-post-review` reviews the user's own draft of one, `forum-post-assessment` grades a classmate's initial post, and `forum-post-reply` writes or checks the user's replies to classmates.
- **Assignment family** (written assignments: essay, report, reflection paper, case study): `assignment-create` writes one, and `assignment-review` reviews the user's own draft.
- `coding-assignment`: programming assignments. It is self-contained and outside the build.
- `forum-post/` and `written-assignment/`: the one-skill originals that the two families supersede. Leave them as they are; the user deletes them.

**Workflow.** The user runs a family's skills one after another in one claude.ai chat, and sends each input only once:

- Written assignment: `assignment-create`, then `assignment-review`.
- Discussion forum: `forum-post-create`, then `forum-post-review`, then `forum-post-reply` once per reply, and sometimes `forum-post-assessment`. Each reply answers one post: a classmate's initial post, a classmate's reply to the user's initial post, or a classmate's reply to one of the user's replies.

Each later skill reuses what the user already sent in the chat, and what earlier runs delivered, such as the post file or an earlier reply: see the "Inputs carry over within a chat" paragraph in its Inputs section. When a skill's inputs or deliverables change, update that paragraph in the skills after it in the sequence. A new skill that joins a sequence gets the same paragraph.

**Build.** `study/build.py` builds the family skills. It copies each family's shared rules from `study/shared/<family>/` into each skill's `references/`, checks each `SKILL.md` against claude.ai's upload rules, and writes one zip per skill to `study/dist/` (untracked) for the user to upload. Its `SKILLS` table lists the built skills and the shared files each one gets.

- Edit a rule in `study/shared/<family>/`. In a family skill, every file in `references/` is a copy that the next build overwrites.
- Keep a change made for one family inside that family's folder.
- After changing a family skill or its shared rules, run `python study/build.py` and fix every `problem:` it prints. Add `--check` to verify without writing.

**Vocabulary.** `study/GLOSSARY.md` holds the study terms and the words to avoid. Read it before writing or rewording study skill text.

**Decisions.** `study/docs/adr/` records why the skills are split by task, built by a script, and kept as separate families. Read it before changing that structure.

## `ai-sdlc/`

One skill per stage. Each stage reads what the stage before it wrote into the epic's folder in the knowledge base.

1. `write-intent`: a raw requirement becomes `intent.md`.
2. `write-spec`: `spec.md` and the API `contracts/`.
3. `write-plan`: `plan.md`, an ordered list of milestones.
4. `write-tickets`: `tickets.yaml`, each ticket split into resumable units.
5. `sync-tickets`: mirrors `tickets.yaml` to Jira. User-invoked only.
6. `implement`: one unit per run, ending in a commit and a handoff file.
7. `review-ticket`: reviews a finished ticket before QC.

Beside the chain: `plan-status` reports an epic's progress, and `apply-doc-updates` is how the knowledge base owner applies the doc-requests that developers raise.

## Keeping this map current

When a skill or a group of the user's own is added, renamed, moved, or removed, update this file in the same commit.
