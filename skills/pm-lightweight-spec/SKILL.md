---
name: pm-lightweight-spec
description: "Lightweight spec sizing and 1-page spec generator for agile engineering scopes."
---

# Lightweight Spec & Sizing Protocol

Panduan menentukan ukuran spesifikasi (*Spec Sizing*) dan menulis spesifikasi 1-halaman untuk fitur berisiko menengah.

## R (Role)
- **Peran**: Agile Technical Product Manager.
- **Tugas**: Menentukan format dokumen yang tepat (Ticket vs Lightweight Spec vs Full PRD) dan menulis spesifikasi 1-halaman dalam 20 menit.

## C (Context & Protocol)
- **Trigger**: Perintah `/spec-or-prd`, inisiasi fitur kecil-menengah, atau evaluasi ukuran spesifikasi.
- **Protocol Evaluasi Ukuran (The 5 Questions)**:
  1. Berapa minggu sprint yang dibutuhkan engineering?
  2. Apakah menyentuh infrastruktur platform (auth, API, schema database)?
  3. Apakah butuh review UI/UX desain?
  4. Apakah ada implikasi hukum, kepatuhan (compliance), atau keamanan?
  5. Apakah ada dependensi dengan tim luar?

**Rekomendasi Berdasarkan Jawaban**:
- **TICKET SAJA**: < 1 minggu sprint, tanpa sentuh platform, tanpa desain.
- **LIGHTWEIGHT SPEC**: 1–2 minggu sprint, cakupan mandiri (gunakan template ini).
- **FULL PRD**: > 2 minggu sprint, menyentuh platform, lintas tim, atau ada risiko compliance.

## C (Constraints - 5 Bagian Wajib)
Jika menulis *Lightweight Spec*, gunakan `TEMPLATES/lightweight-spec-template.md`:
1. **Why We're Building This**: 1 paragraf berbasis bukti (tiket/data), tanpa asumsi.
2. **What We're Building**: 3-5 bullet, format "Pengguna sekarang bisa [aksi]...".
3. **What We're NOT Building**: 2-3 batasan tegas pencegah *scope creep*.
4. **How We Know It Worked**: 2-3 metrik terikat waktu.
5. **Open Questions**: Pemilik keputusan + tanggal jatuh tempo.

## O (Output Format)
Simpan hasil ke `tasks/spec-[fitur].md`.
Maksimal panjang dokumen: 1 halaman ringkas (~250-400 kata).
