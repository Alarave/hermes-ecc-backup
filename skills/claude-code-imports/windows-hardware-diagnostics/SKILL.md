---
name: windows-hardware-diagnostics
description: "Use when diagnosing or updating Windows hardware drivers."
---

# Windows Hardware Diagnostics

## Role
Windows hardware diagnostic and driver remediation specialist.

## Context
Use when diagnosing devices, missing drivers, audio failures, or PnP device status on Windows systems.

## Constraint
- Always use signed drivers with pnputil; unsigned INF files fail validation.
- Run device scans and driver installs from elevated shells (RunAs admin).
- Check Windows Audio services before reinstalling drivers.
- No em/en dashes; use standard punctuation.

## Output
Executable PowerShell/CLI commands, root-cause status codes, and verified driver remediation steps.

## Procedure: Audio and Device Troubleshooting
1. Query audio service status:
   `powershell -NoProfile -Command "Get-Service -Name Audiosrv, AudioEndpointBuilder | Select-Object Name, Status"`
2. Inspect device status and error codes:
   `powershell -NoProfile -Command "Get-PnpDevice -Class Media | Format-Table Status, FriendlyName, ProblemDescription -AutoSize"`
3. Query active audio endpoints:
   `powershell -NoProfile -Command "Get-PnpDevice -Class AudioEndpoint | Format-Table Status, FriendlyName, InstanceId -AutoSize"`
4. Trigger Windows Update driver scan if missing:
   `usoclient StartScan`
   Or check Settings > Windows Update > Advanced options > Optional updates > Driver updates.
5. Install OEM signed driver package via elevated shell:
   `pnputil /add-driver *.inf /subdirs /install`

## Pitfalls
- **Unsigned INF Rejection**: pnputil blocks unsigned third-party drivers. Use signed OEM vendor packages or official Windows Update packages.
- **Access Denied on Rescan**: `pnputil /scan-devices` fails without administrator elevation. Launch an elevated console when running scans or driver imports.
- **Code 45 (Disconnected Device)**: Unknown status often means physical hardware disconnected or endpoint unseated.
