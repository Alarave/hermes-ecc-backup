#!/usr/bin/env python3
"""
scripts/background_learner.py
Daemon / Worker di latar belakang yang berjalan senyap:
1. Memindai pengalaman baru di instincts/shared/
2. Melakukan audit sanitasi otomatis
3. Melakukan git commit dan git push otomatis tanpa perlu interaksi pengguna
"""

import os
import sys
import time
import getpass
import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTINCTS_DIR = BASE_DIR / "instincts" / "shared"

def get_author():
    try:
        user = subprocess.check_output(["git", "config", "user.name"], text=True, cwd=str(BASE_DIR)).strip()
        if user:
            return re.sub(r"[^a-zA-Z0-9_-]", "_", user).lower()
    except Exception:
        pass
    return getpass.getuser().lower()

def auto_commit_and_push(changed_files, author):
    if not changed_files:
        return
    try:
        for f in changed_files:
            subprocess.run(["git", "add", str(f)], cwd=str(BASE_DIR), check=True)
        
        commit_msg = f"koreografi: auto-sync {len(changed_files)} pengalaman baru dari {author} (background-learner)"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
        print(f"[BACKGROUND LEARNER] Sukses push otomatis {len(changed_files)} file ke GitHub!")
    except Exception as e:
        print(f"[BACKGROUND LEARNER WARN] Push tertunda: {e}")

def check_uncommitted_instincts():
    author = get_author()
    try:
        # Cek status file untracked/modified di instincts/shared/
        out = subprocess.check_output(["git", "status", "--porcelain", "instincts/shared/"], text=True, cwd=str(BASE_DIR))
        files_to_sync = []
        for line in out.splitlines():
            parts = line.strip().split()
            if len(parts) >= 2:
                filepath = parts[-1]
                if filepath.endswith(".yaml"):
                    files_to_sync.append(filepath)
        
        if files_to_sync:
            print(f"[BACKGROUND LEARNER] Mendeteksi {len(files_to_sync)} pengalaman baru belum ter-push...")
            auto_commit_and_push(files_to_sync, author)
    except Exception as e:
        print(f"[BACKGROUND LEARNER ERROR] Gagal memeriksa status git: {e}")

def run_daemon():
    print("[BACKGROUND LEARNER] Daemon aktif di latar belakang (Checking every 10 menit)...")
    while True:
        check_uncommitted_instincts()
        # Sleep 10 menit
        time.sleep(600)

if __name__ == "__main__":
    if "--once" in sys.argv:
        check_uncommitted_instincts()
    else:
        run_daemon()
