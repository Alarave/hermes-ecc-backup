---
name: multi-platform-scraper
description: "Aturan Gemini multi-platform-scraper"
---

# Multi-Platform Scraper (Agent-Reach)

**Role:** Data Acquisition Specialist

**Context:** 
User needs to extract data (sentiment, trends, code) from closed or rate-limited platforms (X/Twitter, Reddit, YouTube, Bilibili, XiaoHongShu, GitHub) without paying for official APIs. 

**Constraint / Pitfalls:**
- **MSYS Bash Paths:** Do not use `C:/...` inside `PATH` exports in MSYS bash (the colon acts as a delimiter and breaks it). Use `/c/Users/HP/.agent-reach-venv/Scripts`.
- **GitHub Auth False Negative:** `agent-reach doctor` intentionally skips `gh auth status` to avoid writing `device-id`. If `gh auth status` passes natively, GitHub extraction works even if the doctor tool marks it as `[!]`.
- **YouTube `yt-dlp` Dependency:** Extracting video info/transcripts requires a JS runtime. Always ensure `~/.config/yt-dlp/config` contains `--js-runtimes node`.
- **Account Ban Risk:** When authenticating X/Twitter, Reddit, or XiaoHongShu, strictly instruct the use of dummy/secondary accounts. Cookie/session auth carries high ban risks.
- **Chrome Local Profile Lock:** On Windows, Google Chrome frequently maintains background/tray processes after the window closes, keeping the user profile locked and blocking browser cloning. Run `taskkill /F /IM chrome.exe /T` (after user consent) to terminate lingering instances before using local profile scraping.
- **Google Drive Folder Scraping:** Static scrapers fail on Google Drive folder links, extracting only outer UI shells. To enumerate files, use a headless browser to evaluate `document.querySelectorAll('[role="row"], .WvE1ze, [data-tooltip]')`. Do not attempt to parse preview text directly from web drive previews; download the target file locally to parse it reliably.

**Procedure:**
1. Activate environment or use absolute path: `/c/Users/HP/.agent-reach-venv/Scripts/agent-reach.exe`.
2. Check tool health via `agent-reach doctor`.
3. If YouTube fails on extraction, verify JS runtime config for `yt-dlp`.
4. Use Agent-Reach commands or MCP connection to pull transcripts, posts, and threads.