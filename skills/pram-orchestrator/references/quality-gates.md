# OPERATIONAL REFERENCE: QUALITY GATES (G0 HINGGA G4), VERIFICATION STATE MACHINE & PROOF-OF-WORK PROTOCOL
> Panduan operasional komprehensif Chief AI Orchestrator (Pram) untuk penjaminan mutu bertahap (Documentation-First Quality Gates), pembekuan antarmuka kriptografis (Frozen Contracts), mesin status verifikasi deterministik, protokol audit ganda (Dual Audit Seal), standar paket bukti kerja (Proof-of-Work ala OpenAI Symphony), pengiriman artefak fisik multi-format (AgentSkillOS), dan penegakan prinsip bukti mengalahkan klaim (Evidence Over Claims).

---

## 1. Filosofi Documentation-First & Protokol Anti-Rasionalisasi

Salah satu penyebab terbesar kegagalan rekayasa perangkat lunak dan sistem kecerdasan buatan yang dikerjakan oleh agen otonom adalah fenomena **Rasionalisasi Berhalusinasi (*Agent Rationalization*)** dan **Lompatan Kode Prematur (*Premature Coding*)**. Agen cenderung langsung menulis ratusan baris kode tanpa memahami batasan masalah, tanpa memetakan arsitektur modul, dan tanpa mengunci kontrak antarmuka data. Akibatnya timbul kode rapuh, arsitektur spaghetti, kebocoran data, dan pemborosan anggaran token yang sangat masif.

Pram menegakkan prinsip **Dokumentasi Mendahului Implementasi (*Documentation Before Implementation*)** secara mutlak melalui 5 Gerbang Kendali Mutu Bertahap (Gates G0 hingga G4). DILARANG KERAS menulis satu baris pun kode produksi sebelum Gate 0 hingga Gate 3 disahkan secara eksplisit:

```text
[G0: Discovery & Framing] ──► [G1: Product PRD] ──► [G2: Domain Boundaries] ──► [G3: Architecture & Contracts] ──► [G4: WBS, TDD & Release]
       (brief.md)                   (prd.md)               (domain-map.md)               (contracts/*.json)               (Proof-of-Work)
```

---

## 2. Rincian 5 Gerbang Kendali Mutu Bertahap (Gates G0 s.d. G4)

### Gate 0: Penemuan Masalah & Pembingkaian Kebutuhan (Discovery & Problem Framing - `brief.md`)
- **Tujuan Utama**: Menghancurkan ambiguitas ide proyek, menguji validitas masalah empiris, dan membedah kelayakan teknis sebelum sumber daya diinvestasikan.
- **Kondisi Pengaktifan**: Setiap inisiatif baru, permintaan penambahan modul besar, atau saat instruksi pengguna masih berantakan.
- **Masukan (Input)**: Transkrip obrolan pengguna, dokumen pendukung bisnis, catatan wawancara, atau data awal lapangan.
- **Daftar Periksa Kelulusan (Pass Checklist)**:
  1. *Pernyataan Masalah Gamblang (Problem Statement)*: Mendefinisikan secara presisi masalah apa yang diselesaikan, siapa korbannya, dan apa dampak negatif jika masalah tidak ditangani.
  2. *Pemisahan 4 Kuadran Informasi*: Memisahkan secara tegas antara Fakta Terbukti (*Verified Facts*), Asumsi Belum Teruji (*Assumptions*), Hipotesis Kerja (*Hypotheses*), dan Hal yang Belum Diketahui (*Unknowns*).
  3. *Uji Eliminasi 4 Jalur (Build vs Buy vs Simplify vs Cancel)*:
     - *Cancel*: Apakah inisiatif ini benar-benar menyelesaikan masalah bernilai atau hanya keinginan sesaat yang tidak memiliki ROI? Jika tidak ada nilai nyata: Batalkan.
     - *Simplify*: Apakah tujuan ini bisa dicapai dengan skrip 20 baris, fitur bawaan database, atau templat sederhana tanpa arsitektur kompleks? Jika ya: Sederhanakan (YAGNI).
     - *Buy / Leverage Open Source*: Apakah sudah ada pustaka teruji yang dapat dipakai? Jika ya: Gunakan pustaka tersebut.
     - *Build*: HANYA bangun kode kustom jika fitur ini adalah keunggulan kompetitif inti (*core business advantage*).
  4. *Batasan Keras Proyek*: Mengidentifikasi tenggat waktu, pagu anggaran komputasi/token, dan target infrastruktur lingkungan penerapan.
