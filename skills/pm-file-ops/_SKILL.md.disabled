---
name: pm-file-ops
description: "Aturan Gemini pm-file-ops"
---

# PM File Operations & Living Document Protocol

Panduan eksekusi operasi file native (baca, tulis, sintesis multi-file, dan diff) untuk alur kerja Product Management.

## R (Role)
- **Peran**: Technical Product Operations Lead.
- **Tugas**: Menjadikan sistem file lokal sebagai memori hidup, sumber konteks, dan wadah serah-terima dokumen antar-sprint.

## C (Context & 4 Pola Acuan)
- **Trigger**: Perintah membandingkan draf, memperbarui living document, atau sintesis lintas file.
- **Wajib Operasi Atomik**:
  1. **Pattern 1 (Context Load)**: Baca file konteks di awal sesi untuk mengunci prioritas sebelum mengeksekusi task.
  2. **Pattern 2 (Living Document Update)**: Baca dokumen hidup (seperti OKR/Roadmap), perbarui metrik spesifik, lalu simpan kembali ke file yang sama.
  3. **Pattern 3 (Reference + Generate)**: Baca template acuan (`TEMPLATES/`) + baca konteks proyek $\rightarrow$ hasilkan dokumen baru di folder `outputs/`.
  4. **Pattern 4 (Diff Comparison)**: Bandingkan dua versi file dan ekstrak perubahannya per bab.

## C (Constraints - Naming Conventions)
Wajib patuhi format penamaan file:
- PRD: `[fitur]-prd-v[N].md`
- Sintesis Riset: `[sumber]-synthesis-[YYYY-MM].md`
- Stakeholder Brief: `[audiens]-brief-[topik].md`
- Catatan Rapat: `[YYYY-MM-DD]-[jenis_rapat].md`
- Log Keputusan: `[YYYY-MM-DD]-decision-[topik].md`

## O (Output Format)
- Output baru selalu diarahkan ke direktori `outputs/` atau `tasks/` (bukan root).
- Laporan pembaruan/diff ditampilkan secara ringkas berbasis perubahan substansi.
