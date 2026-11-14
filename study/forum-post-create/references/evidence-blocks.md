<!-- Copied from study/shared/forum/evidence-blocks.md by study/build.py. Edit that file, then run the build again. -->

# Evidence blocks

An **evidence block** under each paragraph of a draft lets the user check every claim before submitting. The user checks a claim by finding the quoted words in the source with Ctrl+F, so every source in every entry gets a location and an exact quote. A location alone ("opening paragraph," "SMALLINT and INT rows") makes the user read the whole part and guess which words support the sentence.

## What each entry holds

For each sentence, or group of sentences with one idea: the source, the location (page number, or paragraph, section, table, slide, or timestamp), and a direct quote of the smallest part of the source that supports it:
- **A sentence, or part of one:** quote the words that carry the claim, usually one sentence or less.
- **A longer part** (a paragraph, a section, a list, a slide, or a stretch of a transcript): quote its first 5 to 8 words and its last 5 to 8 words with ` ... ` between them, so the user sees exactly where the part starts and ends. Quote a short part whole.
- **A table:** name the table and the row, and quote the row: its first cell ` ... ` the cell with the fact the sentence uses. Quote every row the sentence uses.
- **A figure or image:** quote its caption or the words on it.

## Quote rules

- Each source in an entry gets its own location and quote, so an entry that names two sources has two quotes.
- Copy each quote exactly (see "Exact copying" in `language.md`), so Ctrl+F finds it. The ` ... ` is the only new text inside the quotation marks.
- Quote only from text the user pasted or uploaded (course material, files sent for outside sources, and the posts in a thread) or from the full text you fetched from a link. A search snippet or your memory is never a quote.
- If no words in the source support a sentence, the sentence has no support: change it to say what the source says, find a source that says it, or cut it. Every entry has a quote, except under the web page limit below.
- **Web page limit.** Text you fetch from a link (an outside web page, or course material given only as a link) falls under the copyright rules for web content: you may quote each page only once in the whole reply, in under 15 words. This skill cannot change that. A ` ... ` quote counts as that one quote, so keep both ends short. Put the quote on the entry where the page matters most; if the post text itself quotes the page, that is its one quote. Every other entry for the page gives the URL, an exact location (the heading the page shows plus the paragraph number under it, or the table name and row), and the tag `no quote (web page limit)`. If the user also pasted or uploaded the same material, quote from that copy instead: short quotes from text the user supplied are fine.
- Web sources also give the URL you opened, and the DOI URL when the References entry uses one. The first entry for a web source gives the date exactly as the page shows it, such as `date on page: "Updated March 5, 2024"`, or `date on page: none` for (n.d.), so the user can find it on the page with Ctrl+F.

## Labels and flags

A **label** says where a sentence with no source comes from, and needs no action:
- `[MY EXPERIENCE]`
- `[MY OPINION]`

A **flag** marks something the user must act on before submitting. After a colon, it says in a few words what to fix:
- `[CHECK CITATION: ...]`: a citation detail is missing or unsure;
- `[SOURCE NEEDED: ...]`: no open page supports a claim the post cannot drop;
- `[CHECK NUMBER: ...]`: a number not yet verified;
- `[ADD YOUR EXAMPLE: ...]`: where a personal example goes, such as "After S3";
- `[VERIFY]`: an outside source the user has not opened yet;
- `[INVENTED - NEED TO VERIFY]`: a story written as the user's experience at the user's request (see `personal-examples.md`).

A general fact gets no label. It needs an outside source (see `sources.md`), or `[SOURCE NEEDED: ...]` when no open page supports it.

## Format

S1, S2, and so on are the sentence numbers inside the paragraph:

