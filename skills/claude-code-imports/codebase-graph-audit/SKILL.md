---
name: codebase-graph-audit
description: "Senior codebase auditor for AST, call graph, and architecture dependency analysis."
---

# Codebase Graph Audit

**Role:** Senior Codebase Auditor & Navigator

**Context:** 
Proyek raksasa, legacy code, atau repositori asing. Terlalu besar untuk grep/rg manual. Butuh pemetaan visual, arsitektur, dan logika bisnis (domain) menggunakan plugin Understand-Anything.

**Constraint:** 
- YAGNI: Jangan pakai di proyek kecil atau proyek yang sudah dihafal (seperti Berlayar Cafe). Boros token / boncos. Pakai `search_files` + `read_file` untuk harian (lebih sat-set).
- Jalankan `/understand` awal dengan hati-hati. Prioritaskan `--language id` agar output bahasa Indonesia.
- Gunakan fitur spesifik sesuai kebutuhan: `/understand-domain` (alur bisnis), `/understand-chat` (tanya jawab), `/understand-diff` (cek imbas kode sebelum commit).
- Syarat: Jika CLI/plugin belum terpasang, instal dulu via `curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash`

**Output:**
- Graf pengetahuan arsitektur siap diakses (via `/understand-dashboard`).
- Penjelasan ringkas alur bisnis.
- Peta imbas kode yang akurat sebelum integrasi.