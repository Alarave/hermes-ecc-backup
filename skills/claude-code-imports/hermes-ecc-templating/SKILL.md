---
name: hermes-ecc-templating
description: Gunakan saat membuat repo template Hermes yang aman data.
---

# Hermes ECC Repository Templating

## R (Role)
- Spesialis Pemaketan & Keamanan Repositori Hermes.

## C (Context)
- Mempersiapkan konfigurasi lokal Hermes Agent (`skills`, `profiles`, `memories`, `cron`) untuk di-push ke Git (GitHub/GitLab) sebagai *Starter Kit* / *Template Repository* agar bisa digunakan orang lain tanpa mengekspos data pribadi.

## C (Constraints & Guardrails)
- **Pembersihan Kredensial**: JANGAN PERNAH men-track `auth.json`, `.env`, `state.db` (riwayat chat), atau `projects.db`.
- **Konfigurasi & Memori**: Jangan commit `config.yaml`, `profile.yaml`, `SOUL.md`, atau isi folder `memories/`. Buat versi `.example` (misal `config.example.yaml` dan `memories-template/USER.example.md`) dengan placeholder `[Nama Anda]`. Hapus semua API Key.
- **Profil Tambahan**: Folder `profiles/<nama_profil>/` berisi database dan kredensial independen. Pindahkan struktur amannya ke `profiles-template/<nama_profil>/`.
- **Cron Jobs**: `cron/jobs.json` sering menyimpan target pengiriman pribadi (seperti nomor WhatsApp di `deliver:`). Jangan commit `cron/`. Buat `cron-template/jobs.example.json`.
- **Purge History**: Jika info sensitif terlanjur di-commit, reset riwayat menggunakan *orphan branch* (`git checkout --orphan temp`) lalu `git push -f` untuk memusnahkan jejak.
- **Metadata Kategori**: File `DESCRIPTION.md` di dalam folder kosong di `skills/` hanyalah metadata kategori UI Hermes, bukan skill error/kosong. Hapus jika membingungkan.

## O (Output)
- Struktur repo yang steril, dilengkapi `setup.ps1` atau `install.sh` untuk menyalin folder `*-template` dan file `.example` ke jalur aktifnya saat user baru melakukan instalasi.
