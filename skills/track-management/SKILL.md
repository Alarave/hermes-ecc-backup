---
name: track-management
description: "Use when user says 'bikin fitur baru', 'fix bug ini', 'track issue', 'buat spesifikasi track', atau manajemen pelacakan tiket perbaikan sistem."
---

# Track Management (Feature & Bug Tracking)

Skill ini memandu pembuatan, pengelolaan, dan penyelesaian unit kerja logis (disebut "Tracks") untuk fitur baru, perbaikan bug, atau refaktor, menggunakan sistem `spec.md` dan `plan.md`.

## Konsep Dasar (The Track Lifecycle)
Setiap pekerjaan (Track) harus melewati fase yang jelas:
1. **Creation**: Membuat direktori/struktur track baru.
2. **Specification (`spec.md`)**: Apa yang akan dibuat dan kriteria penerimaannya.
3. **Planning (`plan.md`)**: Bagaimana cara membuatnya (Langkah-langkah teknis).
4. **Execution**: Menjalankan langkah-langkah di `plan.md`.
5. **Completion**: Memverifikasi hasil dan menutup track.

## Hubungan dengan Arsitektur Pram (RCCO & Pipeline G0-G4)
- Jika **PRD** dan **WBS** memetakan keseluruhan proyek (Makro), maka **Track** (`spec.md` & `plan.md`) memetakan implementasi satu fitur spesifik atau *bugfix* (Mikro).
- **Semua Track** harus didaftarkan pada file `tracks.md` di *root* dokumentasi proyek agar mudah dilacak.

## Aturan Spesifikasi (`spec.md`)
Setiap track wajib memiliki `spec.md` dengan isi:
- **Title & Context**: Apa yang mau dicapai?
- **Goals & Non-Goals**: Apa yang masuk lingkup kerja dan apa yang dilarang.
- **Acceptance Criteria**: Syarat mutlak agar fitur dianggap selesai.
- **Dependencies**: Hal yang menghambat/memblokir pengerjaan ini.

## Aturan Perencanaan (`plan.md`)
Setelah `spec.md` disetujui, buat `plan.md` dengan format *checklist* (`[ ]`):
- Pecah implementasi menjadi langkah-langkah *atomic* (kecil dan dapat diuji).
- Berikan status pada checklist (`[x]` untuk selesai, `[ ]` untuk belum).
- Jangan menulis kode sebelum seluruh `plan.md` dikonfirmasi masuk akal.

## Manajemen Status (Tracking)
Gunakan status di `tracks.md` untuk memonitor:
- 📝 `DRAFT` : Sedang menyusun spesifikasi
- ⏳ `READY` : Spesifikasi dan Rencana siap dieksekusi
- 🚀 `IN PROGRESS` : Sedang dikerjakan
- 🚧 `BLOCKED` : Menunggu dependensi atau keputusan
- ✅ `DONE` : Telah diuji dan diverifikasi

## Anti-Halusinasi
- Jangan mengubah status menjadi `DONE` sebelum *Acceptance Criteria* di `spec.md` diuji secara nyata dan melewati *Independent Audit*.
- Jika ada kebuntuan saat eksekusi (kode tidak jalan), ubah status `plan.md` dan tuliskan *Root Cause Analysis* di dalam track tersebut.
