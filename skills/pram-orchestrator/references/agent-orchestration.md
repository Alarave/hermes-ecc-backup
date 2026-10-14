# OPERATIONAL REFERENCE: WBS & DIRECTED ACYCLIC GRAPH (DAG) ENGINE, AGENT ORCHESTRATION & DELEGATION PROTOCOL
> Panduan operasional komprehensif Chief AI Orchestrator (Pram) untuk dekomposisi Struktur Rincian Kerja (WBS), orkestrasi graf dependensi (DAG), navigasi pohon kapabilitas, sandboxing pohon kerja Git (Worktree), penentuan jalur kritis (CPM), standarisasi paket konteks (Context Pack), dan koordinasi multi-agen berstandar industri.

---

## 1. Arsitektur WBS & Directed Acyclic Graph (DAG) Engine

Pram mengurai setiap inisiatif proyek perangkat lunak, sistem data, maupun riset menjadi Struktur Rincian Kerja (*Work Breakdown Structure* / WBS) bertingkat. Setiap unit kerja atomik dipetakan ke dalam Graf Berarah Tanpa Siklus (*Directed Acyclic Graph* / DAG) untuk menjamin urutan eksekusi yang deterministik, bebas galat saling kunci (*deadlock-free*), dan terukur.

```text
                                  [Inisiatif Proyek]
                                          │
                                          ▼
                         [Topological Sort & Cycle Check]
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
     [Gelombang 1: Fondasi Skema]                      [Tugas Independen Awal]
                 │                                                 │
                 ├────────────────────────┬────────────────────────┤
                 ▼                        ▼                        ▼
       [Gelombang 2A: API]      [Gelombang 2B: UI]       [Gelombang 2C: Pipeline]
       (Worktree Sandbox 1)     (Worktree Sandbox 2)     (Worktree Sandbox 3)
                 │                        │                        │
                 └────────────────────────┼────────────────────────┘
                                          ▼
                            [Gelombang 3: Audit & Integrasi]
                                          │
                                          ▼
                             [Rilis / Penggelaran Sistem]
```

### A. Algoritma Pengurutan Topologis (Topological Sort via Kahn's Algorithm)
Untuk menjamin tidak ada dependensi melingkar (*circular dependency*) antar-tugas, Pram menjalankan verifikasi topologis secara matematis sebelum pekerjaan diserahkan ke sub-agen:
1. Hitung derajat masuk (*in-degree*) untuk setiap node tugas di dalam graf. Node dengan derajat masuk 0 adalah tugas tanpa prasyarat (dapat langsung dieksekusi).
2. Masukkan seluruh node dengan derajat masuk 0 ke dalam antrean eksekusi (*Ready Queue*).
3. Selama antrean tidak kosong:
   - Ambil node $u$ dari antrean, masukkan ke dalam urutan eksekusi gelombang aktif.
   - Untuk setiap cabang keluar $(u, v)$, kurangi derajat masuk node $v$ sebesar 1.
   - Jika derajat masuk $v$ menjadi 0, masukkan $v$ ke antrean gelombang berikutnya.
4. **Pencegahan Siklus Mutlak**: Jika jumlah node yang diproses kurang dari total node dalam graf, terdeteksi adanya **Siklus Dependensi Ilegal**. Pram WAJIB menghentikan perencanaan, menyusun laporan analisis akar masalah (RCA), dan menolak DAG hingga siklus diputus.

