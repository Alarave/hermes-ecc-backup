# Template Standar Industri: Product Requirements Document (PRD)

Template PRD ini merupakan standar modern perusahaan teknologi top (mengadaptasi kerangka kerja Pendo.io 2025, Figma, dan Y Combinator). Berbeda dengan SRS yang fokus pada teknis/koding, PRD ini berfokus pada **Nilai Bisnis, Pengguna, dan Strategi Rilis**.

Pram wajib menyusun dokumen ini SEBELUM membuat Project Charter dan SRS.

---

# PRODUCT REQUIREMENTS DOCUMENT (PRD)
## [Nama Fitur / Produk]

**Status Dokumen**: [Draft / In Review / Approved]
**Product Manager**: [Nama Anda / Pram]
**Target Rilis**: [Bulan Tahun / Q1 2026]

---

## BAGIAN 1: OVERVIEW & STRATEGI BISNIS

### 1.1 Mission (Elevator Pitch)
- Jelaskan dalam 1-2 kalimat (Maksimal 30 kata) apa produk ini dan apa kegunaannya. Singkat, spesifik, dan berorientasi pada nilai (*value-driven*).

### 1.2 Problem Statement (Masalah Saat Ini)
- Deskripsikan *pain points* (titik sakit) pelanggan saat ini.
- Mengapa masalah ini penting untuk diselesaikan oleh bisnis kita? Apa dampaknya jika dibiarkan?

### 1.3 Target Audience & Personas
- Siapa pengguna utama produk ini? (Contoh: Kader Posyandu usia 30-50 tahun dengan literasi digital menengah).

### 1.4 Jobs To Be Done (JTBD)
Gunakan rumus JTBD modern dari Silicon Valley:
> *As an [Peran Pengguna], I want to [Tindakan], so I can [Hasil yang diharapkan].*
> *Today, [Pengguna] has to [Cara manual saat ini] which costs [Waktu/Biaya/Tenaga].*

### 1.5 Outcomes & Telemetry (Metrik Keberhasilan)
Daftar KPI dan metrik analitik (*telemetry*) yang akan dilacak untuk membuktikan fitur ini sukses:
- **Business Metric**: (Misal: Kenaikan retensi user 15%).
- **Product/Telemetry Metric**: (Misal: Waktu rata-rata pengisian form dari 5 menit menjadi 30 detik. *Click-through rate* tombol X mencapai 40%).

---

## BAGIAN 2: SOLUSI PRODUK

### 2.1 Ideal State (Visi Solusi)
- Bagaimana alur pengguna (*User Flow*) setelah produk ini dirilis? Gambarkan secara singkat.

### 2.2 Daftar Fitur Utama (Features & Functionalities)
Daftar prioritas fitur tingkat tinggi. (Rincian teknis kodingnya akan dijabarkan di dokumen SRS terpisah).
- **[P1 - Must Have]**: Nama Fitur - Alasan kenapa fitur ini wajib ada di Versi 1.0.
- **[P2 - Should Have]**: Nama Fitur - Alasan.
- **[P3 - Nice to Have]**: Nama Fitur - Bisa ditunda ke *update* berikutnya.

### 2.3 Out of Scope (Di Luar Lingkup)
- Sebutkan secara eksplisit apa yang **TIDAK AKAN** dibangun di versi ini agar tim tidak kebingungan.

### 2.4 Alternatives Considered (Alternatif yang Ditolak)
- Apa solusi lain yang sempat dipikirkan? (Contoh: "Kami sempat berpikir pakai WhatsApp Bot saja, tapi ditolak karena privasi data tidak aman."). Kenapa solusi yang dipilih di PRD ini lebih baik?

---

## BAGIAN 3: EKSEKUSI & RISIKO

### 3.1 Assumptions & Risks (Asumsi & Risiko)
- **Asumsi**: Hal yang kita yakini benar (Contoh: Semua kader memiliki *smartphone*).
- **Risiko**: Hal buruk yang mungkin terjadi dan cara mitigasinya (Contoh: Server API Google Maps *down* -> Mitigasi: Sediakan input teks alamat manual).

### 3.2 Cross-Functional Dependencies (Ketergantungan Tim Lain)
- Siapa yang kita tunggu? (Contoh: Menunggu desain UI dari tim Figma, menunggu legal *approval* dokumen privasi).

### 3.3 Go-To-Market (GTM) & Launch Plan
- **Alpha/Internal Testing**: Tanggal.
- **Beta Testing**: Tanggal & jumlah user.
- **Strategi Peluncuran**: (Contoh: Rilis bertahap ke 1 RW dulu selama 1 minggu sebelum di-buka ke seluruh kecamatan).

### 3.4 Open Questions
- Pertanyaan yang belum terjawab saat PRD ini dibuat.

---
**Document Change Log**
| Tanggal | Versi | Perubahan | Oleh |
| :--- | :--- | :--- | :--- |
| [Tanggal] | v1.0 | Draft pertama PRD dibuat | [Nama] |
