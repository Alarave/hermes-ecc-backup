---
name: playbook-replica
description: "Use when user asks to clone, reverse-engineer, or rebuild a competitor app. Orchestrates specialists to extract features, fix user complaints, and build a clean-room parity clone."
---

# Role
Competitor-Driven Development Playbook. Bertindak sebagai panduan orkestrasi mutlak bagi Pram untuk mengeksekusi proyek kloning / *reverse-engineering* perangkat lunak (SaaS/App) secara etis (Clean-Room Design) menggunakan armada agen spesialis.

# Context
Dipicu ketika Project Owner ingin membuat aplikasi yang merupakan kompetitor atau versi lebih baik dari aplikasi yang sudah ada di pasar. Sistem dilarang mencuri hak cipta (kode asli, aset logo, *copywriting*). Sistem hanya meniru *behavior*, *data model*, dan memecahkan *pain points* (keluhan) pelanggan kompetitor.

# Execution DAG (Wajib Diikuti Pram)

## Fase 1: RECON & ENTREPRENEUR (Discovery)
- **Delegasi Ke:** `spesialis-product-bisnis`
- **Instruksi:** Baca tangkapan layar, URL, atau dokumentasi aplikasi target. 
  1. Ekstrak *Data Model* dan *User Flow* (Recon).
  2. Cari kelemahan / keluhan *user* dari aplikasi asli (Entrepreneur).
- **Quality Gate G1:** Hasilkan `docs/01-prd-replica.md`. Harus berisi *Feature Parity List* dan *Differentiator* (Inovasi kita).

## Fase 2: ARCHITECT & DESIGN SYSTEM (Blueprint)
- **Delegasi Ke:** Paralel ke `spesialis-backend` dan `spesialis-ui-templates`
- **Instruksi Backend:** Rancang arsitektur Modular Monolith, skema *Database*, dan API Contract dari hasil Recon.
- **Instruksi UI/UX:** Ekstrak pola UI kompetitor menjadi *Design Tokens* (Warna, Spasi, Tipografi) yang netral.
- **Quality Gate G2:** Hasilkan `docs/03-architecture.md` dan kontrak DTO. Wajib jalankan `contract-freezer`.

## Fase 3: BUILD (Implementasi Clean-Room)
- **Delegasi Ke:** Paralel `spesialis-frontend` dan `spesialis-backend`
- **Instruksi:** Implementasikan kode dari nol (Clean-Room). Dilarang keras mencoba mencari *source code* asli kompetitor. Bangun berdasarkan kontrak di Fase 2.

## Fase 4: REPLICA DIFF & QA (Verifikasi Paritas)
- **Delegasi Ke:** `independent-auditor` dan `spesialis-security-qa`
- **Instruksi:** Lakukan E2E Test (klik fungsional). Hitung **Parity Score** (Berapa % fitur kompetitor berhasil direplikasi dengan baik).
- **Quality Gate G4:** Jika fitur "Must-Have" ada yang hilang, kembalikan ke Fase 3 (REJECT). Jika lulus, deploy.

# Output Format (Status Report)
Pram wajib memberikan laporan *Control Tower* khusus Replica:

```text
## REPLICA PIPELINE STATUS
**Target:** <Nama Aplikasi Kompetitor>
**Differentiator (Inovasi):** <Fitur pembunuh kita>

| Fase | Spesialis | Artefak | Parity Score | Blocker |
|---|---|---|---|---|
| Recon | product-bisnis | PRD.md | - | ... |
| Blueprint | backend, ui | Arch.md | - | ... |
| Build | backend, frontend | Code | - | ... |
| Diff & QA | auditor, qa | Test Log | 85% | ... |
```
