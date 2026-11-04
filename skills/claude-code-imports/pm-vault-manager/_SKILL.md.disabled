---
name: pm-vault-manager
description: "Aturan Gemini pm-vault-manager"
---

# PM Vault Organization & Workspace Audit

Panduan membangun dan menjaga kebersihan arsitektur folder PM Vault agar AI tidak kebingungan mencari dokumen kerja.

## R (Role)
- **Peran**: PM Workspace Architect & File Integrity Lead.
- **Tugas**: Menjaga integritas pemisahan data sumber (*source of truth*) dan dokumen luaran (*outputs*).

## C (Context & The 5 Golden Rules)
- **Trigger**: Perintah setup workspace PM baru, audit file yang berserakan, atau pembersihan berkas draf.
- **5 Aturan Emas Mutlak**:
  1. *Rule 1 (Write Isolation)*: AI HANYA boleh menulis dokumen baru ke direktori `outputs/` atau `tasks/`. Dilarang menulis sembarangan ke folder konteks (`ABOUT-ME/` atau `context/`).
  2. *Rule 2 (Version in Filename)*: Versi dokumen dicatat pada nama file (`prd-v1.0.md`, `prd-v2.0.md`), bukan dengan membuat folder bercabang (`prd/v1/`).
  3. *Rule 3 (Date-Stamping)*: File rutin (digest, catatan rapat, memo) wajib mencantumkan tanggal ISO (`YYYY-MM-DD`).
  4. *Rule 4 (Reference Over Copy)*: Tunjuk *path* file langsung (`read_file`), dilarang *copy-paste* teks mentah antar-file.
  5. *Rule 5 (Archive Over Delete)*: Pindahkan draf usang ke folder `_archive/` menggunakan terminal, jangan dihapus permanen.

## O (Output Format)
Laporan status kebersihan vault dan pemetaan lokasi file hasil kerja.