### B. Pembagian Gelombang Eksekusi (Execution Waves / Tiers)
Seluruh tugas dalam DAG dikelompokkan ke dalam gelombang eksekusi berjenjang:
- **Gelombang 0 (Penetapan Batas & Kontrak)**: Penyusunan PRD, pemetaan bounded context, dan pembekuan kontrak antarmuka API (Gate G0 sampai G3).
- **Gelombang 1 (Struktur Data & Fondasi)**: Pembuatan skema database, migrasi tabel, model domain entitas, dan konfigurasi lingkungan dasar.
- **Gelombang 2 (Implementasi Fitur Independen)**: Pembangunan fungsionalitas modul backend, penyusunan antarmuka frontend, dan pembuatan script pipeline data yang berjalan di cabang pohon kerja terpisah.
- **Gelombang 3 (Verifikasi Integrasi & Audit Ganda)**: Pengujian integrasi ujung ke ujung, validasi kontrak antarmuka, audit keamanan SAST, dan verifikasi Dual Audit Seal.
- **Gelombang 4 (Rilis & Dokumentasi)**: Penggabungan cabang ke garis utama (*main branch*), kompilasi laporan artefak fisik, dan penutupan tiket kerja.

---

## 2. Navigasi Pohon Kapabilitas Hierarkis (Hierarchical Capability Tree Navigation - Adopsi AgentSkillOS)

Pencarian semantik berbasis kemiripan teks harfiah (*pure vector retrieval*) sering mengalami kegagalan sistemik yang disebut **Pandangan Sempit Pemilihan Keahlian (*Myopic Skill Retrieval*)**. Model cenderung hanya memilih alat yang memiliki kemiripan kata kunci tanpa menyadari bahwa penyelesaian tugas membutuhkan agen pendukung dari disiplin ilmu yang berbeda. Mengadopsi arsitektur *AgentSkillOS (arXiv:2603.02176)*, Pram menavigasi ekosistem keahlian melalui **Pohon Kapabilitas 5 Cabang Utama**:

```text
POHON KAPABILITAS AGEN & SKILL (CAPABILITY TREE NAVIGATION):
│
├── [Cabang 1: Tata Kelola, Arsitektur & Kualitas (Governance & Architecture)]
│   ├── pram-orchestrator (Pusat Komando & Manajemen Proyek Teknis)
│   ├── independent-auditor (Verifikator Independen Garis Keras)
│   ├── contract-freezer (Pembeku Antarmuka Hash SHA-256)
│   └── quality-gates (Pengawal Mutu G0 hingga G4)
│
├── [Cabang 2: Sains Data, Pemodelan AI & MLOps (Data, AI & Modeling)]
│   ├── spesialis-data-ai-agentic (Arsitek Pipeline Data & Generative AI)
│   ├── ceemdan-lstm-forecasting (Prediksi Deret Waktu Anti-Leakage)
│   ├── timesfm-forecasting (Model Fondasi Deret Waktu Zero-Shot)
│   └── mlops-orchestration (Siklus Hidup Model, Drift & Registry)
│
├── [Cabang 3: Rekayasa Perangkat Lunak & Sistem (Software Systems)]
│   ├── spesialis-backend (Arsitektur Server, API, Basis Data & Keamanan)
│   ├── spesialis-frontend (Antarmuka Pengguna, Slicing & State Management)
│   ├── git-workflow (Tata Kelola Cabang & Alur Rilis)
│   └── agent-orchestration (Manajemen Sub-Agen & Worktree Sandboxing)
│
├── [Cabang 4: Keamanan Aplikasi, Pengujian & Audit (Security & Verification)]
│   ├── security-reviewer (Protokol Exploit-Patch-Verify Codex Security)
│   ├── security-threat-model (Pemetaan Batas Ancaman & Kebijakan)
│   └── tdd-workflow (Pengembangan Berbasis Pengujian Unit, Coverage >= 80%)
│
└── [Cabang 5: Riset Ilmiah, Produk & Diseminasi (Research & Dissemination)]
    ├── spesialis-research-akademik (Riset SOTA, Metodologi Ilmiah & Uji Statistik)
    ├── research-title-formulator (Formulasi Judul Berbasis Masalah Empiris)
    ├── laporan-generator (Penyusun Naskah Skripsi/Makalah Typst & Pandoc)
    ├── figgenie-paper-diagram (Visualisasi Vektor Kamera-Siap SVG, PDF, PPTX)
    └── campus-repository-scraper (Ekstraksi Metadata & Dokumen EPrints Kampus)
```

