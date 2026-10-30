# Cetak Biru Hierarki Section Prompts untuk Penulisan Skripsi dan Manuskrip Akademik
> Panduan Standar Operasional Injeksi Konteks Bertingkat (Cascading Context Tree) Bab 1 sampai Bab 5 Berdasarkan Pola Hierarkis Jenni AI Editor dan Standar Akademik Indonesia.

---

## 1. Landasan Arsitektur: Pohon Konteks Bertingkat (Cascading Context Tree)

Dalam editor akademik modern seperti Jenni AI, kegagalan umum model kecerdasan buatan (halusinasi, loncatan topik, pengulangan definisi dasar, atau keluaran di luar ruang lingkup) disebabkan oleh ketiadaan batasan konteks lokal. Model hanya membaca instruksi global yang terlalu luas.

Pola *Hierarchical Section Prompts* memecah naskah menjadi pohon konteks tiga lapis yang diinjeksikan secara deterministik saat perakitan draf:

```text
Lapis 1: Global Document Prompt (Judul, Sasaran Utama, Pedoman Kampus, Target Jurnal)
  │
  └── Lapis 2: Chapter Heading Prompt (Fokus Bab: Teori / Metodologi / Hasil)
        │
        └── Lapis 3: Sub-Section Prompt (Tujuan Spesifik, Batasan Negatif, Data Wajib, Struktur SPOK)
              │
              └── Titik Penulisan Aktif (Paragraf Deduktif + Sitasi Valid)
```

### Prinsip Operasional:
1. **Pewarisan Konteks Turunan**: Sub-bab anak (H2 atau H3) otomatis mewarisi batasan bab induk (H1), namun memiliki batasan negatif (*Negative Constraints*) yang lebih ketat.
2. **Karantina Ruang Lingkup**: Sub-bab tertentu (seperti 1.2 Ruang Lingkup) dilarang membahas teori umum yang merupakan hak eksklusif Bab 2.
3. **Ekonomi Tanda Kurung dan Gaya Bahasa**: Setiap sub-bab mematuhi aturan maksimal 10 pasang tanda kurung per 1.000 kata, bebas tanda pisah em-dash atau en-dash, dan menggunakan kalimat aktif SPOK.

---

## 2. Format Baku Kontrak Section Prompt

Setiap rancangan sub-bab wajib mematuhi skema konfigurasi berikut sebelum penulisan dimulai:

```yaml
section_id: "string_identifier_unik"
parent_section: "induk_bab"
title: "Nomor dan Judul Resmi Sub-Bab"
objective: "Tujuan inti yang harus terjawab dalam sub-bab ini"
required_inputs:
  - "Data empiris, tabel, metrik, atau referensi primer yang wajib hadir"
negative_constraints:
  - "Hal yang secara eksplisit DILARANG ditulis dalam sub-bab ini"
paragraph_count: "Jumlah paragraf terencana (misal: 3-5 paragraf)"
paragraph_structure:
  - p1: "Fokus kalimat utama paragraf 1"
  - p2: "Fokus kalimat utama paragraf 2"
citation_rules: "Aturan sitasi primer (misal: jurnal 5 tahun terakhir, format APA 7th)"
```

---

## 3. Cetak Biru Section Prompts: Bab 1 Pendahuluan

### 1.1 Latar Belakang Penelitian
- **Tujuan**: Menjelaskan fenomena empiris lapangan, kesenjangan antara kondisi ideal dan realitas, serta urgensi solusi yang diusulkan.
- **Bahan Bukti Wajib**: Data kuantitatif permasalahan (statistik industri/katalog/data historis), 3 sampai 5 rujukan mutakhir mengenai keterbatasan pendekatan sebelumnya.
- **Larangan Konten (Negative Constraints)**:
  - Dilarang membuka dengan kalimat klise: "Seiring dengan perkembangan teknologi...", "Di era globalisasi...", atau "Kecerdasan buatan berkembang sangat pesat".
  - Dilarang menyajikan penurunan rumus matematis panjang (tempatkan di Bab 2 atau Bab 3).
  - Dilarang menggunakan tanda pisah em-dash atau en-dash.
- **Struktur Paragraf Deduktif (5 Paragraf Standar)**:
  - Paragraf 1: Fenomena makro dan pentingnya domain penelitian secara objektif.
  - Paragraf 2: Fakta permasalahan spesifik di lapangan beserta data kerugian atau inefisiensi nyata.
  - Paragraf 3: Tinjauan ringkas upaya penelitian terdahulu dan identifikasi kelemahan baseline tersebut.
  - Paragraf 4: Solusi yang diajukan beserta rasionalisasi ilmiah mengapa pendekatan ini dipilih.
  - Paragraf 5: Ringkasan kontribusi utama dan penegasan tujuan penulisan skripsi.

