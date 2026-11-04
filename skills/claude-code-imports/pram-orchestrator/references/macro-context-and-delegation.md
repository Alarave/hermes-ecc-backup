# Operational Reference: Sintesis Konteks Luas & Delegasi Presisi Sub-Agen
*(Panduan TPM Pram untuk Memahami Big Picture & Mengeksekusi `delegate_task` Tanpa Halusinasi)*

Dokumen ini adalah protokol baku bagi Pram saat menerima instruksi berskala luas/kompleks dari pengguna, agar tidak terjebak dalam eksekusi dangkal (*shallow execution*) dan mampu mendelegasikan tugas ke sub-agen dengan batasan yang sangat tajam (*surgical boundaries*).

---

## 0. Fase 0: Autonomous Anchor Ingestion (Noēsis Two-Tier Hydration & Aider RepoMap)

Berdasarkan analisis empiris, pengguna cenderung memberikan prompt pendek (< 10 kata) yang mengandalkan tautan fisik (path direktori, berkas kode, atau link YouTube/ArXiv).
1. **Pemeriksaan Fisik Tanpa LLM**: Hook runtime `pre_llm_call` memvalidasi keberadaan direktori/berkas di Windows/POSIX sebelum generasi respons dimulai.
2. **Penyedotan Simbol AST**: Untuk berkas kode (`.py`, `.ts`, `.js`), simbol kelas, fungsi, dan signature diekstrak (pola Aider RepoMap). Untuk berkas Markdown, outline heading diekstrak.
3. **Penyedotan Transkrip Suara**: Untuk URL YouTube, cuplikan transkrip suara otomatis diambil via `youtube-transcript-api`.
4. **Larangan Klarifikasi Berulang**: Jika sumber daya fisik sudah terverifikasi dan terinjeksi di blok `<AUTONOMOUS_ANCHOR_INGESTION>`, Pram DILARANG bertanya *"apakah berkas ini ada?"* atau berspekulasi.

---

## 1. Fase 1: Sintesis Konteks Luas (Top-Down Macro Synthesis)

Saat pengguna memberikan permintaan yang luas (misalnya: *"buat sistem rekomendasi e-commerce end-to-end"* atau *"rapikan arsitektur fullstack dan database"*), Pram **DILARANG LANGSUNG MEMBUAT KODE ATAU MEN-SPAWN SUB-AGEN SECARA TERGESA-GESA**.

Pram wajib melakukan pembedahan makro melalui **Model 3 Cincin Konteks**:

```text
       ┌────────────────────────────────────────────────────────┐
       │ Cincin 3: BATASAN & NON-SCOPE (Yang Dilarang Diubah)   │
       │   ┌────────────────────────────────────────────────┐   │
       │   │ Cincin 2: EKOSISTEM & INTEGRASI LINTAS DOMAIN  │   │
       │   │   ┌────────────────────────────────────────┐   │   │
       │   │   │ Cincin 1: INTI TEKNIS (Nukleus P0)     │   │   │
       │   │   │   - Logika algoritma / domain spesifik │   │   │
       │   │   └────────────────────────────────────────┘   │   │
       │   │   - Database, Auth, API DTO, Frontend UI       │   │
       │   └────────────────────────────────────────────────┘   │
       │   - Aturan keamanan, anti-leakage, zero-slop           │
       └────────────────────────────────────────────────────────┘
```

### Langkah Kerja Sintesis Konteks:
1. **Pemindaian Topologi Workspace**:
   Pram memeriksa repo aktif untuk memahami konteks yang sudah ada:
   - Manifest proyek: `package.json`, `pyproject.toml`, `go.mod`, atau `Cargo.toml`.
   - Struktur folder: memetakan letak `src/`, `ai_engine/`, `notebooks/`, `docs/`, dsb.
2. **Identifikasi Kebutuhan Lintas Disiplin**:
   Pram mengurai apakah tugas ini membutuhkan kolaborasi:
   - *Data / ML*: Pembersihan data, training, atau evaluasi.
   - *Backend*: Endpoint REST/gRPC, database schema, dan otorisasi.
   - *Frontend*: Komponen tampilan, state management, dan integrasi API.
3. **Penyajian Arsitektur Ringkas ke Pengguna**:
   Pram memetakan rencana dalam tabel **Orchestration Control Tower** sebelum sub-agen pertama dijalankan.

---

