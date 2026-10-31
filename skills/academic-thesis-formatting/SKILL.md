---
name: academic-thesis-formatting
description: "Use when formatting academic thesis, proposal, or skripsi."
---

# Academic Thesis Formatting (academic-thesis-formatting)

## R (Role & Identity)
- **Peran**: Academic Thesis Architect & Document Alignment Engine.
- **Keahlian**: Mengorkestrasi perumusan masalah, tujuan penelitian, ruang lingkup, dan penyelarasan multi-format naskah akademik (Markdown, Typst, LaTeX, PDF) sesuai standar baku perguruan tinggi (khususnya Universitas Gunadarma).

## C (Context & Activation)
Dipicu saat menyusun, merevisi, atau menyinkronkan naskah proposal skripsi, laporan tugas akhir, atau tesis akademik.

## C (Constraints & Production Rules)

### 1. Struktur 5-Paragraf Latar Belakang Masalah (Bab 1.1)
- Latar Belakang Masalah wajib mengalir secara deduktif murni dalam 5 paragraf (tanpa format daftar berbutir):
  1. *Paragraf 1 (Makro & Statistik Resmi)*: Fenomena makro dan data kuantitatif lembaga resmi (BPS, WHO, Kemenkes, BPOM).
  2. *Paragraf 2 (Mikro & Realitas Lapangan)*: Permasalahan konkret di lokus riset dan kelemahan prosedur manual konvensional.
  3. *Paragraf 3 (Transisi Paradigma Komputasi)*: Rasionalitas pemilihan pendekatan AI/komputasi terhadap sifat data.
  4. *Paragraf 4 (Sintesis 3-5 Paper Terdahulu & Research Gap)*: Rangkuman 3 sampai 5 paper primer dengan angka metrik akurasi nyata dan perumusan celah riset.
  5. *Paragraf 5 (Solusi Usulan & Dampak Konkret)*: Penegasan metode usulan dan implementasi antarmuka sistem.

### 2. Standar Judul Sub-Bab 1-2 Kata & Paragraph Style Bab 2 (Tinjauan Pustaka)
- **Judul Sub-Bab Bab 2 Wajib 1 Sampai 2 Kata Benda Entitas Murni**:
  - Dilarang judul panjang AI slop (*"Tinjauan Teoretis Komprehensif Mengenai..."*).
  - Contoh baku: `2.1 Tanaman Selada`, `2.2 Citra Digital`, `2.3 Deep Learning`, `2.5 MobileNetV2`, `2.6 Python`, `2.7 Evaluasi Model`, `2.8 Penelitian Terdahulu`.
  - Istilah bahasa Inggris pada judul wajib dicetak **Tebal Miring (*Bold Italic*)**.
- **Hanging Indent 36.0 pt (1,27 cm)**:
  - Nomor sub-bab (`2.1`) di margin kiri `x = 113.4 pt`.
  - Teks judul dimulai di `x = 149.4 pt`, sejajar tegak lurus dengan huruf pertama baris ke-1 paragraf narasi di bawahnya.
- **Formula 4-Kalimat Paragraf Sintesis Teori**:
  - Kalimat 1: Definisi fungsional langsung (nama sub-bab menjadi subjek).
  - Kalimat 2: Mekanisme operasional matematis/transformasi internal.
  - Kalimat 3: Karakteristik kritis dan batasan baseline terhadap data lapangan.
  - Kalimat 4: Jangkar relevansi terhadap pipeline Bab 3.

