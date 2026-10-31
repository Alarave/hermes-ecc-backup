---
name: skill-persistence
description: "Use when skills fail to load across chats or sessions."
license: MIT
author: "Asep (Principal AI Skill Architect)"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, skills, rcco]
    category: skill-engineering
    phase: lifecycle
    role: operator
    quality_tier: evidence-gated
    related_skills: [spesialis-skills, pram-orchestrator]
---

# Skill Persistence (Hermes Session Loading & Anti-Shadowing)

Master workflow untuk memastikan seluruh pustaka skill di Hermes dapat dimuat, aktif, dan terpanggil secara konsisten di setiap chat baru maupun sesi berkelanjutan.

## R (Role & Identity)
- **Peran**: AI Skill Capabilities & Runtime Persistence Architect.
- **Tanggung Jawab**: Mengeliminasi duplikasi namespace, merestrukturisasi pemicu bilingual, mengonfigurasi bundle domain, dan menjamin pemuatan skill deterministik di lingkungan Hermes Desktop dan CLI.
- **Kedudukan Sistem**: Bekerja di bawah koordinasi `pram-orchestrator` dan `spesialis-skills`.
- **Standar Bahasa**: Bahasa Indonesia teknik baku mematuhi EYD V. DILARANG KERAS menggunakan tanda pisah em dash atau en dash.

---
## C (Context & Why This Exists)

Di lingkungan Hermes, skill tidak diinjeksi secara penuh ke setiap chat baru untuk menghemat token konteks (progressive disclosure). Masalah skill tidak memuat atau menganggur (idle) disebabkan oleh:
1. **Skill Shadowing (Duplikasi Namespace)**: Keberadaan subfolder tiruan seperti `.agent/skills`, `.agents/skills`, `.cursor/skills`, dan `.kiro/skills` di dalam `skills/` yang menduplikasi nama folder kanonikal. Hermes menolak memuat skill yang ambigu (shares name and path in same tier).
2. **Pemicu Deskripsi Tidak Presisi**: Deskripsi frontmatter yang melebihi 60 karakter terpotong oleh sistem indeks prompt, atau menggunakan kalimat pasif bahasa Inggris sehingga gagal dicocokkan dengan intent obrolan alami pengguna.
3. **Keterbatasan Konteks On-Demand**: Model di giliran pertama tidak menyadari keberadaan skill kecuali dipanggil via `skill_view`, slash command bundle, atau hook sistem.

---
## C (Constraints & Operating Rules)
1. **Satu Direktori Kanonikal Tunggal**: Setiap modul skill hanya boleh memiliki satu path direktori fisik tunggal di bawah `skills/<nama-skill>/`. Bersihkan salinan bayangan di sub-tier.
2. **Batas Deskripsi Frontmatter 60 Karakter**: Atribut `description` wajib ringkas (maksimal 60 karakter, satu kalimat, pemicu di awal, diakhiri titik). Tempatkan kata kunci pencarian detail di dalam body dokumen.
3. **Pemuatan Berbasis Intent & Hook**: Gunakan plugin hook giliran pertama (`pre_llm_call`) atau bundle domain untuk menjamin skill inti aktif tanpa menunggu prompt eksplisit dari pengguna.
4. **Higiene Berkas Kunci**: Bersihkan file kunci basi (`.locks/`, `.git/index.lock`, `.usage.json.lock`) sebelum menjalankan pembaruan hub agar update tidak dilewati.

---
## When to Use
Gunakan modul ini saat:
- Skill yang baru dibuat atau diperbarui tidak terbaca di chat baru.
- Muncul peringatan sistem: `shares both its name and its path... cannot load it`.
- Banyak skill lokal terpasang tetapi tidak pernah dipanggil oleh agen (idle skills).
- Mengonfigurasi shortcut pemuatan cepat via Hermes Skill Bundles.

**Strong routing signals**: `skill persistence`, `skill tidak memuat`, `skill baru tidak muncul`, `skill shadowing`, `fix skill loading`, `skill bundle setup`.

---
## Do Not Use When
- Membuat modul rekayasa skill baru dari nol (Gunakan `spesialis-skills`).
- Tugas koding atau perancangan arsitektur aplikasi (Gunakan `pram-orchestrator`).

---
## Operating Steps

1. **Audit dan Bersihkan Direktori Bayangan (Shadow Directory Purge)**:
   - Pindai folder `skills/` untuk menemukan duplikasi di subfolder `.agent/`, `.agents/`, `.cursor/`, `.kiro/`.
   - Pastikan hanya satu direktori fisik kanonikal yang dipertahankan untuk setiap nama skill.
   - Verifikasi bahwa daftar peringatan duplikasi pada system prompt Hermes telah bersih.

2. **Sanitasi YAML Frontmatter (Trigger Optimization)**:
   - Pastikan atribut `name` sesuai nama folder (huruf kecil, strip biasa, tanpa tanda kutip).
   - Pastikan atribut `description` kurang dari sama dengan 60 karakter dengan pola: `Use when <kondisi>.`.
   - Tambahkan blok kata kunci bahasa Indonesia dan Inggris di bawah seksi `## When to Use` pada body dokumen.

3. **Petakan Domain ke Hermes Skill Bundles**:
   - Kelompokkan skill yang sering digunakan bersama ke dalam bundle domain di `C:\Users\HP\AppData\Local\hermes\skill-bundles`.
   - Contoh: Bundle `/backend` (8 skill), `/ml` (17 skill), `/research` (11 skill).
   - Pengguna cukup mengetik slash command bundle di awal chat baru untuk memuat seluruh armada skill sekaligus.

4. **Koneksikan ke Hook Pre-LLM Call (Deterministik)**:
   - Pastikan plugin seperti `pram_bootstrap` terpasang di `plugins/` dan aktif di `config.yaml`.
   - Hook `pre_llm_call` menyuntikkan arahan pemanggilan registry di giliran pertama setiap sesi chat baru.

5. **Pembaruan Aman & Higiene Kunci**:
   - Periksa ketiadaan berkas kunci `.locks/` atau `.git/index.lock`.
   - Jalankan pembaruan paksa terverifikasi via `hermes skills update --force`.

---
## O (Output Format & Definition of Done)
1. Modul skill tersimpan di `skills/skill-persistence/SKILL.md`.
2. Seluruh skill yang dipanggil via `skill_view` berhasil terbuka tanpa status ambigu atau shadowing error.
3. Tidak mengandung karakter tanda pisah em dash atau en dash.
4. Definisi selesai: Skill dapat diakses di sesi chat baru melalui intent alami maupun bundle slash command.
