# Each family of study skills has its own shared rules

Written assignments are two claude.ai skills, `assignment-create` and `assignment-review`, split by task for the same reason as the forum skills (ADR 0001). Their shared rules live in `study/shared/assignment/`, the forum skills' rules moved to `study/shared/forum/`, and `study/build.py` copies into each skill only from its own family's folder. Assignment rules differ from forum rules in several places (tone, structure, APA 7 headings, the default standard), and with the families kept apart, a change made for one family never changes the other family's zips, so nothing has to be uploaded or tested again.

## Considered Options

- One set of files worded for both posts and assignments: no rule would live twice, but every assignment change would rewrite the forum skills' copies, and all four forum zips would need another upload.
- A third folder for the rules both families use: the common rules would have to be cut out of the forum files, which changes the forum skills for the sake of the assignment skills.

## Consequences

- Rules that are the same for posts and assignments (the resource check, sources, evidence blocks, personal examples, most of APA 7) live twice. A fix that applies to both families is made in both folders. The two folders use the same file names, so a file can be compared with its partner.
- This replaces the last consequence in ADR 0002: `written-assignment` did not join the forum skills' rules. It was split into two skills with a folder of their own.
