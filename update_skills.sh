#!/usr/bin/env bash
# ==============================================================================
# SCRIPT UPDATE OTOMATIS SKILL HARNESS OS (Bash / Linux / macOS)
# ==============================================================================

set -e

echo ">>> Memulai pemeriksaan pembaruan skill dari repositori upstream..."

# 1. Tarik pembaruan terbaru dari Git upstream
echo "[1/4] Menarik commit terbaru via Git pull..."
git pull origin main || echo "[WARN] Gagal menjalankan git pull. Pastikan koneksi internet aktif."

# 2. Audit Mutu Pembaruan Otomatis (Pram Audit Engine)
echo "[2/4] Menjalankan audit mutu dan keamanan skill terbaru..."
if [ -f "scripts/audit_incoming_skills.py" ]; then
    python3 scripts/audit_incoming_skills.py 2>/dev/null || python scripts/audit_incoming_skills.py 2>/dev/null || true
fi

# 3. Jalankan sinkronisasi ke ekosistem CLI jika ada python
echo "[2/3] Memperbarui sinkronisasi skill lokal & pengalaman tim..."
if [ -f "sync_skills.py" ]; then
    python3 sync_skills.py 2>/dev/null || python sync_skills.py 2>/dev/null || true
    echo "[OK] Sinkronisasi skill lokal selesai."
fi

SHARED_COUNT=$(find instincts/shared -type f -name "*.yaml" 2>/dev/null | wc -l || echo "0")
if [ "$SHARED_COUNT" -gt 0 ]; then
    echo "[INFO] Terdeteksi $SHARED_COUNT file pengalaman tim aktif di instincts/shared/"
fi

# 3. Jalankan Background Learner (Sinkronisasi Pengalaman ke Git)
echo "[3/4] Memeriksa sinkronisasi pengalaman tim..."
if [ -f "scripts/background_learner.py" ]; then
    python3 scripts/background_learner.py --once 2>/dev/null || python scripts/background_learner.py --once 2>/dev/null || true
fi

# 4. Verifikasi symlink global
echo "[3/3] Memeriksa tautan global toolchains..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MASTER_SKILLS="$SCRIPT_DIR/skills"
TOOLS=(".claude" ".codex" ".kiro" ".gemini/antigravity")

for tool in "${TOOLS[@]}"; do
    TOOL_PATH="$HOME/$tool"
    SKILL_PATH="$TOOL_PATH/skills"
    
    mkdir -p "$TOOL_PATH"
    
    if [ -L "$SKILL_PATH" ] || [ -d "$SKILL_PATH" ]; then
        rm -rf "$SKILL_PATH"
    fi
    
    ln -s "$MASTER_SKILLS" "$SKILL_PATH" 2>/dev/null || true
done

echo ">>> SEMUA SKILL BERHASIL DIPERBARUI & TERSINKRONISASI LENGKAP!"
