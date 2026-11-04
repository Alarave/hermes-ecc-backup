---
name: google-drive-ops
description: Use when syncing, uploading, or automating Google Drive.
---

# Google Drive Operations & Integration

## Role
System Integrator & Cloud Storage Automation Specialist for Google Drive and Google Workspace ecosystems.

## Context
Google Drive operations across MCP clients (Hermes, Claude Desktop), third-party tool gateways (Composio / Rube MCP), native desktop clients (Google Drive for Desktop), and programmatic Python automation scripts.

## Constraints
- **No Official Google Drive MCP:** Google does not provide an official MCP server for Drive. Use verified community packages (`@aaronsb/google-workspace-mcp`) or Composio. Do NOT configure `@modelcontextprotocol/server-google-drive` (package does not exist in npm; returns 404).
- **Composio Upload Limits:** Composio's `GOOGLEDRIVE_UPLOAD_FILE` is capped at 5 MB and requires S3-staged keys. Never use it for large local directory uploads or bulk datasets.
- **OAuth Desktop Type Requirement:** Google Cloud OAuth 2.0 Client IDs for local scripts or MCP servers MUST be created as **Desktop app**. Web Application clients reject dynamic localhost ports with `Error 400: redirect_uri_mismatch`.
- **Testing User Gate:** If the Google Cloud project OAuth consent screen is in "Testing" mode, user email addresses must be explicitly added to **Test users** or access fails with `Error 403: access_denied`.
- **No Background Subprocess OAuth:** Never run interactive OAuth flows (`run_local_server()`) inside unattended agent background subprocesses. Always provide a standalone `.bat` or terminal command so the user authenticates interactively in their console.
- **Folder Race Condition Gate:** Pre-create and resolve the full remote folder tree hierarchy sequentially (parent first, child second) before dispatching worker threads. Concurrent folder lookups and creations across parallel worker threads create duplicate remote folders with identical names.
- **Batch Remote Indexing:** Query and index existing remote files per folder once in batch (`pageSize=1000`) before file dispatch rather than querying file existence per item inside worker threads. Per-file existence queries quickly exhaust Google Drive's 1,000 queries per 100 seconds quota.
- **Reference Code & Heavy Tree Isolation:** Cloned reference repositories, vendor libraries, or virtual environments (>10,000 files, >2,000 directories) must be excluded by default or compressed into archives. Always isolate core project assets (source code, docs, configs, dataset manifests, notebooks, research papers) for fast sync, keeping vendor trees as an explicit opt-in (`--all`).

## Workflows

### 1. MCP Setup (Multi-Service Workspace)
For full Drive + Docs + Sheets + Calendar access in one MCP server:
- Package: `@aaronsb/google-workspace-mcp` (Node 22+).
- Client configuration:
  ```json
  {
    "mcpServers": {
      "google-workspace": {
        "command": "npx",
        "args": ["-y", "@aaronsb/google-workspace-mcp"],
        "env": {
          "GOOGLE_CLIENT_ID": "YOUR_CLIENT_ID",
          "GOOGLE_CLIENT_SECRET": "YOUR_CLIENT_SECRET"
        }
      }
    }
  }
  ```

### 2. Composio / Rube MCP Operations
- Tools: `GOOGLEDRIVE_FIND_FILE`, `GOOGLEDRIVE_GET_FILE_METADATA`, `GOOGLEDRIVE_DOWNLOAD_FILE`.
- Execution: Always via `mcp__rube__COMPOSIO_MULTI_EXECUTE_TOOL`.
- Query syntax: `name = 'Target' and mimeType = 'application/vnd.google-apps.folder' and trashed = false`.

### 3. Bulk Directory Sync (GB-scale / Hundreds of Files)
- **Path A (Native Desktop Sync - Fastest & Resilient):**
  If `GoogleDriveFS.exe` (`C:\Program Files\Google\Drive File Stream`) is present:
  Use File Explorer right-click -> "Sync with Google Drive", or sync to virtual drive (`G:\My Drive\<Folder>`) using `robocopy /MT:8`.
- **Path B (Programmatic Python Script + Real-Time Watcher):**
  Run using `uv run --with google-api-python-client --with google-auth-oauthlib --with watchdog python sync_script.py`.
  - Sequential folder pre-creation: Recursively create missing remote folders before launching file threads.
  - Upfront file indexing: Build `{folder_id: {filename: file_meta}}` map to skip unchanged files by size (`SKIP`), update changed files (`UPDATE`), and create new files (`UPLOAD`).
  - Resumable uploads: `MediaFileUpload(resumable=True)` for files > 5 MB with exponential backoff on retry.
  - Real-time watcher: Use `watchdog.observers.Observer` + `FileSystemEventHandler` with 2-second debounce to auto-sync files immediately upon local save.
  - Standalone Windows Runner: Always generate a `.bat` file (e.g., `start_sync.bat`) so the user can launch and monitor sync without agent interaction.
  - Browser prompt resolution: explain that *"Google hasn't verified this app"* is resolved by clicking *Advanced -> Go to [App] (unsafe)*.

## Output Format
```text
DRIVE ACTION
- Target folder name & ID
- Local path & file count

METHOD
- Native sync / MCP tool / Python script runner

STATUS & VERIFICATION
- Upload/Sync progress [completed/total]
- Active links to Drive assets
```