### Aturan Komposisi Lintas Cabang (Cross-Branch Composition Rule):
1. **Larangan Eksekusi Monokultur**: Untuk inisiatif berskala menengah hingga besar (Level XL), Pram DILARANG HANYA menugaskan sub-agen dari satu cabang keahlian.
2. **Paket Penugasan Minimal 3 Dimensi**: Setiap rencana kerja wajib mengombinasikan minimal:
   - Satu agen dari **Cabang Eksekusi** (Cabang 2 atau Cabang 3).
   - Satu agen dari **Cabang Verifikasi Mutlak** (Cabang 1 atau Cabang 4).
   - Satu agen dari **Cabang Diseminasi/Dokumentasi** (Cabang 5) jika proyek melibatkan pelaporan akademik atau pemangku kepentingan.

---

## 3. Klasifikasi Skala Tugas: Level L vs Level XL (Adopsi Vibe-Skills)

Untuk mencegah pemborosan anggaran token dan waktu komputasi, Pram mengadopsi mekanisme klasifikasi ukuran tugas dari *Vibe-Skills (Vibe Code Orchestrator)*:

| Dimensi Parameter | Level L (Pekerjaan Terkelola / Linear) | Level XL (Inisiatif Kompleks / Paralel Terkendali) |
|:---|:---|:---|
| **Karakteristik Masalah** | Perbaikan kutu (*bugfix*) terisolasi, penambahan 1 endpoint, refactoring modul tunggal, atau pembaruan dokumentasi. | Penambahan fitur lintas sistem (skema database baru + endpoint API + antarmuka pengguna), pipeline MLOps dari hulu ke hilir, atau perakitan naskah skripsi lengkap. |
| **Jumlah Berkas Terdampak** | 1 hingga 3 berkas dalam domain yang sama. | Lebih dari 4 berkas atau melintasi batas domain bisnis yang berbeda. |
| **Model Eksekusi** | **Sekuensial Tunggal (Linear Fast Path)**. | **Paralel Terbatas (Bounded Parallelism)**. |
| **Batas Konkurensi** | 1 agen aktif (tanpa percabangan sub-agen). | Maksimal **2 sub-agen paralel non-konflik** pada saat bersamaan. |
| **Alokasi Pohon Kerja (Worktree)**| Bekerja langsung di working tree aktif saat ini. | Wajib menggunakan direktori **Git Worktree terisolasi** per tugas. |
| **Overhead Orkestrasi** | Minimal (menghemat hingga 30% konsumsi token). | Koordinasi penuh dengan Context Pack, Proof-of-Work, dan Dual Audit Seal. |

---

## 4. Aturan Eksekusi Paralel (The Zero Shared-State Principle)

Pram menerapkan disiplin rekayasa ketat untuk mencegah tabrakan data (*race conditions*) dan inkonsistensi status pada eksekusi paralel:

### A. Tiga Syarat Mutlak Paralelisme:
Dua atau lebih tugas HANYA boleh dieksekusi secara serempak jika memenuhi ketiga kriteria:
1. **Isolasi Berkas Fisik (Zero File Overlap)**: Tugas A dan Tugas B tidak boleh menyentuh, membaca secara mutatif, atau menulis pada berkas yang sama dalam basis kode.
2. **Isolasi Penyimpanan Basis Data (Zero Table Contention)**: Tugas A dan Tugas B tidak boleh menjalankan operasi DDL (*Data Definition Language*) atau DML (*Data Manipulation Language*) pada tabel basis data yang sama secara bersamaan.
3. **Kontrak Antarmuka Terkunci di Awal (Frozen Interface Anchor)**: Jika Tugas B mengonsumsi keluaran dari Tugas A, format DTO atau skema API wajib telah disepakati, dibekukan, dan dihitung nilai hash SHA-256 pada Gate G3 sebelum tugas dimulai.

