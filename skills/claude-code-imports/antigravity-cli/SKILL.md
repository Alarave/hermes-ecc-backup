---
name: antigravity-cli
description: "Use when operating or debugging Antigravity CLI and app."
---

# Antigravity CLI (`agy`) & Desktop App

Operator guide for the Antigravity CLI (`agy`) and Antigravity Desktop/Hub. Run all `agy`
commands through the Hermes `terminal` tool; inspect its config and logs with
`read_file`. This skill is reference + procedure - it does not wrap a network
API, so there is nothing to authenticate from Hermes itself.

## When to Use

- Installing, updating, or smoke-testing the `agy` binary
- Driving non-interactive `agy --print` / `agy -p` one-shots
- Debugging Antigravity auth, sandbox, permissions, or plugin state
- Reading Antigravity settings, keybindings, conversations, or logs
- Troubleshooting Antigravity Desktop / Hub (v2.x / Antigravity 2.0) launch crashes
- Syncing and discovering skills between Hermes and Antigravity runtimes

## Mental model

Antigravity has two layers - keep them distinct or the guidance will be wrong:

1. **Shell wrapper commands** - `agy help`, `agy install`, `agy plugin`,
`agy update`, `agy changelog`. Run these through the `terminal` tool.
2. **Interactive in-session slash commands** - `/config`, `/permissions`,
`/skills`, `/agents`, etc. These only exist inside a running `agy` TUI
session, not on the shell wrapper.

`agy help` shows the shell wrapper surface, NOT the in-session slash commands.

## Prerequisites

- The `agy` binary on PATH. Verify through the `terminal` tool:
  `command -v agy && agy --version`.
- No env vars or API keys required by this skill - Antigravity manages its own
  auth via the OS keyring / browser sign-in (see Authentication below).

## How to Run

Invoke every `agy` command through the `terminal` tool. Examples:

```
terminal(command="agy --version")
terminal(command="agy help")
terminal(command="agy plugin list")
terminal(command="agy --print 'Summarize the repo in 3 bullets'", workdir="/path/to/project")
```

For an interactive multi-turn TUI session, launch `agy` with `pty=true` (and
tmux for capture/monitoring), the same pattern the `codex` / `claude-code`
skills use. For one-shot smoke tests and scripted prompts, prefer
`agy --print` (non-interactive).

To inspect Antigravity's own files, use `read_file` on the paths under Core
paths below - do not `cat` them through the terminal.

## Delegation patterns

`agy` is a coding-agent backend in the same family as `codex` / `claude-code`,
so the same delegation shapes apply. Use these when handing real work (features,
fixes, reviews, second opinions) to Antigravity rather than just smoke-testing.

### One-shot (preferred for scripted prompts and second opinions)

```
terminal(command="agy -p 'Review this diff for bugs and security issues' --model 'Gemini 3.1 Pro (High)'", workdir="/path/to/repo", timeout=300)
```

`-p` is non-interactive: it runs the prompt and exits. Pick the engine with
`--model` (run `agy models` for the exact display strings, e.g.
`'Gemini 3.1 Pro (High)'`, `'Claude Opus 4.6 (Thinking)'`). Add extra context
roots with repeatable `--add-dir`.

### Long / bounded runs (tests, builds, multi-file changes)

Background it and get notified on completion, the same as the `codex` skill:

```
terminal(command="agy -p 'Implement the change described in TASK.md and run the tests' --dangerously-skip-permissions", workdir="/path/to/repo", background=true, notify_on_complete=true)
# then: process(action="poll"/"log"/"wait", session_id=<id>)
```

### Interactive multi-turn (PTY + tmux)

For a conversational session, launch `agy -i` (or bare `agy`) under `pty=true`
with tmux for `capture-pane` / `send-keys`, exactly the pattern documented in
the `codex` / `claude-code` skills. Resume later with `--continue` / `-c` or a
specific `--conversation <id>`.

### Parallel instances (batch sub-issue / worktree fan-out)

Create one git worktree per task and launch an independent `agy -p` in each
(background), then collect results - same worktree fan-out the `codex` skill
uses for batch issue fixing. Bound concurrency to what the machine and your
review capacity can absorb.

### Output + bounding caveat (differs from Claude Code)

- `agy -p` returns **plain text** - there is **no `--output-format json`** and
  no result envelope with `session_id` / cost / turn count. Parse stdout
  directly; don't expect a JSON object.
- There is **no `--max-turns`**. A print run is bounded by **`--print-timeout`**
  (default `5m`). Raise it for long tasks: `--print-timeout 20m`. Pair with the
  `terminal` `timeout=` so the outer call doesn't cut the run short.

### Orchestration boundary

