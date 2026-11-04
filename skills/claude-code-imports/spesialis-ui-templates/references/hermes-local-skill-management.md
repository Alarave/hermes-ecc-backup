# Hermes Local Skill Management

Use this skill when creating local Hermes skills, importing external prompt files (like Claude Code or Gemini rules) into Hermes, or when troubleshooting why local skills aren't loading or triggering.

## Procedure: Importing Flat Markdown Rules

When asked to import external flat markdown files (e.g. `rule.md`) into Hermes local skills:
1. **Do NOT just copy flat `.md` files** into the `skills/` directory. Hermes `skills_list` will ignore them.
2. For each file, create a dedicated directory: `skills/<rule-name>/`.
3. Wrap the content into `skills/<rule-name>/SKILL.md`.
4. Prepend YAML frontmatter containing at least `name` and `description`.
   ```yaml
   ---
   name: <rule-name>
   description: <short description>
   ---
   ```

## Procedure: Syncing External Skill Directories (Windows Junction)

When integrating external skill directories (e.g. `~/.agents/skills/` from third-party tools or other AI harnesses):
1. **Use directory junctions instead of copying files** so subsequent updates, syncs, or installs stay automatically in sync without manual duplication.
2. Execute via `cmd.exe` with native Windows paths:
   ```cmd
   cmd.exe /c "mklink /J C:\Users\<User>\AppData\Local\hermes\skills\<group-name> C:\Users\<User>\.agents\skills"
   ```
3. Check `skills_list()` to ensure the linked skills and their categories are discovered properly.

## Procedure: Sharing MCP Servers Across Agents

When an MCP server is configured in Antigravity (`~/.gemini/config/mcp_config.json`) or Claude Desktop/Code:
1. Inspect the command and arguments in `~/.gemini/config/mcp_config.json` or `.claude.json`.
2. Register the same server into Hermes configuration (`C:\Users\<User>\AppData\Local\hermes\config.yaml`) under `mcp_servers`:
   ```yaml
   mcp_servers:
     <server-name>:
       enabled: true
       command: <executable_path>
       args:
         - <script_path>
   ```
3. For tools requiring local background daemons (like `claude-mem`), instruct the user to run the worker in a separate terminal.

## Pitfalls

- **Third-party tool installations hanging:** Always run `npx` or third-party CLI installations with `--yes` and bypass interactive cloud-trial prompts by explicitly setting fallback env variables (e.g. `CLAUDE_MEM_ONLINE_OPTIN=false` or `--provider host`). Default interactive mode hangs when run inside background terminal calls.
- **npm ENOTEMPTY Cache Errors:** If an `npx` install fails with `ENOTEMPTY` in `AppData\Local\npm-cache\_npx`, it's a left-over from a timed-out run. Clear the cache directory (`rm -rf .../_npx`) and retry.
- **`mklink` requires `cmd.exe` and native paths:** `mklink` is a `cmd.exe` builtin, not an executable. Calling `mklink` directly in bash or passing POSIX-style paths (`/c/Users/...`) will fail with syntax errors. Always wrap in `cmd.exe /c` and use escaped backslashes or native paths.
- **Skills are NOT Slash Commands:** Users coming from Claude Code may try to invoke skills by typing `/skill-name`. In Hermes, skills are not registered as standalone slash commands. Do not instruct users to type `/skill-name`. Instead, instruct them to:
  - Let the agent trigger it automatically based on conversational relevance.
  - Use the interactive `/skills` menu.
  - Preload it via the CLI: `hermes -s <skill-name>`.
  - Explicitly ask in natural language: "Use the <skill-name> skill".
- **Flat files are ignored:** A skill must be a directory containing a `SKILL.md` file with valid YAML frontmatter. If you copy a flat `.md` file, the user will report the skill is missing.

## Procedure: Gstack Installation on Hermes

When setting up `gstack` (or similar generators) for Hermes:
1. Run the generation script in the cloned repository: `bun run gen:skill-docs --host hermes`.
2. This generates skill directories under `.hermes/skills/gstack-*` inside the repo.
3. Copy these generated directories into the local Hermes skills directory (`C:\Users\<User>\AppData\Local\hermes\skills\`) so they are auto-loaded.
4. Alternatively, append the generated `.hermes/skills` absolute path to `skills.external_dirs` in `config.yaml`.

## Agentic Methodology & Multi-Skill Loading

- **Auto-Invocation over Slash Commands:** Implement the "Superpowers" methodology. Do NOT wait for slash commands. Automatically load and chain the relevant skills (e.g., `gstack-office-hours` -> `gstack-plan-ceo-review` -> `spesialis-frontend`) based on natural language intent.
- **Multi-Skill Loading:** Hermes supports and encourages loading multiple skills simultaneously. If a task spans multiple disciplines, load all relevant skills in one turn (e.g., `spesialis-frontend` + `gstack-qa`).
- **Spec before Code:** When building features, never jump straight to code. Automatically route to planning skills (e.g., `spesialis-project-manager` or `gstack-plan-eng-review`) to produce a spec -> plan -> TDD -> code pipeline.

## Procedure: Meta-Skill Routing (Managing Skill Bloat)

When a user has hundreds or thousands of micro-skills (e.g., specific React templates, individual UI framework rules) that bloat the global registry and context window, consolidate them into a Meta-Skill router:
1. Create a top-level umbrella skill directory and `SKILL.md` (e.g., `skills/spesialis-frontend/SKILL.md`).
2. Create a `references/` subdirectory inside it.
3. Move all granular sub-skills into `references/` as plain `<topic>.md` files. **Strip their YAML frontmatter and do not name them `SKILL.md`**, ensuring they drop out of the global `skills_list`.
4. In the umbrella `SKILL.md`, add a `

## Linked References
File referensi (SOP & Panduan) untuk manajemen skill:
- `references/skill-adaptation-policy.md`
- `references/skill-anatomy.md`
- `references/skill-comply.md`
- `references/skill-create.md`
- `references/skill-creator.md`
- `references/skill-development-guide.md`
- `references/skill-health.md`
- `references/skill-impact.md`
- `references/skill-installer.md`
- `references/skill-lookup.md`
- `references/skill-placement-policy.md`
- `references/skills-contributing.md`
- `references/skills-mapping.md`
