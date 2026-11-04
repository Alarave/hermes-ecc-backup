# Pedoman Standar Penulisan Akademik & Skripsi Bebas AI-Slop
*(Disarikan dari Korpus Empiris Skripsi UPNVJ & Panduan Baku Gunadarma)*

Dokumen ini adalah acuan mutlak bagi seluruh agen ketika menyusun draf dokumen ilmiah, bab skripsi (Bab 1 sampai Bab 5), artikel jurnal, maupun catatan akademik. Tujuannya adalah mengeliminasi aroma tulisan mesin (AI-flavor) dan menghasilkan naskah ilmiah yang berbobot, mengalir, dan sesuai tradisi akademik Indonesia.

---

## 1. Anatomi Latar Belakang (Pola Piramida Terbalik 5-Paragraf)
Latar belakang BUKAN kumpulan opini atau definisi kamus. Latar belakang wajib mengalir deduktif dari masalah makro hingga justifikasi algoritma tanpa menggunakan daftar berbutir (*zero bullet points*):

- **Paragraf 1 (Konteks Makro & Data Empiris Faktual)**:
  Buka dengan data statistik riil, fenomena nasional/global, tahun pencatatan, dan lembaga resmi (misal: data Korlantas Polri, BPS, WHO, BI, atau Satgas). Wajib menyertakan angka konkret, bukan klaim umum.
  *Contoh*: "Data dari Korps Lalu Lintas Kepolisian Republik Indonesia mencatat sebanyak 103.645 kasus kecelakaan pada tahun 2021 dengan 25.266 korban jiwa..."
- **Paragraf 2 (Objek Studi & Landasan Yuridis/Institusional)**:
  Sebutkan regulasi terkait (Undang-Undang, Perpres, Keputusan Menteri, atau SK Direksi) serta peran objek/sistem yang diteliti.
  *Contoh*: "Berdasarkan Keputusan Menteri Komunikasi dan Informatika Nomor 171 Tahun 2020, pemerintah mengembangkan aplikasi PeduliLindungi sebagai instrumen surveilans kesehatan..."
- **Paragraf 3 (Masalah Nyata di Lapangan / Pain Point Konkret)**:
  Uraikan kegagalan sistem lama, komplain riil pengguna, inefisiensi, atau anomali data di lapangan yang ditemukan.
  *Contoh*: "Kendati demikian, pengguna kerap melaporkan kendala teknis pada kolom ulasan Google Play Store, meliputi ketidakakuratan zona risiko, kegagalan pembaruan sertifikat vaksinasi, hingga konsumsi daya baterai yang berlebihan..."
- **Paragraf 4 (Kebutuhan Solusi Komputasi / Identifikasi Kesenjangan Riset)**:
  Jelaskan mengapa masalah tersebut mendesak untuk diselesaikan dengan pendekatan komputasi dan apa limitasi dari penelitian terdahulu (*research gap*).
- **Paragraf 5 (Usulan Solusi & Justifikasi Ilmiah Pemilihan Metode)**:
  Tutup dengan usulan algoritma/arsitektur spesifik disertai justifikasi teknis mengapa metode tersebut dipilih dibandingkan metode alternatif, didukung oleh sitasi penelitian rujukan.
  *Contoh*: "Oleh karena itu, penelitian ini menerapkan algoritma Long Short-Term Memory (LSTM). Pemilihan LSTM didasarkan pada kemampuannya mengatasi permasalahan vanishing gradient melalui mekanisme gerbang penyimpanan informasi konteks jangka panjang..."

---

## 2. Tabel Kata dan Frasa Terlarang (AI Banned Slop vs Baku Ilmiah)

| Frasa Klise AI (DILARANG KERAS) | Koreksi / Pengganti Akademik Manusiawi |
|---|---|
| "Dalam era globalisasi yang semakin pesat..." | Langsung buka dengan data: "Volume transaksi digital di Indonesia pada tahun 2023 mencapai..." |
| "Hal ini sangat krusial dan esensial..." | "Faktor ini menentukan stabilitas sistem..." |
| "Memegang peranan vital dalam menjembatani..." | "Berfungsi menghubungkan modul A dengan modul B..." |
| "Secara komprehensif dan holistik..." | "Secara menyeluruh..." atau jelaskan cakupan variabelnya satu per satu. |
| "Memberikan hasil yang sangat luar biasa / optimal..." | Sajikan angka uji: "Menghasilkan peningkatan akurasi sebesar 4,8%..." |
| "Paradigma baru yang tak terelakkan..." | "Pendekatan alternatif yang mulai diterapkan..." |
| "Lanskap teknologi yang dinamis..." | "Perkembangan arsitektur perangkat lunak..." |
| "Menyuguhkan sinergi yang harmonis..." | "Menghasilkan integrasi data yang konsisten..." |

