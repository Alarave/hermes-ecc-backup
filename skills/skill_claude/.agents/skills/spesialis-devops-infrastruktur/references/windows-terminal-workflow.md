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

## Pitfalls

- **PowerShell 5.1 Syntax Limitations:** Using `||` or `&&` inside `powershell -Command "..."` throws a parser error (`The token '||' is not a valid statement separator in this version`) on default Windows 11 machines running PS 5.1. Use `;` instead.
- **Winget Package Locations:** Winget packages installed as traditional desktop apps (non-UVP) typically land in `C:\Users\<User>\AppData\Local\Programs\<AppName>\` (under `HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\`) or `C:\Program Files\` (under `HKLM`). Do not assume they are only in `C:\Program Files`.
- **MSYS Path Translation to Native Tools:** Calling native Windows tools (like `winget`, `python`, `node`) with MSYS-style paths (`/c/Users/...`) often fails. Always use native `C:/Users/...` paths when passing arguments to native binaries.
