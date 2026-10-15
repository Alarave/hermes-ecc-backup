# Bulk Upload & Large Dataset Synchronization to Google Drive

## 1. Architecture Choice: MCP vs Native Scripting

- **MCP Tools (Composio / stdio servers)**:
  - Intended for individual file lookups, search queries, reading document contents, and single-file creation.
  - DO NOT use MCP tool calls to loop through hundreds or thousands of files. MCP tool execution introduces per-call serialization latency and toolkits often impose strict file-size limits (e.g. 5MB) or require remote S3 staging.
- **Native Scripting (`google-api-python-client` with `uv`)**:
  - Preferred for batch ingestion, multi-gigabyte folders, and hundreds/thousands of documents.
  - Run via: `uv run --with google-api-python-client --with google-auth-oauthlib python scripts/upload_folder_to_gdrive.py`.

## 2. Open-Source MCP Package Reference

- **Unified Google Workspace MCP**: `@aaronsb/google-workspace-mcp` (Node 20+, unifies Drive, Docs, Sheets, Calendar, Gmail).
- **Standalone Drive MCP**: `@modelcontextprotocol/server-gdrive` (Note: deprecated/legacy).
- **Common Failure**: Never configure `@modelcontextprotocol/server-google-drive` in config files; the package name does not exist on npm and throws HTTP 404.

## 3. Idempotency & Resumable Upload Rules

1. **Pre-fetch Remote Index**:
   - Query the target Google Drive folder ID with `'{FOLDER_ID}' in parents and trashed = false` paginating with `pageSize=1000`.
   - Store remote filenames in a hash set. Skip local files whose filenames are already present.
2. **Resumable Chunks**:
   - For files > 5MB, always set `resumable=True` in `MediaFileUpload` to avoid broken pipes on transient network drops.
3. **Concurrency & Rate Limits**:
   - Use `ThreadPoolExecutor(max_workers=4)`. Keep workers under 6 to stay within Google Drive's default per-user request rate limits (avoid HTTP 403 `userRateLimitExceeded`).
   - Create a separate `build('drive', 'v3', credentials=creds, cache_discovery=False)` client instance per worker thread to avoid thread safety issues.
