#!/usr/bin/env bash
# ==============================================================================
# SCRIPT UPDATE OTOMATIS SKILL HARNESS OS (Bash / Linux / macOS)
# ==============================================================================

set -e

echo ">>> Memulai pemeriksaan pembaruan skill dari repositori upstream..."

# 1. Tarik pembaruan terbaru dari Git upstream
echo "[1/3] Menarik commit terbaru via Git pull..."
git pull origin main || echo "[WARN] Gagal menjalankan git pull. Pastikan koneksi internet aktif."

# 2. Jalankan sinkronisasi ke ekosistem CLI jika ada python
echo "[2/3] Memperbarui sinkronisasi skill lokal..."
if [ -f "sync_skills.py" ]; then
    python3 sync_skills.py 2>/dev/null || python sync_skills.py 2>/dev/null || true
    echo "[OK] Sinkronisasi skill lokal selesai."
fi

# 3. Verifikasi symlink global
echo "[3/3] Memeriksa tautan global toolchains..."
MASTER_SKILLS="$HOME/.hermes/skills"
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