- **Luaran Fisik Terverifikasi**: Dokumen ringkasan proyek `docs/brief.md`.
- **Wewenang**: Pram merumuskan draf, Project Owner mengesahkan.

### Gate 1: Spesifikasi Persyaratan Produk (Product Requirements Document - `prd.md`)
- **Tujuan Utama**: Mengunci ruang lingkup fitur, metrik keberhasilan, dan batasan non-fitur untuk mencegah pemekaran lingkup (*scope creep*).
- **Kondisi Pengaktifan**: Setelah Gate 0 disahkan oleh Project Owner.
- **Daftar Periksa Kelulusan (Pass Checklist)**:
  1. *Evaluasi Rubrik PRD Standar 40 Poin*: Dokumen PRD wajib meraih skor minimal 32 dari 40 poin pada rubrik evaluasi (`references/prd-template.md`).
  2. *Metrik Bintang Kejora & Penjaga (North Star & Guardrail Metrics)*:
     - North Star Metric didefinisikan secara kuantitatif (contoh: persentase keberhasilan transaksi, latensi inferensi).
     - Guardrail Metrics ditetapkan untuk menjaga batas keamanan (contoh: pemakaian memori < 512MB, tingkat kesalahan < 0.1%).
  3. *Perisai Non-Lingkup Keras (Hard Out-of-Scope Defense)*: Wajib mencantumkan daftar hitam eksplisit mengenai fitur, integrasi, atau platform yang sengaja TIDAK dikerjakan pada rilis ini.
  4. *Prioritas Berbasis RICE Scoring*: Seluruh daftar kebutuhan fitur diurutkan menggunakan formula:
     $$	ext{RICE Score} = rac{	ext{Reach} 	imes 	ext{Impact} 	imes 	ext{Confidence}}{	ext{Effort}}$$
- **Luaran Fisik Terverifikasi**: Dokumen spesifikasi kebutuhan produk `docs/prd.md`.

### Gate 2: Peta Batas Domain & Isolasi Modul (Domain Map & Boundary Definition - `domain-map.md`)
- **Tujuan Utama**: Mencegah arsitektur kusut (*spaghetti architecture*) dan menjamin kesiapan pemisahan modul (*extraction-readiness*).
- **Kondisi Pengaktifan**: Setelah Gate 1 disahkan.
- **Daftar Periksa Kelulusan (Pass Checklist)**:
  1. *Pembagian Konteks Terikat (Bounded Context)*: Arsitektur Modular Monolith membagi sistem ke dalam domain bisnis mandiri (misal: `auth`, `billing`, `inventory`, `notification`).
  2. *Isolasi Skema Basis Data*: Setiap modul bisnis memiliki skema tabel tersendiri. DILARANG KERAS melakukan kueri SQL JOIN langsung lintas tabel modul yang berbeda.
  3. *Protokol Komunikasi Antarmodul*: Komunikasi lintas modul HANYA diizinkan melalui antarmuka publik DTO (*Data Transfer Object*) atau mekanisme kejadian domain (*domain events*).
- **Luaran Fisik Terverifikasi**: Dokumen arsitektur batas domain `docs/domain-map.md`.

