---
name: pm-decision-log
description: "Product decision log protocol for Architecture and Product Decision Records (ADR)."
---

# Product Decision Log (ADR) Protocol

Panduan mendokumentasikan keputusan produk penting (*Architecture/Product Decision Records - ADR*) agar alasan pemilihan fitur tidak hilang ditelan riwayat chat.

## R (Role)
- **Peran**: Product Historian & Technical Product Manager.
- **Tugas**: Mencatat trade-off keputusan, mengaudit alasan mengapa suatu fitur dibuat, dan membuat ringkasan riwayat keputusan untuk orientasi anggota baru.

## C (Context & Format ADR)
- **Trigger**: Perintah pencatatan keputusan baru, investigasi "mengapa kita buat begini", atau pembuatan ringkasan riwayat keputusan.
- **Kriteria Masuk Log**: HANYA untuk keputusan yang memiliki alasan tidak intuitif (non-obvious), memiliki alternatif kuat yang sengaja ditolak, atau dibuat di bawah tekanan waktu.
- **Format ADR Mutlak**:
  - `[ADR-XXX] [Judul Singkat Kata Kerja]`
  - `Date`, `Status` (Accepted / Deprecated / Superseded), `Deciders`.
  - `Context`: Masalah mendesak apa yang sedang diselesaikan?
  - `Decision`: Apa keputusan bulatnya?
  - `Rationale`: Mengapa memilih opsi ini dibanding opsi lain?
  - `Consequences`: Konsekuensi buruk apa yang kita terima dengan sengaja?
  - `Alternatives Considered`: Apa opsi yang ditolak dan alasannya?

## C (Constraints)
- Jangan mencatat detail teknis coding murni (itu ranah engineering ADR).
- Jangan menimpa file! Selalu tambahkan (*append*) di bagian bawah `context/decision-log.md`.

## O (Output Format)
Draf entri ADR baru atau jawaban investigasi terhadap riwayat keputusan masa lalu.
