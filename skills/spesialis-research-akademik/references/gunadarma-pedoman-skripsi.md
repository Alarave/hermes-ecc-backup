# PANDUAN BAKU PENULISAN SKRIPSI / TUGAS AKHIR UNIVERSITAS GUNADARMA
> Standar resmi penyusunan dokumen akademik Tugas Akhir / Skripsi Universitas Gunadarma (Fakultas Ilmu Komputer dan Teknologi Informasi / FTI).

---

## 1. Aturan Format Fisik & Tata Letak Halaman (Margin 4-4-3-3)

- **Ukuran Kertas**: A4 (210 x 297 mm), 80 gram putih (dimensi presisi: 595.32 pt x 841.92 pt).
- **Batas Tepi (Margins Presisi Hasil Verifikasi Dokumen Asli)**:
  - Tepi Atas (*Top*): **4,02 cm** (114.0 pt)
  - Tepi Kiri (*Left*): **4,00 cm** (113.4 pt)
  - Tepi Bawah (*Bottom*): **3,00 cm** (85.0 pt)
  - Tepi Kanan (*Right*): **2,90 s/d 3,00 cm** (82.0 s/d 85.0 pt)
  - Lebar Bidang Teks Efektif: **14,1 cm** (399.8 pt, rentang x = 113.4 pt s/d x = 513.2 pt).
- **Tipografi & Spasi**:
  - Jenis Huruf: **Times New Roman** monolitik (didukung Cambria Math untuk rumus). Dilarang mencampur font sans-serif lain di tengah teks.
  - Ukuran Teks Utama: **12 pt**
  - Spasi Antar-baris: **1.5 spasi** (jarak vertikal dy = 20.7 pt pada font 12 pt).
  - Indentasi Paragraf Baru: **36.0 pt (0,5 inci / 1,27 cm)** dari margin kiri (baris pertama mulai di x = 149.4 pt, baris berikutnya kembali ke x = 113.4 pt).
  - Jarak Antar-Paragraf: space after 8 pt bawaan (dy = 28.7 pt). Dilarang menyisipkan baris kosong ganda (*double enter*).
  - Perataan Teks: Rata Kiri-Kanan (*Justify* penuh).
  - Judul Bab (Heading 1): Huruf kapital, tebal (*Bold*), ukuran 14 pt, rata tengah, dy = 56.2 pt sebelum sub-bab/teks pertama.
  - Sub-bab (Heading 2): Huruf tebal (*Bold*), ukuran 12 pt, rata kiri di x = 113.4 pt, **TANPA titik di akhir nomor** (`1.1 Latar Belakang`, `1.2 Rumusan Masalah`).
  - Sub-Sub-bab (Heading 3): Huruf tebal (*Bold*), ukuran 12 pt, rata kiri di x = 113.4 pt, **TANPA titik di akhir nomor** (`2.2.1 Kelebihan...`).
  - Daftar Butir (*Numbered Lists*): Baris pertama mulai di x = 131.4 pt (indentasi 18.0 pt / 0,25 inci), baris lanjutan di x = 149.4 pt (indentasi 36.0 pt / 0,5 inci).

---

## 2. Aturan Penomoran Halaman (Dual Pagination System)

Gunadarma menerapkan sistem dua jenis penomoran halaman:
1. **Bagian Awal (Front Matter)**:
   - Mencakup: Halaman Judul, Lembar Pengesahan, Surat Pernyataan Keaslian, Abstrak (Bahasa Indonesia & English), Kata Pengantar, Daftar Isi, Daftar Gambar, Daftar Tabel, Daftar Lampiran.
   - Menggunakan **Angka Romawi Kecil** (`i, ii, iii, iv, ...`).
   - Posisi: **Tepat di tengah bawah**, 1.5 cm dari tepi bawah kertas.
   - Halaman judul dihitung sebagai halaman `i` tetapi nomornya tidak dicetak.
2. **Bagian Utama & Akhir (Body & Back Matter)**:
   - Mencakup: Bab 1 sampai Bab 5, Daftar Pustaka, dan Lampiran.
   - Menggunakan **Angka Arab** (`1, 2, 3, 4, ...`).
   - Posisi Standar: **Kanan atas**, 1.5 cm dari tepi atas dan 3 cm dari tepi kanan.
   - **Pengecualian Halaman Bab Baru**: Halaman pertama dari setiap bab baru (halaman yang memuat judul bab) nomor halamannya diletakkan di **tengah bawah**.

