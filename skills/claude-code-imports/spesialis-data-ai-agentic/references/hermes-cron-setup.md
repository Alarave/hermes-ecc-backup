# Hermes Cron Job Setup (Windows)

Coverage: cron job creation, WhatsApp/Telegram delivery targeting, Windows auto-start gateway, and external skill linking via NTFS junction.

## 1. Create a cron job

Use `cronjob_manage(action='create')` - required fields: `schedule`, `prompt`.

- `deliver`: platform target (see Delivery section below)
- `continuity: true`: each run sees its own previous output - use for dedup/incremental jobs
- `enabled_toolsets`: narrow to what the job needs (`["web"]`, `["terminal", "web"]`)
- `schedule` forms: `"every day at 7am"`, `"every monday 9am"`, `"30m"`, ISO timestamp

## 2. WhatsApp delivery - CRITICAL PITFALL

`deliver="whatsapp"` alone fails with **"no delivery target resolved"** unless a prior origin session registered a chat ID.

For manual runs or new jobs, always use an explicit chat ID:

```
deliver="whatsapp:33677593546839@lid"
```

Get the chat ID from `channel_directory.json`:

```
cat "$HERMES_HOME/channel_directory.json"
```

Update an existing job's deliver target:

```python
cronjob_manage(action='update', job_id='<id>', deliver='whatsapp:<chat_id>')
```

## 3. Prompt must be self-contained

Cron jobs run in a fresh session with zero chat context. The prompt must include all domain knowledge, folder paths, and output instructions inline. Never rely on context from the creating session.

If the job writes files, include the exact target path in the prompt (e.g. `${OBSIDIAN_VAULT_PATH:-~/notes}/Daily Learning/`).

## 4. Auto-start gateway on Windows boot

Hermes gateway must be running for cron jobs to fire. VBS script in Windows Startup folder handles this:

```
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Hermes_Gateway.vbs
```

Check before creating a new startup script - one likely already exists. Do NOT create duplicates.

Verify gateway status: `hermes gateway status`

## 5. Link external skill folder via NTFS junction (no copy)

To load skills from an external drive without copying:

```python
import subprocess
src = r"E:\path\to\skills"
dst = os.path.expanduser("~/.hermes/skills/my-skills")
cmd = f'cmd.exe /c mklink /J "{dst}" "{src}"'
subprocess.run(cmd, capture_output=True, text=True, shell=True)
```

Pitfall: `mklink /J` via bash `cmd //c` does NOT work reliably in MSYS/git-bash - use Python subprocess calling `cmd.exe /c` directly. The bash shell mangles the arguments before they reach Windows.

Result is a live junction - edits to source folder reflect instantly in Hermes skills with no sync step.

## 6. Catch-up missed jobs

`cron.catch_up_missed: true` in config.yaml means jobs that fire while PC is off run immediately when gateway next starts.

## 7. Windows Task Scheduler / Background Script Pitfall
- **Use `pythonw.exe` for background scripts, never `python.exe`.** If you schedule a Python script using Windows Task Scheduler (`schtasks`) or any hidden background loop, using `python.exe` will spawn a flashing CMD window every time it triggers, disrupting the user's workflow. Always path to `pythonw.exe` (e.g. `venv\Scripts\pythonw.exe`) to execute silently without spawning a console window.

## 8. Quick reference

```bash
hermes cron list          # list all jobs + next run time
hermes cron run <id>      # manual fire (background)
hermes cron pause <id>
hermes cron resume <id>
hermes gateway status
hermes gateway start
```