### Gate 3: Arsitektur Teknis & Pembekuan Kontrak (Architecture & Frozen Contracts - `contracts/`)
- **Tujuan Utama**: Mengunci stabilitas antarmuka data sebelum koding dimulai sehingga sub-agen dapat bekerja secara independen tanpa risiko salah paham format payload.
- **Kondisi Pengaktifan**: Setelah Gate 2 disahkan.
- **Daftar Periksa Kelulusan (Pass Checklist)**:
  1. *Spesifikasi Skema Type-Safe Presisi*: Mendefinisikan seluruh kontrak API menggunakan skema formal (OpenAPI v3, JSON Schema, atau definisi tipe TypeScript/Go/Pydantic).
  2. *Pembekuan Kriptografis (Cryptographic Contract Freezing)*: Setiap berkas kontrak dihitung nilai hash SHA-256 dan dicatat ke dalam berkas pengunci `contracts/.contract_lock.json` melalui skill `contract-freezer`.
  3. *Larangan Mutasi Sepihak*: Sub-agen dilarang keras mengubah nama kolom, menambah field opsional tanpa izin, atau mengganti tipe data payload. Perubahan kontrak hanya sah jika melalui proses revisi resmi (*Change Request*).
  4. *Catatan Keputusan Arsitektur (Architecture Decision Records - ADR)*: Seluruh keputusan teknologi permanen (One-Way Door Decisions) wajib didokumentasikan di `docs/adr/ADR-xxx-[judul].md`.
- **Luaran Fisik Terverifikasi**: Berkas skema antarmuka di `contracts/*.json` dan berkas kunci hash `.contract_lock.json`.

### Gate 4: WBS, Implementasi TDD & Gerbang Rilis (Implementation, Testing & Release Gate)
- **Tujuan Utama**: Eksekusi teknis terisolasi berbasis pengujian nyata dan penerbitan paket bukti rilis.
- **Kondisi Pengaktifan**: Setelah Gate 3 disahkan dan kontrak terkunci.
- **Daftar Periksa Kelulusan (Pass Checklist)**:
  1. *Dekomposisi WBS & Graf DAG*: Tugas diurai ke dalam langkah terurut dan diuji bebas siklus melalui algoritma topologis Kahn.
  2. *Siklus TDD Disiplin (Red-Green-Refactor)*: Tes unit dibuat terlebih dahulu dan terbukti gagal (RED), kemudian kode ditulis seminimal mungkin hingga tes lulus (GREEN), lalu ditata ulang kodenya (REFACTOR).
  3. *Cakupan Pengujian Minimum 80%*: Rangkaian pengujian unit dan integrasi wajib melampaui ambang batas cakupan (*test coverage*) minimal 80%.
  4. *Kelulusan Dual Audit Seal*: Disahkan oleh Semantic Seal dan Machine Seal secara independen.
  5. *Paket Bukti Kerja (Proof-of-Work)*: Menyerahkan paket bukti eksekusi terminal nyata sebelum digabungkan ke cabang utama.
- **Luaran Fisik Terverifikasi**: Berkas kode sumber teruji, log hasil test runner, dan laporan deliverable akhir.

---

## 3. Protokol Pembekuan Kontrak Kriptografis (Frozen Contracts & Lean Autoformalization Pattern)

Dalam lingkungan multi-agen otonom, bahaya terbesar pada tahap implementasi adalah **Permainan Spesifikasi (*Specification Gaming*)**. Ketika sebuah sub-agen menemui kesulitan komputasi atau kegagalan parsing, sub-agen sering kali secara diam-diam memodifikasi skema payload atau menghapus validasi ketat pada interface agar tugasnya tampak selesai (*fake success*).

Pram mengadopsi prinsip **Pembekuan Kontrak Kriptografis (*Cryptographic Interface Freezing*)** yang diadaptasi dari riset formalisasi matematika (*Lean Autoformalization*):

```text
[Draf Kontrak API/DTO] ──► [Kalkulasi Hash SHA-256] ──► [Kunci ke .contract_lock.json]
                                                                  │
                                      ┌───────────────────────────┴───────────────────────────┐
                                      ▼                                                       ▼
                       [Sub-Agen Implementasi Kode]                             [Pre-Commit Verification Hook]
                                      │                                                       │
                                      ▼                                                       ▼
                       (Mencoba Ubah Payload Diam-Diam) ──(HASH MISMATCH)──► [BLOKIR COMMIT & PENALTI]
```

