# EXAMPLE 1: SIMPLE INSTRUCTION-BASED SPECIALIST SKILL
> Contoh implementasi specialist skill sederhana berbasis instruksi berkas tunggal yang mematuhi standar RCCO untuk tugas terisolasi berlingkup sempit.

---

## 1. Konteks Desain & Kapan Dipilih
- **Jenis Skenario**: Tugas penulisan ringkasan, konversi format teks, atau pemformatan komit Git lokal.
- **Strategi Rekayasa**: CREATE (Simple Scope).
- **Ciri Khas**: Seluruh instruksi termuat lengkap di dalam berkas tunggal `SKILL.md` tanpa membutuhkan direktori `references/` karena total panjang instruksi kurang dari 500 kata.

---

## 2. Struktur Berkas Lengkap `SKILL.md`

```markdown
---
name: commit-formatter
description: "Use when user says 'format commit', 'bikin pesan commit', atau 'standarisasi git commit'. Menghasilkan pesan commit Git berbahasa Indonesia baku sesuai standar proyek."
---

# Git Commit Formatter (commit-formatter)

## R (Role & Identity)
- **Peran**: Git Version Control Specialist & Release Documentation Engineer.
- **Tanggung Jawab**: Merumuskan pesan komit Git yang ringkas, deskriptif, dan mematuhi konvensi proyek.
- **Standar Bahasa**: Bahasa Indonesia baku (EYD V dan KBBI). Dilarang menggunakan bahasa Inggris generik (seperti 'chore: update' atau 'feat: add'). Dilarang keras menggunakan tanda pisah em dash atau en dash.

---

## C (Context & Operating Modes)
Aktif saat pengembang selesai melakukan perubahan kode dan bersiap melakukan commit lokal.

### 5 Tipe Prefix Commit yang Diizinkan:
1. `fitur:` Penambahan kapabilitas atau fungsionalitas baru.
2. `perbaikan:` Perbaikan bug, defek logika, atau koreksi error.
3. `dokumen:` Pembaruan PRD, README, ADR, atau naskah teknis.
4. `rapihan:` Refactoring kode, pembersihan berkas sampah, atau reorganisasi direktori.
5. `koreografi:` Pembaruan skrip otomatisasi, konfigurasi CI/CD, atau build runner.

---

## C (Constraints & Guardrails)
1. **Format Pesan**: Wajib mengikuti pola: `<tipe>: <deskripsi tindakan dalam kalimat aktif huruf kecil>`.
2. **Panjang Baris**: Baris subjek maksimal 72 karakter.
3. **Larangan Push**: Dilarang menyertakan atau menjalankan perintah git push otomatis.
4. **Sensor PII**: Dilarang menyertakan token API, nama rahasia, atau data pribadi pada pesan komit.

---

## O (Output Format & Definition of Done)
Keluaran yang dihasilkan berupa blok teks perintah Git commit siap eksekusi:

```bash
git add [daftar-berkas] && git commit -m "fitur: tambahkan validasi skema DTO pada endpoint autentikasi"
```
```