### B. Kondisi Wajib Antre (Sequential Gating):
Tugas WAJIB dijalankan secara berurutan (*sequential*) apabila:
- Luaran fisik dari Tugas A merupakan masukan langsung bagi Tugas B (misal: penyiapan dataset latih sebelum pelatihan model).
- Terdapat dependensi migrasi skema database yang memengaruhi struktur tabel downstream.
- Terjadi eskalasi konflik arsitektur yang membutuhkan keputusan manusia (*One-Way Door Decision*).

---

## 5. Sandboxing Tugas Melalui Pohon Kerja Git (Git Worktree Task Sandboxing - Adopsi Orchestrator.inc & Ralphinho)

Menjalankan beberapa agen pada direktori kerja utama yang sama terbukti menyebabkan tabrakan cabang (*branch collisions*), korupsi indeks Git, dan konflik penggabungan kode yang tidak perlu. Mengadopsi arsitektur *Orchestrator.inc* dan pola *Ralphinho/RFC*, setiap tugas Level XL yang berjalan paralel dialokasikan pohon kerja (*worktree*) terpisah:

```text
[Repositori Induk Lokal: branch main]
               │
               ├─► git worktree add .worktrees/TSK-001 (Branch: task/TSK-001) ──► Sub-Agen Backend
               ├─► git worktree add .worktrees/TSK-002 (Branch: task/TSK-002) ──► Sub-Agen Frontend
               │
               ▼ (Setelah Lolos Dual Audit Seal & Proof-of-Work)
[Fast-Forward Merge ke Main & Prune Worktree Otomatis]
```

### Prosedur Operasional Standar (SOP) Manajemen Worktree:
1. **Inisialisasi Direktori Terisolasi**:
   Pram membuat cabang baru dan mengaitkannya ke direktori terisolasi di bawah `.worktrees/`:
   ```bash
   git worktree add -b task/TSK-BACKEND-01 .worktrees/TSK-BACKEND-01 HEAD
   ```
2. **Pemberian Konteks & Pengerjaan**:
   Sub-agen diarahkan untuk bekerja 100% di dalam direktori `.worktrees/TSK-BACKEND-01`. Seluruh kompilasi, penambahan dependensi lokal, dan eksekusi tes berjalan di dalam sandbox ini tanpa mengganggu cabang utama pengguna.
3. **Pemeriksaan Bukti Kerja Mandiri**:
   Sub-agen wajib menjalankan test suite dan linter di dalam worktree tersebut hingga berstatus hijau (100% lulus).
4. **Penggabungan Terkendali (Controlled Fast-Forward Merge)**:
   Setelah paket Proof-of-Work disahkan oleh Independent Auditor, Pram mengintegrasikan perubahan ke cabang target:
   ```bash
   git checkout main && git merge --ff-only task/TSK-BACKEND-01
   ```
5. **Pembersihan Bersih & Penanganan Kunci File Windows (NTFS EBUSY Guard)**:
   Sebelum menghapus direktori worktree di sistem operasi Windows, pastikan seluruh proses terminal latar belakang atau daemon editor yang memegang handle berkas telah dimatikan:
   ```bash
   git worktree remove .worktrees/TSK-BACKEND-01
   git branch -d task/TSK-BACKEND-01
   git worktree prune
   ```

---

## 6. Pemetaan Jalur Kritis (Critical Path Method / CPM) & Alokasi Kapasitas Model

Pram menganalisis durasi dan dependensi tugas menggunakan formula matematis Metode Jalur Kritis untuk menentukan alokasi sumber daya komputasi dan pemilihan model AI:

### A. Formula Matematis Penjadwalan CPM:
Untuk setiap node tugas $i$ dengan durasi estimasi $D_i$:
- **Waktu Mulai Paling Awal (Earliest Start / ES)**:
  $$ES_i = \max_{p \in 	ext{Predecessors}(i)} (EF_p)$$
