<!-- Copied from study/shared/forum/resource-check.md by study/build.py. Edit that file, then run the build again. -->

# Resource check

Run this before anything else: before reading the rubric, and before a plan, a draft, a review, or an assessment. Every claim must rest on material you have really read, because the grader checks claims and citations against the course material. So if even one item below cannot be opened and read in full, report it and stop.

## What to check

- every file the user uploads or points to, of any type (PDF, Word, PowerPoint, image, and others): course material, the rubric, the instructions, a classmate's post, or a draft sent as a file. Files in a claude.ai Project's knowledge count as uploads;
- every link: readings, web pages, and videos, except the link of a source that has a user's copy (see "The user's copy" below);
- all pasted course material: readings, lecture notes, and slides;
- every reading or video that the discussion question or the instructions name for this task, even if the user did not supply it;
- any extra items your SKILL.md names for its task.

Course material is what the question, the instructions, or the user name as course material. Other sources are outside sources, and they are not part of this check: a web page you find yourself follows the steps in `sources.md`, and an outside source cited in a post you review or grade is checked during that review or assessment.

## The user's copy

A file the user uploads or points to, or text the user pastes, that holds the source itself (such as the textbook, an article, or a page behind a link) is the **user's copy** of that source. At every step, read a source that has a user's copy only in that copy, and stay offline for it: never search the web for it, look up its details online, or open its link, even when the user also gives the link. Check and quote the copy, and take the source's reference details from it. When the reference uses the link, copy it as the user gave it. A copy that stops before the part the task needs fails this check like any other item, and its link is no fallback.

## How to check

Open each item yourself and read all of it, not only the first page. An item passes only after you have opened it: knowing the book, or seeing a search snippet, does not count.

- **Pasted text** passes when it is the reading itself, not only a title, an author name, or a reference entry, and when it runs to the end of the part the task uses. It fails if it stops in the middle of a sentence or before the pages the task names.
- **A file** passes when it opens and every page or slide gives clear, normal text. If its content is shown in the chat, read it there; if only its path is listed, open it with your tools. A page with little or no text may be a scanned image, so look at it as an image; if you still cannot read it, the file fails. For a long file, count the text on each page with a short script, then read closely the pages the task uses. A file also fails if it is empty, damaged, or locked with a password, or if the user mentions it but did not attach it. A Project file that only comes back in pieces fails until the user pastes or uploads the pages the task uses.
- **A link** passes when web fetch returns the full reading. It fails on an error, an empty page, a login page (for example, the course site), a paywall or "subscribe to read" message, an "ask for access" page, only an abstract or a preview, text that stops before the part the task needs, or content that is not the named reading. It also fails when web fetch is not available or will not open the link.
- **A video or audio file** passes only with a full transcript that is pasted, uploaded, or opens as text. You cannot watch or listen, and the title and description of a video are not the video.
- **An image or screenshot** passes when all its text is sharp, complete, and not cut off at the edges.

Missing page numbers alone do not fail an item. The citation rules in `apa7.md` handle them.

## If any item fails, stop

Check every item first. Then report all the problems in one message, so the user can fix everything in one round:

1. The line **Resource check failed. I have not started [the plan / the draft / the review / the assessment].**
2. A table with every item, readable or not: Item (short name and type) | Readable | Problem | What I need. Each failed item gets its exact problem and one clear fix: paste the text with page numbers, upload the file, paste the transcript, or send a link that opens without a login.
3. Any other required input that is missing.
4. The closing line: "Send these, or tell me to leave an item out, and I will check again before I start."

Example table:

| Item | Readable | Problem | What I need |
|---|---|---|---|
| Textbook, Ch. 5 (PDF) | Yes | | |
| Unit 5 lecture video (link) | No | I cannot watch videos, and there is no transcript. | Paste the transcript. |
| Article on TCP, pp. 45-60 (link) | No | The link opens a login page. | Upload the PDF or paste pp. 45-60. |

End the message there. It holds only the report: no rubric notes, plan, outline, or partial work, even from the items that passed. The gap stays open until the user fills it: never from memory, general knowledge, a search snippet, an abstract, or another copy or edition you find yourself. This gate outranks the user's general preference for a finished result over questions.

## After the check

- When the user replies, check the new or fixed items the same way. Start the task only when every item passes. An item the user tells you to leave out drops off the list.
- Check again whenever the user adds or replaces an item later in the chat. Items that already passed in this chat stay passed.
- When every item passes, start your first reply for the task with this line, then carry on with the task in the same reply, up to its first stop:
  `Resource check: all [N] items open and readable ([short names]).`
- If the user sends the inputs and says they will ask for the work later, run the check, report the result, and wait.