### 1.2 Ruang Lingkup Penelitian (Standar 8-Poin Natural)
- **Tujuan**: Membatasi batas operasional penelitian secara tegas agar tidak melebar.
- **Bahan Bukti Wajib**: Spesifikasi objek, parameter input, model komparasi, dan perangkat keras/lunak.
- **Larangan Konten (Negative Constraints)**:
  - DILARANG menggunakan format key-value tebal kaku seperti `**Objek**: ...`. Wajib kalimat bernomor alami.
  - Dilarang memasukkan atribut dinamis per-batch pengiriman (seperti tanggal kedaluwarsa pada katalog e-commerce) jika objek berfokus pada atribut fisik permanen.
- **Struktur 8-Poin Natural**:
  1. Objek spesifik data yang diteliti.
  2. Sumber dan metode akuisisi dataset.
  3. Format dan resolusi data masukan.
  4. Ruang lingkup atribut atau label yang diproses.
  5. Metode atau arsitektur utama yang dibangun.
  6. Model pembanding atau baseline yang digunakan.
  7. Lingkungan komputasi dan spesifikasi infrastruktur pengujian.
  8. Metrik evaluasi dan tolok ukur pengujian performa.

### 1.3 Rumusan Masalah
- **Tujuan**: Merumuskan pertanyaan penelitian spesifik, terukur, dan berbasis kesenjangan ilmiah.
- **Bahan Bukti Wajib**: Keterkaitan langsung dengan kelemahan baseline pada 1.1.
- **Struktur**: Disusun dalam kalimat tanya formal yang diawali kata tanya terarah (misalnya: "Bagaimana performa...", "Sejauh mana pengaruh...").

### 1.4 Tujuan Penelitian
- **Tujuan**: Menjawab secara presisi pertanyaan pada Rumusan Masalah 1.3.
- **Ketentuan Mutlak**: Wajib berkorespondensi satu banding satu dengan Rumusan Masalah 1.3 dan Kesimpulan 5.1.

### 1.5 Manfaat Penelitian
- **Tujuan**: Menguraikan kontribusi teoritis (akademis) dan kontribusi praktis (lapangan/industri).
- **Struktur**: Dibagi menjadi dua aspek tegas: Manfaat Teoritis dan Manfaat Praktis.

---

## 4. Cetak Biru Section Prompts: Bab 2 Tinjauan Pustaka dan SOTA

### 2.1 Landasan Teori Domain dan Dasar Matematika
- **Tujuan**: Memaparkan konsep fundamental yang mendasari sistem tanpa terjebak menjadi kliping definisi.
- **Bahan Bukti Wajib**: Formulasi matematis resmi, fungsi objektif, fungsi aktivasi, atau persamaan optimasi.
- **Larangan Konten (Negative Constraints)**:
  - Dilarang menyalin teks definisi umum kamus tanpa penjelasan fungsi dalam sistem.
  - Dilarang menaruh kutipan sekunder jika dokumen primernya dapat diakses.

### 2.2 Model Komparasi dan Algoritma Baseline
- **Tujuan**: Menguraikan arsitektur model pembanding yang akan diuji secara setara (*head-to-head*).
- **Bahan Bukti Wajib**: Diagram alur kerja model, rujukan publikasi pertama perancang algoritma.

### 2.3 Matriks State-of-the-Art (SOTA) dan Analisis Kesenjangan (Research Gap)
- **Tujuan**: Memetakan posisi penelitian terhadap minimal 5 penelitian terdahulu yang relevan dalam 5 tahun terakhir.
- **Bahan Bukti Wajib**: Tabel Matriks SOTA 6-Kolom (Penulis dan Tahun, Tautan Artikel DOI/URL, Latar Belakang Masalah, Hasil Kuantitatif, Kesimpulan, Relevansi Terhadap Penelitian Ini).
- **Alur Kerja Pemetaan Research Gap**:
  1. Identifikasi *Well-Supported Findings* (hal yang sudah mapan dan disepakati peneliti terdahulu).
  2. Identifikasi *Contested Claims* (perdebatan atau hasil kontradiktif antar-peneliti).
  3. Identifikasi *Under-Explored Areas* (aspek yang belum disentuh atau data yang belum dievaluasi).
  4. Penegasan *Research Niche* (posisi penelitian ini dalam mengisi celah kosong tersebut).