- **Waktu Selesai Paling Awal (Earliest Finish / EF)**:
  $$EF_i = ES_i + D_i$$
- **Waktu Selesai Paling Akhir (Latest Finish / LF)**:
  $$LF_i = \min_{s \in 	ext{Successors}(i)} (LS_s)$$
- **Waktu Mulai Paling Akhir (Latest Start / LS)**:
  $$LS_i = LF_i - D_i$$
- **Waktu Tenggang / Kelonggaran (Slack Time / Float)**:
  $$	ext{Slack}_i = LS_i - ES_i = LF_i - EF_i$$

### B. Aturan Alokasi Kapasitas Berdasarkan Jalur Kritis:
1. **Node Jalur Kritis ($	ext{Slack} = 0$)**:
   - Merupakan rangkaian tugas yang jika tertunda satu jam saja, akan menunda jadwal rilis keseluruhan proyek.
   - **Alokasi Model**: WAJIB menggunakan **Model Tier-1 (Penalaran Paling Cerdas / High IQ)**, misalnya Claude 3.7 Sonnet (Thinking Mode), OpenAI o3/o4-mini, atau GPT-4o. Dilarang mendelegasikan tugas jalur kritis ke model murah demi menghemat token jika berisiko menghasilkan galat arsitektur.
2. **Node Non-Kritis ($	ext{Slack} > 0$)**:
   - Memiliki kelonggaran waktu sebelum memengaruhi jadwal proyek.
   - **Alokasi Model**: Dapat didelegasikan ke **Model Tier-2 atau Tier-3** (misal: Claude Haiku, GPT-4o-mini, atau model lokal terdistribusi) untuk tugas mekanis, penulisan tes boilerplate, pemformatan Markdown, atau sanitasi teks.

---

## 7. Standarisasi Delegasi Paket Konteks (Context Pack Standard)

Meneruskan seluruh riwayat obrolan panjang (*full chat history dump*) ke sub-agen adalah anti-pattern fatal yang memboroskan token, menurunkan fokus model, dan meningkatkan risiko halusinasi. Setiap kali mendelegasikan tugas melalui `delegate_task` atau role simulation, Pram WAJIB menyusun **Context Pack Mandiri**:

```markdown
### CONTEXT PACK OPERASIONAL: [ID-TUGAS]
- **Target Task ID**: TSK-BE-002
- **Nama Sub-Agen / PIC**: Spesialis-Backend
- **Tujuan Utama (Objective)**: Mengimplementasikan endpoint REST API autentikasi voucher dengan validasi signature perangkat.
- **Konteks & Latar Belakang Domain**: Sistem Berlayar Cafe membutuhkan mekanisme autentikasi voucher satu perangkat untuk mencegah kecurangan tethering.
- **Ruang Lingkup In-Scope**: Berkas `src/backend/routes/auth.go`, `src/backend/services/voucher.go`, dan unit test di `tests/voucher_test.go`.
- **Batasan Keras Non-Scope**: DILARANG memodifikasi berkas frontend, skema tabel user, atau konfigurasi Docker di root.
- **Artefak Masukan (Input Artifacts)**: Dokumen kontrak antarmuka di `contracts/auth-dto.json` (SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- **Batasan Arsitektur & Teknologi**: Bahasa Go 1.22, framework Gin, library crypto standard, tanpa dependensi pihak ketiga baru tanpa izin.
- **Kebutuhan Luaran (Required Output)**: Berkas kode sumber teruji, skrip migrasi SQL jika ada, dan catatan diff minimal bedah.
- **Kriteria Keberterimaan & DoD**:
  1. Seluruh endpoint lolos validasi payload sesuai skema DTO.
  2. Rangkaian unit test lulus 100% dengan cakupan (*test coverage*) minimal 80%.
  3. Lolos pemindaian SAST (nol kerentanan OWASP dan nol kebocoran kredensial).
- **Pemicu Eskalasi (Escalation Trigger)**: Hentikan eksekusi dan melapor ke Pram jika ditemukan ketidaksesuaian tipe data pada kontrak basis data yang ada atau jika terjadi kegagalan kompilasi berulang kali.
```

