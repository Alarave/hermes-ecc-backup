# PANDUAN BAKU PENULISAN SKRIPSI / TUGAS AKHIR UNIVERSITAS GUNADARMA
> Standar resmi penyusunan dokumen akademik Tugas Akhir / Skripsi Universitas Gunadarma (Fakultas Ilmu Komputer dan Teknologi Informasi / FTI).

---

## 1. Aturan Format Fisik & Tata Letak Halaman (Margin 4-4-3-3)

- **Ukuran Kertas**: A4 (210 x 297 mm), 80 gram, warna putih.
- **Batas Tepi (Margins)**:
  - Tepi Atas (*Top*): **4 cm**
  - Tepi Kiri (*Left*): **4 cm**
  - Tepi Bawah (*Bottom*): **3 cm**
  - Tepi Kanan (*Right*): **3 cm**
- **Tipografi & Spasi**:
  - Jenis Huruf: **Times New Roman**
  - Ukuran Teks Utama: **12 pt**
  - Spasi Antar-baris: **1.5 spasi**
  - Indentasi Paragraf Baru: **1 cm** (atau 5-7 ketukan karakter) dari margin kiri.
  - Perataan Teks: Rata Kiri-Kanan (*Justify*).
  - Judul Bab: Huruf kapital, tebal (*Bold*), ukuran 14 pt, rata tengah.
  - Sub-bab: Huruf tebal (*Bold*), ukuran 12 pt, rata kiri.

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
  - Struktur piramida terbalik: Isu makro global -> Masalah teknis spesifik -> Dampak jika tidak diselesaikan -> Usulan solusi sistem/algoritma beserta keunggulannya.
- **1.2. Ruang Lingkup**:
  - Wajib menggunakan istilah **"Ruang Lingkup"** (Dilarang menggunakan "Batasan Masalah").
  - Disajikan dalam bentuk daftar angka tegas (8 poin spesifik: objek riset, dataset, parameter masukan, alur algoritma, model/arsitektur, batasan fitur, batasan metrik pengujian, dan pernyataan non-scope).
- **1.3. Tujuan Penelitian**:
  - Pernyataan aktif terukur (misal: "Membangun sistem...", "Menganalisis performa algoritma...").
- **1.4. Sistematika Penulisan**:
  - Narasi mengalir dalam 5 paragraf yang merangkum isi Bab 1 hingga Bab 5 secara kronologis.

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
  - Nomor Tabel: `Tabel [Nomor Bab].[Nomor Urut]` (Contoh: `Tabel 4.1`). Judul diletakkan **di atas tabel**, ukuran 11 pt, rata tengah.
  - Desain Tabel: Format terbuka (*Open Table Style* / Tiga garis horizontal: garis atas, garis bawah kepala kolom, dan garis penutup bawah; tanpa garis vertikal).
  - Keterangan Sumber: Diletakkan di bawah tabel, font 10 pt.
- **Format Persamaan**:
  - Ditulis rata kiri atau tengah dengan penomoran rata kanan dalam kurung:
    $$RMSE = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2} \tag{3.1}$$

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

Setiap penyusunan skripsi menghasilkan bundel artefak fisik terstruktur di folder `artifacts/skripsi_gunadarma/`:
1. `naskah_skripsi_gunadarma.pdf`: Dokumen lengkap A4 dengan margin 4-4-3-3 dan Dual Pagination sempurna.
2. `naskah_skripsi_gunadarma.docx`: Berkas Word hasil kompilasi Pandoc dengan sitasi otomatis BibTeX.
3. `slide_sidang_skripsi.pptx`: Slide presentasi sidang sarjana berisi diagram vektor native dari FigGenie.
4. `figures/`: Kumpulan berkas sumber diagram vektor `.svg` dan rumus `.tex`.
5. `reproducible_code/`: Skrip implementasi dan evaluasi model yang dapat diuji ulang secara mandiri.
