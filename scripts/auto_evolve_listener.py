#!/usr/bin/env python3
"""
scripts/auto_evolve_listener.py
Background Listener / Post-Session Hook
Mendeteksi saat AI selesai menyelesaikan sesi interaksi, menyaring pola sukses/koreksi,
dan secara otomatis mem-push pengalaman baru ke GitHub private tim.
"""

import os
import sys
import getpass
import datetime
import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTINCTS_DIR = BASE_DIR / "instincts" / "shared"

def get_author():
    try:
        user = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
        if user:
            return re.sub(r"[^a-zA-Z0-9_-]", "_", user).lower()
    except Exception:
        pass
    return getpass.getuser().lower()

def sanitize(text: str) -> str:
    text = re.sub(r"[A-Za-z]:\\[Uu]sers\\[A-Za-z0-9_]+", "${USER_HOME}", text)
    text = re.sub(r"(token|key|secret|password)\s*[:=]\s*['\"][^'\"]+['\"]", r"\1: [REDACTED]", text, flags=re.IGNORECASE)
    return text

def record_and_sync_experience(topic: str, context: str, solution: str):
    author = get_author()
    user_dir = INSTINCTS_DIR / author
    user_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", topic.lower()).strip("-")[:40]
    filename = f"{today}_{slug}.yaml"
    filepath = user_dir / filename

    content = f"""---
id: {slug}
title: "{topic}"
author: {author}
date: {today}
confidence: 0.85
domain: auto-evolved
---

# {topic}

## Konteks & Masalah
{sanitize(context)}

## Solusi & Pola Sukses
{sanitize(solution)}

## Catatan Audit
- Otomatis dipelajari dan disinkronkan dari sesi kerja {author} pada {today}.
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[AUTO-EVOLVE] Pengalaman baru tersimpan: instincts/shared/{author}/{filename}")

    # Otomatis push ke GitHub tanpa interupsi
    try:
        subprocess.run(["git", "add", str(filepath)], cwd=str(BASE_DIR), check=True)
        commit_msg = f"koreografi: auto-sync pengalaman baru [{slug}] dari {author}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
        print("[AUTO-EVOLVE] Pengalaman berhasil di-push otomatis ke GitHub tim!")
    except Exception as e:
        print(f"[AUTO-EVOLVE WARN] Push tertunda (mungkin offline): {e}")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        record_and_sync_experience(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2:
        record_and_sync_experience(sys.argv[1], "Interaksi sesi AI lokal", "Pola kerja teruji pada eksekusi perintah pengguna.")
    else:
        print("Penggunaan: python scripts/auto_evolve_listener.py <topik> <konteks> <solusi>")
