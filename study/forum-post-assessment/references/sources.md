<!-- Copied from study/shared/sources.md by study/build.py. Edit that file, then run the build again. -->

# Sources

These rules decide what a post may claim and where each claim comes from. Use them to write a post, and to check one.

## Order and authority

- **Course material first**, in this order: the question's wording, this unit's course material, other course material, then outside sources.
- **The course version wins.** Definitions, terms, models, and formulas follow the course material. When another source says something different, the text names the difference, because the grader checks claims against the course material.
- **Every fact has a source.** Any fact that does not come from the course material is outside information, even when it seems widely known: background facts, definitions, numbers, dates, and study findings. It needs an outside source, an in-text citation, and a References entry. Key definitions still come from the course.
- **The user's own experience and opinions need no source.** They get the labels `[MY EXPERIENCE]` and `[MY OPINION]` in the evidence block, never in the post text.

## Outside sources

Use an outside source only when the question asks for one, or when it adds something the course material does not. When the assignment or rubric allows course material only, use none. To use one, find it yourself; the user does not have to:

1. **Search** with web search. Prefer credible open pages: official documentation, standards bodies, government and university sites, and open-access journals.
2. **Open the full page** with web fetch. A search snippet is not enough.
3. **Check that the page is free and open.** The user must be able to read the whole page for free. Pass over a page that fails to load, needs a login, payment, or a subscription, or shows only an abstract or a preview, and pass over private pages such as course forums, shared drives, or intranets. Words like "subscribe to read," "members only," or "sign in to continue" in the fetched text mean a paywall. If the user cannot open the page, neither the user nor the grader can check the claim.
4. **Write only what the page says.** Base each sentence on the fetched text, and add no facts from memory, even true ones. If the page does not support the sentence, change the sentence or find another page.
5. **Cite what you opened.** Take the author, title, and date from what the page shows (see "Web page dates" in `apa7.md`). Cite the DOI URL when the page shows a DOI, and the exact URL you opened when it does not.

If no open page supports a claim, cut the claim or stay within the course material. Add `[SOURCE NEEDED: ...]` only when the post cannot work without the claim. Without web search or web fetch, use no outside sources, and tell the user why. Each outside source gets the flag `[VERIFY]` on its first evidence entry, until the user has opened it.

## Recency (computer science)

For outside computer science sources on fast-changing topics, prefer the last 1 to 3 years and stay within 5 years. Foundational topics (for example algorithms, OOP principles, protocol standards, and digital logic) may use older classic sources. Course material is exempt, and a recency rule in the rubric overrides this one. Judge recency only by the date the page shows, so prefer pages that show one.

## Numbers

Work out statistics and arithmetic with code, or take them from the user's own software output; never in your head. Show the inputs in the evidence block, and add `[CHECK NUMBER: ...]` to anything not yet verified.
