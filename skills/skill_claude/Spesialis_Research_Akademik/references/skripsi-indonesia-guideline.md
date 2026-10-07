# Standar Penulisan Skripsi / Jurnal Indonesia (KBBI & EYD V)

Panduan ini disusun berdasarkan analisis korpus teks akademik riil (Skripsi/Tugas Akhir Informatika) untuk memastikan gaya penulisan spesialis riset tidak "ngawang" dan memiliki struktur formal yang persis dengan standar perguruan tinggi Indonesia (seperti UPNVJ / Gunadarma).

## 1. Struktur Dokumen Baku (Wajib)

Setiap penyusunan draf harus mengikuti hierarki baku berikut tanpa modifikasi AI:
- **BAB I PENDAHULUAN**
  - 1.1 Latar Belakang (atau Latar Belakang Masalah)
  - 1.2 Perumusan Masalah
  - 1.3 Tujuan Penelitian
  - 1.4 Manfaat Penelitian
  - 1.5 Batasan Masalah
- **BAB II TINJAUAN PUSTAKA** (atau Landasan Teori)
  - 2.1 Penelitian Terkait (State of the Art)
  - 2.2 Teori-Teori Dasar (Contoh: Konsep LSTM, CNN, NLP, Metrik Evaluasi)
- **BAB III METODOLOGI PENELITIAN**
  - 3.1 Kerangka Pikir / Alur Penelitian (Gambarkan dengan narasi Flowchart)
  - 3.2 Pengumpulan Data (Dataset)
  - 3.3 Praproses Data (Preprocessing)
  - 3.4 Arsitektur Model / Pemodelan
  - 3.5 Skenario Pengujian
- **BAB IV HASIL DAN PEMBAHASAN**
  - 4.1 Deskripsi Data / Analisis Data Awal
  - 4.2 Hasil Praproses Data
  - 4.3 Hasil Pelatihan Model
  - 4.4 Evaluasi dan Pembahasan (Komparasi Akurasi, Analisis Error)
- **BAB V PENUTUP**
  - 5.1 Kesimpulan (Bukan "Kesimpulannya,")
  - 5.2 Saran

## 2. Pemilihan Diksi (KBBI) & Gaya Bahasa

- **Lugas & Objektif**: Gunakan kalimat pasif (di-) dan posisikan penulis sebagai "Peneliti" atau "Penulis" jika terpaksa, BUKAN "Kita" atau "Saya".
  - *Benar*: "Penelitian ini diawali dengan tahap pengumpulan data..."
  - *Salah*: "Pertama-tama, kita akan mengumpulkan data..."
- **Glosarium Istilah Informatika Standar KBBI**:
  - *Preprocessing* -> Praproses / Prapemrosesan
  - *Input/Output* -> Masukan/Keluaran
  - *Feature Extraction* -> Ekstraksi Fitur
  - *Dataset* -> Kumpulan Data / Dataset (Cetak miring jika bahasa asing)
  - *Flowchart* -> Diagram Alir
  - *Machine Learning* -> Pembelajaran Mesin
  - *Deep Learning* -> Pembelajaran Mendalam
- **Anti-Slop AI**:
  - DILARANG menggunakan transisi AI klasik seperti: "Secara keseluruhan", "Penting untuk dicatat bahwa", "Di era digital yang serba cepat ini", "Menyelami lebih dalam".
  - Gunakan transisi akademik murni: "Berdasarkan hasil pengujian pada Tabel 4.1...", "Hal tersebut mengakibatkan...", "Penelitian sebelumnya oleh (Nama, Tahun) menunjukkan bahwa...".

## 3. Format Penulisan Sitasi dan Tabel
- Tabel dan Gambar harus direferensikan di dalam teks sebelum muncul. 
  - *Contoh*: "Pada Tabel 4.1 menjelaskan mengenai rincian data yang telah terambil..."
- Sitasi harus melekat pada klaim yang diutarakan. Gunakan format standar (Penulis, Tahun) jika tidak ada format khusus.


## 4. Struktur Spesifik Domain IT (Studi Kasus UPNVJ/Kampus IT RI)

Berdasarkan analisis korpus ratusan skripsi IT (Sistem Informasi & Informatika), struktur laporan **berubah total** tergantung jenis penelitiannya. Gunakan kerangka ini sesuai *niche* tugas:

### A. Skripsi "Rancang Bangun / Pengembangan Sistem" (Software Engineering)
- **Fokus**: Pembuatan aplikasi nyata (Web/Mobile).
- **BAB III (Metodologi)**: Wajib menggunakan SDLC (contoh: *Agile, Waterfall, RAD, Scrum*). Sub-bab: Analisis Kebutuhan Sistem (Fungsional & Non-Fungsional), Perancangan Sistem (UML: Use Case, Activity, Sequence, Class Diagram), Perancangan Basis Data (ERD), Perancangan Antarmuka (Mockup/UI).
- **BAB IV (Hasil)**: Implementasi Antarmuka (Screenshot layar riil), Implementasi Kode, Pengujian Sistem (Black-box testing / UAT - *User Acceptance Test*).

### B. Skripsi "Sistem Pendukung Keputusan (SPK)"
- **Fokus**: Algoritma seleksi/pemilihan (AHP, SAW, SMART, TOPSIS).
- **BAB III (Metodologi)**: Alur algoritma SPK, penentuan Kriteria (Cost/Benefit) dan Bobot, Perancangan Rumus/Perhitungan manual.
- **BAB IV (Hasil)**: Implementasi perhitungan matematis matriks pada studi kasus nyata (normalisasi, perkalian bobot, hasil perankingan akhir).

### C. Skripsi "Evaluasi Tata Kelola TI / Usability" (COBIT / ITIL / SUS)
- **Fokus**: Audit sistem yang sudah ada.
- **BAB III (Metodologi)**: Tahapan Audit, Pemilihan Domain (Misal: COBIT 5 Domain APO/MEA), Penyusunan Kuesioner, Populasi & Sampel.
- **BAB IV (Hasil)**: Hasil rekap kuesioner, Perhitungan Tingkat Kapabilitas (*Capability Level*) atau Skor SUS (*System Usability Scale*), Analisis Kesenjangan (*Gap Analysis*), Rekomendasi Perbaikan.

## 5. Kaidah Anti-Slop Tingkat Lanjut
DILARANG keras memakai:
- "Makalah ini bertujuan untuk menjelajahi..." -> GANTI JADI: "Penelitian ini bertujuan untuk menganalisis..."
- "Sebagai penutup..." -> GANTI JADI: "Berdasarkan hasil pengujian..."
- "Sangat penting untuk mengoptimalkan..." -> GANTI JADI: "Optimasi diperlukan untuk..."
Kalimat harus dibentuk se-objektif mungkin berbasis data (*data-driven*), menggunakan format "Oleh karena itu," atau "Selain itu," sebagai transisi baku (Sesuai frekuensi tertinggi di korpus UPNVJ).
