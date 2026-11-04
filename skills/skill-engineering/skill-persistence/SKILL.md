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
3. **Universal Intent Interceptor Per-Turn**: Hook `pre_llm_call` wajib aktif memindai pesan pengguna pada SETIAP giliran (bukan hanya giliran pertama). Interceptor memetakan 12 domain taksonomi dan mencocokkan nama fisik skill eksak pada disk.
4. **Injeksi Direktif Pengikat Mutlak**: Ketika intent cocok, hook wajib menyuntikkan blok direktif `<PERINTAH_ORCHESTRASI_SKILL_MUTLAK>` yang melarang agen merespons atau koding sebelum memanggil `skill_view` untuk spesialis domain terkait.
5. **Higiene Berkas Kunci**: Bersihkan file kunci basi (`.locks/`, `.git/index.lock`, `.usage.json.lock`) sebelum menjalankan pembaruan hub agar update tidak dilewati.
6. **Anti-Reset Format & Integrasi Brief Proyek**: Saat pengguna mendefinisikan aturan naskah atau format penulisan (seperti standar Gunadarma 4-4-3-3, Harvard 'dkk.', anti-slop kurung), aturan tersebut wajib diintegrasikan ke 3 titik: 1) Tambahkan kata kunci pemicu 'brief', 'paper', 'proposal', 'format penulisan' pada deskripsi YAML frontmatter, 2) Kunci di hook giliran pertama (`pram_bootstrap`) agar terbaca di semua chat baru, 3) Rekonsiliasikan ke gerbang G0/G1 `pram-orchestrator` agar pembuatan folder brief proyek baru otomatis mematuhi format tanpa pengguna mengulang instruksi.

---
## When to Use
Gunakan modul ini saat:
- Skill yang baru dibuat atau diperbarui tidak terbaca di chat baru.
- Muncul peringatan sistem: `shares both its name and its path... cannot load it`.
- Banyak skill lokal terpasang tetapi tidak pernah dipanggil oleh agen (idle skills).
- Mengonfigurasi shortcut pemuatan cepat via Hermes Skill Bundles.
- Menyinkronkan seluruh pustaka skill Hermes agar terbaca otomatis di Antigravity (Hub, CLI, IDE).

**Strong routing signals**: `skill persistence`, `skill tidak memuat`, `skill baru tidak muncul`, `skill shadowing`, `fix skill loading`, `skill bundle setup`, `sinkron skill antigravity`.

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
   - Contoh: Bundle `/backend` (8 skill), `/ml` (20 skill terintegrasi multimodal vision-language), `/research` (11 skill).
   - Pengguna cukup mengetik slash command bundle di awal chat baru untuk memuat seluruh armada skill sekaligus.

4. **Koneksikan ke Universal Intent Interceptor (`pre_llm_call`)**:
   - Pasang interceptor real-time di `plugins/pram_bootstrap/__init__.py`.
   - Pada giliran pertama (`is_first_turn`), suntikkan hierarki orkestrasi lengkap dan tabel anti-alibi.
   - Pada setiap giliran berpesan (`user_message`), jalankan `detect_skill_intent(user_message)`:
     - Lapisan 1: Pindai 12 taksonomi domain berdasarkan leksikon kata kunci dwibahasa.
     - Lapisan 2: Pindai nama fisik skill eksak yang terdaftar di direktori `skills/`.
   - Jika terdeteksi, suntikkan blok `<PERINTAH_ORCHESTRASI_SKILL_MUTLAK>` yang mewajibkan `skill_view("<nama-skill>")` sebelum agen memberikan jawaban atau koding.

5. **Pembersihan Direktori Read-Only pada Windows**:
   - Saat memindahkan atau menghapus direktori bayangan duplikat pada host Windows, berkas sering kali memiliki atribut read-only yang memicu penolakan izin `shutil.rmtree` atau rebase error.
   - Gunakan handler izin eksplisit `os.chmod(path, stat.S_IWRITE)` pada setiap berkas sebelum penghapusan.

6. **Pembaruan Aman, Rekonsiliasi Remote & Higiene Kunci**:
   - Periksa ketiadaan berkas kunci `.locks/` atau `.git/index.lock`.
   - Jika `git push` ditolak karena remote memiliki commit berkala otomatis (`.state/last_evolution.txt`), lakukan `git fetch origin main` lalu `git merge origin/main --no-edit` secara bersih sebelum mendorong kembali.
   - Jalankan pembaruan paksa terverifikasi via `hermes skills update --force`.

7. **Sinkronisasi Multi-Agen Antigravity (Hub 2.0, CLI, IDE)**:
   - Antigravity memindai skill via `~/.gemini/config/skills.json` secara 1-tingkat (`skills/<nama>/SKILL.md`). Skill bersarang (`category/skill-name/SKILL.md`) wajib dibuatkan junction tingkat atas agar terdeteksi.
   - Sambungkan direktori CLI via junction NTFS: `~/.gemini/antigravity-cli/skills` -> `AppData/Local/hermes/skills`.
   - Daftarkan direktori master Hermes, direktori Antigravity, serta seluruh subfolder kategori OMH (`~/.omh/skills/<kategori>`) ke dalam `~/.gemini/config/skills.json`.
   - Jalankan `sync_skills.py` untuk menyalin berkas skill ke `~/.gemini/config/skills/`, `~/.gemini/antigravity-ide/skills/`, dan mengekstrak aturan markdown tanpa frontmatter ke `~/.gemini/config/rules/*.md`.

---
## O (Output Format & Definition of Done)
1. Modul skill tersimpan di `skills/skill-persistence/SKILL.md`.
2. Seluruh skill yang dipanggil via `skill_view` berhasil terbuka tanpa status ambigu atau shadowing error.
3. Tidak mengandung karakter tanda pisah em dash atau en dash.
4. Definisi selesai: Skill dapat diakses di sesi chat baru melalui intent alami maupun bundle slash command.
