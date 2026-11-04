---
name: spesialis-research-akademik-rules
description: "Use when writing or auditing Gunadarma and UPNVJ academic theses. Enforces chapter structures, 1-2 word subheadings, and anti-AI-slop rules."
---

# Aturan Baku Penulisan Skripsi Gunadarma, UPNVJ & Anti-AI-Slop

## 1. Keterlacakan Bisnis & Operasional Rumusan Masalah (Bab 1)
Rumusan masalah dalam penelitian sistem informasi atau komputasi terapan DILARANG KERAS berupa formulasi teknis kering tanpa konteks masalah lapangan. Rumusan masalah WAJIB mengakar langsung pada pemecahan masalah riil dari Latar Belakang Masalah (5-Paragraf Corong Terbalik):
1. Solusi otomasi terhadap kelemahan kurasi/pemeriksaan manual dan penegakan kepatuhan regulasi resmi.
2. Efektivitas deteksi diskrepansi atau klasifikasi fitur bebas bocor untuk memitigasi risiko operasional konkret.
3. Evaluasi performa kuantitatif beserta pengujian signifikansi statistik inferensial (Uji McNemar / Diebold-Mariano / Wilcoxon $p < 0.05$).
4. Integrasi model ke dalam aplikasi/antarmuka operasional (Streamlit/Web/REST API).

## 2. Anatomi 5-Paragraf Latar Belakang Masalah (1.1)
1. **Paragraf 1 (Fenomena Makro & Statistik Lembaga Resmi - Das Sollen)**: Peran faktual objek masalah disertai data kuantitatif resmi (BPS, WHO, Kemenkes, IDF, APJII, BPOM) dan tuntutan standar kualitas.
2. **Paragraf 2 (Realitas Masalah Lapangan & Bottleneck Manual - Das Sein)**: Fakta permasalahan aktual di lokus penelitian, lonjakan kasus/kesalahan, serta keterbatasan prosedur manual yang lambat atau subjektif.
3. **Paragraf 3 (Transisi Paradigma Komputasi & Rasionalitas Algoritma)**: Pengenalan pendekatan pembelajaran mesin/pengolahan citra dan alasan teknis kecocokan metode inti terhadap sifat data pada Paragraf 2.
4. **Paragraf 4 (Sintesis Komparatif 3-5 Studi Terdahulu Berangka Metrik & Research Gap)**: Merangkum 3 sampai 5 paper primer secara mengalir dalam satu paragraf padat dengan mencantumkan Penulis (Tahun) lengkap *first-mention*, objek, metode yang diuji, dan angka metrik capaian (akurasi/presisi/mAP), lalu ditutup dengan perumusan tegas *Research Gap*.
5. **Paragraf 5 (Penegasan Solusi Usulan, Integrasi Antarmuka & Dampak)**: Pernyataan metode usulan, platform implementasi, dan kontribusi nyata yang dihasilkan.

## 3. Larangan Format Buatan Sendiri (Anti-Ad-Hoc Structure)
DILARANG KERAS menciptakan sub-bab artifisial buatan sendiri di luar sistematika resmi (seperti `1.0 Penegasan Objek`, `2.0 Landasan Penegasan`, atau `Pilar Masalah`).
DILARANG membubuhkan label tebal kaku buatan sendiri di depan butir pertanyaan atau ruang lingkup seperti `**RQ1 (Rancang Bangun)**:` atau `**Objek Penelitian**:`. Gunakan langsung nomor urut resmi (`1. Bagaimana...`) dan gunakan kata tanya operasional (*Bagaimana...*, *Sejauh mana...*), DILARANG menggunakan kata tanya biner tertutup (*Apakah...*).

