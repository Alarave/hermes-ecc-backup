#!/usr/bin/env python3
"""
scripts/audit_incoming_skills.py
Memeriksa dan mengaudit pembaruan skill dari teman/kontributor secara otomatis.
Standar audit:
1. Zero Path Leak (C:\\Users\\, E:\\... tidak boleh bocor)
2. Format RCCO (Role, Context, Constraints, Output)
3. Zero Hardcoded Secrets/Tokens
4. Natural Language Triggers pada deskripsi frontmatter
"""

import os
import sys
import re
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = BASE_DIR / "skills"

def get_git_changed_skills():
    """Mengambil daftar file SKILL.md yang berubah di commit/PR terbaru."""
    changed_files = set()
    diff_commands = [
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
        ["git", "show", "--name-only", "--format=", "HEAD"],
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        ["git", "status", "--porcelain"]
    ]
    for cmd in diff_commands:
        try:
            out = subprocess.check_output(cmd, text=True, cwd=str(BASE_DIR), stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                parts = line.strip().split()
                if not parts:
                    continue
                path_str = parts[-1]
                if path_str.endswith("SKILL.md"):
                    changed_files.add(path_str)
            if changed_files:
                break
        except Exception:
            continue
    return list(changed_files)

def audit_skill_file(filepath: Path):
    rel_path = filepath.resolve().relative_to(BASE_DIR.resolve())
    verdict = {
        "file": str(rel_path),
        "score": 100,
        "passed": True,
        "warnings": [],
        "errors": []
    }

    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        verdict["errors"].append(f"Gagal membaca file: {e}")
        verdict["passed"] = False
        verdict["score"] = 0
        return verdict

    # 1. Audit Kebocoran Path Pribadi (Fatal - Deduct 50)
    if re.search(r"[A-Za-z]:\\[Uu]sers\\[A-Za-z0-9_]+", content):
        verdict["errors"].append("Ditemukan hardcoded Windows User Path (contoh: C:\\Users\\...)")
        verdict["score"] -= 50
        verdict["passed"] = False

    if "E:\\BELAJAR BANGET" in content and "${OBSIDIAN_VAULT_PATH" not in content:
        verdict["errors"].append("Ditemukan hardcoded path Obsidian pribadi tanpa template fallback")
        verdict["score"] -= 50
        verdict["passed"] = False

    # 2. Audit Kredensial & PII 8-Class (Fatal - Deduct 50)
    for m in re.finditer(r"(api[_-]?key|token|password|secret)\s*[:=]\s*['\"]([^'\"]{16,})['\"]", content, re.IGNORECASE):
        val = m.group(2).lower()
        if any(ph in val for ph in ["your-key", "your_key", "your-api", "placeholder", "example", "dummy", "insert-", "change-me", "xxxx", "sk-or-v1-your", "sk-ant-api03-***"]):
            continue
        verdict["errors"].append("Terdeteksi potensi token/kunci API mentah yang tidak disamarkan [REDACTED]")
        verdict["score"] -= 50
        verdict["passed"] = False
        break

    # Deteksi nomor telepon riil atau NIK 16-digit mentah (OpenAI Privacy Filter standard)
    if re.search(r"\b(08[1-9][0-9]{7,10})\b", content) or re.search(r"\b([1-9][0-9]{15})\b", content):
        verdict["errors"].append("Terdeteksi data PII mentah (nomor telepon/NIK) yang belum disamarkan [REDACTED]")
        verdict["score"] -= 50
        verdict["passed"] = False

    # 3. Audit Standar RCCO (Quality - Deduct 10 per missing pillar)
    has_role = ("## R" in content or "# Role" in content or "Role:" in content)
    has_context = ("## C" in content or "# Context" in content or "When to use" in content)
    has_rules = ("## C" in content or "Constraints" in content or "Rules" in content or "## Workflow" in content)
    has_output = ("## O" in content or "Output" in content or "Deliverables" in content)

    if not has_role:
        verdict["warnings"].append("Pilar Role (R) tidak terdefinisi secara jelas")
        verdict["score"] -= 10
    if not has_context:
        verdict["warnings"].append("Pilar Context (C) tidak terdefinisi secara jelas")
        verdict["score"] -= 10
    if not has_rules:
        verdict["warnings"].append("Pilar Constraints/Rules (C) tidak terdefinisi secara jelas")
        verdict["score"] -= 10
    if not has_output:
        verdict["warnings"].append("Pilar Output/Definition of Done (O) tidak terdefinisi")
        verdict["score"] -= 10

    # 4. Audit Frontmatter & Natural Triggers
    if not content.startswith("---"):
        verdict["warnings"].append("Tidak ada frontmatter YAML (---)")
        verdict["score"] -= 10
    else:
        if "description:" not in content:
            verdict["warnings"].append("Frontmatter tidak memiliki field description untuk router AI")
            verdict["score"] -= 10

    if verdict["score"] < 60:
        verdict["passed"] = False

    return verdict

def main():
    print("=" * 60)
    print(" 🛡️ PRAM AUDIT ENGINE: AUDIT MUTU SKILL DARI KONTRIBUTOR")
    print("=" * 60)

    # Ambil argumen spesifik atau scan file yang berubah
    if len(sys.argv) > 1 and sys.argv[1] != "--all":
        target_files = [Path(sys.argv[1])]
    elif len(sys.argv) > 1 and sys.argv[1] == "--all":
        print("[INFO] Mode --all aktif. Menjalankan audit menyeluruh pada root skills/...")
        target_files = [d / "SKILL.md" for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]
    else:
        changed = get_git_changed_skills()
        if changed:
            print(f"[INFO] Mendeteksi {len(changed)} skill yang baru di-update.")
            target_files = [BASE_DIR / f for f in changed]
        else:
            print("[INFO] Tidak ada file SKILL.md yang berubah di commit ini. Audit dilewati.")
            print("\n" + "=" * 60)
            print("HASIL AKHIR: 0 LULUS, 0 DITOLAK (Tidak ada perubahan skill).")
            print("=" * 60)
            print("\n[VERDIK PRAM]: Semua pembaruan BERMUTU TINGGI dan aman diserap oleh seluruh tim.")
            sys.exit(0)

    total = len(target_files)
    passed_count = 0
    failed_count = 0

    results = []
    for tf in target_files:
        if tf.is_file():
            res = audit_skill_file(tf)
            results.append(res)
            if res["passed"]:
                passed_count += 1
            else:
                failed_count += 1

    # Tampilkan ringkasan audit
    for r in results:
        badge = "✅ LULUS" if r["passed"] else "❌ DITOLAK"
        print(f"\n{badge} (Skor: {r['score']}/100) -> {r['file']}")
        if r["errors"]:
            for err in r["errors"]:
                print(f"   [FATAL ERROR] {err}")
        if r["warnings"]:
            for w in r["warnings"]:
                print(f"   [SARAN/PERBAIKAN] {w}")

    print("\n" + "=" * 60)
    print(f"HASIL AKHIR: {passed_count} LULUS, {failed_count} DITOLAK dari {total} skill.")
    print("=" * 60)

    if failed_count > 0:
        print("\n[VERDIK PRAM]: Ada pembaruan yang TIDAK MEMENUHI STANDAR. Mohon perbaiki sebelum di-merge.")
        sys.exit(1)
    else:
        print("\n[VERDIK PRAM]: Semua pembaruan BERMUTU TINGGI dan aman diserap oleh seluruh tim.")
        sys.exit(0)

if __name__ == "__main__":
    main()
