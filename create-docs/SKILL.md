---
name: create-docs
description: Generate a CLAUDE.md and a docs/ knowledge base for this repository so Claude can answer questions about architecture, business logic, workflows, and coding conventions. Use whenever the user asks to create, generate, bootstrap, or set up documentation, a knowledge base, CLAUDE.md, or repo docs — including phrases like "document this repo", "create docs", "set up CLAUDE.md", or "help Claude understand this codebase". Always plan first and wait for confirmation before writing files.
---

# Create Docs

Generate a CLAUDE.md plus a docs/ knowledge base for the current repository. This is a two-phase workflow: **plan → confirm → execute**. Never create files before the user confirms the plan.

## Goal

The documentation must help Claude answer questions about:

- **Software architecture** — projects, layers, dependencies, key patterns (e.g. MediatR, EF Core usage)
- **Business logic and domain concepts** — entities, workflows, business rules
- **Workflows** — request lifecycle, background jobs, integrations, deployment
- **Coding conventions** — naming, error handling, testing, PR standards

## Phase 1 — Plan (always do this first)

1. Explore the repository: solution/project structure, entry points, main domains, configuration, tests, and any existing docs.
2. Propose a plan containing:
   - **CLAUDE.md outline** — keep it under ~150 lines: build/test commands, repo map, conventions, pointers into docs/
   - **Proposed docs/ file list** — 1-2 sentences per file describing its content and the questions it answers
   - **Nested CLAUDE.md files** — only if a subfolder genuinely deserves its own (monorepo-style)
   - **Knowledge gaps** — what could NOT be inferred from code (business rules, tribal knowledge); mark these as TODO
3. Note which docs are auto-generatable from code vs. which need user input.
4. Present the plan and **STOP**. Wait for explicit confirmation. The user may approve as-is or request changes (merge files, drop files, add topics).

## Phase 2 — Execute (only after confirmation)

- **CLAUDE.md is an index, not an encyclopedia**: commands, conventions, repo map, and links into docs/. It is read every session, so keep it short.
- **docs/ files are self-contained per topic**, anchored with real file paths and class names (e.g. "see src/Orders/OrderService.cs") so Claude can jump to code.
- **Create docs/README.md as an index** mapping each docs file to the topics/questions it covers.
- **Create docs/code-map.md — a concept-to-code map**: a table with one row per domain concept, pointing at its entry-point file or folder. Columns: Domain concept | Entry point | Notes. Aim for one row per concept (~20-40 rows total), pointing at concepts and folders, NOT method signatures. Do NOT enumerate classes or methods — Claude can grep for symbols; the map is for concepts whose names don't match the code.

  ```markdown
  | Domain concept | Entry point | Notes |
  |---|---|---|
  | Vehicle trade-in valuation | src/Appraisals/AppraisalService.cs | Pricing rules in PricingEngine.cs |
  | Customer sync with OEM | src/Integrations/OemSync/ | Hangfire job, runs nightly |
  ```

- **Create these five standard knowledge files** (in addition to the architecture/workflow docs from the plan):
  - **docs/glossary.md** — domain terminology and abbreviations, especially terms whose meaning differs from code names or industry usage. One line per term. Mostly TODO at generation time; seed it with terms found in code comments, entity names, and UI strings, marked `<!-- VERIFY -->`.
  - **docs/decisions.md** — dated one-paragraph entries explaining WHY non-obvious technical choices were made (library choices, architectural exceptions, deliberate workarounds). Seed with decisions inferable from code (e.g. an unusual pattern used consistently), marked `<!-- VERIFY -->`; leave a TODO asking the user for known history.
  - **docs/gotchas.md** — known traps and do-not rules: operations requiring transactions, shared/legacy tables that must not be altered, external rate limits, ordering constraints. Mostly TODO — ask the user specific questions per area found in code.
  - **docs/data-model.md** — the 10-15 core entities and their relationships in short prose (or a small Mermaid diagram), with file paths to the entity classes. NOT a full schema dump — Claude reads entities/migrations for details.
  - **docs/integrations.md** — external systems table: system | direction | protocol | auth | owning module/path. Include schedules for background sync jobs.
- For business logic **inferred from code**: state what the code does, and flag assumptions with `<!-- VERIFY -->` comments for the user to review.
- Leave **TODO sections** where only the user can supply the answer, each with a specific question.
- Add this section to CLAUDE.md so docs stay in sync:

  ```markdown
  ## Documentation maintenance
  When making changes that affect architecture, business rules, workflows,
  or conventions, update the corresponding file in docs/ in the same
  commit/PR. If unsure which file, check docs/README.md (the index).
  ```

- End with a summary listing all created files and every VERIFY/TODO item in one list, so the user can review in a single pass.

## Rules

- Do NOT write any file during Phase 1.
- Do NOT document trivia (formatting rules already enforced by linters, generated code).
- Prefer a clean working tree before executing, so the update-docs skill has a sane diff baseline afterwards.
