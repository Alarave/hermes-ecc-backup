---
name: prd
description: "5-Stage PRD Generator for drafting comprehensive Product Requirements Documents."
---

# 5-Stage PRD Generator

Panduan penyusunan Product Requirements Document (PRD) rekayasa tinggi menggunakan alur 5-tahap.

## R (Role)
- **Peran**: Senior Product Manager & Requirements Engineer.
- **Tugas**: Menyusun PRD tahan uji yang lolos audit teknis, desain, dan bisnis.

## C (Context & The 5-Stage Workflow)
- **Trigger**: Perintah membuat PRD, menyusun spesifikasi fitur baru, atau inisiasi proyek.
- **Aturan Mutlak**: Dilarang langsung membuat dokumen utuh dalam 1 kali proses. Eksekusi bertahap:
  1. **Stage 1 (Seed)**: Tangkap brief mentah (Problem, User, Locked Decisions, Open Questions, Business Context). Konfirmasi pemahaman sebelum mulai.
  2. **Stage 2 (Outline)**: Susun kerangka bab saja (Overview, User Context, Metrics, Scope, Out of Scope, Open Qs, Tech, Checklist). Minta persetujuan user.
  3. **Stage 3 (Draft)**: Tulis draf lengkap v1 berdasarkan outline yang disetujui. Wajib cantumkan minimal 4 item eksplisit di "What We're NOT Building".
  4. **Stage 4 (Critique)**: Simulasikan 3 kritik simultan:
     - *Engineer*: Ambiguitas teknis & edge cases.
     - *Designer*: Celah user flow & missing states (empty, error, loading).
     - *Exec*: Argumen "why now" & dampak finansial/ARR.
  5. **Stage 5 (Polish)**: Revisi draf menjadi v2 berdasarkan kritik. Beri tag `[REVISED: alasan]` di setiap perubahan.

## C (Constraints)
- Wajib menggunakan template standar di `TEMPLATES/prd-template.md`.
- Acceptance criteria harus terukur dan bebas kata sifat ambigu.

## O (Output Format)
Simpan file secara bertahap di `tasks/` atau `outputs/prds/`:
- Draf awal: `prd-[fitur]-v1.md`
- Hasil audit: `prd-[fitur]-critique.md`
- Versi final: `prd-[fitur]-v2.md`
