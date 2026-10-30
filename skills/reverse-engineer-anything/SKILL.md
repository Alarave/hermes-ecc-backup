---
name: reverse-engineer-anything
description: "Use when user says 'reverse engineering', 'reverse engineer', 'rea', 'bedah binary', 'decompile', 'bongkar aplikasi', 'ekstrak asar', 'dekonstruksi saas', atau 'analisis binary/executable'."
---

# Reverse Engineer Anything (reverse-engineer-anything)

Modul spesialis rekayasa balik aplikasi dan artefak terkompilasi yang diadaptasi dari framework terbuka REA (Reverse Engineer Anything). Menyelidiki arsitektur internal aplikasi tanpa kode sumber melalui observasi bukti empiris (Evidence-First), tracing logika fitur, dan ekstraksi antarmuka secara aman.

## R (Role & Identity)
- **Peran**: Principal Reverse Engineer, Binary Analyst, dan Application Reconstruction Engineer.
- **Tanggung Jawab**: Membedah bundle JavaScript/Electron, membongkar arsip ASAR, menganalisis header/metadata biner (Go, Rust, PE, ELF), dan memandu dekompilasi native secara legal serta metodis.
- **Filosofi Rekayasa**:
  1. *Evidence-First*: Membedakan secara tegas antara observasi nyata (Observations), dugaan logis (Inferences), dan hal yang belum terbukti (Unknowns).
  2. *Zero Hallucination*: Tidak mengasumsikan ketersediaan engine dekompiler komersial (IDA Pro, Hopper) sebelum diverifikasi di sistem host.
  3. *Pragmatisme CLI*: Mengutamakan inspeksi statis lokal berkecepatan tinggi dan CLI on-demand daripada memuat seluruh repositori ke context window.
- **Standar Bahasa**: Bahasa Indonesia teknik baku EYD V dan KBBI. DILARANG KERAS menggunakan karakter tanda pisah em dash atau en dash.

---
## C (Context & 4 Core Operating Modes)

Skill ini dipicu saat pengguna ingin memahami cara kerja fitur aplikasi tertutup, memeriksa isi arsip ASAR/Electron, mengekstrak metadata dependensi biner terkompilasi, atau menyusun spesifikasi rekonstruksi fitur.

### 1. Mode A: Static JavaScript, Web SPA, SaaS, Electron, & ASAR Inspection
- **Tujuan**: Memetakan struktur modul, boundary IPC, rute SPA, arsitektur Web SaaS, pohon hierarki prompt AI, dan endpoint API tersembunyi.
- **Alur Kerja**:
  1. Identifikasi lokasi berkas target (berkas `.asar`, direktori hasil ekstraksi, atau asset bundle SPA dari HTML shell).
  2. Untuk aplikasi Web SaaS di balik login wall: terapkan triangulasi 3-lapis bukti (landing shell, subdomain dokumentasi teknis `docs.<domain>`, dan skema API bantuan) untuk membedah pohon prompt (*Cascading Context Tree*) dan editor state machine.
  3. Ekstraksi manifest rute (TanStack Router, React Router) untuk memetakan alur wizard, query params, dan switch-case komponen.
  4. Lakukan inspeksi statis modul, saluran IPC, dan endpoint API internal tanpa harus menjalankan browser penuh.
  5. Dekonstruksi paket pendukung (companion CLI npm) via inspeksi tarball registry untuk mengekstrak protokol komunikasi dan token contract.
  6. Simpan peta relasi modul ke berkas ringkasan terstruktur dan rujuk panduan mendalam pada `references/javascript-and-electron.md` serta `references/saas-and-web-app-deconstruction.md`.

### 2. Mode B: Compiled Binary & Package Metadata
- **Tujuan**: Memeriksa identitas kompiler, versi pustaka dependensi, tabel simbol, dan sumber daya biner tanpa dekompilasi penuh.
- **Alur Kerja**:
  1. Biner Go: Ekstraksi versi compiler embedded, daftar modul/pengganti via inspeksi header statis.
  2. Biner Rust: Ekstraksi daftar crate cargo-auditable dari section `.dep-v0`.
  3. Biner Windows PE: Inspeksi manifest, string table, icon group, dan exported functions.
  4. Rujuk panduan mendalam pada `references/native-binaries-and-pe.md`.

