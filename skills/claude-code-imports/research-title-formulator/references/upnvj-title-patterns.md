# ANATOMI & POLA SINTAKSIS JUDUL SKRIPSI KORPUS UPNVJ (213 SKRIPSI)
> Analisis empiris struktur judul, kelemahan umum, dan pola formula terbaik dari korpus teks skripsi Fakultas Ilmu Komputer UPN Veteran Jakarta.

---

## 1. Tiga Arketipe Pola Judul Utama

Berdasarkan ekstraksi dan analisis terhadap 213 skripsi mahasiswa Informatika dan Sistem Informasi, terdapat 3 pola dominan:

### Arketipe A: Track Data Science, Machine Learning & AI (42% Korpus)
- **Struktur Baku**:
  `[Tugas Komputasi] + [Objek Data] + MENGGUNAKAN [Algoritma/Model] + DENGAN [Arsitektur/Optimasi] + [Konteks]`
- **Contoh Riil Korpus**:
  1. *DETEKSI CITRA DIGITAL PENYAKIT CACAR MONYET MENGGUNAKAN ALGORITMA CONVOLUTIONAL NEURAL NETWORK DENGAN ARSITEKTUR MOBILENETV2*
  2. *ANALISIS SENTIMEN ULASAN APLIKASI AIRBNB PADA GOOGLE PLAY STORE DENGAN MENGGUNAKAN METODE SUPPORT VECTOR MACHINE (SVM)*
  3. *ANALISIS KLASIFIKASI SENTIMEN PENGGUNA APLIKASI PEDULINDUNGI BERDASARKAN ULASAN DENGAN MENGGUNAKAN METODE LONG SHORT TERM MEMORY*
  4. *ANALISIS DATA ULASAN PENGGUNA TERHADAP FITUR UTAMA APLIKASI MOBILE BANKING BANK XYZ MENGGUNAKAN ALGORITMA NAIVE BAYES*
- **Kelemahan Umum**: Sering kali tidak mencantumkan teknik preprocessing/optimasi dan tidak menyebutkan target metrik yang ingin ditingkatkan.

### Arketipe B: Track Rekayasa Perangkat Lunak, Web & Mobile (35% Korpus)
- **Struktur Baku**:
  `[PENGEMBANGAN / RANCANG BANGUN / PERANCANGAN] + [Tipe Sistem] + BERBASIS [Teknologi/Platform] + MENGGUNAKAN [Metode/Framework] + (STUDI KASUS: [Mitra])`
- **Contoh Riil Korpus**:
  1. *APLIKASI PEMESANAN MENU BERBASIS QR CODE MENGGUNAKAN FRAMEWORK LARAVEL (STUDI KASUS: AYAM MRINGIS)*
  2. *PENGEMBANGAN SISTEM MONITORING PRESENSI OUTSOURCING BERBASIS WEB MENGGUNAKAN METODE AGILE*
  3. *RANCANG BANGUN SISTEM INFORMASI KASIR DAN MANAJEMEN INVENTARIS TOKO KELONTONG BERBASIS CLOUD*
- **Kelemahan Umum**: Sering terjebak menjadi proyek "Software House biasa" tanpa kontribusi ilmiah jika tidak memiliki algoritma pendukung (seperti RAG, rekomendasi, atau optimasi antrean).

### Arketipe C: Track Tata Kelola TI, Audit Keamanan & UI/UX (23% Korpus)
- **Struktur Baku**:
  `[ANALISIS / EVALUASI / REDESIGN] + [Aspek Pengujian] + [Objek Sistem/Institusi] + MENGGUNAKAN METODE/STANDAR [Framework]`
- **Contoh Riil Korpus**:
  1. *ANALISIS TATA KELOLA SISTEM INFORMASI RUMAH SAKIT UMUM BHAKTI ASIH MENGGUNAKAN COBIT 2019*
  2. *EVALUASI PENERAPAN KEAMANAN INFORMASI BERDASARKAN ISO/IEC 27001 PADA RUMAH DATAKU PUSDATIN BKKBN*
  3. *ANALISIS USER EXPERIENCE DAN REDESIGN WEBSITE PT ADIRA DINAMIKA MULTIFINANCE DENGAN MENGGUNAKAN METODE USER CENTERED DESIGN*
  4. *ANALISIS UI/UX WEBSITE ROTTE BAKERY MENGGUNAKAN PENDEKATAN USER EXPERIENCE QUESTIONNAIRE (UEQ) DAN REDESIGN MENGGUNAKAN METODE DESIGN THINKING*
- **Kelemahan Umum**: Terlalu deskriptif jika hanya berhenti pada penyebaran kuesioner tanpa menghasilkan prototype teruji atau rekomendasi teknis berbasis bukti.

---

## 2. Tiga Jebakan Judul Skripsi (The Deadly Traps)

1. **Jebakan Alat-First (Tool-Centric Trap)**:
   - Judul hanya menonjolkan tools/framework (misal: "Membuat Web X dengan Laravel dan Bootstrap").
   - *Koreksi*: Framework hanyalah alat implementasi. Fokus judul harus pada masalah rekayasa dan metode penyelesaiannya.
2. **Jebakan Algoritma Tanpa Justifikasi (Algorithm Hopping)**:
   - Memilih algoritma populer (misal: SVM / Random Forest / LSTM) hanya karena sering dipakai orang lain, tanpa ada bukti data awal bahwa data memiliki karakteristik khusus (seperti non-linearitas atau ketergantungan sekuensial waktu).
3. **Jebakan Judul Terlalu Panjang (>20 Kata)**:
   - Menumpuk semua kata kunci hingga judul mencapai 30 kata.
   - *Koreksi*: Gunakan formula padat 12 sampai 18 kata yang mencakup Metode Utama, Preprocessing/Optimasi, Objek, dan Target.
