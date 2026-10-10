---
name: linear
description: "Use when user says 'Linear', 'bikin tiket', 'cek backlog', 'sprint issue', 'triage bug', 'status task', 'buat issue', atau manajemen proyek di Linear. Mengelola tiket, siklus sprint, dan pelacakan pekerjaan tim."
---

# Linear Project Management

Kelola issues, projects, cycles (sprint), dan alur kerja tim di Linear secara natural language.

## Prerequisites
- Linear connector harus terhubung ke Hermes (dapat diaktifkan via `manage_connections(action='connect', connectors=['linear'])`).

## Core Workflows

### 1. Sprint Planning & Issue Creation
- **Triage & Create**: Saat ada bug atau fitur baru dari PRD, otomatis buat tiket di Linear dengan priority, labels, dan deskripsi terstruktur (AC / Given-When-Then).
- **Cycle Mapping**: Petakan isu ke dalam Cycle/Sprint yang aktif.

### 2. Bug Triage & Backlog Refinement
- Tinjau backlog terbuka, kelompokkan berdasarkan tingkat keparahan (*Urgent, High, Medium, Low*), dan perbarui status ke *In Progress* atau *Done*.

### 3. Cross-Project Dependencies & Blockers
- Tandai issue yang *Blocked* dan hubungkan dengan issue penyebab (*Blocking*).

## Instruksi bagi Pram / Spesialis
1. Jika koneksi Linear belum aktif, minta izin ke user untuk menghubungkan akun Linear.
2. Saat merencanakan proyek (Fase WBS), tawarkan pembuatan tiket Linear otomatis dari daftar task WBS.
