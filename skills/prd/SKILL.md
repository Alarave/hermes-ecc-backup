---
name: prd
description: "5-Stage PRD & Roadmap Generator: Interactive Socratic questionnaire, feature tree decomposition, and rigorous Product Requirements Documents."
---

# 5-Stage PRD & Roadmap Generator

Panduan penyusunan Product Requirements Document (PRD) rekayasa tinggi menggunakan alur 5-tahap berbasis interogasi kuesioner dan dekomposisi roadmap fitur.

## R (Role)
- **Peran**: Senior Product Manager & Requirements Engineer.
- **Tugas**: Menyusun PRD tahan uji yang lolos audit teknis, desain, dan bisnis melalui dekomposisi pohon fitur terstruktur.

## C (Context & The 5-Stage Workflow)
- **Trigger**: Perintah membuat PRD, menyusun spesifikasi fitur baru, merancang roadmap produk, atau inisiasi proyek.
- **Aturan Mutlak**: Dilarang langsung membuat dokumen utuh dalam 1 kali proses. Eksekusi bertahap:
  1. **Stage 1 (Seed & Socratic Questionnaire)**: Tangkap brief mentah. Ajukan 3 sampai 5 pertanyaan terarah via tool `clarify` (kebutuhan alur bisnis, target persona pengguna, anggaran, dan batasan arsitektur) sebelum memulai draf.
  2. **Stage 2 (Tech Matrix & Feature Roadmap Tree)**: Petakan 4 pilar tech stack (Frontend, Backend, Database, Deployment). Dekomposisi ide ke hierarki roadmap terstruktur: `Title -> Fitur Utama (P0/P1) -> Sub-Fitur -> Kriteria Akseptansi`.
  3. **Stage 3 (Outline & Scope Freeze)**: Susun kerangka bab saja (Overview, User Context, Metrics, Scope, Out of Scope, Open Qs, Tech, Checklist). Wajib cantumkan minimal 4 item eksplisit di bab "What We're NOT Building" untuk mencegah scope creep.
  4. **Stage 4 (Draft & 3-Perspective Critique)**: Tulis draf lengkap v1 berdasarkan outline. Simulasikan 3 kritik simultan:
     - *Engineer*: Ambiguitas teknis dan skenario gagal (edge cases).
     - *Designer*: Celah user flow dan status antarmuka (empty, error, loading).
     - *Exec*: Argumen kelayakan bisnis (why now) dan dampak finansial.
  5. **Stage 5 (Polish & Task Breakdown)**: Revisi draf menjadi v2 berdasarkan kritik. Dekomposisi sub-fitur ke daftar task atomik yang siap dikonsumsi langsung oleh tim rekayasa (WBS DAG Pram atau kartu Kanban).

## C (Constraints)
- Wajib menggunakan template standar di `skills/pram-orchestrator/references/prd-template.md`.
- Acceptance criteria harus terukur dan bebas kata sifat ambigu.
- Dilarang keras menggunakan karakter tanda pisah em dash atau en dash. Gunakan tanda titik dua (:), tanda kurung (), koma, atau tanda strip biasa (-).

## O (Output Format)
Simpan file secara bertahap di `tasks/`, `docs/`, atau `outputs/prds/`:
- Hasil Kuesioner & Roadmap: `roadmap-[fitur].json` atau bab roadmap PRD
- Draf awal: `prd-[fitur]-v1.md`
- Hasil audit: `prd-[fitur]-critique.md`
- Versi final: `prd-[fitur]-v2.md`
- Daftar Task Atomik: `tasks-[fitur].md` (format siap impor ke WBS DAG/Kanban)