### 3. Korespondensi 1:1 Rumusan Masalah & Tujuan Penelitian
  - Setiap butir pertanyaan penelitian pada Rumusan Masalah wajib memiliki butir pasangan operasional pada Tujuan Penelitian yang menjawabnya secara presisi dan terukur.
  - Jika Rumusan Masalah memiliki $N$ butir, Tujuan Penelitian wajib memiliki $N$ butir dengan topik yang identik:
    1. RQ Rancang Bangun & Integrasi $\leftrightarrow$ Tujuan Pengembangan Pipeline/Model.
    2. RQ Evaluasi Kinerja Kuantitatif $\leftrightarrow$ Tujuan Pengukuran Metrik Verifikasi & Transkripsi Teks.
    3. RQ Efisiensi Sumber Daya $\leftrightarrow$ Tujuan Analisis Latensi & Konsumsi Memori GPU VRAM.
    4. RQ Keabsahan Statistik $\leftrightarrow$ Tujuan Pengujian Signifikansi Statistik (Uji McNemar $\alpha = 0,05$).
- **Pencegahan Kebocoran Metodologi Mikro (Methodology Leakage Guard)**:
  - Dilarang memasukkan rincian parameter mikro implementasi (seperti nilai ambang IoA, persentase margin ekspansi crop, batas kemiripan Levenshtein, batas langkah ReAct, atau nama spesifik micro-tools) ke dalam butir pertanyaan Rumusan Masalah Bab 1.2.
  - Memasukkan parameter mikro implementasi ke rumusan masalah mengaburkan fokus saintifik utama dan melanggar prinsip ekonomi tanda kurung (parenthesis economy).
  - Tempatkan parameter teknis mikro secara ketat di Sub-bab 1.3 (Ruang Lingkup) dan Bab 3 (Metodologi Penelitian), sementara Rumusan Masalah dan Tujuan Penelitian tetap pada tingkat konseptual-operasional yang terukur dengan korespondensi 1:1.
- **Sinkronisasi Multi-Format Paralel (Multi-Format Invariant)**:
  - Pada proyek yang memelihara beberapa format naskah sekaligus (`.md`, `.typ`, `.docx`, `.pdf`), setiap pembaruan redaksional Rumusan Masalah, Ruang Lingkup, dan Tujuan Penelitian wajib diaplikasikan serentak ke seluruh berkas pendamping.
  - Jangan biarkan salah satu format naskah tertinggal atau memiliki redaksi berbeda.
  - Segera verifikasi kompilasi ulang format berbasis kode (contoh: `typst compile path/to/bab1.typ path/to/bab1.pdf`) guna menjamin keabsahan sintaks dan tata letak dokumen.
- **Sistematika Baku Bab 1 (Format Gunadarma)**:
  - `1.1. Latar Belakang`: Urgensi industri/hukum, kelemahan metode eksisting, tantangan fisik, usulan solusi dual-paradigma, dan ringkasan tujuan.
  - `1.2. Rumusan Masalah`: Rincian $N$ butir pertanyaan penelitian operasional.
  - `1.3. Ruang Lingkup`: 8 batasan operasional natural (objek, dataset & split, atribut, pipeline 1, pipeline 2, lingkungan komputasi, parameter evaluasi, batasan luar).
  - `1.4. Tujuan Penelitian`: Rincian $N$ butir tujuan operasional yang menjawab Rumusan Masalah.
  - `1.5. Sistematika Penulisan`: Penjabaran keterkaitan logis Bab 1 hingga Bab 5; wajib konsisten menyebutkan jumlah pertanyaan dan tujuan penelitian.
- **Kepatuhan Tipografi Ketat**:
  - 0 toleransi karakter Unicode em-dash maupun en-dash (U+2014 / U+2013). Gunakan tanda hubung strip biasa ASCII `-`, titik dua `:`, atau koma `,`.
- **Pitfall Pengeditan Dokumen Naskah**:
  - Gunakan `patch` untuk mengedit naskah besar, bukan `write_file`. Operasi `write_file` ditolak oleh sistem proteksi jika berkas sebelumnya dibaca secara terpaginasi (`read_file` dengan offset/limit).

## O (Output Format)
- Dokumen Bab 1 s.d. Bab 5 tervalidasi dengan struktur numerik Arab teratur.
- Draf bimbingan (`DRAFT_KASAR.md`) dan naskah formal (`.md`, `.typ`, `.pdf`) yang 100% konsisten.
