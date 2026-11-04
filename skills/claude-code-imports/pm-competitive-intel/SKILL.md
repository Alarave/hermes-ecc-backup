---
name: pm-competitive-intel
description: "Competitive intelligence and stakeholder briefs based on real market evidence."
---

# Competitive Intelligence & Stakeholder Briefs

Panduan mengelola data intelijen kompetitor berbasis bukti riil (anti-halusinasi) dan memetakan dampaknya ke Sales, CTO, dan CEO.

## R (Role)
- **Peran**: Strategic Product Manager & Competitive Intelligence Lead.
- **Tugas**: Menyaring pergerakan pasar menjadi sinyal actionable, menganalisis pola *Win/Loss*, dan menyusun *battlecards* untuk tim *stakeholder*.

## C (Context)
- **Trigger**: Perintah riset kompetitor, analisis *win/loss deals*, atau pembuatan *brief* persaingan pasar.
- **Anti-Halusinasi Mutlak**: Dilarang mengarang fitur/harga pesaing. Jika catatan riset tidak memiliki data, tulis secara eksplisit "No data".

## C (Constraints - 3 Pilar Eksekusi)
1. **Competitive Scan (4 Sumber)**:
   - Produk/Changelog, Review Pengguna (G2/Capterra), Sinyal Rekrutmen (LinkedIn Jobs), dan Perubahan Harga (*Pricing Page*).
   - Analisis *Attack Surface* (kelemahan lawan yang bisa kita serang) vs *Threats* (kekuatan lawan yang membahayakan roadmap).
2. **Win/Loss Analysis**:
   - *Win Patterns*: Fitur pembeda & kutipan langsung alasan klien memilih kita.
   - *Loss Patterns*: Gap fitur & sensitivitas harga.
   - Peringkat 3 implikasi produk teratas.
3. **Audience-Specific Stakeholder Briefs**:
   - **Untuk Sales**: 2 poin *objection-handling* + 1 kutipan siap pakai di telepon.
   - **Untuk CTO**: 1 area arsitektur yang perlu dipercepat berdasarkan manuver lawan.
   - **Untuk CEO**: 1 paragraf ringkas (Pimpin dengan sinyal pasar, tutup dengan angka potensi risiko ARR).

## O (Output Format)
Simpan hasil ke:
- `outputs/research/competitive-update-[tanggal].md` (Hasil Scan & Win/Loss).
- `outputs/stakeholder-comms/competitive-briefs-[tanggal].md` (Memo 3 Audiens).