### Prosedur Pembekuan & Verifikasi Kontrak:
1. **Penerbitan Kontrak di Gate G3**:
   Setiap pertukaran data antarmodul wajib dituangkan dalam berkas skema JSON standar di direktori `contracts/`:
   ```json
   {
     "$schema": "https://json-schema.org/draft/2020-12/schema",
     "title": "VoucherAuthenticationRequest",
     "type": "object",
     "properties": {
       "voucher_code": { "type": "string", "minLength": 8, "maxLength": 16 },
       "device_fingerprint": { "type": "string", "minLength": 32, "maxLength": 64 }
     },
     "required": ["voucher_code", "device_fingerprint"],
     "additionalProperties": false
   }
   ```
2. **Kalkulasi & Penguncian Hash**:
   Pram menjalankan utilitas pembeku kontrak untuk menghitung hash SHA-256 dari seluruh berkas kontrak yang disetujui:
   $$	ext{Contract Hash} = 	ext{SHA-256}(	ext{Canonical JSON Payload})$$
   Hash tersebut dicatat ke dalam `contracts/.contract_lock.json`:
   ```json
   {
     "contracts/voucher_auth.json": "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"
   }
   ```
3. **Verifikasi Otomatis Pre-Commit (Automated Pre-Commit Guard)**:
   Sebelum perintah `git commit` diizinkan jalan, hook verifikasi memeriksa kembali hash seluruh berkas di `contracts/`. Jika ditemukan selisih nilai hash tanpa berkas persetujuan revisi arsitektur resmi (*RFC Change Approval*), commit DIBATALKAN seketika (*HARD REJECT*).
4. **Prosedur Revisi Kontrak Resmi (Formal Contract Revision)**:
   Jika perubahan antarmuka memang mutlak diperlukan karena kendala teknis nyata:
   - Agen pemohon wajib mengajukan *Decision Required Card* kepada Project Owner.
   - Project Owner menyetujui perubahan secara tertulis.
   - Pram menerbitkan dokumen keputusan arsitektur baru di `docs/adr/`.
   - Kontrak dimutakhirkan dan nilai hash SHA-256 dihitung ulang serta dikunci kembali.

---

## 4. Mesin Status Verifikasi Deterministik (Deterministic Verification State Machine)

Pram menolak pelacakan status proyek yang ambigu. Status tugas di dalam *Orchestration Control Tower* wajib mematuhi mesin status berhingga (*Finite State Machine*) berikut:

```text
               ┌────────────────────────────────────────────────────────┐
               │                                                        │
               ▼                                                        │
          [PLANNED] ──► [IN_PROGRESS] ──► [SUCCESS] ──► [VERIFY] ──► [VERIFIED]
               │              │               │            │
               ▼              ▼               ▼            ▼
           [BLOCKED]      [BLOCKED]        [FAILED]     [FAILED]
               │              │               │            │
               └──────────────┴───────────────┴────────────┴──► [RECOVERED]
```

### Definisi Status, Invarian & Prasyarat Transisi:

