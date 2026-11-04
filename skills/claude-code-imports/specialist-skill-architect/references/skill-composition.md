# OPERATIONAL REFERENCE: SKILL COMPOSITION, MERGING & MODULAR ARCHITECTURE
> Panduan operasional komprehensif Specialist Skill Architect untuk menggabungkan dua atau lebih skill yang terfragmentasi, menyusun komposisi kapabilitas multi-agen, dan merancang arsitektur modul skill yang kohesif tanpa menimbulkan monolit instruksi yang kusut.

---

## 1. Masalah Fragmentasi Skill & Solusi Konsolidasi

Dalam ekosistem AI yang berkembang pesat, sering kali muncul fenomena **Fragmentasi Skill Berlebih (*Skill Proliferation & Fragmentation*)**. Kondisi ini terjadi ketika terlalu banyak skill kecil dibuat untuk tugas-tugas mikro yang sebenarnya berada dalam satu domain yang sama.
Contoh konkret:
- Memisahkan penulisan skripsi akademik menjadi dua skill berbeda (`spesialis-laporan-akademik` vs `spesialis-research-akademik`).
- Akibatnya:
  1. Pengguna dan agen orkestrator bingung memilih skill mana yang harus dipanggil (*Cognitive Load*).
  2. Terjadi tabrakan kata pemicu (*Trigger Collision*).
  3. Terjadi duplikasi berkas referensi yang memboroskan ruang disk dan mempersulit sinkronisasi.

Specialist Skill Architect menerapkan prinsip **Penyatuan Domain Kohesif (*Cohesive Domain Consolidation*)**: Skill yang melayani satu tujuan domain terpadu wajib dikonsolidasikan menjadi satu modul komprehensif, sementara pemisahan fungsional diatur melalui mode operasional internal atau modul referensi.

---

## 2. Studi Kasus Riil: Menggabungkan `spesialis-laporan-akademik` ke dalam `spesialis-research-akademik`

Berikut adalah dokumentasi langkah demi langkah dari konsolidasi riil yang dilakukan arsitek:

### A. Analisis Awal (Baseline Inspection & Gap Analysis)
1. *Karakteristik `spesialis-laporan-akademik`*:
   - Hanya berupa berkas stub `SKILL.md` sederhana yang mendaftarkan pemicu penulisan laporan dan menautkan berkas referensi Bab 1 sampai Bab 5.
   - Pemicu utama: `"nulis laporan"`, `"skripsi"`, `"tesis"`, `"paper"`, `"format akademis"`.
2. *Karakteristik `spesialis-research-akademik`*:
   - Merupakan modul riset ilmiah komprehensif yang telah memuat 3 mode operasional (Socratic Grill, Guided Drafting, Defense Simulation), standar format Gunadarma (margin 4-4-3-3, dual pagination), integrasi FigGenie, dan 30+ berkas referensi lengkap (termasuk Bab 1 sampai Bab 5).
3. *Temuan Kritis*:
   - Terjadi tumpang tindih 100% pada berkas referensi dan irisan besar pada kata pemicu. Keberadaan `spesialis-laporan-akademik` sebagai skill mandiri tidak memberikan nilai tambah dan hanya menimbulkan kebingungan routing.

### B. Prosedur Penggabungan 4 Langkah:
```text
[spesialis-laporan-akademik]                    [spesialis-research-akademik]
            │                                                 │
            ├─ 1. Ekstraksi Kata Kunci Pemicu                │
            │    ('nulis laporan', 'format akademis', dll.)   │
            │                                                 ▼
            └───────────────────────────────────► [2. Injeksi Pemicu ke SKILL.md]
                                                              │
                                                              ▼
            [3. Hapus Direktori Redundan]        [4. Uji Verifikasi & Linter 100/100]
            (rm -rf spesialis-laporan-akademik)  (scripts/audit_incoming_skills.py)
```

1. **Langkah 1: Injeksi Kata Pemicu**:
   Memperbarui atribut `description` pada `skills/spesialis-research-akademik/SKILL.md` agar mencakup seluruh kata kunci pemicu lama:
   ```yaml
   description: "Use when user says 'cari paper', 'riset literatur', 'metodologi', 'jurnal ilmiah', 'bedah paper', 'review akademik', 'bikin skripsi', 'bimbingan skripsi', 'tulis manuskrip', 'nulis laporan', 'skripsi', 'tesis', 'paper', 'jurnal', 'format akademis', 'daftar pustaka', 'sitasi', atau 'sidang skripsi'. Agen orkestrasi riset akademik dan laporan ilmiah end-to-end (Q1/Q2 & Gunadarma standard)."
   ```
2. **Langkah 2: Sinkronisasi Referensi Prosedural**:
   Memastikan seluruh panduan penulisan naskah (Bab 1 s.d. 5, pedoman Gunadarma, cover, dan format sitasi) tersedia dan diperbarui di `skills/spesialis-research-akademik/references/`.
3. **Langkah 3: Pembersihan Bersih (Clean Deprecation)**:
   Menghapus direktori fisik `skills/spesialis-laporan-akademik/` dari disk lokal agar tidak terjadi tabrakan indeks pada sistem runtime.
4. **Langkah 4: Validasi Integritas**:
   Menjalankan linter `scripts/audit_incoming_skills.py` untuk mengonfirmasi bahwa skill penerus lolos audit mutu tanpa ada tautan referensi yang rusak (*broken links*).

---

## 3. Desain Komposisi Skill Multi-Agen (Cross-Skill Orchestration)

Ketika sebuah proyek besar membutuhkan kerja sama antara beberapa specialist skill, Specialist Skill Architect merancang **Kontrak Komposisi Antar-Skill (*Inter-Skill Composition Contract*)**.

### Prinsip Komposisi Sehat:
1. **Tanggung Jawab Tunggal (Single Responsibility)**:
   - `pram-orchestrator`: Mengatur perencanaan, WBS, DAG dependensi, dan alokasi tugas.
   - `spesialis-backend`: Bertanggung jawab penuh atas API, database, dan logika server.
   - `spesialis-frontend`: Bertanggung jawab atas UI, antarmuka pengguna, dan interaksi visual.
   - `specialist-skill-architect`: Bertanggung jawab atas rekayasa, audit, dan perluasan skill itu sendiri.
2. **Ketergantungan Bebas Siklus (Acyclic Dependency Principle)**:
   - Skill DILARANG memanggil satu sama lain dalam siklus melingkar (Circular Dependency: Skill A -> Skill B -> Skill A).
   - Seluruh alur koordinasi lintas skill wajib dimediasi oleh Orchestrator (Pram) melalui gerbang data yang terdefinisi.
3. **Kontrak Antarmuka Eksplisit (Explicit Data Handoff)**:
   - Data yang diserahkan antar-skill wajib berupa berkas artefak fisik di disk (skema JSON, DTO, atau dokumen Markdown terstruktur) dengan nilai hash integritas yang tercatat.