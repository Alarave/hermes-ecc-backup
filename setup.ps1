Write-Host "Memulai setup ECC Hermes untuk pengguna baru..." -ForegroundColor Green

if (-Not (Test-Path "config.yaml")) {
    Copy-Item "config.example.yaml" "config.yaml"
    Write-Host "[OK] config.yaml dibuat. Harap isi API Key Anda."
}
if (-Not (Test-Path "profile.yaml")) {
    Copy-Item "profile.example.yaml" "profile.yaml"
    Write-Host "[OK] profile.yaml dibuat."
}
if (-Not (Test-Path "SOUL.md")) {
    Copy-Item "SOUL.example.md" "SOUL.md"
    Write-Host "[OK] SOUL.md dibuat."
}
if (-Not (Test-Path "memories")) {
    New-Item -ItemType Directory -Force -Path "memories" | Out-Null
    Copy-Item "memories-template/USER.example.md" "memories/USER.md"
    Copy-Item "memories-template/MEMORY.example.md" "memories/MEMORY.md"
    Write-Host "[OK] Folder memories disiapkan."
}
if (-Not (Test-Path "cron")) {
    New-Item -ItemType Directory -Force -Path "cron" | Out-Null
    Copy-Item "cron-template/jobs.example.json" "cron/jobs.json"
    Write-Host "[OK] Folder cron disiapkan."
}

Write-Host "Setup selesai! Silakan buka config.yaml dan memories/USER.md untuk penyesuaian." -ForegroundColor Cyan
