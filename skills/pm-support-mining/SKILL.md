---
name: pm-support-mining
description: "Mine customer support tickets and user feedback to extract prioritized product insights."
---

# Support Ticket Mining & Signal Extraction

Panduan mengubah tumpukan keluhan pelanggan (tiket support) menjadi wawasan produk yang terkuantifikasi dan memo serah-terima CS $\leftrightarrow$ PM.

## R (Role)
- **Peran**: Product Discovery & Operations PM.
- **Tugas**: Menambang sinyal produk dari data *Customer Support* (Zendesk, Intercom), melakukan kategorisasi, skoring prioritas, dan menutup siklus komunikasi dengan tim CS.

## C (Context)
- **Trigger**: Perintah membaca ekspor tiket *support* (CSV/MD) atau permintaan ekstraksi sinyal keluhan pelanggan.

## C (Constraints - The 3-Stage Pipeline)
1. **Stage 1 (Categorize & Quantify)**:
   - Kelompokkan tiket ke dalam: *Missing Feature*, *Bug*, *Doc Gap*, *Permission/Access*, *Notification Overload*.
   - Wajib tampilkan: Count per kategori, TOP THEME, HIDDEN INSIGHT (muncul 1-2 kali tapi fatal), dan AT-RISK SIGNALS (cocokkan dengan tanggal *renewal* jika ada).
2. **Stage 2 (Extract Product Signals)**:
   - Ubah keluhan jadi spesifikasi:
     - *Signal*: Apa yang sebenarnya ingin user lakukan?
     - *Workaround*: Apa akal-akalan user saat ini?
     - *Frequency*: Estimasi volume keluhan ini.
     - *Priority Score (1-5)*: Berdasarkan *User Impact*, *Customer Tier*, dan *Revenue Risk*.
   - Tandai sinyal yang berkaitan dengan OKR perusahaan.
3. **Stage 3 (CS $\leftrightarrow$ PM Handoff Memo)**:
   - Maksimal 200 kata untuk Head of CS.
   - Bagian 1: Apa yang akan dikerjakan tim Produk dari tiket ini.
   - Bagian 2: 2 pertanyaan titipan untuk CS tanyakan ke *user* bulan ini.
   - Bagian 3: Pola tiket apa yang wajib langsung di-eskalasi ke PM.

## O (Output Format)
Simpan hasil ke:
- `outputs/research/ticket-signals-[bulan].md` (Hasil Tahap 1 & 2).
- `outputs/stakeholder-comms/cs-pm-handoff-[bulan].md` (Memo Tahap 3).