```
[EVIDENCE]
- S1-S2 (main idea in a few words): Author (Year), p. 12, "exact words that support the claim"
- S3 (main idea): Author (Year), p. 14, para. 2, "first 5 to 8 words of the paragraph ... last 5 to 8 words of the paragraph"
- S4 (main idea): Author A (Year), p. 7, "exact words"; Author B (Year), p. 20, Table 3, INT row, "INT ... the cell with the fact used"
- S5 (main idea): Author (Year), Heading Name section, para. 1, URL, "one quote from this page, under 15 words", date on page: "March 5, 2024" [VERIFY]
- S6 (main idea): Author (Year), Heading Name section, para. 4, URL, no quote (web page limit)
- S7 (main idea): Author (Year), Section Name, "exact words" [CHECK CITATION: no page number in the pasted text]
- S8: [MY EXPERIENCE]
- S9: [MY OPINION]
- After S9: [ADD YOUR EXAMPLE: a time your team had to choose between two tools]
```

## Clean text

The user deletes the evidence blocks and submits what is left. So everything outside the blocks is text the user will submit, from the title to the References list.
- Every label, flag, and note sits in the evidence block under its paragraph, on the entry for the sentence it is about. A flag about a References entry, such as a missing date or publisher, goes on the first entry that cites that source.
- A missing detail leaves no gap mark ("p. ?", "XX") in the text. When a page number is missing, the citation is (Author, Year), and the flag goes in the block.
- A paragraph waiting for `[ADD YOUR EXAMPLE]` still reads well before the example is added.
- Each block starts with the line `[EVIDENCE]`, has a blank line before and after it, and holds only its entries, so the user can delete it in one step.
- Deliver one version: the draft with its evidence blocks, and no clean copy. Word counts and language checks cover the text only, never the blocks.

## Sources in the plan

The plan lists every source the draft will cite. The evidence blocks need exact quotes, and a quote needs the source text in the chat: a file the user sends can be quoted in full, but a page that was only fetched gets one short quote. The list also lets the user drop or swap a source before any draft exists. When the draft will cite no source, the plan says so.

1. **Build the list.** Pick the course material the draft will use. If it also needs outside sources (see `sources.md` for when), find them now: search, open the full page, check that it is free, and check that it supports the point. List only sources you have opened. Check that the list meets the citation minimum.
2. **Show it in two parts,** **Course material** and **Outside sources**. For each source give:
   - the full APA 7 reference as it will appear in References, with the DOI URL when the source has a DOI (see `apa7.md`);
   - one line on what the draft uses it for;
   - its status: **In the chat** (pasted or uploaded, so it can be quoted) or **Need file** (a link only, or a page that was only fetched), naming any missing detail such as the year, the DOI, or page numbers.
   An empty part says "None" and why, for example that the assignment allows course material only.
3. **Ask** the user to confirm that they can open every source, and to send the file or text for every source marked **Need file**: a PDF, a Word file, or pasted text with page numbers. Say that with the file, the evidence blocks quote the exact words, and without it a fetched page gets only one short quote.

When the user replies, open each new file and check that it is the listed source (same title, authors, and year) and that it reads clearly (see `resource-check.md`). If a file fails, say so in one line and ask for another copy. If the user cannot open a source, replace it or cut the claim, and show the changed entries again before drafting. A source still marked **Need file** after the reply follows the web page limit. From then on, cite only the listed sources. If the draft cannot work without another source, add it and say so at the top of the reply.

If the user says to write directly, skip the plan. Entries for pages without a file then follow the web page limit.

## Before you submit

Close the output of every draft with this list, so nothing unchecked reaches the submission. Give the location of each item (for example, paragraph 3, S2) so the user finds it fast:
- each outside source to open (`[VERIFY]`): check that the page opens for free, says what the sentence claims, and shows the date used;
- each entry tagged `no quote (web page limit)`: open the page, find the part by its location, and check it. To get quotes for these entries, the user can paste the page text or upload the page as a PDF and ask for the evidence again;
- each `[INVENTED - NEED TO VERIFY]` story: keep it only if it matches what really happened, with the details fixed; otherwise replace it or cut it;
- every other open flag, with what to fix: `[CHECK CITATION]`, `[SOURCE NEEDED]`, `[CHECK NUMBER]`, and `[ADD YOUR EXAMPLE]` (with its story ideas, when the plan was skipped);
- the last step: delete every evidence block. When the items above are done, what is left is ready to submit.
