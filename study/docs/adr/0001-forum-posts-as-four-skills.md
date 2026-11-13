# Forum posts are four skills, one per task

Help with discussion forum posts is split into four claude.ai skills: `forum-post-create` (the user's initial post), `forum-post-review` (a review of the user's own initial post), `forum-post-assessment` (grading a classmate's initial post), and `forum-post-reply` (the user's replies, and reviews of replies the user wrote). claude.ai loads a skill's whole SKILL.md on every run, so the original one-skill version made each run carry about 8,900 words for tasks it was not doing; four skills load only their own task, and each description routes one kind of request. The cost is that the skills share most of their rules (see ADR 0002).

## Considered Options

- One skill with modes (the original `forum-post`): every run loads every mode.
- One skill whose SKILL.md only routes, reading one mode's file per run: this also cuts the load, but it was rejected so that each task triggers on its own requests and can be uploaded or changed alone.
