---
name: publish-from-warehouse
description: Publish a pre-written PMP scenario from pmp_questions_pack.md to the live Astro content collection. Use when the user wants to move a warehouse scenario to the blog.
paths:
  - "pmp_questions_pack.md"
  - "src/content/pmp-questions/**"
---

# Publish from Warehouse

## When to use

- User asks to publish a scenario from the warehouse pack
- User references `pmp_questions_pack.md` or `agent_output.txt`
- User wants to promote a draft scenario to the live site

## Source file

`pmp_questions_pack.md` is a private staging area. The live site only reads from `src/content/pmp-questions/`.

## Conversion steps

1. Read the selected scenario from `pmp_questions_pack.md`
2. Strip any `token-handoff` code blocks and `READY_FOR_EXECUTION` markers
3. Transform the raw scenario into the full canonical format (see `write-pmp-question` skill):
   - Add missing frontmatter fields (`pubDate`, `topic`, `correctAnswer`, `slug`)
   - Restructure body into **The Scenario**, **Options**, and **Explanation & Analysis** sections
   - Assign a correct answer and write a robust explanation if not already present
4. Write the finished file to `src/content/pmp-questions/YYYY-MM-DD-topic-slug.md`
5. Run `npm run build` to validate
6. Commit and open a PR

## Notes

- The legacy `watch_agent.py` listener is optional; prefer writing directly to `src/content/pmp-questions/` in Cloud Agent runs
- Do not delete scenarios from the warehouse unless the user explicitly asks
