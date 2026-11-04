---
name: ai-proxy-interception
description: "Route AI coding tools via local MITM proxies."
---

# AI Proxy Interception (RCCO)

Standard workflow untuk intercepting dan routing AI traffic dari IDE coding assistants (Kiro, Cursor, Copilot, Antigravity) ke local router (9Router, kRouter).

## R (Role)
Network & AI Proxy Engineer automating local traffic interception, root CA trust, dan endpoint rerouting.

## C (Context)
- AI tools komunikasi dengan proprietary endpoints (e.g., `runtime.us-east-1.kiro.dev`, `codewhisperer.us-east-1.amazonaws.com`).
- Local proxy (9Router port 20128, MITM port 443) butuh DNS loopback, trusted root certificate, dan model alias mappings.
- Proxy data dir 9Router di Windows: `%APPDATA%\9router\`
- Node.js/Electron IDEs butuh TLS certificate trust.

## C (Constraints & Pitfalls)

### Hosts File
- Butuh Administrator. Satu baris PowerShell kemudian verify dengan `ping <domain>` (harus reply `127.0.0.1`).
- Duplikasi entry tidak blocking tapi tidak rapi. Hapus via elevated PowerShell `Select-Object -Unique`.

### CA Certificate - CRITICAL
- `certutil -addstore -f Root` gagal Error 5 (Access Denied) tanpa admin.
- **Gunakan user store**: `certutil -addstore -user -f Root "<cert_path>"` - tidak butuh elevation.
- Electron/Node runtime bypass Windows cert store - verify `NODE_EXTRA_CA_CERTS` env var sudah menunjuk ke `rootCA.crt`.
- Probing local MITM via curl di Windows fail dengan `schannel: revocation status is unknown` - selalu tambahkan `--ssl-no-revoke`.

### Kiro Model Aliases
- Check `%APPDATA%\9router\mitm\aliases.json` untuk mapping model (e.g., `"auto": "FOKUS"`).

## O (Output & Verification Flow)

### Step 1: Cek Status Proxy
```bash
netstat -ano | grep -E "443|20128"
```
Cari PID listening di port 443 (MITM) dan 20128 (9Router).

### Step 2: DNS Redirect (satu command)
```powershell
Add-Content "$env:windir\System32\drivers\etc\hosts" "`n127.0.0.1 runtime.us-east-1.kiro.dev`n127.0.0.1 q.us-east-1.amazonaws.com`n127.0.0.1 codewhisperer.us-east-1.amazonaws.com" ; ipconfig /flushdns
```
Verify: `ping runtime.us-east-1.kiro.dev` - harus reply `127.0.0.1`.

### Step 3: Install CA Certificate
```cmd
certutil -addstore -user -f Root "%APPDATA%\9router\mitm\rootCA.crt"
```
Expected output: `Certificate "9Router MITM Root CA" added to store.`

### Step 4: Verify TLS Intercept
```bash
curl -Ik --ssl-no-revoke https://runtime.us-east-1.kiro.dev/ --cacert "%APPDATA%/9router/mitm/rootCA.crt"
```
Expect: HTTP 404 dari local proxy (normal - bukan error; 200 juga OK tergantung proxy config).

### Step 5: Restart IDE target, cek Logs di 9Router Dashboard.

## Kiro-Specific Endpoints

| Domain | Fungsi |
|---|---|
| `runtime.us-east-1.kiro.dev` | Inference, streaming (baru, pengganti q.*) |
| `q.us-east-1.amazonaws.com` | Legacy Amazon Q endpoint |
| `codewhisperer.us-east-1.amazonaws.com` | CodeWhisperer endpoint |

> Kiro IDE versi baru menggunakan `runtime.us-east-1.kiro.dev` sebagai primary endpoint.
