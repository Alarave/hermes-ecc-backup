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
- **Aturan Hemat Tanda Kurung (Parenthesis Economy - Audit E:\SKRIPSI_UPNVJ_TEXT)**:
  - Berdasarkan audit empiris 484 naskah skripsi riil di `E:\SKRIPSI_UPNVJ_TEXT`, rata-rata pemakaian tanda kurung dalam skripsi resmi hanya berkisar **6 pasang per 1.000 kata**.
  - DILARANG KERAS menyelipkan istilah bahasa Inggris di dalam kurung setelah terjemahan Indonesianya (seperti `penjual pihak ketiga (*third-party sellers*)`, `ketidaksesuaian katalog (*catalog mismatch*)`, `pantulan cahaya (*glare*)`, atau `kebocoran data (*data leakage*)`). Pola ini adalah ciri khas *AI Slop*.
  - Istilah asing cukup dicetak miring (*italic*) secara langsung menyatu di dalam kalimat tanpa tanda kurung (misalnya: *e-commerce*, *third-party seller*, *catalog mismatch*, *visual grounding*, *data leakage*), atau gunakan padanan bahasa Indonesia yang baku.
  - Tanda kurung HANYA diizinkan untuk 3 fungsi sah: 1) Akronim / singkatan pada penyebutan pertama (misal: *Optical Character Recognition* (OCR)), 2) Tahun sitasi rujukan (misal: Zhang et al. (2023)), dan 3) Rujukan pasal/ayat perundang-undangan (misal: Pasal 8 ayat (1)).
- **Anti-Slop & Anti-Fluff**: Dilarang menggunakan kalimat berbunga-bunga, klausa bertumpuk, atau kata hiperbolis robotik. Kalimat harus padat, lugas, beralur logis, dan mematuhi EYD V.

### 2. Identifikasi Masalah
- Wajib menggunakan **Kalimat Deklaratif Berita** bernomor (Bukan kalimat tanya).
- Setiap butir masalah harus merupakan kristalisasi langsung dari fakta yang telah dipaparkan pada Latar Belakang Masalah (Dilarang mengarang masalah baru yang tiba-tiba muncul).

### 3. Batasan Masalah / Ruang Lingkup (Scope Defenses)
- Bertindak sebagai **Perisai Penguji**: Membatasi ruang lingkup agar tidak diserang pada aspek di luar penelitian.
- **Larangan Format Label Kaku (Anti-Key-Value Slop)**: DILARANG menggunakan format key-value tebal ala prompt AI seperti `**Objek Penelitian**: ...`, `**Dataset**: ...`, `**Tumpukan Teknologi**: ...`, `**Pernyataan Non-Scope**: ...`. Format ini membuat naskah terlihat seperti draf mentah generator AI.
- Wajib disajikan dalam bentuk butir kalimat naratif bernomor yang mengalir secara alami (misalnya: "1. Objek penelitian difokuskan pada...", "2. Data yang digunakan berupa...", "3. Penelitian ini tidak mencakup...").
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

### 7. Sistematika Penulisan (Anti-AI-Slop Standard)
- **Landasan Empiris Korpus (E:\SKRIPSI_UPNVJ_TEXT)**: Berdasarkan audit korpus 205 naskah skripsi komputasi riil, sistematika penulisan berfungsi memetakan bab secara jernih, lugas, dan fungsional kepada pembaca dan dewan penguji.
- **Daftar Larangan AI Slop (Strict Anti-Slop Rules)**:
  - DILARANG menggunakan kata-kata hiperbolis atau puitis buatan bot: *"membedah"*, *"mengupas tuntas"*, *"secara holistik"*, *"saling berkesinambungan"*, *"secara komprehensif mengintegrasikan"*, *"menjawab secara revolusioner"*.
  - DILARANG membocorkan frasa meta-prompting ke dalam naskah: *"memetakan secara satu-ke-satu (1:1)"*, *"anti-data leakage protocol"*, *"strict gate"*. Gunakan bahasa akademis natural: *"menjawab tujuan penelitian"*, *"pembagian data latih dan uji terisolasi"*.
- **Pola Pembuka Baku**: Gunakan kalimat pengantar formal dan wajar:
  *"Sistematika penulisan skripsi ini disusun untuk memberikan gambaran menyeluruh dan sistematis mengenai alur pembahasan pada setiap bab. Adapun sistematika penulisan laporan ini diuraikan sebagai berikut:"*
- **Penyajian Terpilih**:
  1. *Format Heading per Bab (Standar Nasional / UPNVJ)*: Format paling disukai penguji karena memudahkan *scanning* cepat saat sidang. Setiap bab dituliskan nama babnya, diikuti 1 paragraf ringkas berisi komponen operasionalnya.
  2. *Format Naratif Bergradasi (Standar Gunadarma)*: Terdiri dari 5 paragraf terpisah (1 paragraf per bab) atau narasi proporsional yang lugas, tidak bertele-tele, dan secara konkret menyebutkan variabel, metode, dan metrik yang diuji.

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
Sistematika penulisan laporan skripsi ini disusun untuk memberikan gambaran menyeluruh dan sistematis mengenai alur pembahasan pada setiap bab. Adapun sistematika penulisan pada penelitian ini diuraikan sebagai berikut:

**BAB I PENDAHULUAN**  
Bab ini menguraikan latar belakang permasalahan yang mendasari penelitian, identifikasi masalah, pembatasan ruang lingkup penelitian, rumusan masalah, tujuan penelitian, manfaat penelitian (baik teoretis maupun praktis), serta sistematika penulisan laporan.

