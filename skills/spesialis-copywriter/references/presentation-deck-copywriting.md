# PANDUAN PENULISAN WARA SLIDE & PRESENTASI (PRESENTATION DECK COPYWRITING)

Dokumen referensi teknis spesialis-copywriter untuk merancang arsitektur narasi, naskah slide (PPTX/Marp), dan skrip pembicara (speaker notes) bagi dua audiens utama: Klien Bisnis/Investor (Pitch Deck) dan Dosen Penguji Sidang (Academic Defense Deck).

---

## 1. Tiga Hukum Emas Penulisan Slide

1. **Judul Slide adalah Klaim, Bukan Topik (Titles are Claims, Not Topics)**:
   - Judul slide wajib menyatakan kesimpulan atau argumen utama dari slide tersebut dalam 1 kalimat lugas.
   - *Buruk (Topik Pasif)*: "Hasil Pengujian Model"
   - *Baik (Klaim Konklusif)*: "Model CEEMDAN-LSTM Memangkas Galat Prediksi RMSE Sebesar 34,2%"
   - *Buruk (Topik Pasif)*: "Fitur Sistem Kasir"
   - *Baik (Klaim Konklusif)*: "Otomasi Kasir Memangkas Waktu Tutup Toko dari 3 Jam Jadi 10 Menit"

2. **Satu Gagasan Pokok per Slide (One Idea per Slide)**:
   - Jika satu slide membutuhkan konjungsi "dan" untuk menggabungkan dua topik besar, pecah slide tersebut menjadi dua slide terpisah.
   - Jangan menjejalkan data finansial dan arsitektur teknis dalam satu kanvas tampilan.

3. **Pemisahan Format: Presented Deck vs Read Deck**:
   - **Presented Deck (Slide Presentasi Langsung)**: Kepadatan teks minimal (< 25 kata per slide), visual/diagram sebagai jangkar perhatian, angka ditulis besar sebagai pahlawan, dilengkapi *Speaker Notes* (skrip lisan).
   - **Read Deck / Leave-Behind (Slide yang Dikirim untuk Dibaca)**: Format mandiri (self-contained), memuat narasi penjelas lengkap, sumber rujukan data, dan lampiran antisipasi sanggahan (*Appendix*).

---

## 2. Playbook Pitch Deck Klien & Investor (Business Pitch Deck)

Mengadopsi alur narasi McKinsey SCR (Situation, Complication, Resolution) dan standar 10-Slide Sequoia/YC:

```text
[1. COVER & HOOK]        ──► Nama produk + One-liner penawaran nilai terjelas
       │
[2. MASALAH NYATA]       ──► Rasa sakit berbiaya tinggi yang dialami pelanggan
       │
[3. AKAR MASALAH]        ──► Mengapa solusi lama gagal & sudut pandang baru (The Reframe)
       │
[4. SOLUSI PRODUK]       ──► Mekanisme unik produk menyelesaikan masalah
       │
[5. FITUR KE MANFAAT]    ──► FAB Matrix: Fitur teknis diterjemahkan jadi efisiensi uang/waktu
       │
[6. BUKTI & TRAKSI]      ──► Angka sebagai pahlawan (omzet, pengguna aktif, retensi, rating)
       │
[7. MODEL BISNIS & ROI]  ──► Skema harga (Rupiah tanpa spasi), proyeksi balik modal klien
       │
[8. KEUNGGULAN UNIK]     ──► Pembeda kompetitif sejati (Unfair Advantage)
       │
[9. TIM EKSEKUTOR]       ──► Pengalaman dan kredensial tim di industri terkait
       │
[10. AJAKAN BERAKSI]     ──► Langkah konkret berikutnya (Uji coba gratis / Komitmen kemitraan)
```

### Template Naskah Slide Klien per Halaman:

- **Slide 1 (Cover)**:
  - *Judul*: Berlayar POS: Sistem Kasir & Manajemen Stok Multi-Cabang Otomatis
  - *Sub-judul*: Membantu pemilik toko retail memantau omzet dan mengamankan stok tanpa ketergantungan internet.
  - *Speaker Notes*: "Selamat pagi rekan-rekan. Hari ini saya akan menunjukkan bagaimana Berlayar POS menghentikan kebocoran stok dan memangkas waktu tutup toko retail hingga 80%."

