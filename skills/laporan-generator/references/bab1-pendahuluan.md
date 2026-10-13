# STANDAR OPERASIONAL & TEMPLATE: BAB I PENDAHULUAN
> Dokumen referensi resmi penulisan Bab 1 Pendahuluan (Standar Akademik & Panduan Skripsi Indonesia/Universitas Gunadarma).

---

## 🏛️ PEDOMAN ARSITEKTUR BAB I (RULES & CONSTRAINTS)

### 1. Latar Belakang Masalah (LBM)
- **Pola Corong Terbalik (Inverted Funnel)**:
  1. *Paragraf 1 (Makro)*: Fenomena umum, konteks industri/sains, dan kondisi ideal yang diharapkan (*Das Sollen*). DILARANG memulai dengan definisi kamus/buku teks (misal: "Menurut KBBI...") atau frasa klise (*"Di era globalisasi saat ini..."*).
  2. *Paragraf 2-3 (Mikro & Realitas)*: Masalah faktual di lapangan (*Das Sein*). Wajib didukung bukti empiris atau data metrik kuantitatif (angka kerugian, persentase error, latensi, dsb).
  3. *Paragraf 4 (State-of-the-Art & Research Gap)*: Kaji keterbatasan 3-5 paper rujukan terdahulu. Tunjukkan apa yang *belum* terselesaikan.
  4. *Paragraf 5 (Solusi yang Diusulkan)*: Argumen kuat mengapa metode/arsitektur yang Anda bawa adalah solusi paling rasional untuk menutup *gap* tersebut.
- **Standar Sitasi**: Wajib menggunakan format Markdown Citation Keys `[@citekey]` yang terhubung ke `references.bib` untuk kompilasi Pandoc/Typst.
- **Anti-Slop & Anti-Fluff**: Dilarang melakukan *word-vomit* / pengulangan kalimat demi memenuhi target halaman. Kalimat harus padat, lugas, dan mematuhi EYD V (bedakan kata depan "di " dan imbuhan "di-").

### 2. Identifikasi Masalah
- Wajib menggunakan **Kalimat Deklaratif Berita** bernomor (Bukan kalimat tanya).
- Setiap butir masalah harus merupakan kristalisasi langsung dari fakta yang telah dipaparkan pada Latar Belakang Masalah (Dilarang mengarang masalah baru yang tiba-tiba muncul).

### 3. Batasan Masalah (Scope Defenses)
- Bertindak sebagai **Perisai Penguji**: Membatasi ruang lingkup agar tidak diserang pada aspek di luar penelitian.
- Wajib memuat **Hard-Boundaries**:
  - Ruang lingkup data (jumlah sampel, rentang waktu pengambilan, resolusi/format, kriteria inklusi/eksklusi).
  - Algoritma/arsitektur spesifik yang dipakai (bukan seluruh cabang ilmu AI).
  - Lingkungan pengujian / batasan lingkungan eksekusi.

### 4. Rumusan Masalah (Research Questions)
- Wajib menggunakan **Kalimat Tanya Ilmiah Terukur** bernomor yang diakhiri tanda tanya (`?`).
- **Dilarang keras menggunakan kata tanya biner tertutup** seperti *"Apakah..."* yang bisa dijawab dangkal dengan "Ya/Tidak".
- Gunakan kata tanya operasional: *"Bagaimana...", "Sejauh mana...", "Seberapa besar..."*.
- Jumlah ideal: **2 hingga 4 butir pertanyaan**.

### 5. Tujuan Penelitian
- Wajib memiliki **One-to-One Alignment (Cermin Sempurna)** terhadap Rumusan Masalah (Jika Rumusan Masalah ada 3 butir, Tujuan Penelitian wajib 3 butir dengan urutan yang bersesuaian).
- Awali setiap butir dengan **Kata Kerja Operasional (KKO)** yang terukur (contoh: *"Merancang...", "Menganalisis perbandingan...", "Mengevaluasi akurasi..."*). Dilarang menggunakan kata kognitif pasif seperti *"Untuk mengetahui..."* atau *"Untuk memahami..."*.

### 6. Manfaat Penelitian
- Wajib dipisahkan menjadi dua kategori tegas:
  1. **Manfaat Teoretis**: Kontribusi terhadap khazanah keilmuan, literatur akademik, atau dasar penelitian selanjutnya.
  2. **Manfaat Praktis**: Manfaat terukur dan realistis yang dirasakan langsung oleh pihak terkait/objek penelitian (Dilarang membuat klaim muluk-muluk/utopis).

### 7. Sistematika Penulisan
- Berupa deskripsi naratif singkat per bab (Bab I hingga Bab V) yang memandu alur baca penguji, bukan sekadar salinan Daftar Isi (Table of Contents).

---

## 📝 TEMPLATE STRUKTUR BAB I PENDAHULUAN

