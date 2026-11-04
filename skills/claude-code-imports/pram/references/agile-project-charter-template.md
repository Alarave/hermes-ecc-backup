# Template Standar Industri: Agile Enterprise Project Charter

Template ini merupakan standar emas (*Gold Standard*) untuk inisiasi proyek perangkat lunak, menggabungkan format nyata dari studi kasus "Sistem Posyandu Bekasi" (Tim C&C) dengan tata kelola **PMO Enterprise** tingkat global (berdasarkan praktik terbaik GitLab Handbook & FAANG 2025). 

Semua *Project Charter* yang dibuat oleh Pram WAJIB mengikuti 8 elemen absolut ini:

---

## 1. Executive Summary & Metadata (Informasi Umum)
- **Judul Proyek**: [Nama Sistem/Proyek]
- **Sponsor / Klien**: [Nama Pemilik Dana atau Jabatan Eksekutif]
- **Project Manager**: [Nama Anda/Firman atau Pram]
- **Anggaran (Budget)**: Rp [Total Anggaran]
- **Tanggal Mulai & Target Selesai**: [DD MMMM YYYY] – [DD MMMM YYYY]
- **Penyelarasan OKR (Objectives and Key Results)**: Proyek ini sejalan dengan *Objective* bisnis ke-[X] perusahaan.

## 2. Project Vision & Business Objectives (Visi & Tujuan Bisnis)
- **Visi (The "Why")**: Paragraf lugas tentang masalah saat ini dan bagaimana transformasi digital sistem ini akan menyelesaikannya.
- **Key Success Factors (KPI)**:
  - Sisi Manajemen/Klien: (Misal: Mengurangi *bounce rate*, akurasi data 99%).
  - Sisi Pengguna Akhir: (Misal: Waktu muat halaman di bawah 2 detik, UX yang intuitif).

## 3. Scope & Acceptance Criteria (Ruang Lingkup & Kriteria Penerimaan)
- **In-Scope (Di Dalam Lingkup)**: Daftar fitur mutlak (1... 2... 3...).
- **Out-of-Scope (Di Luar Lingkup)**: Fitur yang DITOLAK atau ditunda ke *Phase 2* (sangat penting untuk mencegah *Scope Creep*).
- **Definition of Done (DoD) Mutlak**:
  - Kode harus lolos pengujian *Black-box* dan UAT klien.
  - Kode terunggah ke repositori, tidak ada *P0/P1 bugs*.

## 4. Key Stakeholders & RACI Matrix (Susunan Tim)
Gunakan matriks *Responsible, Accountable, Consulted, Informed* (RACI) atau daftar spesifik:
| No | Nama / Peran | Posisi Utama | Tanggung Jawab Agile (Termasuk Testing) |
|:---|:---|:---|:---|
| 1 | PM (Pram) | Project Manager | *Accountable* - Orkestrasi, *Budgeting*, UAT |
| 2 | Backend Engineer | Programmer | *Responsible* - API, Database, Keamanan |
| 3 | Frontend Engineer | Designer/Dev | *Responsible* - UI/UX, Integrasi API |
| 4 | Client/Sponsor | Stakeholder | *Consulted/Informed* - Approval, Validasi Fitur |

## 5. Agile Sprint Schedule & Financial Budgeting (Estimasi Biaya)
Siklus dibagi dalam iterasi *Sprint* (maksimal 2-3 minggu per Sprint). Penganggaran dihitung riil: `Durasi x Tenaga Kerja x Tarif/Hari`.

| Sprint # | Deskripsi Epics/Kegiatan | Durasi | T.Kerja | Tarif Harian | Total Tenaga Kerja | Biaya Ekstra | Total Biaya |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **Sprint 1** | *Sprint Planning*, Arsitektur (ADR), Setup Auth | 5 Hari | 3 | Rp 150.000 | Rp 2.250.000 | Rp 0 | Rp 2.250.000 |
| **Sprint 2** | *CRUD* Data Utama & *Database Schema* | 10 Hari | 2 | Rp 150.000 | Rp 3.000.000 | Rp 0 | Rp 3.000.000 |
| **Sprint X** | *Final UAT, Deployment ke Cloud, Serah Terima* | 3 Hari | 3 | Rp 150.000 | Rp 1.350.000 | Rp 1.500k | Rp 2.850.000 |
| **Dana Antisipasi** | *Contingency Fund* (Risiko/Bug Ekstra) | - | - | - | - | Rp 2.000k | Rp 2.000.000 |

## 6. RAID Log Summary (Risiko & Antisipasi)
Tabel matriks PMO internasional untuk mitigasi hambatan sebelum proyek dimulai:
- **Risks (Risiko)**: Ancaman proyek (Contoh: Klien lambat memberi *feedback*). *Mitigasi: Paksa tanda tangan SLA revisi*.
- **Assumptions (Asumsi)**: Asumsi awal (Contoh: Server klien siap dipakai).
- **Issues (Masalah Saat Ini)**: (Jika ada).
- **Dependencies (Ketergantungan)**: Ketergantungan eksternal (Contoh: Menunggu API Payment Gateway aktif).

## 7. Architecture & Tech Stack (Keputusan Arsitektur Tingkat Tinggi)
- **Frontend**: [React / Next.js / Vue]
- **Backend / Database**: [Node.js / Go / Supabase / PostgreSQL]
- **Infrastruktur**: [Docker / AWS / Vercel]

## 8. Executive Approval (Tanda Tangan Pengesahan)
Bagian *sign-off* serah terima untuk memastikan komitmen hukum dan profesional antara *Project Manager* dan Sponsor.