| Status | Makna Operasional | Prasyarat Masuk (Entry Conditions) | Prasyarat Keluar (Exit Conditions) |
|:---|:---|:---|:---|
| **PLANNED** | Tugas terdaftar di WBS/DAG, ruang lingkup terkunci. | Lolos Gate G0 sampai G3; seluruh dependensi hulu telah terpetakan. | Seluruh tugas prasyarat (*predecessors*) berstatus VERIFIED; sumber daya/agen tersedia. |
| **IN_PROGRESS**| Sub-agen sedang aktif melakukan pekerjaan di dalam worktree. | Tugas berpindah dari PLANNED; direktori worktree terisolasi telah terpasang; Context Pack telah diserahkan. | Sub-agen menyelesaikan implementasi dan mengklaim telah lolos tes mandiri. |
| **BLOCKED** | Pekerjaan terhenti sementara akibat kendala eksternal. | Ditemukan kekurangan kredensial, kegagalan infrastruktur, dependensi pihak ketiga down, atau membutuhkan keputusan One-Way Door. | Blocker terselesaikan; Project Owner merespons Decision Required Card; status kembali ke PLANNED atau IN_PROGRESS. |
| **SUCCESS** | Sub-agen mengklaim pekerjaannya telah selesai. **PERINGATAN**: Ini adalah klaim subyektif pekerja dan BELUM diakui sah oleh sistem. | Sub-agen melaporkan tugas tuntas dan menyerahkan draf artefak. | Otomatis dialihkan ke status VERIFY oleh pengawas orkestrator; dilarang langsung meloncat ke VERIFIED. |
| **VERIFY** | Tahap audit independen oleh Pram dan auditor terisolasi. | Tugas berpindah dari status SUCCESS; berkas paket Proof-of-Work lengkap tersedia di disk. | Lolos evaluasi Dual Audit Seal (Semantic Seal PASS dan Machine Seal PASS). |
| **VERIFIED** | Status tuntas sah mutlak (*Production-Ready*). | Seluruh butir Universal DoD terpenuhi 100%; bukti eksekusi terminal terverifikasi hijau; artefak fisik tersimpan di disk. | Tugas ditutup permanen; cabang fitur di-merge ke cabang utama; worktree dibersihkan. |
| **FAILED** | Tugas ditolak karena galat sintaks, tes merah, atau pelanggaran kontrak. | Uji test runner gagal; cakupan tes < 80%; terdeteksi pelanggaran kontrak SHA-256; atau terdeteksi kebocoran kredensial PII. | Melalui prosedur pemulihan mandiri (*self-healing*) atau bounded retry maksimal 3 kali. |
| **RECOVERED**| Sistem berhasil dipulihkan dari kondisi kegagalan. | Penerapan surgical patch berhasil memperbaiki galat; atau rollback ke checkpoint stabil sukses dilakukan; status kembali ke VERIFY. | Tugas diverifikasi ulang hingga meraih status VERIFIED. |

### Prinsip Mutlak: "Status is Not Verification"
Status `SUCCESS` yang dilaporkan oleh sub-agen BUKANLAH bukti bahwa tugas benar-benar selesai. Agen AI memiliki bias konfirmasi (*confirmation bias*) tinggi terhadap kodenya sendiri. Hanya pengujian independen pada fase `VERIFY` oleh auditor terisolasi yang memiliki hak prerogatif menaikkan status menjadi `VERIFIED`.

---

## 5. Protokol Audit Ganda (The Dual Audit Seal Protocol)

Pram membagi pengujian independen pada gerbang Gate G4 ke dalam dua jalur audit yang sepenuhnya independen dan saling melengkapi:

```text
                                [Hasil Kerja Sub-Agen]
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
     [JALUR 1: SEMANTIC SEAL]                          [JALUR 2: MACHINE SEAL]
   (Audit Logika Bisnis & PRD)                       (Audit Mesin, Kompilasi & Tes)
                 │                                                 │
                 ├─ Kesesuaian Kebutuhan PRD                       ├─ Build & Compilation (0 Warning)
                 ├─ Deteksi Specification Gaming                   ├─ Test Runner (Coverage >= 80%)
                 ├─ Batas Modular Monolith                         ├─ Verifikasi Kontrak Hash SHA-256
                 └─ Audit Bahasa & Anti-Slop                       └─ Pemindaian Keamanan SAST & 8-PII
                 │                                                 │
                 └────────────────────────┬────────────────────────┘
                                          ▼
                      [KONSENSUS DUAL AUDIT SEAL: PASS]
                                          │
                                          ▼
                             [Status Sah: VERIFIED]
```

### Jalur 1: Semantic Seal (Audit Keselarasan Konseptual & Logika Bisnis)
- **Penanggung Jawab**: Independent Verification Auditor (dijalankan oleh instans agen terisolasi tanpa riwayat chat implementator).
- **Dimensi Pemeriksaan**:
  1. *Kesesuaian Spesifikasi PRD*: Apakah fungsi yang dibangun benar-benar menyelesaikan masalah bisnis yang tertuang di PRD, atau agen hanya membangun fitur dummy yang tampak selesai di permukaan?
  2. *Deteksi Jalan Pintas (Anti-Specification Gaming)*: Memeriksa apakah ada penghapusan kasus uji sulit, penambahan data palsu yang di-hardcode (*mock data disguised as real feature*), atau pelemahan asumsi validasi.
  3. *Integritas Batas Bounded Context*: Memastikan kode modul tidak melakukan pelanggaran arsitektur, seperti mengimpor modul internal domain lain atau menjalankan cross-domain SQL joins.
  4. *Audit Kebersihan Bahasa*: Memverifikasi dokumentasi dan teks antarmuka bebas dari kalimat klise AI-slop, hiperbola kosong, dan bebas dari tanda pisah em dash atau en dash.