---

## 3. Sistematika Penulisan Bab Numerik Arab (Bukan Huruf Romawi)

Universitas Gunadarma menggunakan sistem penomoran bab **Numerik Arab Bergradasi** (DILARANG menggunakan kata "BAB I", melainkan angka "1."):

### 1. PENDAHULUAN
- **1.1. Latar Belakang**:
  - Struktur piramida terbalik: Isu makro regulasi/industri -> Masalah riil lapangan -> Celah riset terdahulu -> Usulan solusi sistem/algoritma.
  - Aturan Hemat Tanda Kurung (Parenthesis Economy): Dilarang menulis terjemahan istilah asing di dalam tanda kurung seperti `penjual pihak ketiga (*third-party sellers*)` atau `pantulan cahaya (*glare*)`. Istilah teknis asing langsung dicetak miring (*italic*) tanpa tanda kurung. Tanda kurung dibatasi hanya untuk singkatan perdana, sitasi tahun, dan pasal perundang-undangan.
- **1.2. Ruang Lingkup**:
  - Wajib menggunakan istilah **"Ruang Lingkup"** (Dilarang menggunakan "Batasan Masalah").
  - Disajikan dalam bentuk butir-butir kalimat bernomor yang mengalir secara wajar dan alami (mencakup 8 aspek pembatasan tanpa format label-key-value kaku seperti `**Objek**: ...`).
- **1.3. Tujuan Penelitian**:
  - Pernyataan aktif terukur (misal: "Membangun sistem...", "Menganalisis performa algoritma...").
- **1.4. Sistematika Penulisan**:
  - Disajikan secara proporsional dalam 5 paragraf terpisah (1 paragraf ringkas per bab) yang menguraikan alur pengerjaan penelitian secara runtut, lugas, dan substantif.
  - DILARANG KERAS menggunakan kata-kata AI slop ("membedah", "saling berkesinambungan", "memetakan 1:1", "secara komprehensif mengintegrasikan"). Gunakan bahasa Indonesia akademik baku dan objektif sesuai bukti korpus skripsi nasional.

### 2. LANDASAN TEORI
- Teori fundamental pendukung sistem, dasar matematika algoritma, arsitektur deep learning, dan konsep rekayasa perangkat lunak.
- **Matriks Komparasi Penelitian Terdahulu (SOTA Matrix)**:
  - Tabel perbandingan minimal 5 penelitian bereputasi (Penulis, Tahun, Metode, Dataset, Kelebihan, dan Keterbatasan).
  - Identifikasi kesenjangan riset (*Research Gap*) yang dijawab oleh skripsi ini.
- **Kerangka Pemikiran Teoritis**:
  - Visualisasi hubungan variabel, input, proses, dan output sistem.
  - WAJIB digambar menggunakan engine vektor `figgenie-paper-diagram` (dilarang menggunakan diagram Mermaid kaku atau screenshot bitmap).

### 3. METODOLOGI PENELITIAN
- Sandaran kerangka kerja baku:
  - Skripsi AI / Data Science / Time-Series: **CRISP-DM** (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment).
  - Skripsi Rekayasa Perangkat Lunak: **SDLC Waterfall** atau **Agile Scrum**.
- **Standar Khusus Penelitian Machine Learning / Time Series (Anti-Leakage Protocol)**:
  - *Train/Test Split*: Pemisahan data latih dan uji WAJIB dilakukan sebelum operasi scaling (*MinMaxScaler*) atau dekomposisi sinyal (CEEMDAN).
  - *Lag Lookback*: Penentuan lag berbasis korelasi nyata (*PACF analysis*).
  - *Clustering IMF*: Pengelompokan frekuensi berbasis Sample Entropy.
- **Standar Khusus Penelitian Generative AI / RAG**:
  - *Hybrid Retrieval*: Penggabungan Dense Vector Embedding (`text-embedding-3`) dan BM25 Sparse via Reciprocal Rank Fusion ($k=60$).
  - *Cross-Encoder Re-Ranking*: Filter akhir konteks untuk menekan halusinasi.
- **Diagram Alir Penelitian**:
  - Visualisasi alur tahapan riset dari awal hingga akhir menggunakan format vektor kamera-siap via `figgenie-paper-diagram`.