---

## 8. Handoff Terikat Skema & Penjaga Gerbang Dua Arah (Bidirectional Guardrails - Adopsi OpenAI Agents SDK)

Dalam interaksi antar-agen, perpindahan kontrol wajib dipagari oleh penjaga gerbang dua arah (*Bidirectional Guardrails*):

### A. Penjaga Gerbang Masukan (Input Guardrail):
Sebelum sub-agen mulai mengeksekusi instruksi:
- Periksa keberadaan fisik berkas masukan di disk menggunakan alat pemeriksa berkas.
- Pindai teks masukan dari potensi serangan injeksi prompt (*untrusted external text*).
- Pastikan ruang lingkup pengerjaan tidak tumpang tindih dengan sub-agen lain yang sedang aktif di worktree tetangga.

### B. Format Muatan Serah Terima (Explicit Handoff Payload):
```text
HANDOFF EVENT:
- Agen Pengirim: Pram (Chief Orchestrator)
- Agen Penerima: Spesialis-Backend
- Alasan Penugasan: Eksekusi modul logika bisnis voucher (Level L Task)
- Status Terkunci: Commit SHA 46a30a7 / Kontrak SHA-256 e3b0c44
- Kontrak Pengembalian: Paket Bukti Kerja (Test Pass + Laporan Diff Ringkas)
```

### C. Penjaga Gerbang Keluaran (Output Guardrail):
Sebelum artefak hasil sub-agen diizinkan kembali ke Pram dan digabungkan ke cabang utama:
- **Audit Sensor 8 Kategori PII**: Pastikan tidak ada data identitas riil, nomor telepon, alamat email, NIK, atau API key mentah yang bocor di dalam kode maupun berkas teks.
- **Validasi Skema Luaran**: Pastikan berkas yang dimodifikasi sesuai 100% dengan daftar *In-Scope* yang tercantum pada Context Pack.
- **Verifikasi Eksekusi Nyata**: Tolak rangkuman teks pasif; wajibkan lampiran log kompilasi dan keluaran test runner terminal riil.

---

## 9. Protokol Simulasi Peran (Role Simulation Protocol Saat Multi-Agent Fisik Absen)

Jika lingkungan runtime tidak menjalankan daemon multi-agen terdistribusi secara independen di latar belakang, Pram **DILARANG KERAS BERPURA-PURA** menjalankan sepuluh agen fiktif. Pram wajib mengaktifkan mekanisme **Simulasi Peran Bertingkat yang Transparan**:
1. **Deklarasi Pergantian Perspektif**:
   Pram menyatakan pergantian topi berpikir secara eksplisit di awal blok pemikiran:
   `[PERGANTIAN PERSPEKTIF OPERASIONAL: SPESIALIS-BACKEND]`
2. **Isolasi Konteks Internal**:
   Pram membatasi fokus analisis hanya pada ranah keahlian spesialis tersebut sesuai batasan Context Pack yang dirancang.
3. **Audit Silang oleh Auditor Independen**:
   Setelah implementasi selesai, Pram berganti peran menjadi pengawas mutu:
   `[PERGANTIAN PERSPEKTIF OPERASIONAL: INDEPENDENT-AUDITOR]`
   Auditor memeriksa hasil kerja implementator dengan sikap skeptis garis keras (*Zero Trust Policy*).

---

## 10. Lingkaran Mutu Bertolak Belakang (The Santa Method: Adversarial Quality Loop)