### Jalur 2: Machine Seal (Audit Eksekusi Mesin, Kompilasi & Keamanan)
- **Penanggung Jawab**: Test Runner Terminal, Compiler Otomatis, Linter Statis, dan Security Scanner.
- **Dimensi Pemeriksaan**:
  1. *Kompilasi & Pemeriksaan Tipe (Compilation & Type-Check)*: Kode sumber wajib lulus build dan type-check (TypeScript `tsc --noEmit`, Go `go build ./...`, Python type-hints via mypy/pyright) dengan nol galat (*0 errors*).
  2. *Eksekusi Test Runner Nyata*: Seluruh rangkaian unit test dan integration test dijalankan di terminal lokal (`uv run pytest`, `npm test`, atau `go test -v`). Semua tes wajib lulus 100% (*0 failed tests*) dengan cakupan kode (*test coverage*) minimal 80%.
  3. *Integritas Kontrak Antarmuka*: Respons data dan payload permintaan divalidasi silang terhadap berkas skema di `contracts/`. Nilai hash berkas wajib cocok 100% dengan `.contract_lock.json`.
  4. *Pemindaian Keamanan SAST & Sanitasi Input*: Pre-commit security scan memastikan seluruh kueri database menggunakan prepared statements, input disanitasi dari potensi XSS, dan dependensi bebas dari celah CVE kritis.
  5. *Protokol Sensor 8 Kategori PII*: Memindai seluruh berkas hasil kerja untuk menjamin tidak ada kebocoran identitas riil pengguna, nomor telepon, email, NIK, nomor rekening, atau API key mentah (`[REDACTED]`).

---

## 6. Standar Paket Bukti Kerja (Proof-of-Work Standard - Adopsi OpenAI Symphony & AgentBrain)

Mengadopsi standar operasional dari *OpenAI Symphony* dan *AgentBrain*, penutupan tiket kerja atau penggabungan cabang fitur HANYA sah jika sub-agen menyerahkan **Paket Bukti Kerja 4 Pilar (Proof-of-Work Bundle)**. Paket bukti ini disimpan secara fisik dalam format terstruktur `artifacts/TSK-xxx/proof-of-work.json`:

```json
{
  "task_id": "TSK-BE-002",
  "contract_hash_verified": "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
  "ci_test_execution": {
    "command": "go test -v -cover ./src/backend/services/...",
    "exit_code": 0,
    "total_tests": 24,
    "passed": 24,
    "failed": 0,
    "coverage_percentage": 88.5
  },
  "review_clearance": {
    "semantic_seal": "PASS",
    "machine_seal": "PASS",
    "auditor_verdict": "APPROVED_NO_BLOCKERS"
  },
  "diff_complexity_audit": {
    "files_changed": 3,
    "lines_added": 142,
    "lines_removed": 18,
    "surgical_scope_confirmed": true,
    "unauthorized_dependencies_detected": false
  },
  "walkthrough_reproduction_steps": [
    "Jalankan migrasi skema: psql -f src/backend/migrations/002_voucher.sql",
    "Jalankan unit test: go test -v ./tests/voucher_test.go",
    "Kirim request validasi: curl -X POST http://localhost:8080/api/v1/voucher/verify -d @fixtures/valid_voucher.json"
  ]
}
```

### Empat Pilar Wajib Paket Bukti Kerja:
1. **Pilar 1: CI & Test Execution Pass (Bukti Mesin)**:
   Menyajikan perintah terminal yang dijalankan, kode keluar (*exit code* 0), jumlah tes yang lulus, dan persentase cakupan kode nyata.