- **Slide 2 (Masalah Nyata Lapangan)**:
  - *Judul*: Rekap Manual Multi-Cabang Membakar 3 Jam Kerja Setiap Malam
  - *Poin Utama*:
    - Selisih nota kertas dan stok fisik menyebabkan kerugian rata-rata Rp6,7 juta per bulan per 3 cabang.
    - Kasir terhenti total saat internet provider mengalami gangguan di jam ramai pelanggan.
  - *Speaker Notes*: "Masalah terbesar pemilik retail bukan pada mendatangkan pembeli, melainkan kebocoran kas dan stok di meja kasir saat toko sedang ramai."

- **Slide 3 (Solusi & Mekanisme Unik)**:
  - *Judul*: Arsitektur Offline-First Menjamin Transaksi Tetap Berjalan Tanpa Sinyal
  - *Poin Utama*:
    - Penyimpanan lokal instan di perangkat kasir.
    - Sinkronisasi otomatis ke cloud dalam 2 detik saat sinyal kembali terhubung.
  - *Speaker Notes*: "Kami membangun mesin offline-first. Kasir Anda tetap bisa mencetak struk dan memindai barcode walau kabel internet diputus."

- **Slide 4 (Tawaran Investasi / Model Bisnis)**:
  - *Judul*: Berlangganan Fleksibel Mulai Rp149.000 per Bulan Tanpa Biaya Pemasangan
  - *Poin Utama*:
    - Paket Starter: Rp149.000 per bulan per cabang (Maksimal 2 kasir).
    - Paket Pro Multi-Cabang: Rp299.000 per bulan per cabang (Inventaris terpusat).
    - Penghematan operasional terbukti: Klien balik modal dalam 14 hari pertama penggunaan.
  - *Speaker Notes*: "Dengan investasi kurang dari harga 2 cangkir kopi sehari, pemilik toko mengamankan potensi kerugian jutaan Rupiah akibat selisih stok."

---

## 3. Playbook Slide Sidang Skripsi & Akademik (Academic Defense Deck)

Mengadopsi alur ujian sarjana/magister terstandarisasi untuk memuaskan dosen penguji garis keras:

```text
[1. JUDUL & IDENTITAS]    ──► Judul baku, nama, NPM, dosen pembimbing
       │
[2. DATA AWAL LAPANGAN]   ──► Angka anomali nyata / grafik kerugian sistem (Bukan definisi kamus)
       │
[3. RUANG LINGKUP & GAP]  ──► Batasan 8 poin & posisi celah riset terhadap rujukan SOTA
       │
[4. MATRIKS SOTA]         ──► Komparasi 5 penelitian terdahulu & kelemahan baseline
       │
[5. METODOLOGI PENELITIAN]──► Framework (CRISP-DM), Anti-Leakage Split, alur dekomposisi sinyal
       │
[6. ARSITEKTUR ALUR]      ──► Diagram vektor alur sistem (FigGenie tight-box)
       │
[7. EVALUASI KUANTITATIF] ──► Tabel metrik komparasi (RMSE, MAE, MAPE, MDA, Akurasi)
       │
[8. UJI SIGNIFIKANSI]     ──► Uji Diebold-Mariano / Wilcoxon (Bukti p < 0,05 bukan kebetulan)
       │
[9. PEMBAHASAN EMPIRIS]   ──► Menjawab masalah Slide 2 dengan capaian angka Slide 7
       │
[10. KESIMPULAN & SARAN]  ──► Pemetaan 1:1 Kesimpulan ke Tujuan, saran teknis terarah
```

### Panduan Wara Slide Sidang per Halaman:

- **Slide Latar Belakang (Slide 2)**:
  - *Larangan*: Dilarang menulis paragraf sejarah teknologi atau definisi umum ("Saham adalah surat berharga...").
  - *Format Wajib*: Tampilkan grafik volatilitas harga ekstrem atau data kerugian finansial akibat model peramalan baseline gagal mendeteksi sinyal non-stasioner.
  - *Judul Slide*: Volatilitas Saham Perbankan Memicu Galat Prediksi Baseline Hingga 18,4%