---

## 3. Tata Bahasa Impersonal & Kalimat Pasif Ilmiah
Naskah skripsi Indonesia berorientasi pada proses dan objek penelitian, bukan subjek peneliti:
- **DILARANG**:
  - *"Kami melakukan eksperimen pembersihan data..."*
  - *"Penulis mengusulkan model transformer..."*
  - *"AI ini bertugas mengekstrak fitur..."*
- **WAJIB**:
  - *"Pembersihan data dilakukan melalui tahapan eliminasi derau..."*
  - *"Model transformer diusulkan untuk menangani..."*
  - *"Ekstraksi fitur dilakukan menggunakan lapisan konvolusi..."*
  - Jika mutlak harus menyebut peneliti, gunakan kata *"peneliti"* secara hemat dan formal.

---

## 4. Protokol Penyajian Gambar dan Tabel (The Narrative Bridge)
Setiap gambar, diagram alir, dan tabel data TIDAK BOLEH ditaruh berdiri sendiri tanpa kalimat pengantar:
1. **Kalimat Pengantar Sebelum Elemen**:
   Wajib menuliskan narasi rujukan sebelum tabel/gambar muncul.
   *Format*: "Rincian atribut dataset kecelakaan disajikan pada Tabel 4.1." atau "Tahapan kerangka pikir penelitian diilustrasikan pada Gambar 3.1 sebagai berikut:"
2. **Penamaan Baku**:
   - Judul Gambar di bawah gambar: `Gambar 3.1 Kerangka Pikir Penelitian`
   - Judul Tabel di atas tabel: `Tabel 4.1 Rincian Atribut Dataset`
3. **Narasi Pembahasan Pasca-Elemen**:
   Setelah tabel/gambar, wajib ada paragraf yang membedah arti angka atau alur diagram, bukan sekadar membiarkan pembaca menebak maknanya.

---

## 5. Larangan Format Berbutir (Anti-Bullet-Pointitis)
- **Bab Pembahasan (Bab 4) dan Landasan Teori (Bab 2)**:
  DILARANG keras menyajikan analisis dalam bentuk deretan bullet points (`- Poin 1`, `- Poin 2`).
  Ubah menjadi paragraf naratif:
  *Buruk (Gaya AI)*:
  - Presisi: Model mencapai 89%.
  - Recall: Model mencapai 85%.
  - Kesimpulan: Model bekerja baik.
  *Benar (Gaya Akademik Manusiawi)*:
  "Berdasarkan hasil pengujian pada skenario uji ketiga, model menghasilkan nilai presisi sebesar 89,2% dan nilai perolehan kembali (recall) sebesar 85,1%. Keseimbangan kedua metrik tersebut menunjukkan bahwa mekanisme attention mampu menekan jumlah positif palsu tanpa mengorbankan sensitivitas deteksi kelas minoritas."

---

## 6. Standar Tipografi, Paragraph Style Judul, & Geometri Fisik Naskah
- **Margin Kertas**: Atas 4 cm (`113.4 pt`), Kiri 4 cm (`113.4 pt`), Bawah 3 cm (`85.0 pt`), Kanan 3 cm (`85.0 pt`) (Kertas A4).
- **Huruf & Spasi**: Times New Roman 12 pt, spasi 1.5, perataan justify (rata kiri-kanan).
- **Indentasi Paragraf**: Awal alinea menjorok ke dalam tepat **1,27 cm (`36.0 pt` / `0,5 inci`)**.
- **Aturan Judul Sub-Bab Bab 2 (1 Sampai 2 Kata Murni)**:
  - Judul sub-bab Bab 2 wajib terdiri dari **1 sampai 2 kata benda entitas murni** (contoh: `2.1 Tanaman Selada`, `2.2 Citra Digital`, `2.3 *Deep Learning*`, `2.6 Python`, `2.7 Evaluasi Model`, `2.8 Penelitian Terdahulu`).
  - DILARANG menggunakan kalimat panjang AI slop atau menggabungkan dua topik dengan kata `dan`.
  - Menggunakan *hanging indent* `36.0 pt` (`1,27 cm`): nomor sub-bab di `x = 113.4 pt` dan teks judul di `x = 149.4 pt` (sejajar vertikal dengan awal baris pertama paragraf), serta mencetak istilah bahasa Inggris dengan format **Tebal Miring (*Bold Italic*)**.
- **Tanda Baca**: Dilarang menggunakan tanda pisah panjang em-dash atau en-dash. Gunakan tanda titik dua (:), kurung (), koma, atau tanda strip biasa (-).
- **Penulisan Angka Desimal**: Gunakan koma (,) untuk bahasa Indonesia teknis (misal: `92,4%`, `0,05`) atau titik (.) jika mematuhi konvensi naskah komputasi berbahasa Inggris.