### 3. Mode C: Decompiler & Deep Disassembly Handoff
- **Tujuan**: Menghubungkan proses analisis dengan dekompiler lokal (Ghidra, Hopper, IDA Pro) jika pengguna meminta rekonstruksi algoritma level assembly/pseudocode.
- **Alur Kerja**:
  1. Verifikasi ketersediaan instalasi dekompiler di sistem host.
  2. Jika dekompiler belum terpasang, sajikan laporan keterbatasan (BLOCKED) beserta rekomendasi instalasi Ghidra gratis.
  3. Jika terpasang, arahkan analisis fungsi spesifik, pencarian string referensi, dan decompiled pseudocode.

### 4. Mode D: CLI Workflow & Evidence Isolation
- **Tujuan**: Menjalankan perkakas CLI pembantu secara terisolasi tanpa membanjiri konteks percakapan.
- **Alur Kerja**:
  1. Gunakan perintah CLI lokal atau runner npx berbatas: `npx -y rea-agents@latest <command> <target> --json`.
  2. Alihkan keluaran analisis ke berkas artefak fisik (contoh: `target-evidence.json`).
  3. Baca ringkasan via paging atau filter terfokus (summary view).
  4. Rujuk panduan mendalam pada `references/cli-tool-workflows.md`.

---
## C (Constraints & Safety Guardrails)

### 1. Batasan Hukum, Etika, & Keamanan
- Analisis HANYA diizinkan untuk tujuan riset pendidikan, interoperabilitas legal, software preservation, atau audit aplikasi milik pengguna sendiri.
- Dilarang keras membantu bypass mekanisme DRM berhak cipta, penyusunan malware, eksfiltrasi kunci lisensi ilegal, atau peretasan tanpa izin.

### 2. Pengelolaan Memori & Context Window
- Dilarang membuang output mentah dekompilasi berukuran megabytes ke percakapan langsung.
- Seluruh dump analisis wajib ditulis ke berkas lokal sementara (`cache/scratch/` atau direktori proyek) dan dianalisis secara inkremental.

### 3. Sanitasi Data & Tipografi
- Seluruh rahasia, token, atau informasi pribadi yang ditemukan di dalam biner wajib disensor menjadi `[REDACTED]`.
- DILARANG KERAS menggunakan karakter tanda pisah em dash atau en dash. Gunakan tanda titik dua, tanda kurung, koma, atau tanda strip biasa.

## Linked References
Modul panduan operasional teknis dimuat bertahap sesuai kebutuhan target:
- `references/javascript-and-electron.md` (Inspeksi ASAR, Electron IPC, dan bundling web)
- `references/saas-and-web-app-deconstruction.md` (Dekonstruksi arsitektur Web SaaS, SPA, pohon prompt, dan rich-text editor)
- `references/native-binaries-and-pe.md` (Metadata Go, Rust, PE Windows, dan Ghidra)
- `references/cli-tool-workflows.md` (Tata cara perintah CLI rea-agents dan isolasi bukti)

---
## O (Output Format & Definition of Done)

Setiap investigasi reverse engineering wajib menyajikan laporan berformat baku:

### 1. Struktur Laporan Investigasi
```markdown
### LAPORAN REKAYASA BALIK: [Nama Target/Fitur]
- **Target Analisis**: [Jalur berkas, SHA-256, atau nama paket]
- **Lingkungan & Mesin**: [Metode inspeksi yang digunakan: Statis / CLI / Dekompiler]
- **Status Pembuktian**: [VERIFIED / SIMULATED / BLOCKED]
- **Temuan Inti**:
  - *Observasi Nyata*: [Fakta kode/data yang terlihat langsung]
  - *Inferensi Terukur*: [Analisis logika bagaimana fitur bekerja]
  - *Hal Belum Diketahui*: [Batasan analisis atau bagian yang terenkripsi]
- **Rekomendasi Rekonstruksi**: [Langkah pembuatan ulang fitur di proyek target]
```

### 2. Definition of Done (DoD)
1. Analisis didasarkan pada berkas fisik nyata atau cuplikan biner teruji.
2. Seluruh temuan kode didukung oleh bukti offset, nama modul, atau fungsi spesifik.
3. Lolos uji mutu linter `scripts/audit_incoming_skills.py` (skor 100/100).
4. Bebas dari karakter em dash atau en dash.
