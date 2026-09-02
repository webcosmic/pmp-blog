# PMP Blog — Agent Instructions

This repository powers **noteskeep.com**, an Astro static site with PMP situational questions.

## Cursor Cloud specific instructions

### Commands

| Task | Command |
|------|---------|
| Install dependencies | `npm ci` |
| Dev server | `npm run dev -- --host 0.0.0.0 --port 4321` |
| Build (required before PR) | `npm run build` |
| Preview production build | `npm run preview` |

### Content location

- **Live posts:** `src/content/pmp-questions/*.md`
- **Draft warehouse:** `pmp_questions_pack.md` (not published until converted)
- **Content schema:** `src/content.config.ts`

### Adding a new question

1. Read the canonical example: `src/content/pmp-questions/2026-06-07-regulatory-stakeholder-power-shift.md`
2. Create a new file at `src/content/pmp-questions/YYYY-MM-DD-topic-slug.md`
3. Include all required frontmatter: `title`, `pubDate`, `topic`, `category`, `difficulty`, `correctAnswer`, `slug`
4. Structure the body with **The Scenario**, **Options** (A–D), and **Explanation & Analysis**
5. Run `npm run build` — fix any errors before committing
6. Commit: `feat(content): add PMP question on <topic>`
7. Open a pull request

### Skills

Use the project skills in `.cursor/skills/blog/`:

- **write-pmp-question** — draft new questions from scratch
- **publish-from-warehouse** — convert scenarios from `pmp_questions_pack.md`

### Legacy automation

`soul.md` describes a dual-agent research/format pipeline. `watch_agent.py` watches `agent_output.txt` for `READY_FOR_EXECUTION` handoffs. Cloud Agents should write directly to `src/content/pmp-questions/` instead.

### PR expectations

- One question per PR unless the user requests a batch
- Build must pass
- PR title format: `blog: add PMP question — <short title>`

## Automation prompt template

Use this at [cursor.com/automations](https://cursor.com/automations) for recurring content:

```
You are maintaining the noteskeep.com PMP blog (Astro static site).

Each run:
1. Read recent posts in src/content/pmp-questions/ to avoid duplicate topics.
2. Draft ONE new situational PMP question on a project-management topic not covered in the last 8 weeks.
3. Follow the write-pmp-question skill and match the canonical post format.
4. Run npm run build and fix any errors.
5. Open a PR titled "blog: add PMP question — <title>" with a summary of the scenario topic and difficulty.

If no suitable topic remains or the build fails twice, do not open a PR.
```
