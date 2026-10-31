---
name: spesialis-research-akademik-rules
description: "Rules for Gunadarma academic thesis and research writing."
---

# Aturan Baku Penulisan Skripsi Gunadarma & Anti-AI-Slop

## 1. Keterlacakan Bisnis Rumusan Masalah
Rumusan masalah dalam penelitian sistem informasi / komputasi terapan DILARANG KERAS berupa formulasi teknis kering tanpa jiwa bisnis (seperti hanya menanyakan cara perakitan model atau sekadar membeberkan deretan nama metrik ML tanpa arah). Rumusan masalah WAJIB mengakar langsung pada pemecahan masalah riil lapangan dari latar belakang:
1. Solusi otomasi terhadap kelemahan kurasi manual dan penegakan kepatuhan regulasi hukum (misal UU Perlindungan Konsumen No. 8/1999).
2. Efektivitas deteksi diskrepansi dan transkripsi fisik bebas bocor untuk memitigasi risiko bisnis konkret (pricing error, laju retur produk, pembatalan pesanan).
3. Kelayakan operasional bisnis ditinjau dari kompromi (trade-off) kecepatan pemrosesan (throughput) dan efisiensi konsumsi sumber daya komputasi (alokasi memori GPU VRAM / OPEX server).
4. Pengujian signifikansi statistik inferensial non-parametrik (Uji McNemar / Wilcoxon p < 0.05) sebagai dasar justifikasi ilmiah dalam pengambilan keputusan investasi arsitektur sistem informasi bagi industri/lokapasar.

## 2. Larangan Format Buatan Sendiri (Anti-Ad-Hoc Structure)
DILARANG KERAS menciptakan sub-bab artifisial buatan sendiri di luar sistematika resmi Gunadarma (seperti 1.0 Penegasan Objek, 2.0 Landasan Penegasan, atau Pilar Masalah). Objek material dan objek formal penelitian wajib dilebur secara terintegrasi dan alami di dalam paragraf Latar Belakang Masalah (LBM).
DILARANG membubuhkan label tebal kaku buatan sendiri di depan butir pertanyaan seperti **RQ1 (Rancang Bangun)**:. Gunakan langsung nomor urut resmi 1. Bagaimana... dan gunakan kata tanya operasional (Bagaimana..., Sejauh mana...), DILARANG menggunakan kata tanya biner tertutup (Apakah...).

## 3. Disiplin Sitasi Dalam Teks (First-Mention Rule & Anti-Et-Al)
1. Aturan Penyebutan Pertama (First-Mention): Untuk karya ilmiah dengan 3 hingga 5 penulis, pada pemunculan pertama dalam teks WAJIB menyebutkan seluruh nama belakang penulis secara lengkap dihubungkan dengan kata 'dan' (contoh: Ramadhani, Dewanta, dan Gunawan, 2026). Dilarang langsung memotong menjadi singkatan pada pemunculan pertama. Baru pada penyebutan kedua dan seterusnya disingkat menjadi 'dkk.' (contoh: Ramadhani dkk., 2026).
2. Standarisasi Bahasa Indonesia Baku: Pada naskah berbahasa Indonesia, WAJIB menggunakan singkatan 'dkk.' (huruf kecil semua dan diakhiri tanda titik tunggal) serta kata hubung 'dan' (bukan ampersand '&' di teks naratif). Penggunaan istilah 'et al.' hanya diizinkan untuk naskah bertaraf internasional berbahasa Inggris penuh.
3. Dua Penulis: Selalu sebutkan kedua nama belakang pada setiap pemunculan (contoh: Han dan Yi, 2025).

## 4. Eliminasi Terjemahan Harfiah Kaku & AI Slop Konseptual
1. Tolak terjemahan harfiah robotik yang tidak lazim di komunitas akademik informatika/komputer (contoh buruk: 'Deteksi Objek Pembelajaran Mendalam' untuk Deep Learning Object Detection). Gunakan istilah baku yang alami seperti 'Deteksi Objek Berbasis Deep Learning' atau pertahankan istilah asing cetak miring.
2. Tolak kalimat berbunga-bunga abstrak (seperti 'mentransformasi analisis dari manual menuju representasi otomatis berlapis'). Gunakan definisi operasional konkret: masukan citra, proses ekstraksi fitur matematis, dan format luaran parametrik (bounding box koordinat pusat $[x_c, y_c, w, h]$ atau batas sudut $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$ beserta skor keyakinan).
3. Sertakan justifikasi kegagalan metode baseline di lapangan (misal mengapa klasifikasi citra tunggal gagal membedakan multi-tandan buah pada konveyor pabrik sehingga mutlak memerlukan deteksi objek per tandan).
