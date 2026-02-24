📘 Assignment: Customize Your GitHub Copilot Experience

## 🎯 Objective

Configure and document project-level GitHub Copilot guidance so teammates (and future you) receive consistent, helpful suggestions. By the end of this assignment you'll update repository guidance and write a short usage guide.

## 🎓 Learning Outcomes

- Describe what project-level Copilot guidance controls and why it matters
- Write concise, actionable instructions for Copilot users
- Verify Copilot behavior locally using VS Code or a dev container
- Apply consistent style and language conventions across a repo

**Difficulty:** Beginner–Intermediate

**Topics:** GitHub Copilot, documentation, Markdown, repository hygiene

## ⏱️ Estimated Time

30–60 minutes

## ⚙️ Prerequisites

- Basic familiarity with Git and GitHub
- Comfort reading and editing Markdown

## 📦 Files Provided

- `.github/copilot-instructions.md` — file to update (create if missing)
- `.devcontainer/` (optional) — dev container configuration to test locally
- `templates/assignment-template.md` — assignment content template

## 📝 Tasks

### 🛠️ Task 1 — Inspect the repository

#### Description
Locate existing Copilot guidance and dev-container configuration in the repo (start in `.github/` and `.devcontainer/`).

#### Requirements

- List any files or locations where guidance exists (e.g., `.github/copilot-instructions.md`, `.github/copilot-instructions.yaml`)

### 🛠️ Task 2 — Update `copilot-instructions.md`

#### Description
Edit or create `.github/copilot-instructions.md` to provide clear, project-specific guidance: preferred language, tone, style, coding conventions, and things Copilot should avoid.

#### Requirements

- Add at least four concrete guidance bullets covering language, style, examples, and do/don't items
- Keep the tone concise and student-friendly

### 🛠️ Task 3 — Add a short usage guide

#### Description
Add a short README section (or update this file) describing how contributors should use the Copilot guidance and how to test it locally.

#### Requirements

- Include one example prompt that follows the guidance (see example below)
- Describe how to verify the behavior locally (opening the repo in the dev container or VS Code with Copilot)

Example prompt that follows guidance:

"Write a short, student-friendly function in Python that validates an email address and includes a brief usage example and unit test. Use clear variable names and add a one-line comment explaining the purpose."

Verification steps (local):

1. Open the repository in VS Code or the provided dev container
2. Ensure the GitHub Copilot extension is enabled
3. Invoke Copilot with the example prompt and confirm suggestions follow the documented style

## ✅ Deliverables

1. Updated `.github/copilot-instructions.md` with explicit guidance
2. This `README.md` (this file) updated with objective, tasks, and verification steps

## 📚 Resources

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- `templates/assignment-template.md` for structure

---

© 2026 Course Materials — Educational use only
