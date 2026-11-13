"""Build the study skills for claude.ai.

Shared rules live once in study/shared/. This script copies the files each
skill needs into that skill's references/ folder, checks each SKILL.md
against claude.ai's upload rules, and writes one zip per skill to study/dist/.
Never edit a copied file: the next build overwrites it. Edit the file in
study/shared/ and run the build again (see study/docs/adr/0002).

Usage:
    python study/build.py           copy the shared files, then write study/dist/<skill>.zip
    python study/build.py --check   change nothing; exit 1 if a copy is missing,
                                    out of date, or stale, or a SKILL.md breaks the upload rules
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

STUDY = Path(__file__).resolve().parent
SHARED = STUDY / "shared"
DIST = STUDY / "dist"

# The shared files each skill gets, copied into <skill>/references/.
# A rule that only one skill uses lives in that skill, not here.
SKILLS = {
    "forum-post-create": [
        "resource-check.md", "rubric.md", "strong-post.md", "top-band-standard.md",
        "sources.md", "evidence-blocks.md", "personal-examples.md",
        "language.md", "voice-sample.md", "apa7.md",
    ],
    "forum-post-review": [
        "resource-check.md", "rubric.md", "strong-post.md", "top-band-standard.md",
        "language.md", "voice-sample.md", "apa7.md", "sources.md",
    ],
    "forum-post-assessment": [
        "resource-check.md", "rubric.md", "strong-post.md", "top-band-standard.md",
        "apa7.md", "sources.md", "language.md", "voice-sample.md",
    ],
    "forum-post-reply": [
        "resource-check.md", "sources.md", "evidence-blocks.md", "personal-examples.md",
        "language.md", "voice-sample.md", "apa7.md",
    ],
}

COPY_MARK = "<!-- Copied from study/shared/"
HEADER = COPY_MARK + "{name} by study/build.py. Edit that file, then run the build again. -->\n\n"

# Upload rules from the claude.ai Help Center article "How to create custom Skills".
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 200

SKIP_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}


def read(path):
    # Universal newlines, so a CRLF checkout compares equal to an LF build.
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def is_copy(path):
    try:
        return read(path).startswith(COPY_MARK)
    except (OSError, UnicodeDecodeError):
        return False


def frontmatter_problems(skill):
    skill_md = STUDY / skill / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill}/SKILL.md is missing"]
    match = re.match(r"---\n(.*?)\n---\n", read(skill_md), re.DOTALL)
    if not match:
        return [f"{skill}/SKILL.md has no frontmatter block"]

    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()

    problems = []
    name = fields.get("name", "").strip("\"'")
    if name != skill:
        problems.append(f"{skill}: name '{name}' must match the folder name")
    if not NAME_PATTERN.match(name) or len(name) > NAME_MAX:
        problems.append(
            f"{skill}: name must be lowercase letters, digits, and single hyphens, "
            f"at most {NAME_MAX} characters"
        )

    raw = fields.get("description", "")
    quoted = len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'"
    description = raw[1:-1] if quoted else raw
    if not description:
        problems.append(f"{skill}: description is missing")
    if len(description) > DESCRIPTION_MAX:
        problems.append(
            f"{skill}: description is {len(description)} characters; "
            f"claude.ai allows {DESCRIPTION_MAX}"
        )
    if "<" in description or ">" in description:
        problems.append(f"{skill}: description must not contain < or >")
    if not quoted and (": " in description or " #" in description):
        problems.append(f"{skill}: put the description in quotes, because it contains ': ' or ' #'")
    return problems


def reference_problems(skill, names):
    """Every shared rule file or references/ or assets/ path a skill's text names must ship inside that skill."""
    skill_dir = STUDY / skill
    shared_names = {path.name for path in SHARED.glob("*.md")}
    sources = [skill_dir / "SKILL.md"] + [SHARED / name for name in names]
    sources += sorted((skill_dir / "assets").glob("*.md"))
    problems = []
    for source in sources:
        if not source.is_file():
            continue
        for target in sorted(set(re.findall(r"`([\w./-]+\.md)`", read(source)))):
            if target not in shared_names and not target.startswith(("references/", "assets/")):
                continue  # an example file name, such as an output file, not a pointer
            candidates = [skill_dir / target, skill_dir / "references" / target]
            shipped = target in names or any(c.is_file() for c in candidates)
            if not shipped:
                problems.append(f"{skill}: {source.name} points to {target}, which the skill does not ship")
    return problems


def sync(check):
    """Bring every skill's copies in line with study/shared/. Return the problems found."""
    problems = []
    for skill, names in SKILLS.items():
        problems += frontmatter_problems(skill)
        problems += reference_problems(skill, names)
        refs = STUDY / skill / "references"
        for name in names:
            source = SHARED / name
            if not source.is_file():
                problems.append(f"study/shared/{name} is missing")
                continue
            target = refs / name
            expected = HEADER.format(name=name) + read(source)
            current = read(target) if target.is_file() else None
            if current == expected:
                continue
            if check:
                state = "missing" if current is None else "out of date"
                problems.append(f"{skill}/references/{name} is {state}")
            else:
                write(target, expected)
                print(f"copied   {skill}/references/{name}")
        # A copy of a shared file the skill no longer uses is stale.
        if refs.is_dir():
            for path in sorted(refs.iterdir()):
                if path.is_file() and path.name not in names and is_copy(path):
                    if check:
                        problems.append(f"{skill}/references/{path.name} is a stale copy")
                    else:
                        path.unlink()
                        print(f"removed  {skill}/references/{path.name}")
    return problems


def package():
    """Write study/dist/<skill>.zip with the skill folder at the root of the zip."""
    DIST.mkdir(exist_ok=True)
    for skill in SKILLS:
        zip_path = DIST / f"{skill}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted((STUDY / skill).rglob("*")):
                if path.is_file() and path.name not in SKIP_FILES:
                    zf.write(path, path.relative_to(STUDY).as_posix())
        print(f"zipped   study/dist/{zip_path.name}")


def main():
    parser = argparse.ArgumentParser(description="Build the study skills for claude.ai.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="change nothing; exit 1 if a copy is missing, out of date, or stale, "
        "or a SKILL.md breaks the upload rules",
    )
    args = parser.parse_args()

    problems = sync(args.check)
    if problems:
        for problem in problems:
            print(f"problem: {problem}", file=sys.stderr)
        return 1
    if args.check:
        print("All skills are up to date.")
        return 0
    package()
    return 0


if __name__ == "__main__":
    sys.exit(main())
