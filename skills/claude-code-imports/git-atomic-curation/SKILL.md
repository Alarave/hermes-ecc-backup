---
name: git-atomic-curation
description: "Use when curating dirty git repos into atomic commits."
---

# Git Atomic Curation

Workflow for decomposing massive, multi-file uncommitted working tree changes into structured, verified atomic commits.

## Procedure

1. **Audit and Inventory**:
   - Inspect status using `git status -s` and porcelain output.
   - Categorize files by semantic domain: typography/formatting (rapihan), core features/architecture (fitur), specifications/documentation (dokumen), new skills/plugins, and metadata/lockfiles.
2. **Submodule Isolation**:
   - Check if any submodule contains untracked content (`modified: ... (untracked content)`).
   - Resolve, stage, and commit untracked files inside the submodule's own directory first. Staging the parent while a submodule is dirty leaves the tree in an un-cleanable state.
3. **Typography and Lint Pre-Screening**:
   - Scan modified and untracked files for formatting rules (such as zero em-dash / en-dash violations, line endings CRLF/LF).
   - Sanitize before staging so clean history is preserved.
4. **Layered Atomic Staging and Commits**:
   - Commit strictly by semantic layer using standard prefixes (`rapihan:`, `fitur:`, `dokumen:`, `perbaikan:`, `koreografi:`):
     - Layer A: `rapihan:` (formatting, typography sanitization, styling)
     - Layer B: `fitur:` (core feature implementation and architecture)
     - Layer C: `dokumen:` (specifications, requirements, academic guidelines)
     - Layer D: `fitur:` (new skills, extensions, plugin integrations)
     - Layer E: `rapihan:` (metadata, locks, usage logs, generated cache)
   - Never combine unrelated formatting changes with functional logic changes.
5. **Deferred Tool Handling (tool_call)**:
   - When using orchestration tools like `todo_list` discovered via `tool_search`, invoke them through `tool_call` envelopes rather than bare function calls.
6. **Verification and Clean Tree Gate**:
   - Verify `git status` reports `nothing to commit, working tree clean`.
   - Verify commit history with `git log -n 5 --oneline`.
   - Strict no auto-push: never push to remote without explicit user authorization.

## Pitfalls

- **Submodule Untracked State**: Untracked files inside submodules cannot be staged from the parent root with `git add <submodule>`. Always cd into the submodule to stage and commit, then stage the updated submodule ref in the parent.
- **Monolithic Commit Blunder**: Staging all 100+ files at once destroys git bisect capability and obfuscates architectural changes behind formatting noise.
- **Direct Function Invocation of Deferred Tools**: Tools discovered via `tool_search` are not in the top-level executor namespace. Calling them directly causes "Tool does not exist" errors. Wrap in `tool_call`.
