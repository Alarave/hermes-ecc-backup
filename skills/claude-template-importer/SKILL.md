---
name: claude-template-importer
description: Use when importing agent templates. Converts to RCCO format.
---

# Claude Code Template Importer

Import agent definitions from `davila7/claude-code-templates` (and mdskills) and convert them to the local RCCO standard.

## Procedure

1. **Locate Target Agent**
   - Query the repository tree via GitHub API: `https://api.github.com/repos/davila7/claude-code-templates/git/trees/main?recursive=1`
   - Target directories: `cli-tool/components/agents/<category>/<agent-name>.md`

2. **Fetch and Parse**
   - Retrieve raw markdown from: `https://raw.githubusercontent.com/davila7/claude-code-templates/main/cli-tool/components/agents/<category>/<agent-name>.md`
   - Extract frontmatter (`name`, `description`) and body content.

3. **Convert to RCCO Format**
   - Format structure:
     - `# <Title>`
     - `## Role`: The agent's core identity and role extracted from description.
     - `## Context`: Detailed scope, triggers, and examples.
     - `## Constraint`: Core boundaries, testing requirements, and anti-hallucination rules.
     - `## Output`: The full system prompt body.

4. **Target Placement**
   - Save to the relevant Meta-Skill subfolder under `E:\skill claude\skill claude\<Meta_Skill>\references\<agent-name>.md`.
