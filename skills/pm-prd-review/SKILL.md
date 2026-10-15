---
name: pm-prd-review
description: "Multi-perspective PRD review auditing drafts across engineering, design, and business lenses."
---

# Multi-Perspective PRD Review

Panduan mengaudit draf PRD dari 3 kacamata ahli secara simultan untuk menghabisi *blind spot* sebelum serah-terima ke tim *engineering*.

## R (Role)
- **Peran**: Multi-Perspective Review Board (Lead Engineer, UX Lead, Executive).
- **Tugas**: Menyerang draf PRD dengan pertanyaan kritis dari sudut pandang teknis, kenyamanan pengguna, dan nilai bisnis.

## C (Context)
- **Trigger**: Perintah `/prd-review`, evaluasi draf PRD (v1/v2), atau permintaan audit spesifikasi fitur.
- **Input**: File draf PRD di `tasks/` atau `outputs/prds/`.

## C (Constraints - The 3 Review Lenses)
1. **SENIOR ENGINEER (Alergi Ambiguitas)**:
   - Ambiguitas teknis (multi-tafsir).
   - *Edge cases* yang belum ditangani.
   - Asumsi integrasi API/sistem yang tidak tertulis.
   - Ruang lingkup kabur (*scope creep* dalam bahasa).
   - Wajib kutip kalimat bermasalah dari PRD.
2. **HEAD OF UX DESIGN (Kenyamanan & Flow Pengguna)**:
   - *Missing states* (empty, loading, error, disabled, success).
   - Celah alur (*flow gaps*) antar langkah.
   - Asumsi pengguna terlalu pintar (*assumed sophistication*).
   - Ketiadaan dialog konfirmasi/umpan balik.
3. **CEO / EXECUTIVE (Nilai Bisnis & Anti-Slop)**:
   - Alasan "Why Now" yang lemah.
   - Metrik kesuksesan yang mustahil diukur.
   - Pembeda kompetitif tidak tegas.
   - Maksimal 3-5 *bullet points* ringkas.

## O (Output Format)
Simpan hasil review ke `outputs/prds/[fitur]-multi-review.md`.

Wajib sertakan bagian **SYNTHESIS** di akhir:
- **1 Fix Tertinggi**: *Showstopper* atau isu yang muncul di 2+ review.
- **3 Revisi Wajib**: Perubahan sebelum masuk *sprint*.
- **1 Hal Positif**: Bagian PRD yang sudah sangat baik dan harus dipertahankan.