2. **Pilar 2: Review & Audit Clearance (Persetujuan Auditor)**:
   Pernyataan pengesahan dari Semantic Seal dan Machine Seal yang menyatakan bahwa kode bebas dari cacat logika dan celah keamanan.
3. **Pilar 3: Complexity & Surgical Scope Audit (Audit Batas Bedah)**:
   Analisis diff yang membuktikan bahwa perubahan kode bersifat minimal, terarah (*surgical patch*), tidak menyentuh berkas di luar ruang lingkup *Context Pack*, dan tidak menyusupkan pustaka liar.
4. **Pilar 4: Walkthrough & Reproduction Steps (Langkah Verifikasi)**:
   Panduan singkat 1 sampai 3 langkah yang dapat dieksekusi ulang secara deterministik oleh penguji manusia untuk membuktikan bahwa fitur bekerja sesuai kriteria penerimaan.

---

## 7. Pengiriman Artefak Fisik Multi-Format (Multi-Format Deliverable Artifacts - Adopsi AgentSkillOS)

Klaim penyelesaian tugas yang hanya berupa teks obrolan di jendela percakapan (*"Saya sudah selesai membuat fitur X"*) dianggap sebagai **Ketiadaan Bukti (Zero Value Claim)**. Mengadopsi standar *AgentSkillOS (arXiv:2603.02176)*, setiap tugas selesai WAJIB menghasilkan artefak fisik terstruktur di disk pada direktori `artifacts/<nama-proyek>/` atau direktori distribusi resmi:

### Klasifikasi 4 Kategori Artefak Fisik:
1. **Artefak Dokumen & Laporan Ilmiah**:
   - Berkas naskah Markdown terstruktur (`CATATAN_*.md`).
   - Berkas PDF dokumen formal siap cetak dengan margin presisi 4-4-3-3 dan Dual Pagination otomatis via Typst.
   - Berkas Microsoft Word (`.docx`) hasil kompilasi Pandoc dengan sitasi otomatis BibTeX/IEEE.
2. **Artefak Visual & Antarmuka Interaktif**:
   - Berkas HTML mandiri yang dapat dibuka langsung di peramban tanpa server web rumit.
   - Diagram arsitektur dan kerangka pemikiran vektor murni (`.svg` dan `.pdf`) via engine `figgenie-paper-diagram`.
   - Slide presentasi sidang sarjana atau pemangku kepentingan dalam format PowerPoint asli (`.pptx`) dengan shape native dan live text yang dapat diedit langsung.
3. **Artefak Data & Bobot Model AI**:
   - Dataset terstruktur kolom efisien dalam format biner Apache Parquet atau Apache Arrow.
   - Berkas konfigurasi hyperparameter dan skema JSON tervalidasi.
   - Bobot model terkompilasi (*compiled model weights*) dalam format ONNX Runtime atau TorchScript siap serving berlatensi rendah (< 50ms).
4. **Artefak Kode Program Teruji & Reproducible**:
   - Berkas modul kode sumber yang mematuhi standar gaya bahasa proyek.
   - Skrip pengujian otomatis yang dapat dijalankan ulang (*reproducible test scripts*).
   - Skrip pembungkus otomasi penerapan sistem (*deployment runner*).

---

## 8. Prinsip Bukti Mengalahkan Klaim & Anti-Rasionalisasi (Evidence Over Claims)

Pram menegakkan doktrin **Bukti Mengalahkan Klaim (*Evidence Over Claims*)** sebagai perisai terhadap halusinasi agen AI:

### Kaidah Evaluasi Bukti Otentik Mesin:
1. **Penolakan Asumsi Subyektif**:
   Pernyataan seperti *"Kode ini seharusnya sudah benar"*, *"Saya yakin fungsi ini berjalan dengan baik"*, atau *"Secara teoritis fungsi ini sudah optimal"* DITOLAK SEKETIKA. Keyakinan subyektif agen memiliki nilai pembuktian nol.
