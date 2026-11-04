---
name: windows-terminal-workflow
description: "Windows Terminal CLI execution, PowerShell commands, and profile configuration."
---

# Windows Terminal Workflow

Procedures and pitfalls for executing CLI operations reliably on Windows hosts that mix native Windows binaries, MSYS bash, and PowerShell.

## Procedure: Executing PowerShell Commands from Bash
When invoking PowerShell from MSYS bash (the default Hermes `terminal` environment on Windows):
1. Wrap the command string in double quotes if it contains spaces or symbols: `powershell -Command "..."`.
2. Do NOT use modern shell logical operators like `||` or `&&` inside the PowerShell 5.1 command string.
3. Fall back to `;` to sequence commands, or check `$?` manually if conditional execution is required.

## Procedure: Handling Git Clone Timeouts
When a `git clone` times out (common on slow networks or large repos hitting bounded execution limits):
1. Add the `--depth 1` flag to minimize history download.
2. Add the `--progress` flag so the execution environment receives stdout activity and doesn't terminate the process for being silently stalled.
3. If it fails, remove the partial clone directory (`rm -rf <dir>`) before retrying.

## Procedure: Querying Process Command Lines (WMIC Deprecation)
`wmic` is deprecated and removed from modern Windows 11 builds by default. Query processes and arguments via CIM:
```powershell
powershell.exe -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match '<target>' } | Select-Object ProcessId, Name, CommandLine"
```

## Procedure: Deleting Elevated Scheduled Tasks from Standard Shell
When a task is registered with `RunLevel: HighestAvailable` (admin), standard `schtasks /delete` or `schtasks /change /disable` fails with `ERROR: Access is denied` in unelevated shells:
1. Neuter payload immediately: delete or empty the target script/batch file so triggers execute nothing.
2. Terminate running instance if active: `schtasks /end /tn "\TaskName"` (succeeds for user-owned tokens).
3. Elevate deletion via UAC prompt in interactive sessions:
   ```powershell
   powershell.exe -NoProfile -Command "Start-Process cmd.exe -Verb RunAs -ArgumentList '/c schtasks /delete /tn \"\TaskName\" /f' -Wait"
   ```
4. Verify task is removed: `schtasks /query /tn "\TaskName"` returns error / not found.

## Procedure: Running Multi-Line Generator Scripts & Launching Detached GUI Apps
1. **Avoid Large Inline Heredocs (`WinError 206`)**: Never embed large multi-line Python/Node scripts inline via `cat << 'EOF' > ...` in `terminal` on Windows. Write the script to `$TMPDIR` (`C:/Users/<user>/AppData/Local/hermes/cache/scratch/<script>.py`) using `write_file`, then execute `python "C:/Users/<user>/AppData/Local/hermes/cache/scratch/<script>.py"`.
2. **Launch Desktop GUI Apps Detached**: To open a native desktop GUI application (e.g., `figcraft.exe`) with a target file without blocking the terminal session, use:
   ```bash
   cmd.exe /c start "" "C:\Program Files\App\app.exe" "C:\path\to\file"
   ```

## Procedure: Silent Per-User Execution of NSIS/Setup Installers Without UAC
Installers with `Installer`/`Setup` in the filename or `<requestedExecutionLevel level="highestAvailable" uiAccess="false"/>` in their manifest trigger a UAC prompt and fail in non-elevated shells (`The operation was canceled by the user`). To install silently into per-user `AppData\Local\Programs`:
1. Locate the real Downloads folder if redirected to another drive:
   ```powershell
   powershell.exe -NoProfile -Command "(New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path"
   ```
2. Run the installer with `__COMPAT_LAYER=RunAsInvoker` and `/S`:
   ```bash
   export __COMPAT_LAYER=RunAsInvoker
   "/path/to/Installer.exe" /S
   ```

## Pitfalls

- **PowerShell 5.1 Syntax Limitations:** Using `||` or `&&` inside `powershell -Command "..."` throws a parser error (`The token '||' is not a valid statement separator in this version`) on default Windows 11 machines running PS 5.1. Use `;` instead.
- **WMIC Deprecated on Windows 11:** Calling `wmic` fails with `FileNotFoundError: [WinError 2]` on modern Windows builds. Always use PowerShell `Get-CimInstance Win32_Process` instead.
- **Elevated Task Scheduler Deletion Access Denied:** Tasks with `RunLevel: HighestAvailable` cannot be deleted directly from standard unelevated MSYS/Bash shells. Use PowerShell `Start-Process -Verb RunAs` with `schtasks /delete` to request UAC elevation, and delete the underlying action file first to prevent mid-turn execution.
- **Task Scheduler AC Power/Charger Auto-Trigger:** Tasks configured with `<DisallowStartIfOnBatteries>true` and `<StopIfGoingOnBatteries>true` pause on battery and automatically launch/resume when AC power (charger) is connected. When investigating apps that launch on charger plug-in, inspect Task Scheduler XML power management settings.
- **Heavy I/O Git Operations:** Running `git add` on massive directories (like full Next.js/React open-source repos with tens of thousands of files) is extremely slow on Windows and often hits the 180s terminal timeout (Exit 124). Always use `background: true` or significantly raise the `timeout` when staging massive scaffolds.
- **Winget Package Locations:** Winget packages installed as traditional desktop apps (non-UVP) typically land in `C:\Users\<User>\AppData\Local\Programs\<AppName>\` (under `HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\`) or `C:\Program Files\` (under `HKLM`). Do not assume they are only in `C:\Program Files`.
- **MSYS Path Translation to Native Tools:** Calling native Windows tools (like `winget`, `python`, `node`) with MSYS-style paths (`/c/Users/...`) often fails, and passing `$TMPDIR` inside double quotes to native Windows `python` can resolve to `/tmp` (`C:\tmp\...` not found). Always pass explicit forward-slash Windows paths (`C:/Users/...`) to native binaries.
- **Command-Line Length Limit (`[WinError 206]`):** Large inline bash commands or heredocs in `terminal` exceed the Windows 32,767-character `CreateProcess` limit and fail with `FileNotFoundError: [WinError 206] The filename or extension is too long`. Write scripts to disk with `write_file` first instead of inline heredocs.
- **OpenRig / tmux on Native Windows:** Tools that require `tmux` session orchestration (like OpenRig) fail on native Windows ports of tmux (`arndawg.tmux-windows`) with `create window failed: spawn failed` due to Windows backslash path conversion in `-c`. Run tmux-dependent orchestration inside WSL2 (Ubuntu) instead of native Windows CMD/Git Bash.
