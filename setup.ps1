Write-Host "Memulai setup ECC Hermes untuk pengguna baru..." -ForegroundColor Green

# Setup Root Profile
$userProfilePath = $env:USERPROFILE
if (-Not (Test-Path "config.yaml")) { 
    $content = Get-Content "config.example.yaml" -Raw
    $content = $content.Replace('C:\Users\Template', $userProfilePath).Replace('C:\Users\HP', $userProfilePath)
    Set-Content "config.yaml" -Value $content
} else {
    $content = Get-Content "config.yaml" -Raw
    $content = $content.Replace('C:\Users\Template', $userProfilePath).Replace('C:\Users\HP', $userProfilePath)
    Set-Content "config.yaml" -Value $content
}
if (-Not (Test-Path "profile.yaml")) { Copy-Item "profile.example.yaml" "profile.yaml" }
if (-Not (Test-Path "SOUL.md")) { Copy-Item "SOUL.example.md" "SOUL.md" }
if (-Not (Test-Path "memories")) {
    New-Item -ItemType Directory -Force -Path "memories" | Out-Null
    Copy-Item "memories-template/USER.example.md" "memories/USER.md"
    Copy-Item "memories-template/MEMORY.example.md" "memories/MEMORY.md"
}
if (-Not (Test-Path "cron")) {
    New-Item -ItemType Directory -Force -Path "cron" | Out-Null
    Copy-Item "cron-template/jobs.example.json" "cron/jobs.json"
}

# Setup Trading Profiles
$profiles = @("trading", "trading-agen")
foreach ($p in $profiles) {
    $targetDir = "profiles/$p"
    if (-Not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
        New-Item -ItemType Directory -Force -Path "$targetDir/memories" | Out-Null
        
        if (Test-Path "profiles-template/$p/SOUL.example.md") { Copy-Item "profiles-template/$p/SOUL.example.md" "$targetDir/SOUL.md" }
        if (Test-Path "profiles-template/$p/profile.example.yaml") { Copy-Item "profiles-template/$p/profile.example.yaml" "$targetDir/profile.yaml" }
        if (Test-Path "profiles-template/$p/config.example.yaml") { Copy-Item "profiles-template/$p/config.example.yaml" "$targetDir/config.yaml" }
        if (Test-Path "profiles-template/$p/memories/USER.example.md") { Copy-Item "profiles-template/$p/memories/USER.example.md" "$targetDir/memories/USER.md" }
        if (Test-Path "profiles-template/$p/memories/MEMORY.example.md") { Copy-Item "profiles-template/$p/memories/MEMORY.example.md" "$targetDir/memories/MEMORY.md" }
    }
}

Write-Host "[OK] Sinkronisasi Skill ke Antigravity / Gemini CLI..." -ForegroundColor Yellow
if (Test-Path "sync_skills.py") {
    python sync_skills.py
    Write-Host "[OK] Skill berhasil di-inject ke ekosistem CLI." -ForegroundColor Green
}

Write-Host "[OK] Menghubungkan skill secara global (Claude, Codex, Kiro, Antigravity)..." -ForegroundColor Yellow
$masterSkills = "$env:USERPROFILE\AppData\Local\hermes\skills"
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
Write-Host "[OK] Skill global berhasil di-link." -ForegroundColor Green

Write-Host "Setup selesai! Silakan buka config.yaml (root dan profil) untuk mengisi API Key." -ForegroundColor Cyan