Antigravity is a **worker execution backend or third-opinion reviewer** - an
execution detail owned by the agent/profile running a task, NOT a first-class
orchestration primitive. Do not put `agy` on a kanban board as its own card or
treat it as a coordination layer; route work through the normal task graph and
let the assigned worker choose `agy` (vs. codex/claude-code/direct tools) as its
method. Reach for it explicitly only when the user asks, when a worker is
configured to wrap it, or when you want a Gemini-family cross-check against
another agent's plan or diff.

## Core paths

- Binary / entrypoint: `agy`
- App data dir: `~/.gemini/antigravity-cli/`
- Settings file: `~/.gemini/antigravity-cli/settings.json`
- Keybindings file: `~/.gemini/antigravity-cli/keybindings.json`
- Logs: `~/.gemini/antigravity-cli/log/cli-*.log`
- Desktop logs: `%APPDATA%\Antigravity\logs\main.log`
- Desktop binary: `%LOCALAPPDATA%\Programs\antigravity\Antigravity.exe`
- Antigravity IDE binary: `%LOCALAPPDATA%\Programs\Antigravity IDE\Antigravity IDE.exe`
- Antigravity IDE settings: `%APPDATA%\Antigravity IDE\User\settings.json`
- Antigravity IDE logs: `%APPDATA%\Antigravity IDE\logs\`
- Antigravity IDE state DB: `%APPDATA%\Antigravity IDE\User\globalStorage\state.vscdb`
- Antigravity IDE conversations: `~/.gemini/antigravity-ide/conversations/`
- Central skills registry: `~/.gemini/config/skills.json`
- Central rules dir: `~/.gemini/config/rules/`
- Central hooks file: `~/.gemini/config/hooks.json`
- Conversations: `~/.gemini/antigravity-cli/conversations/`
- Brain artifacts: `~/.gemini/antigravity-cli/brain/`
- History: `~/.gemini/antigravity-cli/history.jsonl`
- Plugin staging: `~/.gemini/antigravity-cli/plugins/<plugin_name>/`

## Quick Reference

### Wrapper commands
- `agy changelog`
- `agy help`
- `agy install`
- `agy plugin` / `agy plugins`
- `agy update`

### Useful flags
- `--add-dir`
- `--continue` / `-c`
- `--conversation`
- `--dangerously-skip-permissions`
- `--print` / `-p`
- `--print-timeout`
- `--prompt`
- `--prompt-interactive` / `-i`
- `--sandbox`
- `--log-file`
- `--version`

### Plugin subcommands (`agy plugin --help`)
- `list`, `import [source]`, `install <target>`, `uninstall <name>`,
  `enable <name>`, `disable <name>`, `validate [path]`, `link <mp> <target>`,
  `help`

### Install flags (`agy install --help`)
- `--dir`, `--skip-aliases`, `--skip-path`

### In-session slash commands
- **Conversation control:** `/resume` (`/switch`), `/rewind` (`/undo`),
  `/rename <name>`, `/clear`, `/fork`, `/reset`, `/new`
- **Settings & tools:** `/config`, `/settings`, `/permissions`, `/model`,
  `/keybindings`, `/statusline`, `/tasks`, `/skills`, `/mcp`, `/open <path>`,
  `/usage`, `/logout`, `/agents`
- **Prompt helpers:** `@` path autocomplete, `esc esc` clears the prompt (when
  not streaming), `!` runs a terminal command directly, `?` opens help

## Settings and permissions

### Common settings keys (`settings.json`)
- `allowNonWorkspaceAccess`
- `colorScheme`
- `permissions.allow`
- `trustedWorkspaces`

### Permission modes
`request-review`, `always-proceed`, `strict`, `proceed-in-sandbox`.

### Sandbox behavior
- `enableTerminalSandbox` is a boolean in `settings.json`; default `false`.
- Launch-time overrides (`--sandbox`, `--dangerously-skip-permissions`) can
  supersede persistent settings for the current session.

## Authentication behavior

- The CLI tries the OS secure keyring first.
- With no saved session, it falls back to browser-based Google sign-in.
- Locally it opens the default browser; over SSH it prints an authorization URL
  and expects the auth code pasted back.
- `/logout` removes saved credentials.

## Plugins

- Plugins stage under `~/.gemini/antigravity-cli/plugins/<plugin_name>/`.
- They can bundle skills, agents, rules, MCP servers, and hooks.
- `agy plugin list` returning no imported plugins is a valid empty state.

## Pitfalls

- `agy help` shows wrapper commands, not interactive slash commands.
- `agy --version` is the safe non-interactive version check; `agy version` is
  interactive and can fail without a real TTY.
- First place to look for failures: `~/.gemini/antigravity-cli/log/cli-*.log`
  (read with `read_file`). For Antigravity Desktop/Hub (v2.x), inspect `%APPDATA%\Antigravity\logs\main.log`.
- Electron launch crash on Windows (immediate exit / flash): When the install directory has AppContainer package SIDs without `ALL APPLICATION PACKAGES`, Electron aborts in `install_dir_access.cc:52`. Grant `ALL APPLICATION PACKAGES` (`*S-1-15-2-1`) to the install folder and the parent `%LOCALAPPDATA%\Programs` via `icacls "%LOCALAPPDATA%\Programs" /grant "*S-1-15-2-1:(OI)(CI)(RX)"` and `icacls "%LOCALAPPDATA%\Programs\antigravity" /grant "*S-1-15-2-1:(OI)(CI)(RX)" /t /q` so that auto-updates inherit the correct permissions.
- GUI GPU rendering crash: If Electron window terminates right after launch, append `--no-sandbox --disable-gpu` to the launcher shortcut arguments to prevent GPU compositing failure.
- Skill Discovery & Scan Depth: Antigravity scans paths in `~/.gemini/config/skills.json` only 1 level deep for `<name>/SKILL.md`. Nested skills (`category/skill/SKILL.md`) are ignored unless linked to top-level or their parent folder is registered in `skills.json`. Ensure `~/.gemini/antigravity-cli/skills` exists as an NTFS junction pointing to the master skills folder.
- Hooks JSON Schema (`hooks.json`): In `~/.gemini/config/hooks.json`, Antigravity's Go runtime parses `jsonhook.JSONHookSpec` as a map of objects (`"PreInvocation": {"command": "...", "timeout": 10000}`), NOT arrays (`[{"matcher": "*", "hooks": [...]}]`). Array syntax triggers `json: cannot unmarshal array into Go struct field`.
- Rule File 24KB Ceiling: In `~/.gemini/config/rules/*.md`, Antigravity truncates rule files over 24,000 bytes. Put detailed manuals and API specs in skill `references/` instead of bloated root rule files.
- Don't confuse persistent JSON settings with launch-time overrides.
- `~/.gemini/antigravity-cli/bin/agentapi` is a thin wrapper to `agy agentapi`.
- On WSL, token storage is file-based, so auth issues are usually local-file /
  session-state problems, not browser-only problems.
- Workspace identity can depend on launch directory and the `.antigravitycli`
  project marker.
- `agy -p` prints plain text only - no `--output-format json`, no result
  envelope. Don't try to parse a JSON object out of it (unlike `claude-code`).
- Bound print runs with `--print-timeout` (default `5m`), not `--max-turns`
  (which does not exist on `agy`).
- Antigravity IDE Prompt Failures / "Model Not Found": When Antigravity IDE fails on every user prompt, check `%APPDATA%\Antigravity IDE\User\settings.json`. If `"antigravity.ai.provider"` is set to `"openai-compatible"`, ensure `"antigravity.ai.model"` points to a valid active model ID or combo recognized by the local proxy router (e.g. 9Router). Do not use placeholders like `9router-combo`.
- Proxy Router Upstream Deadlock & Latency (503/404/Timeout): When routing between Hermes and Antigravity via a local proxy router (e.g., 9Router on port 20128), dead or unsupported upstream models (such as `gemini-4-argon-high` returning 404 NOT_FOUND from Google Cloud Code) cause 1-5 second cooldown sleeps on every request before failing over. Purge unverified or 404-returning models from combo pools in `%APPDATA%\9router\db\data.sqlite` (`combos` table), keeping only verified responsive endpoints (e.g., `ag/gemini-3.8-flash-high`, `ag/gemini-3.8-flash-medium`, `ag/claude-sonnet-5-5`).
- Deprecated Upstream Model Errors ("Claude Sonnet 4.6 is no longer available. Please switch to Claude Sonnet 5.5"): When Google Cloud Code / Vertex AI sunsets an upstream model, all prompts in conversations bound to that model fail with this exact message. Resolve across two layers:
  1. **Antigravity Desktop / Hub (v2.x)**: Existing conversation threads in `~/.gemini/antigravity/conversations/<id>.db` retain their model binding in `gen_metadata` (`claude-sonnet-4-6`). To fix, start a new chat (`Ctrl+N`), click the model dropdown in the prompt bar, and select `Claude Sonnet 5.5` (or `Gemini 3.8 Flash (High)`). To rescue locked conversations without losing history, update `gen_metadata.data` via SQLite to replace `claude-sonnet-4-6` with `claude-sonnet-5-5`.
  2. **9Router Proxy Combos**: Purge `ag/claude-sonnet-4-6` and `ag/claude-opus-4-6-thinking` from the `combos` table in `%APPDATA%\9router\db\data.sqlite` (e.g. in `FOKUS`, `power`, `gemini`), updating them to `ag/claude-sonnet-5-5` and `ag/claude-opus-5-5-high`.
- Corrupted Thought Signature Trapping (HTTP 400 Bad Request / INVALID_ARGUMENT): When using models with reasoning/thinking blocks (Claude with extended thinking or Gemini Thinking) on Google Vertex AI / Cloud Code via Antigravity, switching models mid-conversation (e.g., Claude to Gemini) or running long multi-turn sessions where context pruning or tool mutations alter thought blocks causes Google's backend to reject subsequent turns with `Corrupted thought signature`. Because Antigravity appends every turn and resends the entire conversation trajectory, every subsequent retry or prompt in that Cascade thread fails permanently in an infinite loop. Fix across two paths:
  1. **Clean Reset (Preferred)**: Open a fresh conversation (`Ctrl+L` / New Cascade icon `+`) with the desired model selected before turn 1; fresh conversations have 0 turns and cannot carry stale thought signatures.
  2. **Database Surgical Repair**: To rescue an active Cascade thread without losing work, backup `~/.gemini/antigravity/conversations/<cascade-id>.db`, delete failed retry steps (`DELETE FROM steps WHERE idx >= <first_failed_step>`), and remove mismatched model entries from `gen_metadata` (`DELETE FROM gen_metadata WHERE idx >= <fallback_idx>`). Then restart Antigravity or execute `/rewind` in-session.
- Quota Exhaustion Asymmetry & Antigravity MITM Interception Pitfall: In multi-account Antigravity setups behind a proxy router (e.g. 9Router), Claude & GPT quotas deplete rapidly (red), while Gemini quotas remain at 97-100% capacity (green). To prioritize Gemini safely:
  1. **Reorder Combos (`data.sqlite`)**: In `%APPDATA%\9router\db\data.sqlite` (`combos` table), place high-throughput Gemini models at the head (`ag/gemini-4-argon-high`, `ag/gemini-4-argon-medium`, `ag/gemini-3.8-flash-high`, `ag/gemini-3.8-flash-medium`) and Claude at the tail as a last-resort fallback.
  2. **DO NOT Map Antigravity in `aliases.json`**: Leave `"antigravity": {}` empty in `%APPDATA%\9router\mitm\aliases.json`. 9Router's MITM interceptor (`Jf`) passes raw Google Cloud Code payload (`contents`) to `/v1/chat/completions` without transforming to OpenAI format (`messages`), returning `HTTP 400: contents is not specified` -> `HTTP 503: All fusion panel models failed`. This sends Antigravity's Go Language Server into an exponential retry loop (`Run: attempt 1 failed... attempt 8 failed retrying in 3m25s`), freezing the UI on permanent **"Reconnecting..."** with no output. Keeping `"antigravity": {}` empty forces 9Router to use clean HTTP/2 passthrough (`tr`), which streams Google Cloud Code responses natively.
- Antigravity "Reconnecting..." Freeze from Rules Flooding (`~/.gemini/config/rules/`): Never dump broad skill libraries into `~/.gemini/config/rules/`. Antigravity's Go language server (`rules.go:482`) parses every `.md` file in that folder on every prompt turn and enforces a strict 24,000-byte cap and Cortex Memory trigger syntax. Flooding it with non-rule markdown files triggers thousands of `Invalid rule trigger: CORTEX_MEMORY_TRIGGER_UNSPECIFIED` errors and truncation warnings per second, choking I/O and causing the language server to freeze. Keep `~/.gemini/config/rules/` clean or store external skills under `~/.gemini/antigravity-cli/skills/` instead.
- Antigravity Multi-Account Hygiene & Recovery: When 9Router marks Antigravity accounts as `unavailable` or locked, the trigger is almost always a 404 from a dead combo model rather than an invalid project ID (both companion projects like `artful-quartet-842v0` and standard `aicode-consumers` work natively for `gemini-3.8-flash-high`). To revive accounts: (1) purge the dead model from combos; (2) refresh tokens via Google OAuth token endpoint; (3) reset `modelLock_*` fields, error timestamps, and rate limits in `providerConnections.data`; (4) set `testStatus = "active"` and `isActive = 1`; and (5) set provider fallback strategy to `fill-first` so 9router drains the primary account before smoothly failing over on real 429 quota limits, avoiding round-robin thrashing.
- Hermes Gateway Background Reconnect Loop: If Hermes logs continuous reconnect attempts (e.g., WhatsApp bridge failing with `PermissionError: [WinError 5] Access is denied`), disable the unused platform cleanly with `hermes config set whatsapp.enabled false` to stop background worker churn.

## Verification

Confirm the install is real and usable, all through the `terminal` tool (read
files with `read_file`):

1. `terminal(command="command -v agy")`
2. `terminal(command="agy --version")`
3. `terminal(command="agy help")`
4. `terminal(command="agy plugin list")`
5. `read_file` on `~/.gemini/antigravity-cli/settings.json`
6. `read_file` on the latest `~/.gemini/antigravity-cli/log/cli-*.log`
7. If needed, `read_file` on `~/.gemini/antigravity-cli/keybindings.json`
