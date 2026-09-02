---
name: write-pmp-question
description: Create or update a PMP situational question post for noteskeep.com. Use when drafting new questions, publishing content, or when an automation asks for a new blog entry.
paths:
  - "src/content/pmp-questions/**"
  - "pmp_questions_pack.md"
---

# Write PMP Question

## When to use

- User asks to add, draft, or publish a PMP question
- Automation runs that need fresh blog content
- Converting a scenario from `pmp_questions_pack.md` into a live post

## Canonical example

Read `src/content/pmp-questions/2026-06-07-regulatory-stakeholder-power-shift.md` before writing. Match its structure exactly.

## Content requirements

Each question must include:

1. **Frontmatter** (YAML between `---` delimiters)
2. **The Scenario** — situational paragraph ending with a clear question
3. **Options** — exactly 4 choices labeled A–D
4. **Explanation & Analysis** — core takeaway plus detailed breakdown of why the correct answer wins and why distractors fail

### Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `title` | string | Descriptive, includes "Situational PMP Question" when appropriate |
| `pubDate` | date | `YYYY-MM-DD` format |
| `topic` | string | Short topic label shown on the homepage |
| `category` | string | PMI domain (e.g. Stakeholder, Scope Management, Risk) |
| `difficulty` | number | 1–5 scale |
| `correctAnswer` | string | Single letter: A, B, C, or D |
| `slug` | string | `YYYY-MM-DD-kebab-case-topic` |

Optional: `tags` (array of strings), `description` (string).

### Filename convention

Save to `src/content/pmp-questions/YYYY-MM-DD-topic-slug.md` where the date prefix matches `pubDate` and `slug`.

## Writing guidelines

- Ground scenarios in realistic project management situations aligned with PMI standards
- Write 3 highly plausible distractors — not obviously wrong answers
- Explanation must be educational: teach the underlying PMI principle, not just state the answer
- Do not include `token-handoff` blocks or `READY_FOR_EXECUTION` markers in published files

## Workflow

1. Scan `src/content/pmp-questions/` to avoid duplicate topics
2. Draft the markdown file at the correct path
3. Run `npm run build` and fix any content schema or syntax errors
4. Commit with message: `feat(content): add PMP question on <topic>`
5. Open a pull request summarizing the new question

## Do not

- Edit `node_modules/`, `dist/`, or generated files
- Remove or overwrite existing questions unless explicitly asked
- Publish placeholder or lorem ipsum content