### 4. HASIL DAN PEMBAHASAN
- **4.1. Implementasi Sistem & Model**:
  - Konfigurasi lingkungan perangkat keras dan perangkat lunak.
  - Implementasi basis data dan skema relasional/vektor.
  - Dokumentasi proses pelatihan model (epoch, loss curve, alokasi VRAM/RAM).
- **4.2. Pengujian Sistem & Evaluasi Kinerja**:
  - *Pengujian Fungsional (Black-Box Testing)*: Tabel pengujian lengkap mencakup ID Skenario, Deskripsi Kasus, Input, Ekspektasi, Hasil Aktual, dan Kesimpulan (Valid).
  - *Pengujian Keamanan (Security Audit Checklist)*: Audit sanitasi input, autentikasi rute, dan proteksi dari injeksi (Codex Security standard).
  - *Evaluasi Kuantitatif*: Pengukuran performa multivariat:
    - Regresi/Time-Series: RMSE, MAE, MAPE, $R^2$, dan Directional Accuracy (MDA).
    - Klasifikasi: Precision, Recall, Macro-F1, ROC-AUC, dan Confusion Matrix.
    - AI RAG: Evaluasi RAG Triad (Context Relevance, Groundedness, Answer Relevance).
- **4.3. Uji Signifikansi Statistik (Diebold-Mariano / Wilcoxon)**:
  - Untuk membuktikan bahwa model usulan mengungguli baseline secara signifikan (bukan karena faktor kebetulan), wajib menyajikan nilai statistik $DM$ dan *p-value* ($p < 0.05$).
- **4.4. Pembahasan Temuan Ilmiah**:
  - Analisis mendalam mengenai akar penyebab keberhasilan maupun kegagalan model pada kondisi data tertentu.

### 5. PENUTUP
- **5.1. Kesimpulan**:
  - Poin-poin ringkas yang menjawab langsung 1.3 Tujuan Penelitian secara jujur berdasarkan angka nyata dari Bab 4.
- **5.2. Saran**:
  - Saran teknis spesifik dan operasional untuk penelitian lanjutan (bukan saran umum atau klise).

---

## 4. Standar Visualisasi & Gambar Publikasi (`figgenie-paper-diagram`)

Setiap gambar skripsi (Kerangka Pemikiran, Diagram Alir Metodologi, Arsitektur Sistem) WAJIB mematuhi standar:
1. **Format Vektor SVG & PDF**:
   - Dibuat pada resolusi cetak asli (lebar satu kolom 240 pt atau dua kolom 504 pt).
   - Huruf menyatu (*embedded fonts*) dengan tipografi Helvetica / Times New Roman yang selaras dengan naskah.
2. **Formula Matematika Tersemat**:
   - Notasi variabel matematika di dalam kotak diagram dirender menggunakan kurva vektor TeX (MathJax).
3. **Ekspor Slide Sidang Skripsi (`.pptx`)**:
   - Gambar diagram diekspor ke PowerPoint asli dengan *native shapes* dan *live text* agar dapat dipresentasikan secara interaktif saat sidang skripsi di hadapan dewan penguji.
4. **Penomoran Gambar**:
   - Format: `Gambar [Nomor Bab].[Nomor Urut]` (Contoh: `Gambar 2.1`, `Gambar 3.1`). Judul berada **di bawah gambar**, ukuran 11 pt, rata tengah.

---

## 5. Standar Format Tabel dan Persamaan Matematika

- **Format Tabel**:
  - Nomor dan Judul Tabel: `Tabel [Nomor Bab].[Nomor Urut] [Judul Tabel]` (Contoh: `Tabel 2.1 Penelitian Terdahulu`). DILARANG menggunakan titik setelah nomor sub-bab (`Tabel 2.1.` salah). Judul diletakkan **di atas tabel**, ukuran 12 pt Regular, **100% RATA TENGAH (*Center* pada x = 313.3 pt)**.
  - Header Kolom (Baris Pertama): Ukuran 12 pt Bold Rata Tengah, diberi **arsiran warna abu-abu 15%** (`fill=(0.85, 0.85, 0.85)` atau `#D9D9D9`).
  - Desain Garis Tabel: Menggunakan garis kisi penuh (*Box Grid*) dengan garis luar dan pembatas kolom vertikal tipis `0.5 pt` (0.48 pt).
  - Isi Sel Tabel: Ukuran 12 pt untuk tabel konsep/teori; ukuran 9 pt s/d 10 pt untuk tabel data metrik evaluasi besar di Bab 4. Spasi baris dalam sel adalah 1.5 spasi (`dy = 20.7 pt`).
  - Keterangan Sumber / Catatan: Diletakkan di bawah tabel, font 10 pt.
