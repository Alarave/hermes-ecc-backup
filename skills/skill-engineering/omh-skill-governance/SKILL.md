---
name: omh-skill-governance
description: "Use when standardizing skills to Oh My Hermes standard."
license: MIT
author: "oh-my-hermes maintainers"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, skills, rcco, standardization, governance]
    category: skill-engineering
    phase: lifecycle
    role: operator
    quality_tier: evidence-gated
    related_skills: [spesialis-skills, specialist-skill-architect, rules-distill]
---

# OMH Skill Governance & Standardization

SOP rekayasa dan standardisasi pustaka skill berskala masif agar memenuhi spesifikasi baku Oh My Hermes (OMH), arsitektur RCCO, dan standar tipografi mesin.

## Why This Exists

Pustaka skill berskala besar (500+ modul) sering mengalami degradasi akibat inkonsistensi metadata YAML, deskripsi tanpa pemicu intent, tautan referensi usang yang tidak eksis di disk, serta karakter Unicode non-standar (em-dash dan en-dash) yang menggagalkan parser lintas platform. Skill ini menyediakan alur kerja deterministik untuk audit, pembersihan, dan validasi mutu otomatis.

## When to Use

- Merapikan berkas `SKILL.md` agar mematuhi standar metadata Oh My Hermes.
- Mengeliminasi karakter terlarang em dash dan en dash dari repositori.
- Memperbaiki peringatan linter `validate_skill.py` (Broken references, missing triggers, unquoted names).
- Menjalankan audit kepatuhan pustaka skill lintas gelombang (wave execution).
- Strong routing signals: `omh-skill-governance`, `standardisasi skill`, `audit skill omh`, `bersihkan skill md`.

## Do Not Use When

- Membuat fitur aplikasi baru: gunakan `orch-add-feature` atau `pram-orchestrator`.
- Debugging logika kode aplikasi: gunakan `systematic-debugging`.
- Mendesain arsitektur skill dari nol tanpa basis berkas: gunakan `spesialis-skills`.

## Operating Steps

### 1. Discovery & Inventarisasi
Pindai direktori pustaka skill dan klasifikasikan berkas berdasarkan klaster domain (Gelombang/Wave):
- Catat modul yang memiliki karakter em dash (`\u2014`) atau en dash (`\u2013`).
- Catat modul yang tidak memiliki klausul pemicu baku `Use when the user says: ...`.
- Batasi ukuran gelombang kerja antara 20 hingga 40 modul per putaran agar tidak memicu context overflow.

### 2. Normalisasi Frontmatter YAML OMH
Pastikan struktur metadata YAML memenuhi kontrak:
- `name`: Ditulis polos tanpa tanda petik ganda atau tunggal (`name: my-skill`), wajib identik 1:1 dengan nama folder direktori kanonikal.
- `description`: Ditulis dalam satu baris utuh (hindari blok skalar `|` atau `>`). Wajib diawali tag `[omh]` dan diakhiri klausul `Use when the user says: ...`.
- `metadata.hermes`: Wajib memuat `tags`, `category`, `phase`, `role`, `quality_tier`, dan `related_skills`.

### 3. Sanitasi Tipografi Mutlak (Zero Dash)
Ganti seluruh karakter Unicode tanda pisah:
- Ganti spasi em dash atau en dash menjadi `: ` untuk pemisah klausa utama.
- Ganti tanda pisah pada poin daftar atau tabel menjadi strip biasa (`-`) atau kurung `()`.
- Hindari menyisakan karakter byte Unicode U+2014 atau U+2013 pada seluruh baris berkas.

### 4. Resolusi Integritas Referensi Fisik
Periksa setiap rujukan berkas internal di dalam teks:
- Berkas di bawah `references/` wajib eksis secara fisik di disk direktori lokal modul terkait. Buang daftar referensi usang yang tidak memiliki berkas fisik.
- Hindari tautan markdown eksternal yang memuat substring `references/<file>.md` (seperti `../shared-references/`) untuk mencegah false positive pada parser linter lokal.

### 5. Verifikasi Mesin (Machine Seal)
Jalankan pengujian kepatuhan pada setiap modul yang dimodifikasi:
- Jalankan `python skills/specialist-skill-architect/scripts/validate_skill.py skills/<nama-skill>`.
- Wajib mencapai status `[PASS 100/100]` tanpa peringatan (0 errors, 0 warnings).

## Completion Checklist

- [ ] Frontmatter YAML valid, unquoted name, deskripsi satu baris dengan pemicu baku.
- [ ] 0 kemunculan karakter Unicode em dash dan en dash terverifikasi regex.
- [ ] Seluruh berkas referensi fisik terverifikasi eksis di disk (tidak ada broken reference).
- [ ] Pengujian `validate_skill.py` menghasilkan skor `[PASS 100/100]`.
- [ ] Komit Git lokal dibuat dengan format bahasa Indonesia standar (`rapihan:`).

## Recovery Notes

- **Berkas Berukuran Besar (>100 KB / >1.500 baris)**: Selesaikan kasus batas (edge cases) tanda pisah terisolasi (seperti awalan baris atau akhir baris) secara spesifik terlebih dahulu sebelum menerapkan penggantian massal pada pola spasi umum untuk mencegah timeout.
- **Name Mismatch Warning**: Jika linter melaporkan ketidakcocokan nama frontmatter dengan folder, selaraskan nama kunci `name` mengikuti basename direktori tanpa mengubah path fisik.
