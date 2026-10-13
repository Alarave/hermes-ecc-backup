# OPERATIONAL REFERENCE: QUALITY GATES & DUAL AUDIT SEAL
> Standar verifikasi bertahap (G0-G4), mesin status verifikasi, dan audit ganda (Semantic & Machine) untuk mencegah halusinasi dan utang teknis.

---

## 1. Documentation-First Quality Gates (G0 s.d. G4)

Pram menerapkan 5 gerbang kendali mutu bertahap sebelum kode produksi diizinkan rilis:

```text
[G0: Discovery] ──► [G1: Product PRD] ──► [G2: Domain & Boundaries] ──► [G3: Architecture & Contracts] ──► [G4: WBS, TDD & Release]
```

### Gate 0: Discovery & Problem Framing (`brief.md`)
- **Tujuan**: Menghancurkan ambiguitas ide proyek.
- **Kriteria Lolos (Checklist)**:
  - Problem Statement terdefinisi jelas (Masalah apa yang diselesaikan? Untuk siapa?).
  - Pemisahan tegas: Fakta vs Asumsi vs Hal yang Belum Diketahui.
  - Batasan waktu, anggaran biaya, dan target infrastruktur terdata.
  - Opsi: *Build vs Buy vs Simplify vs Cancel* telah dipertimbangkan.

### Gate 1: Product Requirements (`prd.md`)
- **Tujuan**: Mengunci cakupan fitur dan indikator kesuksesan.
- **Kriteria Lolos (Checklist)**:
  - Lolos evaluasi Rubrik PRD minimal skor 32/40 (`prd-template.md`).
  - *North Star Metric* dan *Guardrail Metrics* terdefinisi kuantitatif.
  - Bagian *Hard Out-of-Scope* terkunci rapat untuk mencegah *scope creep*.
  - Pemetaan prioritas menggunakan metode *RICE Scoring*.

### Gate 2: Domain Map & Boundary Definition (`domain-map.md`)
- **Tujuan**: Mencegah arsitektur spaghetti sejak hari pertama.
- **Kriteria Lolos (Checklist)**:
  - Pembagian *Bounded Context* bisnis (Modular Monolith) selesai.
  - Pemisahan skema database per domain terkunci.
  - Larangan mutlak SQL JOIN atau akses database langsung lintas domain disahkan.

### Gate 3: Architecture & Frozen Contracts (`contracts/`)
- **Tujuan**: Mengunci stabilitas antarmuka antartim / antaragen.
- **Kriteria Lolos (Checklist)**:
  - Kontrak API terdefinisi presisi (OpenAPI / Type-Safe DTO / Schema JSON).
  - Skema antarmuka dibekukan dan dihitung hash SHA-256 (`contract-freezer`).
  - Sub-agen atau pengembang dilarang mengubah payload tanpa persetujuan revisi kontrak resmi.
  - Architecture Decision Records (ADR) tersimpan di `docs/adr/`.

### Gate 4: WBS, TDD Implementation, & Release Gate
- **Tujuan**: Eksekusi teknis terverifikasi bukti nyata.
- **Kriteria Lolos (Checklist)**:
  - Work Breakdown Structure (WBS) dan Directed Acyclic Graph (DAG) siap.
  - Test-Driven Development (TDD): Unit tests dibuat terlebih dahulu dan lolos 80%+ coverage.
  - Lolos Dual Audit Seal (Semantic Seal + Machine Seal).
  - Definition of Done (DoD) terpenuhi 100%.

---

## 2. Verification State Machine (Mesin Transisi Status)

Status tugas dalam Orchestration Control Tower harus mengikuti mesin status deterministik berikut:

```text
[PLANNED] ──► [IN_PROGRESS] ──► [SUCCESS] ──► [VERIFY] ──► [VERIFIED]
     │              │               │            │
     ▼              ▼               ▼            ▼
 [BLOCKED]     [BLOCKED]         [FAILED]     [FAILED]
     │                                           │
     └─────────────► [RECOVERED] ◄───────────────┘
```

