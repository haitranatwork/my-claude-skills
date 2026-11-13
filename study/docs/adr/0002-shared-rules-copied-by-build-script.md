# Shared study rules are copied into each skill by a build script

claude.ai loads each uploaded skill on its own, so a skill cannot rely on another skill's files. Rules that several study skills use (the resource check, language and voice, APA 7, sources, rubric reading, evidence blocks, personal examples) live once in `study/shared/`, and `study/build.py` copies the files each skill needs into its `references/` folder and writes one zip per skill to `study/dist/` for upload. The copies are committed so every skill folder is complete, but they are never edited by hand: each starts with a line naming its source, and the next build overwrites it.

## Considered Options

- Hand-made copies in each skill: this is how `forum-post` and `written-assignment` drifted apart (an average sentence length of 12 to 18 words in one and 12 to 20 in the other; language checks at 20 and 25 words).
- A fifth skill holding the shared rules: the four skills would then depend on Claude loading a second skill, so they would no longer work on their own.

## Consequences

- Run the build before every upload. A hand edit to a copied file is lost on the next build.
- `written-assignment` can adopt the shared rules later by adding its name to the build script.
