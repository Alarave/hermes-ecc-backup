# OPERATIONAL REFERENCE: CONTEXT ENGINEERING & MEMORY PERSISTENCE
> Panduan manajemen jendela konteks, retensi status proyek lintas sesi, penataan anggaran token, dan model routing dinamis.

---

## 1. Arsitektur Memori Bertingkat (Tiered Memory Architecture)

Untuk mencegah amnesia proyek dan pembengkakan token (*Context Window Collapse*), Pram memisahkan jenis memori ke dalam 3 lapisan:

```text
[Lapisan 1: Ephemeral Context] ──► Chat Session Aktif (Prompt saat ini, pesan sementara)
          │ (Melewati batas 80% window)
          ▼
[Lapisan 2: Working Memory]    ──► File-based Task Ledger (`tracks.md`, `.state/`, ADRs)
          │ (Keputusan lintas sesi)
          ▼
[Lapisan 3: Persistent Rules]  ──► Core Skills (`SKILL.md`), System Prompts, Config YAML
```

---

## 2. File-Based Working Memory (`tracks.md`)

Pram tidak mengandalkan ingatan RAM obrolan untuk proyek jangka panjang. Status proyek dicatat secara fisik pada berkas pelacak di repositori lokal:

```markdown
# TASK LEDGER: [Nama Proyek / Fitur]
**Terakhir Diperbarui**: YYYY-MM-DD HH:MM WIB  
**Status Keseluruhan**: ACTIVE / BLOCKED / VERIFIED  

| Task ID | Nama Tugas | PIC Agen | Dependensi | Status | Bukti / Artefak |
|---|---|---|---|---|---|
| TSK-01 | Desain Skema Database | Spesialis-Backend | - | VERIFIED | `src/models/schema.sql` |
| TSK-02 | Kontrak DTO Auth | Spesialis-Backend | TSK-01 | VERIFIED | `src/types/auth.dto.ts` |
| TSK-03 | Implementasi Endpoint | Spesialis-Backend | TSK-02 | IN_PROGRESS | `src/routes/auth.ts` |
| TSK-04 | Unit Testing API | Security-QA | TSK-03 | PLANNED | `tests/auth.test.ts` |
```

---

## 3. Protokol Strategic Compaction

Ketika riwayat percakapan mendekati batas kapasitas konteks (>80% token budget):
1. **Penyimpanan Status Fisik**: Pastikan seluruh progres terakhir, keputusan ADR, dan status tugas sudah ditulis ke `tracks.md` atau `docs/`.
2. **Kompaksi Konteks**: Rangkum histori panjang menjadi ringkasan deterministik:
   - *Goal Asli Proyek*.
   - *Keputusan Kunci yang Sudah Disahkan*.
   - *Tugas Aktif yang Sedang Berjalan*.
   - *Pointer File / Artefak Sumber Kebenaran*.
3. **Pembersihan Log**: Buang traceback error usang yang sudah teratasi dan teks percakapan basa-basi.

---

## 4. Token Budgeting & Dynamic Model Routing

Pram mengalokasikan kapasitas model LLM berdasarkan tingkat kerumitan tugas untuk menghemat biaya operasional:

| Tier Model | Tipe Beban Kerja | Contoh Tugas | Karakteristik Model |
|---|---|---|---|
| **Tier 1 (Reasoning Heavy)** | Arsitektur, Problem Framing, Security Audit, Root Cause Analysis | Pembuatan PRD, Desain DAG, Mediasi Merge Conflict, ADR | Penalaran mendalam, IQ tinggi, konteks besar |
| **Tier 2 (Implementation)** | Koding TDD, Penulisan Kode Modul, Pembuatan Skrip | Penulisan fungsi backend, slicing UI React, skrip Python | Cepat, presisi sintaks, eksekusi kode bersih |
| **Tier 3 (Mechanical / Light)** | Formatting, Linting, Regex, Pembersihan Teks | Format Markdown, sortir baris, cek spasi, sanitasi log | Kecepatan kilat, biaya token sangat murah |

---

## 5. Isolated Worker Sandboxing

Setiap sub-tugas yang didelegasikan dijalankan dalam isolasi:
- Sub-agen hanya menerima berkas input yang relevan dan kontrak spesifik (Context Pack).
- Eksekusi terminal atau kompilasi pengujian dilakukan di lingkungan kerja terbatas.
- **Hanya artefak akhir yang telah lolos verifikasi** (kode bersih, laporan ringkas, atau diff) yang ditarik kembali ke konteks utama Pram. Log terminal mentah ribuan baris ditinggalkan di file log disk (`logs/`).

---

## 6. Two-Stage Progressive Skill Routing (Adopsi Vibe-Skills)

Memuat puluhan file `SKILL.md` secara utuh ke dalam prompt menyebabkan pembengkakan konteks (*context bloat*) dan degradasi penalaran. Pram menerapkan penyaringan 2 tahap:

```text
[Pool 100+ Skill Terpasang]
           │
           ▼ (Tahap 1: Metadata Filter)
[Katalog Ringan: Nama + Trigger 1 Baris] ──► Seleksi 2-3 Kandidat Relevan
           │
           ▼ (Tahap 2: Just-In-Time Loading)
[Muat Penuh SKILL.md Kandidat Terpilih] ──► Eksekusi Rencana Kerja
```

1. **Tahap 1 (Fast Candidate Discovery)**:
   - Pram memindai metadata ringkas: nama skill dan trigger alami.
   - Pilih hanya 2 sampai 3 skill yang paling sesuai dengan tugas aktif.
2. **Tahap 2 (Just-In-Time Loading)**:
   - HANYA file `SKILL.md` dan modul acuan dari kandidat terpilih yang dimuat ke memori kerja.
   - Skill yang tidak relevan tidak dibaca, menghemat hingga 29.6% token dan mencegah distorsi instruksi.

---

## 7. Hierarchical Capability Tree Navigation (Adopsi AgentSkillOS)

Pencarian vektor teks murni sering mengalami *Myopic Retrieval* (pandangan sempit), hanya mencocokkan kemiripan kata kunci tanpa menyadari kebutuhan skill komplementer. Pram menavigasi ekosistem melalui **Pohon Kapabilitas 5 Cabang**:

```text
POHON KAPABILITAS SKILL (CAPABILITY TREE):
│
├── [Branch 1: Governance & Quality Control]
│   └── pram-orchestrator, independent-auditor, contract-freezer, quality-gates
│
├── [Branch 2: Data, AI & Modeling]
│   └── spesialis-data-ai-agentic, ceemdan-lstm-forecasting, timesfm-forecasting, mlops-orchestration
│
├── [Branch 3: Software Architecture & Systems]
│   └── spesialis-backend, spesialis-frontend, git-workflow, agent-orchestration
│
├── [Branch 4: Security & Verification]
│   └── security-reviewer (Codex Loop), security-threat-model, tdd-workflow
│
└── [Branch 5: Research, Product & Dissemination]
    └── spesialis-research-akademik, research-title-formulator, spesialis-product-bisnis, note, campus-repository-scraper
```

### Aturan Komposisi Lintas Cabang (Cross-Branch Composition):
- Untuk tugas berskala **Level XL**, Pram DILARANG hanya memilih 1 skill tunggal.
- Pram wajib mengomposisikan kombinasi komplementer lintas cabang ke dalam DAG:
  - *Cabang Eksekusi*: Misal Branch 2 (Data AI) atau Branch 3 (Software Systems).
  - *Cabang Verifikasi Mutlak*: Wajib mengikutsertakan Branch 4 (Security Reviewer) atau Branch 1 (Independent Auditor) sebagai gerbang penyelesaian.
