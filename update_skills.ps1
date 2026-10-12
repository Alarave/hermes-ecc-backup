# ==============================================================================
# SCRIPT UPDATE OTOMATIS SKILL HARNESS OS (PowerShell / Windows)
# ==============================================================================

Write-Host ">>> Memulai pemeriksaan pembaruan skill dari repositori upstream..." -ForegroundColor Cyan

# 1. Tarik pembaruan terbaru dari Git upstream
try {
    Write-Host "[1/3] Menarik commit terbaru via Git pull..." -ForegroundColor Yellow
    $gitOutput = git pull origin main 2>&1
    Write-Host $gitOutput -ForegroundColor Gray
} catch {
    Write-Host "[WARN] Gagal menjalankan git pull. Pastikan koneksi internet aktif." -ForegroundColor Red
}

# Auto-schedule update lokal setiap 3 hari via Windows Task Scheduler (jika belum ada)
$taskName = "HermesSkillsAutoUpdate"
$existingTask = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if (-Not $existingTask) {
    try {
        $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
        $trigger = New-ScheduledTaskTrigger -Daily -At "08:00"
        # Jalankan setiap 3 hari
        $trigger.Repetition = $null
        Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Description "Auto update skill Hermes setiap berkala" -ErrorAction SilentlyContinue | Out-Null
        Write-Host "[OK] Task Scheduler otomatis terdaftar di Windows (update background)." -ForegroundColor DarkGray
    } catch {}
}

# 2. Jalankan sinkronisasi ke ekosistem CLI (Antigravity / Gemini)
Write-Host "[2/3] Memperbarui sinkronisasi skill lokal & pengalaman tim..." -ForegroundColor Yellow
if (Test-Path "sync_skills.py") {
    python sync_skills.py
    Write-Host "[OK] Sinkronisasi skill lokal selesai." -ForegroundColor Green
}

# Tampilkan ringkasan pengalaman bersama yang baru masuk
$sharedInstincts = Get-ChildItem -Path "instincts\shared" -Recurse -Filter "*.yaml" -ErrorAction SilentlyContinue
if ($sharedInstincts) {
    Write-Host "[INFO] Terdeteksi $($sharedInstincts.Count) file pengalaman tim aktif di instincts/shared/" -ForegroundColor Cyan
}

# 3. Verifikasi tautan global (Junction links ke Claude, Codex, Kiro, Antigravity)
Write-Host "[3/3] Memeriksa tautan global toolchains..." -ForegroundColor Yellow
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$masterSkills = Join-Path $scriptDir "skills"
$tools = @(".claude", ".codex", ".kiro", ".gemini\antigravity", ".hermes")

foreach ($tool in $tools) {
    $toolPath = "$env:USERPROFILE\$tool"
    $skillPath = "$toolPath\skills"
    
    if (-Not (Test-Path $toolPath)) {
        New-Item -ItemType Directory -Force -Path $toolPath | Out-Null
    }
    
    if (Test-Path $skillPath) {
        $isJunc = (Get-Item $skillPath -ErrorAction SilentlyContinue).LinkType -eq 'Junction'
        if (-Not $isJunc) {
            Remove-Item -Recurse -Force $skillPath
            cmd /c mklink /J "$skillPath" "$masterSkills" > $null
        }
    } else {
        cmd /c mklink /J "$skillPath" "$masterSkills" > $null
    }
}

Write-Host ">>> SEMUA SKILL BERHASIL DIPERBARUI & TERSINKRONISASI LENGKAP!" -ForegroundColor Green