### Definisi dan Syarat Transisi:
1. **PLANNED**: Tugas terdaftar di WBS/DAG, dependensi terpetakan.
2. **IN_PROGRESS**: Tugas sedang dikerjakan oleh sub-agen atau sesi aktif.
3. **BLOCKED**: Pekerjaan terhenti karena dependensi upstream belum selesai, kekurangan kredensial, atau menunggu keputusan manusia.
4. **SUCCESS**: Agen pekerja mengklaim tugas selesai. **PERINGATAN**: Status ini BELUM sah menjadi hasil akhir.
5. **VERIFY**: Fase pemeriksaan Proof of Work independen oleh Pram dan auditor terisolasi.
6. **VERIFIED**: Status sah mutlak. Pekerjaan dinyatakan selesai HANYA JIKA paket Proof-of-Work (Symphony Standard) divalidasi penuh.
7. **FAILED**: Tugas gagal kompilasi, test runner merah, atau melanggar kontrak arsitektur.
8. **RECOVERED**: Tindakan *self-healing*, rollback ke checkpoint stabil, atau perbaikan *bounded retry* berhasil memulihkan kondisi sistem.

---

## 3. Proof-of-Work Standard (Adopsi OpenAI Symphony)

Sebelum tiket kerja atau Pull Request diizinkan mendarat (*merge/close*), agen wajib menyerahkan paket bukti kerja 4 pilar:
1. **CI / Test Execution Pass**: Log eksekusi test runner nyata di terminal lokal (coverage >= 80%, 0 failed test).
2. **Review Clearance**: Lolos Dual Audit Seal (Semantic + Machine) tanpa catatan merah (*blocking issue*).
3. **Complexity & Scope Audit**: Analisis diff kode membuktikan perubahan bersifat minimal bedah (*surgical*), tidak ada perubahan di luar *Context Pack*, dan tidak ada penambahan dependensi liar.
4. **Walkthrough / Verification Steps**: Panduan verifikasi singkat (1-3 langkah konkret) yang membuktikan fitur/bugfix berfungsi sesuai kriteria penerimaan.

---

## 4. Dual Audit Seal Protocol

Pram membagi pengujian independen menjadi dua jalur audit terpisah:

### A. Semantic Seal (Audit Keselarasan Konseptual)
- **Fokus**: Logika bisnis dan pemenuhan kebutuhan pengguna.
- **Pemeriksaan**:
  - Apakah output benar-benar menyelesaikan masalah yang tercantum di PRD?
  - Apakah ada skenario *edge case* bisnis yang terlewatkan?
  - Apakah interaksi antar-modul mematuhi batas arsitektur Modular Monolith?
  - Apakah bahasa dan terminologi yang digunakan bebas dari *AI-Slop* dan hiperbola?

### B. Machine Seal (Audit Eksekusi Mesin & Teknis)
- **Fokus**: Sintaks, keandalan komputasi, dan keamanan sistem.
- **Pemeriksaan**:
  - Kompilasi: Kode lulus build dan type-check (TypeScript `tsc`, Go `go build`, Python type annotations).
  - Testing: Test runner dijalankan di terminal nyata dan lulus 80%+ coverage.
  - Keamanan: Pre-commit security scan lulus (Nol hardcoded secret, lolos SAST).
  - Integritas Kontrak: Payload response cocok 100% dengan skema SHA-256 yang dibekukan di Gate 3.

---

## 5. Multi-Format Deliverable Artifacts (Adopsi AgentSkillOS)

Sebuah deliverable tidak boleh hanya berupa klaim teks di jendela chat. Deliverable wajib disimpan sebagai artefak fisik terstruktur di disk (`artifacts/` atau `cache/<project>/`):
1. **Dokumentasi & Laporan**: Berkas Markdown terstruktur (`CATATAN_*.md`), PDF, atau DOCX.
2. **Visual & Antarmuka**: Berkas HTML mandiri yang dapat dibuka di browser, kanvas interaktif, atau diagram SVG.
3. **Data & Model**: File dataset biner kolom efisien (Parquet), konfigurasi JSON skema tervalidasi, atau bobot model terkompilasi (ONNX).
4. **Kode & Script**: Skrip Python/Bash executable yang siap dijalankan ulang tanpa error (*Reproducible Execution*).

---

## 6. Universal Definition of Done (DoD) Checklist

Sebuah deliverable atau sprint dianggap tuntas (`DONE / VERIFIED`) HANYA JIKA seluruh butir terpenuhi:
- [ ] Berkas artefak fisik ada di disk (`artifacts/`) dan dapat diakses.
- [ ] Kode sumber lulus kompilasi tanpa peringatan kritis.
- [ ] Automated tests (Unit / Integration) lulus dengan coverage >= 80%.
- [ ] Dokumentasi teknis, API contract, atau ADR telah diperbarui.
- [ ] Tidak ada kredensial, token pribadi, atau 8 taksonomi PII yang bocor.
- [ ] Status audit: Semantic Seal dan Machine Seal keduanya bertanda **PASS**.
