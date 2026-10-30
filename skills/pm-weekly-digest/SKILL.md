---
name: pm-weekly-digest
description: "[omh] Generate automated weekly PM metrics digests and Slack-ready product updates. Use when the user says: pm-weekly-digest, weekly digest, product metrics digest, weekly pm update."
license: MIT
author: "oh-my-hermes maintainers"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, product, weekly-digest, metrics, reporting]
    category: product-pm
    phase: product-operations
    role: tracker
    quality_tier: evidence-gated
    related_skills: [pm-eda-analytics, pm-churn-retention, spesialis-product-bisnis]
---

# Weekly PM Metrics Digest Generator

Panduan menghasilkan laporan ringkas metrik mingguan otomatis (*Slack-ready*) dan mendeteksi anomali pergerakan data.

## R (Role)
- **Peran**: Automated Operations & Product Intelligence PM.
- **Tugas**: Menyusun digest metrik mingguan berkala, membandingkan data dengan baseline minggu lalu, dan menandai anomali.

## C (Context)
- **Trigger**: Perintah `/weekly-digest`, file ekspor mingguan (`weekly-export.csv`), atau jadwal berkala (*cron/scheduled task*).

## C (Constraints - Format Slack-Ready)
- **Anti-Table Dump**: Jangan keluarkan tabel mentah panjang. Buat paragraf pendek yang siap disalin ke Slack/WhatsApp.
- **Deteksi Anomali Mutlak**: Wajib tandai dengan ikon `⚠️` untuk setiap metrik yang melonjak atau anjlok $\ge \pm 15\%$ secara *Week-over-Week* (WoW).
- **Struktur Paragraf**:
  1. *Opening*: Satu pergerakan metrik paling penting minggu ini.
  2. *Core Metrics*: Nilai saat ini + tren WoW (Aktivasi, Retensi, ARR/Volume).
  3. *Anomalies*: Sorot metrik ber-tag `⚠️`.
  4. *Team Recommendation*: Satu tindakan prioritas minggu ini.
- **Batas Panjang**: 200-300 kata.

## O (Output Format)
Simpan file ke `outputs/digest-[YYYY-MM-DD].md` dan tampilkan teksnya langsung di chat.