```markdown
# BAB I PENDAHULUAN

## 1.1 Latar Belakang Masalah
[Paragraf 1: Fenomena makro, standar ideal / Das Sollen, pentingnya topik ini secara global atau nasional [@sitasi1]. Hindari kalimat klise.]

[Paragraf 2: Kenyataan di lapangan / Das Sein. Tunjukkan data spesifik, metrik kegagalan, atau inefisiensi yang saat ini terjadi [@sitasi2].]

[Paragraf 3: Tinjauan riset terkini (State-of-the-Art). Sebutkan solusi yang pernah dicoba oleh peneliti sebelumnya [@penelitiA2022; @penelitiB2023].]

[Paragraf 4: Research Gap. Paparkan kelemahan, celah, atau batasan dari penelitian terdahulu yang masih menyisakan masalah terbuka.]

[Paragraf 5: Justifikasi Solusi. Usulkan metode, arsitektur, atau integrasi baru Anda sebagai jawaban atas research gap tersebut.]

## 1.2 Identifikasi Masalah
Berdasarkan latar belakang masalah yang telah diuraikan, masalah-masalah yang dapat diidentifikasi adalah sebagai berikut:
1. Tingkat akurasi deteksi pada kondisi [X] masih rendah akibat tingginya tingkat derau (*noise*).
2. Lamanya waktu inferensi model konvensional yang menghambat implementasi sistem secara *real-time*.
3. Belum tersedianya arsitektur hibrida yang mampu menangani ketidakseimbangan kelas (*class imbalance*) pada dataset [Y].

## 1.3 Batasan Masalah
Agar penelitian ini tetap terarah dan tidak meluas di luar ruang lingkup yang direncanakan, maka batasan masalah dalam penelitian ini ditetapkan sebagai berikut:
1. Data yang digunakan terbatas pada dataset [Nama Dataset] yang dikumpulkan pada periode [Bulan/Tahun - Bulan/Tahun].
2. Pra-pemrosesan data difokuskan pada pembersihan [fitur A] dan normalisasi nilai menggunakan metode [Metode X].
3. Model kecerdasan buatan yang dikembangkan dan dianalisis dibatasi pada arsitektur [Nama Arsitektur/Algoritma].
4. Evaluasi performa sistem diukur menggunakan metrik *Root Mean Squared Error* (RMSE), *Mean Absolute Error* (MAE), dan pengujian signifikansi statistik Diebold-Mariano.

## 1.4 Rumusan Masalah
Berdasarkan batasan masalah di atas, rumusan masalah dalam penelitian ini adalah:
1. Bagaimana merancang dan mengimplementasikan arsitektur [Model] untuk menangani [Masalah X]?
2. Bagaimana perbandingan performa akurasi antara [Model yang Diusulkan] terhadap [Model Pembanding/Baseline] berdasarkan metrik [Metrik Y]?
3. Sejauh mana integrasi [Komponen Z] mampu meningkatkan efisiensi waktu komputasi dalam proses pelatihan model?

## 1.5 Tujuan Penelitian
Tujuan yang hendak dicapai dalam penelitian ini adalah:
1. Merancang dan mengimplementasikan arsitektur [Model] dalam mengatasi permasalahan [Masalah X].
2. Menganalisis perbandingan performa akurasi antara [Model yang Diusulkan] terhadap [Model Pembanding/Baseline] berdasarkan metrik [Metrik Y].
3. Mengevaluasi dampak integrasi [Komponen Z] terhadap efisiensi waktu komputasi selama proses pelatihan.

## 1.6 Manfaat Penelitian
Penelitian ini diharapkan dapat memberikan manfaat sebagai berikut:

### 1.6.1 Manfaat Teoretis
1. Memberikan kontribusi terhadap pengembangan literatur di bidang [Nama Bidang Ilmu], khususnya mengenai penerapan arsitektur [Model].
2. Menjadi rujukan ilmiah bagi penelitian lanjutan yang meneliti topik optimasi [Masalah X].

### 1.6.2 Manfaat Praktis
1. Membantu praktisi/organisasi [Nama Pihak] dalam mempercepat proses [Kegiatan X] dengan margin kesalahan yang lebih rendah.
2. Menyediakan instrumen otomatisasi berbasis data yang dapat digunakan secara terukur oleh pengembang sistem di industri.

## 1.7 Sistematika Penulisan
Sistematika penulisan laporan ini disusun ke dalam lima bab sebagai berikut:

- **BAB I PENDAHULUAN**: Menguraikan latar belakang masalah, identifikasi masalah, batasan masalah, rumusan masalah, tujuan penelitian, manfaat penelitian, serta sistematika penulisan.
- **BAB II TINJAUAN PUSTAKA**: Membahas landasan teori yang relevan mengenai [Teori 1], [Teori 2], serta penelitian terdahulu yang mendasari perancangan sistem.
- **BAB III METODOLOGI PENELITIAN**: Menjelaskan tahapan penelitian, desain arsitektur sistem, teknik pengumpulan data, instrumen evaluasi, dan skenario eksperimen.
- **BAB IV HASIL DAN PEMBAHASAN**: Menyajikan hasil eksperimen, visualisasi data, analisis perbandingan performa terhadap model baseline, serta interpretasi temuan ilmiah.
- **BAB V KESIMPULAN DAN SARAN**: Berisi kesimpulan akhir yang menjawab rumusan masalah secara komprehensif serta saran strategis untuk pengembangan penelitian di masa depan.
```
