# OPERATIONAL REFERENCE: QUALITY ASSURANCE & FIVE-PHASE QUALITY GATES
> Standar penjaminan mutu komprehensif Specialist Skill Architect untuk memastikan setiap modul skill mematuhi standar keandalan tinggi melalui 5 Gerbang Kendali Mutu Bertahap (Gates G0 s.d. G4) dan audit linter otomatis 100/100.

---

## 1. Filosofi Penjaminan Mutu Tanpa Kompromi (Zero-Defect Quality Assurance)

Sebuah specialist skill yang cacat desain atau mengandung inkonsistensi instruksi dapat merusak seluruh alur kerja proyek rekayasa perangkat lunak. Kegagalan umum meliputi:
- Pemicu skill yang terlalu luas sehingga skill aktif secara tidak tepat saat pengguna membicarakan topik lain (*false positive*).
- Pemicu skill yang terlalu sempit sehingga skill tidak pernah dipanggil saat dibutuhkan (*false negative*).
- Pelanggaran keamanan yang membiarkan kredensial rahasia tersimpan di dalam dokumen referensi.
- Adanya tanda pisah tipografis liar em dash atau en dash yang melanggar standar penulisan proyek.

Specialist Skill Architect menerapkan **Sistem Pintu Tol Mutu Bertahap (Gates G0 hingga G4)** untuk seluruh siklus hidup pembuatan dan modifikasi skill.

---

## 2. Rincian 5 Gerbang Kendali Mutu Rekayasa Skill (Gates G0 s.d. G4)

```text
[G0: Validasi Niat & Domain] ──► [G1: Spesifikasi RCCO] ──► [G2: Arsitektur Berkas] ──► [G3: Verifikasi Linter] ──► [G4: Uji Regresi & Rilis]
      (Problem Framing)               (Draft SKILL.md)             (Scaffolding)             (Audit 100/100)               (Production Ready)
```

### Gate 0: Validasi Niat & Kebutuhan Domain (Domain Framing Gate)
- **Kriteria Kelulusan**:
  - Domain keahlian terdefinisi secara jelas dan tidak tumpang tindih dengan skill lokal lain.
  - Telah diputuskan strategi yang tepat melalui matriks keputusan 7 strategi (REUSE, EXTEND, COMBINE, CREATE, ADAPT, REFACTOR, DEPRECATE).
  - Target deliverable fisik terpetakan.

### Gate 1: Spesifikasi Instruksi RCCO (Instruction Specification Gate)
- **Kriteria Kelulusan**:
  - Memuat struktur lengkap: Role, Context, Constraints, dan Output Format.
  - Frasa pemicu di frontmatter YAML memuat kata kunci spesifik dan diuji tidak memicu tabrakan pemicu (*trigger collision*).
  - Batasan In-Scope dan Hard Out-of-Scope dirumuskan secara tegas.
  - Teks mematuhi bahasa Indonesia baku (EYD V dan KBBI) tanpa kata klise AI-slop.

### Gate 2: Arsitektur Berkas & Modularitas (File Scaffolding Gate)
- **Kriteria Kelulusan**:
  - Mengikuti struktur direktori Agent Skills (`SKILL.md`, `references/`, `examples/`, `tests/`, `CHANGELOG.md`).
  - Berkas `SKILL.md` utama berukuran ringkas (< 5.000 token) dan mendelegasikan materi panjang ke modul referensi terpisah.
  - Seluruh tautan internal berkas diuji keberadaannya secara fisik di sistem berkas lokal.

### Gate 3: Verifikasi Linter Mutu Otomatis (Automated Linter Gate - Skor 100/100)
- **Kriteria Kelulusan**:
  - Dijalankan pengujian otomatis menggunakan utilitas linter resmi proyek:
    ```bash
    python scripts/audit_incoming_skills.py skills/<nama-skill>/SKILL.md
    ```
  - **Ambang Batas**: Wajib meraih skor **100/100 (LULUS)**.
  - Nol pelanggaran aturan RCCO.
  - Nol kebocoran path lokal absolut (path drive direktori lokal).
  - Nol kebocoran data sensitif pada 8 taksonomi PII.
  - Nol karakter tanda pisah panjang em dash atau en dash.

### Gate 4: Pengujian Regresi Fungsional & Rilis (Regression & Delivery Gate)
- **Kriteria Kelulusan**:
  - Lolos seluruh kasus uji fungsional pada berkas `tests/regression-cases.md`.
  - Berkas contoh di direktori `examples/` terbukti dapat direproduksi secara deterministik.
  - Riwayat pembaruan dicatat secara lengkap pada berkas `CHANGELOG.md`.
  - Artefak siap digabungkan ke cabang kerja utama.

---

## 3. Matriks Penalti & Resolusi Kegagalan Mutu

| Jenis Pelanggaran Mutu | Tingkat Keparahan | Tindakan Korektif Arsitek |
|:---|:---|:---|
| **Kebocoran Path Komputer Lokal** | CRITICAL | Ganti seluruh path lokal absolut menjadi path relatif proyek atau placeholder `[PROJECT_ROOT]`. |
| **Kebocoran Kredensial / PII** | CRITICAL | Sensor nilai sensitif menjadi label `[REDACTED]` seketika dan bersihkan dari riwayat commit. |
| **Skor Linter Audit < 100** | HIGH | Bedah pesan galat linter, lakukan perbaikan struktural pada berkas, dan uji ulang linter hingga sempurna. |
| **Ditemukan Tanda Pisah Em/En Dash**| MEDIUM | Jalankan skrip pembersih tipografi otomatis untuk mengganti em/en dash menjadi titik dua, tanda kurung, atau koma. |
| **Tautan Referensi Berkas Rusak** | HIGH | Buat berkas referensi yang hilang atau perbaiki penamaan path pada blok `Linked References`. |
| **Deskripsi Pemicu Terlalu Luas** | MEDIUM | Tajamkan kata pemicu dengan menambahkan kata kunci teknis spesifik agar tidak memicu false positive. |