- **Format Gambar**:
  - Posisi Gambar: Diletakkan rata tengah (*center*) pada bidang halaman.
  - Judul / Caption Gambar: `Gambar [Nomor Bab].[Nomor Urut] [Judul Gambar]` diletakkan **di bawah gambar**, ukuran 12 pt Regular, spasi 1.5, **100% RATA TENGAH (*Center*)**.
- **Format Persamaan Matematika**:
  - Ditulis menggunakan font **`Cambria Math`**, posisi formula di tengah (*center*):
    $$RMSE = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2} \tag{3.1}$$
  - Nomor persamaan diletakkan di batas margin kanan dalam tanda kurung: `(3.1)`.
  - Keterangan variabel di bawah formula menjorok di x = 127.6 pt (indentasi ~0,5 cm), font Times New Roman 12 pt Cetak Miring (*Italic*).

---

## 6. Standar Penulisan Daftar Pustaka & Privasi Data

- **Format Sitasi**: Standar **IEEE** (numerik berurutan `[1], [2]`) atau **APA 7th Edition**.
- **Komposisi Literatur**:
  - Minimal **80% bersumber dari artikel jurnal ilmiah bereputasi (Scopus/SINTA) atau prosiding internasional** dalam 5 tahun terakhir.
  - Sumber buku teks maksimal 20% (hanya untuk landasan teori fundamental).
- **Protokol Privasi 8-Class PII (Zero Leakage)**:
  - Dilarang keras mempublikasikan identitas mahasiswa/staf riil, NIK KTP, nomor telepon, alamat email pribadi, atau kredensial database kampus pada naskah dan lampiran skripsi. Semua data sensitif wajib disamarkan menjadi `[REDACTED]`.

---

## 7. Paket Deliverables Skripsi Terpadu (AgentSkillOS Standard)

Setiap penyusunan skripsi menghasilkan bundel artefak fisik terstruktur di folder `docs/` dan folder proyek terkait:
1. **Kompilasi Naskah Ganda (Pandoc & Typst)**:
   - `docs/naskah_skripsi_gunadarma.docx`: Dihasilkan via `pandoc <file>.md -o <file>.docx`.
   - `docs/naskah_skripsi_gunadarma.pdf`: Dihasilkan via `typst compile <template>.typ <output>.pdf` dengan margin baku `top: 4cm, left: 4cm, bottom: 3cm, right: 3cm`, tipografi `Times New Roman 12pt`, spasi 1.5 (`leading: 0.9em`), dan Dual Pagination otomatis (nomor halaman awal bab di tengah bawah, halaman berikutnya di kanan atas).
   - `docs/naskah_skripsi_gunadarma.md` dan `docs/bab*.typ`: Sumber berkas teks mentah.
2. **Standar Kebersihan Struktur Direktori Proyek (Project Hygiene Gate)**:
   - `/docs`: Wadah resmi naskah akademik (PDF, DOCX, Markdown, Typst).
   - `/src`: Kode program utama, notebook preprocessing, dan skrip inferensi/aplikasi.
   - `/dataset`: Wadah citra dan file anotasi master ground truth.
   - `/REFERENSI JURNAL`: Kumpulan berkas PDF rujukan ilmiah dan file indeks matriks SOTA.
   - `/tools/generators`: Tempat isolasi seluruh skrip generator sementara, raw crawl JSON, dan utilitas penunjang. DILARANG KERAS membiarkan skrip generator bekas dan file JSON mentah berserakan di root direktori.
3. **Slide Presentasi Sidang Sarjana**:
   - `docs/slide_sidang_skripsi.pptx`: Slide presentasi sidang sarjana berisi diagram vektor native dari FigGenie.
4. **Kode Pengujian Mandiri**:
   - `src/reproducible_code/`: Skrip implementasi dan evaluasi model yang dapat diuji ulang secara mandiri.