- **Slide Metodologi & Anti-Leakage (Slide 5)**:
  - *Poin Kritis Penguji*: Penguji selalu mencari celah kebocoran data (*data leakage*).
  - *Judul Slide*: Protokol Anti-Leakage: Pemisahan Data Latih-Uji Mendahului Dekomposisi CEEMDAN
  - *Wara Penegas*: "Dekomposisi sinyal dilakukan secara terisolasi pada set data latih (80%) dan set data uji (20%) secara terpisah guna menjamin nol kebocoran informasi masa depan."

- **Slide Uji Signifikansi Statistik (Slide 8)**:
  - *Poin Kritis Penguji*: Membuktikan bahwa kemenangan model baru bukan faktor keberuntungan.
  - *Judul Slide*: Uji Diebold-Mariano Membuktikan Keunggulan Model Signifikan pada Tingkat 95%
  - *Wara Penegas*: "Nilai p-value DM = 0,012 (< 0,05). Hipotesis nol ditolak secara mutlak, membuktikan akurasi prediksi model usulan secara statistik mengungguli baseline LSTM konvensional."

---

## 4. Format Penulisan Catatan Pembicara (Speaker Notes Formula)

Setiap slide yang disusun WAJIB menyertakan blok *Speaker Notes* dengan rumus 3 kalimat (Durasi: 30-45 detik):
1. **Kalimat 1 (Pernyataan Klaim)**: Tegaskan fakta atau temuan terpenting dari slide.
2. **Kalimat 2 (Penjelasan Data/Visual)**: Arahkan pandangan audiens ke grafik, tabel, atau diagram yang ditampilkan.
3. **Kalimat 3 (Jembatan Transisi)**: Kaitkan slide ini dengan slide berikutnya untuk menjaga momentum presentasi.

*Contoh Speaker Notes untuk Slide Hasil Pengujian*:
"Bapak dan Ibu Dosen Penguji, tabel ini merangkum perbandingan metrik kinerja antara model baseline dengan model usulan kami. Perhatikan baris kedua pada kolom RMSE: model CEEMDAN-LSTM berhasil menekan galat dari 142,5 poin menjadi 93,8 poin, yang mencerminkan peningkatan akurasi sebesar 34,2%. Sekarang mari kita bedah apakah keunggulan angka ini terbukti secara statistik pada slide pengujian Diebold-Mariano berikut."

---

## 5. Kartu Antisipasi Sanggahan Penguji / Klien (Defense Q&A Cards)

Di akhir dokumen naskah slide, cantumkan minimal 3 kartu antisipasi pertanyaan sulit:

```text
KARTU SANGGAHAN AKADEMIK 01:
- Pertanyaan Penguji: "Mengapa Anda memilih CEEMDAN dibanding EMD standar atau Wavelet?"
- Jawaban Lugas (Direct Answer): "EMD standar rentan terhadap permasalahan mode mixing, sedangkan Wavelet sangat bergantung pada pemilihan mother wavelet secara subjektif. CEEMDAN menambahkan derau putih Gaussian adaptif pada setiap tahap dekomposisi sehingga menghasilkan residu yang terisolasi sempurna dan rekonstruksi data yang eksak."
- Rujukan Slide Cadangan: Slide Appendix A-02 (Perbandingan Spektral Dekomposisi).

KARTU SANGGAHAN KLIEN 01:
- Pertanyaan Klien: "Bagaimana jika tablet kasir kami dicuri atau rusak mendadak?"
- Jawaban Lugas: "Seluruh data transaksi dan stok cabang tersimpan aman di cloud terenkripsi. Anda cukup mengunduh aplikasi di tablet baru dan login kembali; seluruh konfigurasi dan data transaksi akan pulih sempurna dalam 60 detik."
- Rujukan Slide Cadangan: Slide Appendix B-01 (Protokol Pencadangan & Enkripsi Data).
```