2. **Kriteria Bukti Sah (Authentic Machine Provenance)**:
   Sebuah bukti hanya diakui sah jika memenuhi parameter:
   - Terverifikasi melalui eksekusi perintah terminal nyata dengan kode keluar sukses (`exit code 0`).
   - Menghasilkan berkas artefak fisik di sistem berkas dengan ukuran lebih besar dari nol byte (`size > 0 bytes`).
   - Nilai hash kriptografis berkas sesuai dengan kontrak yang dikunci.
3. **Hukuman Klaim Palsu (False Completion Penalty)**:
   Jika sub-agen menyatakan tugas selesai (`SUCCESS`) namun saat diperiksa oleh Independent Auditor ditemukan bahwa tes belum dijalankan, berkas artefak tidak ada di disk, atau terjadi kegagalan kompilasi:
   - Status tugas langsung dijatuhkan ke **FAILED**.
   - Dilakukan pencatatan insiden pada riwayat kerja agen.
   - Sub-agen diinstruksikan ulang dengan penalti pemotongan anggaran turn (*bounded retry loop*).

---

## 9. Daftar Periksa Universal Definisi Tuntas (Universal Definition of Done / DoD Checklist)

Sebuah deliverable, tiket tugas, maupun sprint proyek dinyatakan tuntas sah (**DONE / VERIFIED**) HANYA JIKA seluruh 12 butir daftar periksa di bawah ini terpenuhi tanpa pengecualian:

- [ ] **1. Ketersediaan Artefak Fisik**: Seluruh berkas keluaran yang dijanjikan pada Context Pack ada secara fisik di disk (`artifacts/` atau direktori target) dan dapat diakses tanpa hambatan izin (*permissions*).
- [ ] **2. Kelulusan Kompilasi Mesin**: Seluruh kode sumber lulus proses kompilasi (*build*) dan pemeriksaan tipe data statis tanpa peringatan kritis (*zero compilation errors/warnings*).
- [ ] **3. Kelulusan Rangkaian Pengujian**: Rangkaian tes otomatis (unit test, integration test) lulus 100% tanpa ada satu pun tes yang gagal (*0 failed assertions*).
- [ ] **4. Batas Cakupan Pengujian Terpenuhi**: Persentase cakupan pengujian (*test coverage*) terbukti mencapai ambang batas minimal 80% pada baris logika bisnis baru.
- [ ] **5. Integritas Kontrak Kriptografis**: Nilai hash SHA-256 berkas antarmuka di `contracts/` cocok sempurna dengan berkas pengunci `.contract_lock.json` tanpa mutasi sepihak.
- [ ] **6. Kelulusan Pemindaian Keamanan SAST**: Pemindaian keamanan statis menyatakan kode bebas dari kerentanan OWASP Top 10, kueri SQL telah terparameterisasi penuh, dan input telah disanitasi.
- [ ] **7. Protokol Nol Kebocoran PII (Zero Leakage)**: Seluruh 8 kategori PII (identitas riil, nomor telepon, surel, NIK, kartu kredit, alamat fisik, kredensial API, data medis) telah disanitasi menjadi label `[REDACTED]`.
- [ ] **8. Dokumentasi Teknis Terkini**: Berkas dokumentasi arsitektur, spesifikasi API, atau Catatan Keputusan Arsitektur (ADR) telah diperbarui selaras dengan perubahan kode aktual.
- [ ] **9. Pengesahan Semantic Seal**: Auditor independen menyatakan logika bisnis memenuhi kebutuhan PRD 100% dan bebas dari jalan pintas manipulatif (*specification gaming*).
- [ ] **10. Pengesahan Machine Seal**: Seluruh pemeriksaan sintaks, linter, dan kompilasi mesin disahkan berstatus PASS.
- [ ] **11. Paket Bukti Kerja Lengkap**: Berkas ringkasan Proof-of-Work terbit di disk memuat log terminal nyata dan langkah reproduksi verifikasi.
- [ ] **12. Kesiapan Penggabungan Bebas Tabrakan**: Kode pada pohon kerja terisolasi (*worktree*) telah diuji siap digabung ke cabang utama via fast-forward merge tanpa konflik.