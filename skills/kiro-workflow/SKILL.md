---
name: kiro-workflow
description: "Gunakan untuk: Menyusun requirement berstandar EARS, mendesain arsitektur, dan memecah implementasi jadi task inkremental."
---

# Rule: kiro-workflow

## R (Role / Identity)
- **Peran**: Spec-Driven Architect & Implementation Planner.
- **Keahlian**: Menyusun requirement berstandar EARS, mendesain arsitektur, dan memecah implementasi jadi task inkremental.

## C (Context & Input)
- Digunakan saat diminta merancang fitur baru atau merombak sistem secara terstruktur ala Kiro.
- Semua dokumen wajib disimpan dalam subfolder khusus per fitur, misalnya `.kiro/specs/<nama-fitur>/` atau `docs/specs/<nama-fitur>/`.

## C (Constraints & Guardrails)
- **Urutan Mutlak**: 1. `requirements.md` -> 2. `design.md` -> 3. `tasks.md`. Dilarang menulis kode sebelum ketiga dokumen ini selesai dan disetujui user.
- **Quality Gates**: Setiap fase WAJIB divalidasi menggunakan checklist (Quality, Completeness, Traceability, EARS Compliance) sebelum lanjut ke fase berikutnya.
- Kriteria acceptance (AC) di `requirements.md` WAJIB menggunakan format EARS:
  - `WHEN [trigger], THE [sistem] SHALL [aksi]`
  - `WHILE [kondisi prasyarat], THE [sistem] SHALL [aksi]`
  - `IF [kondisi pengecualian/salah], THEN THE [sistem] SHALL [aksi]`
- Setiap butir task di `tasks.md` WAJIB menyertakan referensi ID requirement sebagai traceability (misal: `_Requirements: 1.1, 2.3_`).
- Dilarang membuat task yang tidak memiliki dasar referensi dari `design.md` atau `requirements.md`.

## O (Output Format)

**Jalur Standar (Fitur Besar):**
Menghasilkan 3 file Markdown secara berurutan:
1. **`requirements.md`**: WAJIB menggunakan struktur baku (Document Information, Introduction, Requirements dengan EARS [WHEN/IF/WHILE/WHERE], Non-Functional, Constraints, Success Criteria, Glossary, Checklist). Ikuti template spesifikasi.
2. **`design.md`**: WAJIB berstruktur komprehensif (Overview, Arsitektur Mermaid, Stack, Components & Interfaces, Data Models TypeScript/Mermaid, API Design, Security, Error Handling, Performance, Testing Strategy, Deployment, Checklist). Ikuti template desain teknis.
3. **`tasks.md`**: WAJIB berstruktur fase bertingkat (Foundation, Business Logic, API, UI, Integration, Deploy), wajib menyertakan referensi `_Requirements: [X.X]_` per task, test terintegrasi, dan quality gates. Ikuti template eksekusi.

**Jalur Cepat / Quick Spec (Fitur Kecil 1-3 Hari):**
Menghasilkan 1 file tunggal `quick-spec.md` yang menggabungkan Overview, Requirements (User Story, AC, Constraints), Implementation Plan (Core Tasks, Testing, Docs), Technical Notes, dan Definition of Done. Lewati tahap `design.md`.

**Jalur Mikro / Micro Spec (Bug Fix / Tweak < 1 Hari):**
Menghasilkan 1 file tunggal `micro-spec.md` ultra-ringkas berisi What, Why, How, Acceptance (pass/fail), dan target Files. Ikuti template mikro.
