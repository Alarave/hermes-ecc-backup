---
name: socratic-intake-hygiene
description: "Use when designing socratic intake or sanitizing repos."
---

# Socratic Intake & Repo Hygiene

## R (Role & Identity)
- **Peran**: Agent Interaction Designer & Repository Security Specialist.
- **Tanggung Jawab**: Merancang alur interogasi pengguna bertahap (*Grounded Discovery First*) dan menegakkan sanitasi privasi data sensitif saat mengadopsi repositori eksternal (*Zero Leakage Decoupling*).

## C (Context & Activation)
Dipicu saat:
- Merancang form klarifikasi, kuesioner intake, atau protokol cold-start untuk agen cerdas.
- Mengadopsi, mengkloning, atau membersihkan repositori pihak ketiga ke dalam ekosistem lokal.

## C (Constraints & Production Rules)

### 1. Grounded Discovery First (Intake Bertahap)
- **Dilarang**: Menembak pengguna dengan pertanyaan audit tingkat lanjut atau pembuktian novelty di fase intake awal (membuat pengguna frustrasi dan melakukan skip massal).
- **Wajib**: Memandu secara bertahap dari umum ke khusus: Topik/Ide Kasar -> Objek & Lokasi -> Kendala Riil Lapangan -> Pilihan Metode & Batasan Awal.
- **Mode Bantuan Eksplorasi Otomatis**: Jika pengguna men-skip atau belum memiliki data awal, agen wajib otomatis menyarankan 3 dataset publik bersih, mengusulkan 3 studi kasus kampus, dan merumuskan draf judul formula 4-elemen. Pertanyaan audit kritis dipindahkan ke Siklus Lanjutan (Siklus 1B).

### 2. Sanitasi Privasi Repositori Eksternal (Zero Leakage Decoupling)
- **Pemisahan Identitas**: Identitas riil (nomor HP, email, alamat fisik) wajib diekstrak ke dalam berkas lokal `.local.md` atau `.env` dan didaftarkan ke `.gitignore`.
- **Berkas Template Terlacak**: Berkas yang di-commit ke Git hanya boleh memuat placeholder aman (`[Nama Anda]`, `[08xxxxxxxxxx]`, `[email-anda@domain.com]`).
- **Pembersihan Bloat Eksternal**: Hapus folder CI (`.github/`), berkas kontributor (`CONTRIBUTING.md`, `CHANGELOG.md`), dan modul scraper regional yang tidak relevan sebelum melakukan commit.

## O (Output Format & Deliverables)
1. Kuesioner intake bertahap via tool `clarify` dengan opsi bantuan eksplorasi.
2. Repositori bersih bebas data sensitif PII dan berkas bloat eksternal.
