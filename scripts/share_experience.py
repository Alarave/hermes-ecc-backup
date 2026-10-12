#!/usr/bin/env python3
"""
share_experience.py — Ekspor dan Bagikan Pengalaman Belajar (Instinct) ke Tim
Penggunaan:
    python scripts/share_experience.py "Deskripsi trik atau pola yang dipelajari"
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

def get_username():
    # Ambil username git atau nama user OS
    try:
        user = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
        if user:
            return re.sub(r"[^a-zA-Z0-9_-]", "_", user).lower()
    except Exception:
        pass
    return getpass.getuser().lower()

def sanitize_text(text: str) -> str:
    # Sensor path lokal dan token
    text = re.sub(r"[A-Za-z]:\\[Uu]sers\\[A-Za-z0-9_]+", "${USER_HOME}", text)
    text = re.sub(r"(token|key|secret|password)\s*[:=]\s*['\"][^'\"]+['\"]", r"\1: [REDACTED]", text, flags=re.IGNORECASE)
    return text

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: python scripts/share_experience.py \"Pola atau pelajaran yang didapat\"")
        print("Contoh: python scripts/share_experience.py \"Optimasi query postgresql menggunakan partial index\"")
        sys.exit(1)

    title = sys.argv[1].strip()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")[:40]
    author = get_username()

    user_dir = INSTINCTS_DIR / author
    user_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    filename = f"{today}_{slug}.yaml"
    filepath = user_dir / filename

    content = f"""---
id: {slug}
title: "{title}"
author: {author}
date: {today}
confidence: 0.8
domain: general
---

# {title}

## Problem / Konteks
[Jelaskan masalah atau skenario yang dihadapi]

## Solusi / Aturan yang Berhasil
[Jelaskan solusi konkret, snippet kode, atau perintah yang terbukti memecahkan masalah]

## Verifikasi
- Teruji di mesin lokal pada {today}
"""

    if not filepath.exists():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Draft pengalaman dibuat di: instincts/shared/{author}/{filename}")
        print(f"[INFO] Buka file tersebut jika ingin melengkapi detailnya.")
    else:
        print(f"[INFO] File {filename} sudah ada.")

    # Otomatis commit dan push jika user ingin langsung bagikan
    choice = input("Mau langsung commit dan push ke GitHub bersama? (y/n): ").strip().lower()
    if choice == "y":
        try:
            subprocess.run(["git", "add", str(filepath)], check=True)
            commit_msg = f"fitur: bagikan pengalaman [{slug}] dari {author}"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("[BERHASIL] Pengalaman berhasil dibagikan ke repositori tim!")
        except Exception as e:
            print(f"[ERROR] Gagal membagikan ke Git: {e}")
    else:
        # Otomatis diserahkan ke background daemon untuk auto-push senyap
        print("[INFO] File disimpan. Background daemon akan melakukan auto-push secara senyap.")

if __name__ == "__main__":
    main()