---

## 5. Cetak Biru Section Prompts: Bab 3 Metodologi Penelitian

### 3.1 Data Penelitian dan Pemahaman Data (Data Understanding)
- **Tujuan**: Menjelaskan karakteristik dataset secara menyeluruh dan transparan.
- **Bahan Bukti Wajib**: Jumlah total sampel, sebaran kelas, resolusi, kondisi pencahayaan/akustik, dan rasio ketidakseimbangan kelas.
- **Larangan Konten**: Dilarang menyembunyikan adanya anomali atau data rusak. Data anomali wajib dicatat penanganannya.

### 3.2 Siklus Metodologi (CRISP-DM atau SDLC)
- **Tujuan**: Menjabarkan fase-fase eksekusi secara runtut berdiagram alir vektor FigGenie.
- **Bahan Bukti Wajib**: Diagram alur visual penelitian berstandar publikasi (format SVG/tight-box PDF).

### 3.3 Protokol Anti-Data Leakage Mutlak
- **Tujuan**: Membuktikan bahwa eksperimen bebas dari kebocoran data (*data leakage*).
- **Bahan Bukti Wajib**: Penjelasan tegas bahwa pembagian data latih dan uji (*Train/Test Split*) dilakukan sebelum penskalaan (*scaling*), imputasi, atau dekomposisi sinyal (seperti CEEMDAN/Wavelet).

### 3.4 Skenario Pengujian dan Desain Eksperimen
- **Tujuan**: Merinci konfigurasi hiperparameter, optimizer, learning rate, jumlah epoch, dan lingkungan pengujian.
- **Bahan Bukti Wajib**: Tabel spesifikasi perangkat keras (GPU/CPU/RAM) dan versi pustaka perangkat lunak.

---

## 6. Cetak Biru Section Prompts: Bab 4 Hasil dan Pembahasan

### 4.1 Implementasi dan Proses Pelatihan
- **Tujuan**: Menyajikan dinamika proses pelatihan model tanpa fabrikasi data.
- **Bahan Bukti Wajib**: Grafik konvergensi loss dan metrik per-epoch, waktu komputasi, dan penggunaan memori.

### 4.2 Evaluasi Metrik Kuantitatif
- **Tujuan**: Menyajikan hasil pengujian komparatif dalam tabel matriks performa.
- **Bahan Bukti Wajib**: Tabel perbandingan metrik formal (RMSE, MAE, MAPE, R2, MDA, Precision, Recall, Macro-F1, atau mAP).

### 4.3 Uji Signifikansi Statistik Formal (Diebold-Mariano atau Wilcoxon)
- **Tujuan**: Membuktikan secara matematis bahwa keunggulan model yang diusulkan bukan kebetulan semata.
- **Bahan Bukti Wajib**: Nilai statistik hitung, derajat kebebasan, dan nilai signifikansi p-value formal (wajib p < 0.05).
- **Larangan Konten**: Dilarang menyatakan suatu model "lebih unggul secara signifikan" jika tidak disertai uji signifikansi statistik formal.

### 4.4 Pembahasan Korelatif Empiris (Discussion)
- **Tujuan**: Menghubungkan temuan angka kuantitatif dengan fenomena masalah yang diangkat pada Bab 1.
- **Bahan Bukti Wajib**: Analisis kegagalan (*error analysis*) pada sampel yang salah diklasifikasi atau diprediksi meleset.

---

## 7. Cetak Biru Section Prompts: Bab 5 Penutup

### 5.1 Kesimpulan
- **Tujuan**: Menjawab seluruh tujuan penelitian yang tertuang pada Sub-bab 1.3 secara tuntas.
- **Ketentuan Mutlak**:
  - Butir kesimpulan berkorespondensi satu banding satu dengan butir tujuan penelitian.
  - Setiap butir wajib memuat bukti angka metrik nyata yang diperoleh pada Bab 4.
  - Dilarang memuat teori baru atau spekulasi yang tidak dibahas di Bab 4.

### 5.2 Saran
- **Tujuan**: Memberikan rekomendasi teknis yang konkret, terarah, dan dapat ditindaklanjuti oleh peneliti berikutnya.
- **Larangan Konten**: Dilarang memberikan saran umum yang klise (misalnya: "Perlu diteliti lebih lanjut dengan data yang lebih banyak"). Wajib sebutkan arsitektur lanjutan atau teknik spesifik yang disarankan.
