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
- **Idempotency Gate:** Bulk upload scripts must always query existing remote files in the target folder before uploading, skipping duplicates to ensure resume safety.

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
- **Path B (Programmatic Python Script):**
  Run using `uv run --with google-api-python-client --with google-auth-oauthlib python upload_script.py`.
  - Parallel workers: `ThreadPoolExecutor(max_workers=4)`.
  - Resumable uploads: `MediaFileUpload(resumable=True)` for files > 5 MB.
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
