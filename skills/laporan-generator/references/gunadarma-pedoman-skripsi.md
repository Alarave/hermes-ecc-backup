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
- Teori fundamental pendukung sistem, arsitektur deep learning, algoritma pembanding.
- Matriks Komparasi Penelitian Terdahulu (*State-of-the-Art / SOTA Matrix*).
- Kerangka Pemikiran Teoritis (disajikan dalam diagram visual via `figgenie-paper-diagram`).

### 3. METODOLOGI PENELITIAN
- Wajib menyandarkan alur riset pada metodologi baku:
  - Proyek AI/Data Science: **CRISP-DM** (Business Understanding -> Data Understanding -> Data Preparation -> Modeling -> Evaluation -> Deployment).
  - Proyek Rekayasa Perangkat Lunak: **SDLC Waterfall** atau **Agile Scrum**.
- Diagram Alir Penelitian (*Research Flowchart*): Wajib menggunakan diagram vektor presisi tinggi (SVG/PDF via `figgenie-paper-diagram`).
- Metode Pengumpulan Data dan Teknik Pengujian Kinerja.

### 4. HASIL DAN PEMBAHASAN
- **4.1. Implementasi Sistem / Model**:
  - Konfigurasi lingkungan hardware/software, implementasi antarmuka/API, dan proses pelatihan model (epoch, loss curve, alokasi memori).
- **4.2. Pengujian & Evaluasi Kinerja**:
  - Pengujian Fungsional: Tabel *Black-Box Testing* lengkap dengan skenario, input, output harapan, dan hasil aktual.
  - Pengujian Kuantitatif: Metrik evaluasi terukur (RMSE, MAE, MDA, F1-Score, RAGAS) dan uji signifikansi statistik (Diebold-Mariano / Wilcoxon).
- **4.3. Pembahasan Temuan**:
  - Analisis mendalam mengapa model berhasil atau gagal, komparasi terhadap baseline penelitian terdahulu.

### 5. PENUTUP
- **5.1. Kesimpulan**:
  - Poin-poin jawaban langsung yang menjawab 1.3 Tujuan Penelitian secara jujur berdasarkan hasil eksperimen Bab 4.
- **5.2. Saran**:
  - Rekomendasi teknis konkret untuk peneliti selanjutnya (bukan saran klise seperti "perlu ditingkatkan").

---

## 4. Format Penomoran Gambar, Tabel, dan Persamaan

- **Format Relatif Bab**:
  - Gambar: `Gambar [Nomor Bab].[Nomor Urut]` (Contoh: `Gambar 1.1`, `Gambar 3.2`). Judul diletakkan **di bawah gambar**, rata tengah.
  - Tabel: `Tabel [Nomor Bab].[Nomor Urut]` (Contoh: `Tabel 2.1`, `Tabel 4.3`). Judul diletakkan **di atas tabel**, rata tengah.
  - Persamaan Matematika: Nomor diletakkan dalam tanda kurung di margin kanan `(1.1)`, `(3.1)`. Rumus wajib ditulis dengan LaTeX Math.
- **Keterangan Sumber**: Jika gambar atau tabel diambil dari pihak luar, cantumkan sumber di baris berikutnya: `Sumber: [Nama Penulis, Tahun]` dengan font 10 pt.

---

## 5. Standar Penulisan Daftar Pustaka

- Gunakan format standar **IEEE** (numerik berurutan `[1], [2]`) atau **APA 7th Edition** (alfabetis).
- Komposisi rujukan: Minimal **80% bersumber dari artikel jurnal ilmiah / prosiding konferensi bereputasi** dalam 5 tahun terakhir.
- Seluruh sitasi di naskah wajib tercatat di Daftar Pustaka dan sebaliknya.