**BAB II LANDASAN TEORI**  
Bab ini menyajikan teori-teori dasar dan konsep fundamental yang mendukung topik penelitian, mencakup kajian pustaka mengenai [Nama Teori/Metode Utama], serta telaah penelitian-penelitian terdahulu yang relevan sebagai acuan pembanding.

**BAB III METODOLOGI PENELITIAN**  
Bab ini menguraikan tahapan pelaksanaan penelitian secara terperinci, meliputi teknik pengumpulan data, prapemrosesan data, perancangan arsitektur pemodelan [Nama Metode/Sistem], serta instrumen dan metrik pengujian yang digunakan untuk mengevaluasi kinerja sistem.

**BAB IV HASIL DAN PEMBAHASAN**  
Bab ini memaparkan hasil implementasi sistem atau model, analisis hasil pengujian performa berdasarkan metrik evaluasi kuantitatif, pengujian signifikansi statistik terhadap model pembanding, serta pembahasan mendalam terhadap temuan empiris hasil eksperimen.

**BAB V KESIMPULAN DAN SARAN**  
Bab ini menyajikan kesimpulan akhir yang ditarik dari hasil analisis dan pembahasan guna menjawab tujuan penelitian yang telah ditetapkan, serta memuat saran-saran teknis yang relevan bagi pengembangan penelitian lanjutan di masa depan.

**DAFTAR PUSTAKA**  
Bagian ini memuat daftar seluruh sumber referensi ilmiah, jurnal, buku, dan dokumen resmi yang dijadikan acuan dalam penyusunan penelitian ini.

**LAMPIRAN**  
Bagian ini menyajikan data pendukung, cuplikan kode program utama, dokumentasi pengujian, atau berkas pendukung lainnya yang melengkapi laporan penelitian.
```

---

## 🏛️ STRUKTUR ALTERNATIF: PRESET UNIVERSITAS GUNADARMA (4 SUB-BAB)

Khusus mahasiswa Universitas Gunadarma (FIKTI/FTI), gunakan struktur numerik 4 sub-bab baku:

```markdown
# 1. PENDAHULUAN

## 1.1. Latar Belakang
[Piramida terbalik 4 paragraf: Makro industri -> Masalah lapangan & data awal -> Research Gap -> Solusi usulan.]

## 1.2. Ruang Lingkup
Agar penelitian ini terarah dan tidak meluas pada aspek di luar fokus utama, maka ruang lingkup penelitian ini dibatasi sebagai berikut:
1. Objek penelitian difokuskan pada [Objek Penelitian] khususnya pada kategori [Kategori Spesifik].
2. Data yang digunakan bersumber dari [Sumber Data] periode [Rentang Waktu] dengan total sampel sebanyak [Jumlah Observasi].
3. Masukan sistem berupa [Fitur/Karakteristik Citra atau Teks] dengan luaran berupa [Status/Keputusan/Klasifikasi].
4. Pemodelan utama menerapkan arsitektur [Metode/Model Inti] yang dipadukan dengan [Metode Pendukung].
5. Implementasi sistem dibangun menggunakan bahasa pemrograman [Bahasa] serta pustaka komputasi [Framework/Library].
6. Antarmuka pengujian sistem disajikan dalam bentuk [Web/REST API/Dashboard].
7. Evaluasi kinerja sistem diukur menggunakan metrik kuantitatif [Daftar Metrik] serta pengujian signifikansi statistik [Nama Uji Statistik].
8. Penelitian ini tidak mencakup [Batasan yang sengaja dikecualikan, misal integrasi live database internal].

## 1.3. Tujuan Penelitian
Tujuan operasional yang hendak dicapai dalam penelitian ini adalah:
1. Mengembangkan arsitektur [Model] untuk mengatasi masalah [X].
2. Menganalisis signifikansi peningkatan akurasi model usulan terhadap baseline.

## 1.4. Sistematika Penulisan
Sistematika penulisan laporan skripsi ini disusun untuk mempermudah penyampaian alur penelitian secara runtut ke dalam lima bab pembahasan:

Bab 1 Pendahuluan menguraikan latar belakang permasalahan mengenai [isu utama], batasan ruang lingkup penelitian dalam 8 aspek spesifik, perumusan masalah, tujuan operasional penelitian, serta sistematika penulisan laporan.

Bab 2 Landasan Teori memuat tinjauan pustaka dan konsep fundamental yang melandasi penelitian, meliputi teori [konsep inti], arsitektur [model utama], matriks perbandingan State-of-the-Art (SOTA) dari penelitian terdahulu, serta kerangka pemikiran teoritis penelitian.

Bab 3 Metodologi Penelitian menjelaskan tahapan pelaksanaan riset berbasis kerangka kerja CRISP-DM, mencakup teknik pengumpulan dataset [jumlah sampel], prosedur prapemrosesan data dan partisi data uji terisolasi, perancangan arsitektur [model hibrida/metode], serta formula metrik evaluasi kinerja.

Bab 4 Hasil dan Pembahasan memaparkan implementasi sistem dan model, dokumentasi pengujian fungsional black-box, evaluasi metrik kinerja kuantitatif per atribut, hasil pengujian signifikansi statistik terhadap model pembanding, serta pembahasan mendalam terhadap faktor yang mempengaruhi performa model.

Bab 5 Penutup menyajikan kesimpulan akhir yang ditarik secara objektif untuk menjawab tujuan penelitian berdasarkan hasil pengujian empiris, serta merumuskan saran-saran teknis yang konkret untuk pengembangan penelitian lanjutan.
```