## 4. Standar Penamaan & Paragraph Style Judul Sub-Bab Bab 2 (Aturan 1 Sampai 2 Kata Anti-Slop)
Berdasarkan audit empiris 3.866 judul sub-bab pada 192 berkas Bab 2 skripsi FIK UPNVJ:
1. **Batas Baku 1 Sampai 2 Kata Entitas Murni**: Judul sub-bab Bab 2 wajib berupa kata benda tunggal atau frasa nomina 1 sampai 2 kata (contoh: `2.1 Tanaman Selada`, `2.2 Citra Digital`, `2.3 *Deep Learning*`, `2.5 MobileNetV2`, `2.6 Python`, `2.7 Evaluasi Model`, `2.8 Penelitian Terdahulu`). Maksimal 3 kata hanya untuk nama algoritma baku yang tidak dapat dipenggal (`2.4 *Convolutional Neural Network*`).
2. **Larangan Menggabungkan Dua Topik (`dan` / `&` / `/`)**: DILARANG menulis judul gabungan seperti `2.3 Arsitektur Model dan Fungsi Objektif` atau `2.2 Representasi Sinyal dan Prapemrosesan Data`. Pecah menjadi sub-bab masing-masing 1-2 kata.
3. **Larangan Preposisi & Kata Sifat Hiperbolis**: Dilarang menggunakan awalan *Mengenai, Tentang, Pemanfaatan, Tinjauan, Konsep, Landasan, Analisis* dan kata sifat *Komprehensif, Krusial, Esensial*.
4. **Telemetri Paragraph Style Fisik PDF**:
   - **Heading 2 (`2.1`, `2.2`)**: `Times New Roman 12 pt Bold` (*Bold Italic* untuk istilah bahasa Inggris). Menggunakan *Hanging Indent* 36.0 pt (1,27 cm): nomor sub-bab di margin kiri `x = 113.4 pt`, teks judul dimulai di `x = 149.4 pt` (sejajar vertikal sempurna dengan huruf pertama baris ke-1 paragraf narasi di bawahnya).
   - **Heading 3 (`2.4.1`, `2.4.2`)**: `Times New Roman 12 pt Bold` (*Bold Italic* untuk istilah asing: **2.4.1 *Convolutional Layer***, **2.4.2 *Pooling Layer***, **2.4.3 *Softmax***). Nomor dimulai di `x = 149.4 pt` (`leftIndent = 36.0 pt`), teks judul dimulai di `x = 185.4 pt` (`tabStop = 72.0 pt`).
5. **Pola 4-Kalimat Paragraf Sintesis Teori**: Kata pada judul sub-bab langsung menjadi subjek kalimat pertama (definisi fungsional + sitasi primer), diikuti kalimat mekanisme matematis, kalimat karakteristik kritis/batasan baseline, dan kalimat jangkar relevansi terhadap desain sistem di Bab 3.

## 5. Disiplin Sitasi Dalam Teks (First-Mention Rule & Anti-Et-Al)
1. **Aturan Penyebutan Pertama (First-Mention)**: Untuk karya ilmiah dengan 3 hingga 5 penulis, pada pemunculan pertama dalam teks WAJIB menyebutkan seluruh nama belakang penulis secara lengkap dihubungkan dengan kata `dan` (contoh: `Ramadhani, Dewanta, dan Gunawan (2026)`). Baru pada penyebutan kedua dan seterusnya disingkat menjadi `dkk.` (`Ramadhani dkk. (2026)`).
2. **Standarisasi Bahasa Indonesia Baku**: Pada naskah berbahasa Indonesia, WAJIB menggunakan singkatan `dkk.` serta kata hubung `dan` (bukan `&` atau `et al.`).
3. **Dua Penulis**: Selalu sebutkan kedua nama belakang pada setiap pemunculan (contoh: `Han dan Yi (2025)`).

## 6. Eliminasi Terjemahan Harfiah Kaku & AI Slop Konseptual
1. Tolak terjemahan harfiah robotik (contoh buruk: `Deteksi Objek Pembelajaran Mendalam`). Gunakan istilah baku yang alami seperti `Deteksi Objek Berbasis Deep Learning` atau pertahankan istilah asing cetak miring.
2. Tolak kalimat berbunga-bunga abstrak dan kata sambung `di mana / yang mana` non-spasial. Gunakan definisi operasional konkret: masukan citra/data, proses matematis, dan format luaran parametrik.