Untuk menghasilkan kode dan dokumentasi berdaya tahan tinggi, Pram menerapkan metode adversarial ala GAN (*Generative Adversarial Network*):
1. **Agen Pembangun (Generator)**: Merancang dan menulis draf kode awal berdasarkan spesifikasi.
2. **Agen Pengkritik (Evaluator / Red Team)**: Mengaudit draf tersebut secara agresif, mencari kelemahan skenario batas (*edge cases*), potensi pembengkakan memori (OOM), celah injeksi input, dan kueri N+1 yang lambat.
3. **Konvergensi Maksimal 3 Putaran**:
   - Putaran 1: Pembangun menyajikan kode -> Pengkritik menemukan celah.
   - Putaran 2: Pembangun memperbaiki celah -> Pengkritik memverifikasi ulang.
   - Putaran 3: Penyempurnaan akhir hingga kedua agen sepakat bahwa kode memenuhi standar produksi.
4. **Batas Putaran**: Jika setelah 3 putaran kode belum mencapai konsensus, Pram menghentikan lingkaran dan menerbitkan *Decision Required Card* kepada Project Owner.

---

## 11. Mediasi Tabrakan Kode (Agent Merge Conflict Arbiter) & Deteksi Macet (Stall Detection)

### A. Protokol Mediasi Tabrakan Penggabungan (Merge Conflict Arbiter):
Jika dua agen secara tidak sengaja memodifikasi berkas konfigurasi bersama:
1. **Pembekuan Eksekusi Seketika**: Hentikan seluruh operasi penulisan otomatis pada berkas yang berkonflik.
2. **Isolasi Pembacaan Diff**: Baca kedua versi diff secara terpisah menggunakan alat pembanding berkas.
3. **Penyelarasan Terhadap Dokumen Keputusan Arsitektur (ADR)**: Evaluasi perubahan mana yang paling patuh terhadap kontrak antarmuka Gate G3.
4. **Rekonsiliasi Deterministik**:
   - Jika perubahan Agen A melanggar kontrak, tolak perubahan Agen A.
   - Jika kedua perubahan melengkapi bagian berbeda, satukan secara manual dan jalankan test suite integrasi.
   - Jika terjadi tabrakan paradigma mendasar, ajukan opsi trade-off ke Project Owner via Decision Required Card.

### B. Protokol Deteksi Macet & Perlindungan Putaran Tanpa Henti (Stall Detection):
- **Indikator Macet**: Agen mengulangi pesan galat terminal yang sama sebanyak 3 kali berturut-turut tanpa mengubah strategi penanganan.
- **Tindakan Penyelamatan Pram**:
  1. Kirim sinyal interupsi darurat dan bekukan proses sub-agen.
  2. Eksekusi analisis akar masalah (*Root Cause Analysis* / RCA 5-Whys).
  3. Lakukan pembatalan mundur (*rollback*) ke titik pemeriksaan Git stabil terakhir.
  4. Sajikan kartu keputusan alternatif penyelesaian kepada pengguna.

---

## 12. Standar Komando Bahasa Indonesia Baku & Zero AI-Slop

Seluruh taklimat penugasan dari Pram ke sub-agen maupun laporan sprint ke Project Owner wajib mematuhi standar komunikasi teknis tingkat tinggi:
1. **Konstruksi Kalimat Komando Taklimat**:
   `[Subyek Operasional] + [Kata Kerja Aktif] + [Objek Komponen] + [Batasan Kontrak] + [Bukti Luaran Mesin]`
2. **Kepatuhan Glosarium Resmi**: Wajib merujuk pada senarai padanan istilah bahasa Indonesia baku (`references/kamus-istilah-rekayasa-dan-tpm.md`). Prioritaskan istilah Kelas A (*unduh, unggah, tembolok, basis data, berkas, fungsi, galat*) dan sertakan padanan Kelas B untuk istilah sains.
3. **Gaya Dingin, Lugas, dan Objektif**: Dilarang menggunakan pengantar basa-basi klise AI, pujian berlebihan, atau bahasa pemasaran kosong. Ganti klaim subjektif dengan fakta angka terukur. DILARANG KERAS menggunakan tanda pisah em dash atau en dash.