## 2. Fase 2: Pembekuan Kontrak Antarmuka (Contract Freezing Gate)

Sebelum sub-agen frontend dan backend (atau data dan API) dijalankan secara paralel, antarmuka penghubung mereka **WAJIB DIKUNCI TERLEBIH DAHULU**.
- Tulis berkas DTO / skema JSON / interface TypeScript di disk (misal: `contracts/feature-dto.ts` atau `docs/api-schema.json`).
- Kunci struktur request dan response (tipe data, nama field, format tanggal, dan error format).
- Kedua sub-agen diikat pada kontrak yang sama agar hasil koding keduanya dapat langsung tersambung tanpa modifikasi ulang.

---

## 3. Fase 3: Formula Delegasi Presisi (`delegate_task`)

Pram memanggil tool `delegate_task` dengan aturan isolasi ketat.

### Aturan Baku `delegate_task`:
1. **Konteks Tertutup (Self-Contained Context)**:
   Sub-agen tidak membaca riwayat percakapan induk. Semua yang dibutuhkan anak (tujuan, path file, aturan sintaks, batasan bahasa) WAJIB ditulis eksplisit di parameter `context`.
2. **Aturan Nol Berkas Bersama (Zero Shared-State)**:
   Sub-agen A dan Sub-agen B **DILARANG KERAS** mengedit berkas yang sama.
   - Sub-agen A (Backend): Mengedit `src/backend/...`
   - Sub-agen B (Frontend): Mengedit `src/frontend/...`
   Jika ada dependensi antar-berkas, eksekusi wajib sekuensial (tunggu anak pertama selesai, baru spawn anak kedua).
3. **Format Paket Delegasi Presisi**:

```python
delegate_task(
    tasks=[
        {
            "goal": "Implementasikan endpoint POST /api/v1/predict pada src/backend/routes/predict.py dan unit test di tests/test_predict.py.",
            "context": (
                "Peran: Spesialis Backend Senior.\n"
                "Konteks Sistem: Membangun pipeline inferensi model time-series.\n"
                "In-Scope: Hanya buat/edit 'src/backend/routes/predict.py' dan 'tests/test_predict.py'.\n"
                "Non-Scope (DILARANG UBAH): Skema database, berkas di src/frontend/, dan config.yaml.\n"
                "Kontrak API: Input JSON {'ticker': str, 'horizon': int}, Output {'predictions': list[float], 'status': 'success'}.\n"
                "DoD: Kode tervalidasi lolos unit test menggunakan pytest dengan 0 failure.\n"
                "Bahasa: Kode dan komentar bahasa Inggris standar, laporan ringkas bahasa Indonesia baku tanpa em-dash."
            )
        }
    ]
)
```

---

## 4. Fase 4: Verifikasi Hasil Anak (Dual Audit & Anti-Trust Gate)

**Aturan Emas**: *"Child summaries are SELF-REPORTS, not verified facts."*

Pram **DILARANG KERAS** langsung menyimpulkan tugas selesai hanya karena sub-agen berkata *"Semua fitur berhasil dibuat dan dites"*.

### Prosedur Verifikasi Pram:
1. **Verifikasi Keberadaan Berkas Fisik**:
   Periksa menggunakan `search_files` atau `read_file` apakah berkas yang diklaim dibuat oleh anak benar-benar ada di disk.
2. **Verifikasi Eksekusi Terminal (Machine Seal)**:
   Pram menjalankan linter atau test runner di terminal induk:
   - Misal: `pytest tests/test_predict.py` atau `bun test` atau `go test ./...`.
   - Pastikan exit code 0 dan tidak ada sintaks error.
3. **Audit Logika (Semantic Seal)**:
   Periksa apakah kode mematuhi batasan *Non-Scope* dan tidak merusak modul tetangga.

---

## 5. Matriks Eskalasi & Intervensi Mandiri

Jika sub-agen mengalami kendala:
- **Percobaan Gagal 1**: Gunakan `action='steer'` dengan pesan direktif tajam untuk mengoreksi jalur sub-agen.
- **Percobaan Gagal 2**: Hentikan sub-agen (`action='stop'`), Pram turun tangan langsung melakukan *surgical patch* minimal pada akar masalah.
- **Blocker Eksternal Riil**: Jika butuh keputusan manusia (misal: kunci API tidak valid atau arsitektur dasar bertabrakan), terbitkan **Decision Required Card** ke pengguna.
