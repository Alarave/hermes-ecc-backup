# OPERATIONAL REFERENCE: STEP-BY-STEP IMPLEMENTATION WORKFLOWS
> Panduan prosedur operasional standar (SOP) langkah demi langkah untuk mengeksekusi 4 Mode Kerja Utama Specialist Skill Architect (EXPLAIN, CREATE, EXTEND, IMPROVE).

---

## 1. SOP Mode A: EXPLAIN (Analisis & Penjelasan Arsitektur Skill)

Mode ini dijalankan saat pengguna meminta penjelasan mengenai kapabilitas, batasan, atau cara kerja skill tertentu.

### Prosedur Eksekusi 5 Langkah:
1. **Langkah 1: Inspeksi Berkas Sumber**:
   - Baca berkas `SKILL.md` utama dan periksa daftar berkas di direktori `references/`.
2. **Langkah 2: Pemetaan 4 Dimensi RCCO**:
   - Ekstrak Role, Context (Operating Modes), Constraints (Scope & Rules), dan Output Format.
3. **Langkah 3: Analisis Realisme Tools**:
   - Identifikasi tools yang dibutuhkan skill dan periksa apakah tools tersebut tersedia di sistem lokal.
4. **Langkah 4: Evaluasi Kelemahan & Titik Kritis**:
   - Identifikasi potensi kegagalan umum (failure modes) dan kondisi di mana skill rentan mengalami halusinasi.
5. **Langkah 5: Penyusunan Laporan Penjelasan**:
   - Sajikan laporan terstruktur memuat identitas, alur kerja, batasan operasional, contoh pemicuan, dan saran pemanfaatan terbaik.

---

## 2. SOP Mode B: CREATE (Pembuatan Skill Baru dari Nol)

Mode ini dijalankan saat pengguna membutuhkan skill baru untuk domain keahlian yang belum tercakup di sistem lokal.

### Prosedur Eksekusi 7 Fase:
1. **Fase 1: Penegasan Kebutuhan & Lingkup**:
   - Tetapkan nama skill dalam format kebab-case presisi.
   - Rumuskan In-Scope dan Hard Out-of-Scope secara tegas.
2. **Fase 2: Riset Kemampuan Serupa**:
   - Periksa inventaris lokal dan teliti repositori GitHub resmi jika membutuhkan pola arsitektur mutakhir.
3. **Fase 3: Pembuatan Struktur Direktori Fisik**:
   - Buat folder `skills/<nama-skill>/` beserta subdirektori `references/`, `examples/`, dan `tests/`.
4. **Fase 4: Penulisan Berkas Entrypoint `SKILL.md`**:
   - Tulis frontmatter YAML valid dengan deskripsi pemicu tajam.
   - Susun tubuh dokumen mematuhi standar empat pilar RCCO dalam bahasa Indonesia baku.
5. **Fase 5: Penulisan Modul Referensi Prosedural**:
   - Pecah instruksi teknis panjang ke dalam berkas-berkas terpisah di direktori `references/`.
6. **Fase 6: Penyusunan Kasus Uji & Contoh Implementasi**:
   - Buat minimal 3 berkas contoh di `examples/` dan daftar kasus uji regresi di `tests/`.
7. **Fase 7: Audit Kepatuhan & Penyelesaian**:
   - Jalankan linter `python scripts/audit_incoming_skills.py` dan pastikan meraih skor 100/100.
   - Buat berkas `CHANGELOG.md` awal (v1.0.0).

---

## 3. SOP Mode C: EXTEND (Perluasan Kemampuan Eksisting)

Mode ini dijalankan untuk menambahkan kemampuan baru tanpa merusak fungsionalitas sebelumnya.

### Prosedur Eksekusi 5 Langkah:
1. **Langkah 1: Pencatatan Baseline**:
   - Periksa versi terkini dan pastikan repositori Git dalam kondisi bersih tanpa perubahan tertunda.
2. **Langkah 2: Desain Modul Tambahan**:
   - Buat berkas referensi baru di direktori `references/` untuk menampung prosedur baru (Progressive Disclosure).
3. **Langkah 3: Pembaruan Entrypoint `SKILL.md`**:
   - Tautkan berkas referensi baru pada section `Linked References`.
   - Perbarui atribut `description` di frontmatter jika ada kata kunci pemicu baru yang perlu didaftarkan.
4. **Langkah 4: Pengujian Regresi Kompatibilitas**:
   - Jalankan uji regresi untuk memastikan kemampuan lama tidak mengalami penurunan kualitas.
5. **Langkah 5: Pencatatan Riwayat & Kenaikan Versi**:
   - Naikkan nomor versi Minor pada `CHANGELOG.md` (misal: v1.0.0 -> v1.1.0).

---

## 4. SOP Mode D: IMPROVE (Audit, Refactoring & Penggabungan Skill)

Mode ini dijalankan saat melakukan optimasi, pembersihan slop, atau penggabungan dua skill yang tumpang tindih.

### Prosedur Eksekusi 5 Langkah:
1. **Langkah 1: Audit Mendalam 10 Aspek**:
   - Evaluasi aspek: integritas struktur, realisme tools, efisiensi konteks, keamanan PII, dan kebersihan tipografi.
2. **Langkah 2: Perumusan Rencana Perbaikan (Upgrade Plan)**:
   - Buat matriks keputusan perbaikan yang merinci apa yang ditambah, diubah, atau dihapus beserta alasannya.
3. **Langkah 3: Penerapan Surgical Refactoring**:
   - Terapkan perbaikan minimal yang berdampak tinggi (*minimal sufficient change*).
   - Bersihkan kalimat klise AI-slop dan hilangkan seluruh karakter em/en dash.
4. **Langkah 4: Pengujian & Linter Clearance**:
   - Jalankan linter proyek dan pastikan meraih skor kelulusan 100/100.
5. **Langkah 5: Kompilasi Laporan Eksekutif**:
   - Rangkum temuan audit, matriks keputusan, dan hasil pengujian ke dalam laporan akhir.