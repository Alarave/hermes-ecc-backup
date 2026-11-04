---
name: google-workspace-ops
description: Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.
metadata:
  origin: ECC
---

# Google Workspace Ops

This skill is for operating shared docs, spreadsheets, and decks as working systems, not just editing one file in isolation.

## When to Use

- User needs to find a doc, sheet, or deck and update it in place
- Consolidating plans, trackers, notes, or customer lists stored in Google Drive
- Cleaning or restructuring a shared spreadsheet
- Importing, repairing, or reformatting a Google Slides deck
- Producing summaries from Docs, Sheets, or Slides for decision-making

## Preferred Tool Surface

Use Google Drive as the entry point, then switch to the right specialist:

- Google Docs for text-heavy docs
- Google Sheets for tabular work, formulas, and charts
- Google Slides for decks, imports, template migration, and cleanup

Do not guess structure from filenames alone. Inspect first.

## Bulk Upload and Dataset Ingestion

For batch synchronization, local directory backups, or uploading hundreds of files (>5MB total):
- Do NOT use individual MCP upload tool calls; per-call overhead, payload caps, and timeouts make MCP unsuitable for large datasets.
- Use native multi-threaded script: `scripts/upload_folder_to_gdrive.py`.
- Detailed architecture and quota rules: `references/bulk-upload-sync.md`.

## Pitfalls

- **Invalid MCP package name**: Do NOT configure `@modelcontextprotocol/server-google-drive` in configs (it does not exist on npm and throws 404). Use `@aaronsb/google-workspace-mcp` (Node 20+) for unified Workspace access or `@modelcontextprotocol/server-gdrive` (legacy).
- **Bulk uploads via MCP**: Never loop MCP upload tools over bulk folders because toolkits enforce payload caps (often 5MB) or require remote staging keys. Use a native multi-threaded script with `uv run` and `google-api-python-client`.
- **Duplicate files during batch upload**: Always pre-fetch existing filenames in the target Drive folder before starting uploads to guarantee idempotency and instant resume upon interruption.

## Workflow

### 1. Find the asset

Start with the Drive search surface to locate:

- the exact file
- sibling assets
- likely duplicates
- recently modified versions

If several documents look similar, confirm by title, owner, modified time, or folder.

### 2. Inspect before editing

Before making changes:

- summarize current structure
- identify tabs, headings, or slide count
- detect whether the task is local cleanup or structural surgery

Pick the smallest tool that can safely perform the work.

### 3. Edit with precision

- For Docs: use index-aware edits, not vague rewrites
- For Sheets: operate on explicit tabs and ranges
- For Slides: distinguish content edits from visual cleanup or template migration

If the requested work is visual or layout-sensitive, iterate with inspection and verification instead of one giant blind update.

### 4. Keep the working system clean

When the file is part of a larger workflow, also surface:

- duplicate trackers
- outdated decks
- stale docs vs canonical docs
- whether the asset should be archived, merged, or renamed

## Output Format

Use:

```text
ASSET
- file name
- type
- why this is the right file

CURRENT STATE
- structure summary
- key problems or blockers

ACTION
- edits made or recommended

FOLLOW-UPS
- archive / merge / duplicate cleanup / next file to update
```

## Good Use Cases

- "Find the active planning doc and condense it"
- "Clean up this customer spreadsheet and show me the churn-risk rows"
- "Import this deck into Slides and make it presentable"
- "Find the current tracker, not the stale duplicate"
