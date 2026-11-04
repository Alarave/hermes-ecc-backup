---
name: openrig-team-assembly
description: "Use when creating or validating OpenRig YAML specs."
category: "DevOps"
---

# OpenRig Team Assembly

Always follow this procedure when assembling an OpenRig team (`rig.yaml`), resolving validation errors, or setting up custom agent runtimes (Hermes, Antigravity) via the `terminal` adapter.

## Procedure

1. **Verify Prerequisites:**
   - Ensure `npm` and `node` are available. Install OpenRig: `npm install -g @openrig/cli`.
   - On Windows, install tmux via Winget: `winget install --id arndawg.tmux-windows --exact`. You **must** manually add the Winget package path to `$PATH` (e.g., `export PATH="$PATH:/c/Users/<User>/AppData/Local/Microsoft/WinGet/Packages/arndawg.tmux-windows_Microsoft.Winget.Source_8wekyb3d8bbwe"`) before running `rig` commands.

2. **Draft the `rig.yaml` (RigSpec v0.2):**
   - The top-level keys must be `version: "0.2"`, `name`, `summary`, `culture_file`, `pods`, and `edges`.
   - Do NOT nest the definition under a `rig:` root key.

3. **Configure Built-in Agents (Claude Code):**
   - Built-in models (like `claude-code`) must have their `agent_ref` resolved properly.
   - Do NOT use `builtin:orchestrator` or `builtin:implementer`.
   - Instead, copy the built-in specs locally (e.g., `cp -r <global_node_modules>/@openrig/cli/daemon/specs/agents ./agents`) and use `agent_ref: "local:agents/orchestration/orchestrator"`.
   - If using `path:`, it must be an absolute POSIX path starting with `/` (e.g., `path:/c/Users/...`).

4. **Configure Custom Agents (Hermes, Antigravity):**
   - Use the `terminal` runtime adapter for agents that aren't natively supported.
   - `runtime: terminal`
   - `profile: none`
   - `agent_ref: builtin:terminal`
   - Provide a `startup:` block with `command: "./scripts/wrapper.sh"`. The wrapper script receives the prompt via the `$OPENRIG_SEAT_TASK` environment variable.

5. **Define Edges (Topology):**
   - In cross-pod edges (defined at the root `edges:` level), `from` and `to` **must** be fully qualified using the format `<pod_id>.<member_id>` (e.g., `command.lead`, `dev.backend`).

6. **Validate and Boot:**
   - Run `rig spec validate <path-to-rig.yaml>` to catch schema errors.
   - Run `rig setup` to configure workspace trust and hook providers.
   - Boot the daemon: `rig daemon start --no-kernel`.
   - Check the deployment plan: `rig up rig.yaml --plan`.

## Pitfalls

- **Do not use `rig:` as the root key in a v0.2 RigSpec.** OpenRig validation will reject it with "unknown key". The root properties should sit at the top level.
- **Do not use `builtin:<name>` for agent_refs (except `builtin:terminal`).** The validation demands `local:` or `path:`. Copying the specs folder locally and using `local:agents/...` is the most reliable cross-platform method.
- **Do not use Windows backslashes or drive letters without a leading slash in `path:` refs.** It expects an absolute path starting with `/` (e.g., `path:/c/...`).
- **Do not forget to fully qualify edge IDs.** Edges defined outside a pod's scope must use `<pod_id>.<member_id>`. Using just the member ID causes validation failures ("member not found in pod").
- **Do not assume `tmux` is natively available on Windows.** You must install `tmux-windows` and export its path into the session running the daemon.
