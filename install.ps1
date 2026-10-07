# =========================================================
# HERMES ECC (Enterprise Command Center) - Auto Installer
# =========================================================
$ErrorActionPreference = "Stop"

$RepoUrl = "https://github.com/Alarave/hermes-ecc-backup.git"
$EccDir = "$env:LOCALAPPDATA\hermes-ecc"
$HermesSkillsDir = "$env:LOCALAPPDATA\hermes\skills"
$GeminiRulesDir = "$env:USERPROFILE\.gemini\config\rules"

Write-Host ">>> Memulai Instalasi Hermes ECC (Alarave)..." -ForegroundColor Cyan

# 1. Clone atau Update Repo
if (Test-Path "$EccDir\.git") {
    Write-Host ">>> Melakukan update ECC dari server..." -ForegroundColor Yellow
    Set-Location $EccDir
    git pull origin main
} else {
    Write-Host ">>> Mendownload sistem ECC..." -ForegroundColor Yellow
    git clone $RepoUrl $EccDir
}

# 2. Deploy ke Hermes (Symlink atau Copy)
Write-Host ">>> Mengaktifkan Skills di Hermes Agent..." -ForegroundColor Yellow
if (-Not (Test-Path $HermesSkillsDir)) { New-Item -ItemType Directory -Force -Path $HermesSkillsDir | Out-Null }

$eccSkills = Get-ChildItem -Path "$EccDir\skills" -Directory
foreach ($skill in $eccSkills) {
    # Hindari duplikasi / symlink
    $targetPath = "$HermesSkillsDir\$($skill.Name)"
    if (Test-Path $targetPath) { Remove-Item -Recurse -Force $targetPath }
    
    # Gunakan Junction (Hardlink folder di Windows) agar selalu tersinkronisasi otomatis
    cmd /c mklink /J "$targetPath" "$($skill.FullName)" > $null
}

# 3. Deploy ke Antigravity / Gemini CLI
Write-Host ">>> Mengaktifkan Skills di Antigravity / Gemini CLI..." -ForegroundColor Yellow
if (-Not (Test-Path $GeminiRulesDir)) { New-Item -ItemType Directory -Force -Path $GeminiRulesDir | Out-Null }

Set-Location $EccDir
if (Test-Path "sync_skills.py") {
    python sync_skills.py
}

Write-Host ""
Write-Host "=========================================================" -ForegroundColor Green
Write-Host " INSTALASI BERHASIL! (Plug-and-Play Selesai)" -ForegroundColor Green
Write-Host "=========================================================" -ForegroundColor Green
Write-Host "Semua agent (Hermes & Antigravity) kini memiliki keahlian ECC."
Write-Host "Coba jalankan chat baru dengan: 'Pram, buatkan plan untuk...'"
