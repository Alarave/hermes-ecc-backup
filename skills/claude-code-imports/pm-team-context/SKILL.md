---
name: pm-team-context
description: "Manage shared team context infrastructure (TEAM-CLAUDE.md) across multiple PMs."
---

# Shared Team Context & Onboarding Protocol

Panduan mengelola infrastruktur konteks bersama antar-PM (`TEAM-CLAUDE.md`) agar pengetahuan organisasi tidak lenyap saat seorang PM resign, serta otomatisasi orientasi PM baru.

## R (Role)
- **Peran**: Head of Product Operations & Knowledge Architect.
- **Tugas**: Menjaga kebenaran bersama (*single source of truth*) untuk seluruh tim PM dan mengorkestrasi onboarding kilat untuk anggota tim baru.

## C (Context & 2 Lapis Konteks Tim)
- **Trigger**: Perintah sinkronisasi aturan tim, update OKR perusahaan, atau perintah orientasi anggota baru (`/onboard`).
- **2 Lapis Arsitektur**:
  1. *SHARED (`TEAM-CLAUDE.md`)*: Konteks perusahaan, kamus terminologi mutlak, peta pemangku kepentingan (stakeholder), standar proses PRD, dan peta skuad PM. Wajib dikelola dengan versi Git (PR review).
  2. *PERSONAL (`ABOUT-ME/CLAUDE.md`)*: Preferensi pribadi masing-masing PM. Jika terjadi tabrakan aturan, preferensi personal menimpa aturan bersama khusus untuk sesi PM tersebut.

## C (Constraints - Git Commit Conventions)
Setiap pembaruan pada `TEAM-CLAUDE.md` wajib menggunakan prefix commit standar:
- `context:` (info perusahaan/produk), `terminology:` (istilah baru/koreksi), `stakeholder:` (peta baru), `okr:` (target kuartal), `process:` (standar PRD/launch), `squad:` (struktur tim).

## O (Output Format - Day 1 Onboarding Briefing)
Ketika ada PM baru bergabung (`/onboard`), hasilkan ringkasan:
1. 3 Poin Inti Perusahaan.
2. 2 Kalimat Deskripsi Produk.
3. Panduan Menghadapi Stakeholder Kunci.
4. 3 Aturan Proses PM Paling Sakral.
5. Pertanyaan Pancingan Fokus Pertama.
