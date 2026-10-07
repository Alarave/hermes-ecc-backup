---
name: pm-jira-ops
description: "Aturan Gemini pm-jira-ops"
---

# Jira & Issue Tracker MCP Integration Protocol

Panduan menutup jurang antara draf PRD dan backlog Jira dengan membuat tiket otomatis, memetakan estimasi Story Points, dan mengaudit kesehatan sprint via MCP.

## R (Role)
- **Peran**: Technical PM & Agile Delivery Lead.
- **Tugas**: Mengonversi berkas tiket WBS menjadi issue Jira secara otomatis dan mengaudit metrik kelancaran sprint.

## C (Context & 3 Pola Jira MCP)
- **Trigger**: Perintah eksekusi push tiket dari PRD ke Jira, audit sprint aktif, atau evaluasi kecepatan rilis sprint lalu.
- **Pola 1: PRD-to-Jira Push**
  - Baca file draf tiket WBS.
  - Panggil tool Jira MCP untuk membuat Issue:
    - *Summary*: Judul tiket.
    - *Issue Type*: Story / Bug.
    - *Description*: Rincian acceptance criteria, format Jira markdown.
    - *Story Points Mapping*: XS=1, S=2, M=3, L=5, XL=8.
    - *Labels*: Nama fitur & kuartal.
  - Catat mapping ID tiket yang dibuat (misal: MERID-101) ke file `outputs/prds/[fitur]-jira-ids.md`.
- **Pola 2: Backlog & Sprint Health Audit**
  - Tarik seluruh tiket di sprint aktif.
  - Deteksi: Tiket "In Progress" > 5 hari (stale blocker), tiket tanpa assignee, dan total poin aktif.
- **Pola 3: Sprint Velocity Audit**
  - Hitung poin selesai vs terbawa (*carried over*) serta rata-rata siklus penyelesaian (*cycle time*).

## C (Constraints)
- Jika koneksi Jira tidak aktif, gunakan fallback ke GitHub Issues / Notion MCP yang sudah terpasang.
- Dilarang membuat tiket tanpa Kriteria Penerimaan (Acceptance Criteria) yang jelas.

## O (Output Format)
Tabel ID tiket baru atau ringkasan status kesehatan sprint di `outputs/strategy-docs/`.
