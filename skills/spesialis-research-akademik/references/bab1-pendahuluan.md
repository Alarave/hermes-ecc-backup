# STANDAR OPERASIONAL & TEMPLATE: BAB I PENDAHULUAN
> Dokumen referensi resmi penulisan Bab 1 Pendahuluan (Standar Akademik & Panduan Skripsi Indonesia/Universitas Gunadarma).

---

## 🏛️ PEDOMAN ARSITEKTUR BAB I (RULES & CONSTRAINTS)

### 1. Latar Belakang Masalah (LBM) - Anatomi 5-Paragraf Korpus FIK UPNVJ
- **Pola Corong Terbalik 5-Paragraf (Inverted Funnel Korpus UPNVJ)**:
  Berdasarkan audit empiris terhadap naskah Bab 1 Fakultas Ilmu Komputer UPNVJ (`E:\SKRIPSI_UPNVJ_PDF` & `E:\SKRIPSI_UPNVJ_TEXT`), Latar Belakang wajib disusun dalam 5 paragraf terstruktur di mana setiap paragraf terdiri dari 4 kalimat padat:
  1. *Paragraf 1 (Fenomena Makro, Regulasi & Statistik Resmi Nasional/Global - Das Sollen)*:
     - Kalimat 1: Pernyataan peran penting objek atau domain masalah secara faktual tanpa pembuka klise (*"Di era revolusi industri 4.0..."* dilarang keras).
     - Kalimat 2-3: Data statistik kuantitatif dari lembaga resmi (BPS, WHO, Kemenkes, IDF, APJII, BPOM, atau laporan industri resmi) yang membuktikan skala urgensi objek tersebut.
     - Kalimat 4: Tuntutan standar kualitas atau kondisi ideal yang harus dipenuhi pada sektor tersebut.
  2. *Paragraf 2 (Realitas Masalah Lapangan & Bottleneck Prosedur Konvensional - Das Sein)*:
     - Kalimat 1: Fakta permasalahan spesifik yang terjadi di lokus penelitian atau platform objek saat ini.
     - Kalimat 2: Bukti angka lonjakan kasus, tingkat kegagalan, atau volume data yang tidak tertangani.
     - Kalimat 3: Kelemahan metode konvensional/manual yang masih berjalan (bergantung pada pengamatan subjektif manusia, membutuhkan waktu 2 sampai 3 hari, atau rentan kesalahan verifikasi).
     - Kalimat 4: Konsekuensi langsung apabila keterbatasan prosedur manual tersebut tidak segera diatasi dengan instrumen otomatis.
  3. *Paragraf 3 (Transisi Paradigma Komputasi & Rasionalitas Metode Inti)*:
     - Kalimat 1: Pengenalan pendekatan komputasi (*machine learning*, *deep learning*, pengolahan citra digital, atau pemodelan bahasa alami) sebagai solusi objektif berbasis data.
     - Kalimat 2-3: Penjelasan teknis mengenai cara kerja algoritma inti yang diusulkan (misal: kemampuan CNN mengekstraksi fitur spasial daun, ketangguhan Random Forest terhadap derau data tabular, atau presisi *visual grounding* dan OCR pada kemasan produk).
     - Kalimat 4: Alasan kecocokan karakteristik algoritma tersebut terhadap sifat data pada Paragraf 2.
  4. *Paragraf 4 (Sintesis Komparatif 3-5 Studi Terdahulu Berangka Metrik & Research Gap)*:
     - Wajib merangkum 3 hingga 5 penelitian terdahulu secara berkesinambungan langsung di dalam satu paragraf padat menggunakan penanda transisi (*Sementara itu, Penelitian lain oleh, Dalam konteks objek serupa*).
     - Setiap rujukan wajib mencantumkan: **Penulis (Tahun) dengan aturan First-Mention lengkap**, **objek/masalah**, **arsitektur yang diuji**, dan **angka metrik hasil eksperimen** (contoh: *"Pengembangan model klasifikasi menggunakan arsitektur VGG16 oleh Zalianty, Pratama, dan Wibowo (2024) pada tanaman hidroponik menghasilkan akurasi sebesar 96%. Sementara itu, Ristanti (2024) membandingkan VGG16 dan MobileNetV2 pada citra daun cabai, yang menunjukkan bahwa MobileNetV2 memperoleh akurasi 92% dibandingkan VGG16 sebesar 74%. Dalam konteks tanaman selada, Rahman, Putri, dan Santoso (2023) menguji model CNN pada 361 citra daun dengan akurasi pengujian sebesar 84%."*).
     - Kalimat penutup Paragraf 4 wajib menegaskan **Celah Penelitian (*Research Gap*)**: apa keterbatasan metode/akurasi/efisiensi dari studi-studi tersebut yang belum terselesaikan.
  5. *Paragraf 5 (Penegasan Solusi Usulan, Integrasi Sistem & Dampak Konkret)*:
     - Kalimat 1: Pernyataan tegas bahwa penelitian ini mengembangkan dan mengevaluasi arsitektur/metode [X] untuk menyelesaikan celah pada Paragraf 4.
     - Kalimat 2: Spesifikasi luaran implementasi (misal: dikemas dalam antarmuka berbasis web/Streamlit/REST API atau pipeline pengujian komparatif terkontrol).
     - Kalimat 3-4: Kontribusi terukur yang dihasilkan dalam meningkatkan kecepatan, akurasi, dan objektivitas pengambilan keputusan.
- **Standar Sitasi**: Wajib menerapkan format Harvard *First-Mention* (3 sampai 5 penulis ditulis lengkap pada kemunculan pertama: *PenulisA, PenulisB, dan PenulisC (2024)*; kutipan berikutnya *PenulisA dkk. (2024)*). DILARANG menggunakan `et al.` atau simbol `&`.
- **Aturan Hemat Tanda Kurung (Parenthesis Economy - Audit E:\SKRIPSI_UPNVJ_TEXT)**:
  - Berdasarkan audit empiris 484 naskah skripsi riil di `E:\SKRIPSI_UPNVJ_TEXT`, rata-rata pemakaian tanda kurung dalam skripsi resmi hanya berkisar **6 pasang per 1.000 kata**.
  - DILARANG KERAS menyelipkan istilah bahasa Inggris di dalam kurung setelah terjemahan Indonesianya (seperti `penjual pihak ketiga (*third-party sellers*)`, `ketidaksesuaian katalog (*catalog mismatch*)`, `pantulan cahaya (*glare*)`, atau `kebocoran data (*data leakage*)`). Pola ini adalah ciri khas *AI Slop*.
  - Istilah asing cukup dicetak miring (*italic*) secara langsung menyatu di dalam kalimat tanpa tanda kurung (misalnya: *e-commerce*, *third-party seller*, *catalog mismatch*, *visual grounding*, *data leakage*), atau gunakan padanan bahasa Indonesia yang baku.
  - Tanda kurung HANYA diizinkan untuk 3 fungsi sah: 1) Akronim / singkatan pada penyebutan pertama (misal: *Optical Character Recognition* (OCR)), 2) Tahun sitasi rujukan (misal: Santoso dkk. (2023)), dan 3) Rujukan pasal/ayat perundang-undangan (misal: Pasal 8 ayat (1)).
- **Anti-Slop & Anti-Fluff**: Dilarang menggunakan kalimat berbunga-bunga, klausa bertumpuk, kata sambung *"di mana / yang mana"* non-spasial, atau kata hiperbolis robotik (*krusial, esensial, revolusioner, komprehensif*). Kalimat harus padat, lugas, beralur logis, dan mematuhi EYD V.

### 2. Identifikasi Masalah & Rumusan Masalah (1.2)
- **Identifikasi Masalah (Opsional sesuai pedoman prodi)**: Wajib menggunakan **Kalimat Deklaratif Berita** bernomor (bukan kalimat tanya). Setiap butir masalah harus merupakan kristalisasi langsung dari fakta empiris pada Paragraf 2 dan Paragraf 4 Latar Belakang.
- **Rumusan Masalah (Research Questions)**:
  - Kalimat pengantar baku: *"Berdasarkan uraian latar belakang di atas, rumusan masalah dalam penelitian ini adalah sebagai berikut:"*.
  - Wajib menggunakan **Kalimat Tanya Ilmiah Terukur** bernomor (`1, 2, 3` atau `a, b, c`) yang diakhiri tanda tanya (`?`).
  - **Dilarang keras menggunakan kata tanya biner tertutup** seperti *"Apakah..."* yang dijawab dangkal dengan "Ya/Tidak".
  - Gunakan kata tanya operasional: *"Bagaimana..."*, *"Sejauh mana..."*, *"Seberapa besar..."*.
  - Pola 3 Butir Baku Korpus FIK UPNVJ:
    1. *Butir 1 (Perancangan/Pembangunan Model)*: *"Bagaimana membangun dan mengimplementasikan model [Algoritma/Arsitektur X] untuk mengklasifikasikan/mendeteksi [Objek Y]?"*
    2. *Butir 2 (Evaluasi Performa Kuantitatif)*: *"Bagaimana performa model yang dihasilkan berdasarkan evaluasi menggunakan metrik [Akurasi, Precision, Recall, F1-Score, mAP, atau RMSE] serta pengujian signifikansi statistik [Uji McNemar / Diebold-Mariano]?"*
    3. *Butir 3 (Integrasi Aplikasi / Komparasi)*: *"Bagaimana mengintegrasikan model [X] ke dalam aplikasi/antarmuka [Streamlit/Web] guna mendukung proses verifikasi/identifikasi secara otomatis?"*

### 3. Batasan Masalah / Ruang Lingkup Penelitian (1.3)
- Bertindak sebagai **Perisai Penguji**: Membatasi ruang lingkup agar tidak diserang pada aspek di luar penelitian saat sidang.
- Kalimat pengantar baku: *"Untuk menjaga fokus analisis agar penelitian tetap terarah dan sesuai dengan perencanaan awal, batasan masalah dalam penelitian ini ditetapkan sebagai berikut:"*.
- **Larangan Format Label Kaku (Anti-Key-Value Slop)**: DILARANG menggunakan format key-value tebal ala prompt AI seperti `**Objek Penelitian**: ...`, `**Dataset**: ...`, `**Tumpukan Teknologi**: ...`, `**Pernyataan Non-Scope**: ...`.
- Wajib disajikan dalam bentuk **5 hingga 8 butir kalimat deklaratif bernomor** yang mengalir alami dan mengunci **Hard-Boundaries**:
  1. Sumber data, lokasi/platform akuisisi, periode pengambilan, dan jumlah total sampel.
  2. Fokus objek dan pembatasan kelas/kategori target (misal: kelas 0 dan kelas 1, atau 3 atribut statis: nama merek, berat bersih, nomor izin edar BPOM/P-IRT) beserta pengecualian tegas terhadap kelas/atribut di luar cakupan.
  3. Spesifikasi format berkas masukan (.jpg, .png, teks, atau deret waktu) dan tahapan prapemrosesan data yang diterapkan.
  4. Pembatasan algoritma/arsitektur kecerdasan buatan yang diuji dan dibandingkan.
  5. Bahasa pemrograman, pustaka komputasi utama, serta bentuk antarmuka/luaran sistem.

### 4. Tujuan Penelitian (1.4)
- Kalimat pengantar baku: *"Merujuk pada latar belakang dan rumusan masalah yang telah ditetapkan, tujuan yang hendak dicapai dalam penelitian ini adalah sebagai berikut:"*.
- Wajib memiliki **One-to-One Alignment (Cermin Sempurna 1:1)** terhadap Rumusan Masalah (jika Rumusan Masalah terdiri dari 3 butir, Tujuan Penelitian wajib 3 butir dengan urutan yang bersesuaian).
- Awali setiap butir dengan **Kata Kerja Operasional (KKO)** aktif yang terukur:
  1. *"Mengolah dan mempersiapkan dataset [Objek] serta membangun model [Arsitektur X]..."*
  2. *"Menganalisis dan mengevaluasi performa model [Arsitektur X] menggunakan metrik [Daftar Metrik]..."*
  3. *"Mengembangkan aplikasi/antarmuka [Web/Streamlit] yang mengintegrasikan model [X]..."*
- DILARANG KERAS menggunakan frasa kognitif pasif seperti *"Untuk mengetahui..."* atau *"Memahami..."*.

### 5. Manfaat Penelitian (1.5) & Luaran Penelitian (1.6)
- **Manfaat Penelitian**:
  - Dapat disajikan berdasarkan **Dimensi Keilmuan** (*Manfaat Teoretis* dan *Manfaat Praktis*) atau berdasarkan **Penerima Manfaat (Standar Korpus FIK UPNVJ)**:
    1. *Bagi Pengguna Lapangan / Praktisi / Konsumen*: Menyediakan alat bantu identifikasi/verifikasi otomatis yang cepat dan objektif.
    2. *Bagi Institusi / Penyelenggara Platform*: Memberikan landasan pengambilan keputusan berbasis data untuk pengendalian mutu atau mitigasi risiko.
    3. *Bagi Akademisi / Peneliti Selanjutnya*: Menambah rujukan empiris mengenai kinerja arsitektur [X] pada domain [Y] sebagai pijakan pengembangan riset lanjutan.
- **Luaran Penelitian (1.6 - Sub-bab Standar FIK UPNVJ)**:
  - Menyebutkan artefak terukur yang dihasilkan saat penelitian selesai: (1) Model terlatih (*trained model*) dengan bobot optimal, (2) Tabel hasil evaluasi metrik dan signifikansi statistik, serta (3) Purwarupa aplikasi/dashboard interaktif atau repositori perangkat lunak.

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

## 📝 TEMPLATE STRUKTUR BAB I PENDAHULUAN (STANDAR FIK UPNVJ 7 SUB-BAB)

```markdown
# BAB I PENDAHULUAN

## 1.1 Latar Belakang
[Paragraf 1 - Fenomena Makro & Statistik Resmi (4 Kalimat): (1) Peran penting sektor/objek masalah secara faktual, (2) Data kuantitatif lembaga resmi nasional/global seperti BPS, WHO, Kemenkes, atau APJII (Tahun), (3) Tren pertumbuhan atau urgensi regulasi, (4) Tuntutan standar kualitas ideal yang harus dipenuhi.]

[Paragraf 2 - Realitas Masalah Lapangan & Bottleneck Manual (4 Kalimat): (1) Permasalahan aktual yang terjadi pada lokus atau platform objek penelitian, (2) Data empiris peningkatan kasus atau tingginya tingkat kesalahan saat ini, (3) Keterbatasan prosedur manual yang masih bergantung pada pengamatan subjektif atau memakan waktu lama, (4) Dampak kerugian apabila keterbatasan tersebut tidak diatasi secara otomatis.]

[Paragraf 3 - Transisi Paradigma Komputasi & Rasionalitas Metode (4 Kalimat): (1) Peluang penerapan teknologi pengolahan citra digital atau pembelajaran mesin dalam mendukung identifikasi otomatis, (2) Pengenalan algoritma/arsitektur inti yang dipilih beserta cara kerjanya dalam mengekstraksi fitur, (3) Keunggulan teknis metode tersebut terhadap derau atau variasi data, (4) Kesesuaian karakteristik metode dengan permasalahan pada Paragraf 2.]

[Paragraf 4 - Sintesis Komparatif 3-5 Studi Terdahulu Berangka Metrik & Research Gap: Pengembangan model menggunakan arsitektur [Metode A] oleh Penulis1, Penulis2, dan Penulis3 (2024) untuk mengklasifikasikan [Objek A] berhasil mencapai akurasi sebesar 96,00%. Sementara itu, Penulis4 dan Penulis5 (2024) membandingkan arsitektur [Metode A] dan [Metode B] pada objek [Objek B], yang menunjukkan bahwa [Metode B] memberikan akurasi lebih tinggi sebesar 92,00% dibandingkan [Metode A] sebesar 74,00%. Penelitian lain oleh Penulis6, Penulis7, dan Penulis8 (2023) menerapkan [Metode C] pada [Jumlah] citra dengan capaian akurasi pengujian sebesar 84,00%. Meskipun berbagai penelitian tersebut menunjukkan performa yang baik, sebagian besar studi masih terbatas pada kondisi pencahayaan homogen dan belum menangani [Celah Spesifik / Research Gap].]

[Paragraf 5 - Penegasan Solusi Usulan & Dampak Operasional (4 Kalimat): (1) Berdasarkan uraian tersebut, penelitian ini membangun dan mengevaluasi arsitektur [Nama Metode Usulan] untuk menyelesaikan masalah [Objek Penelitian], (2) Integrasi model ke dalam aplikasi/antarmuka [Streamlit/Web/Pipeline], (3) Kemampuan sistem dalam menyajikan hasil prediksi/verifikasi secara objektif dan cepat, (4) Kontribusi nyata yang diharapkan bagi pengguna dan pengembangan keilmuan.]

## 1.2 Rumusan Masalah
Berdasarkan latar belakang yang telah diuraikan di atas, rumusan masalah dalam penelitian ini adalah sebagai berikut:
1. Bagaimana membangun dan mengimplementasikan model [Algoritma/Arsitektur X] untuk mengklasifikasikan/mendeteksi [Objek Penelitian]?
2. Bagaimana performa model yang dihasilkan berdasarkan evaluasi menggunakan metrik [Akurasi, Precision, Recall, F1-Score, dan Confusion Matrix] serta pengujian signifikansi statistik [Nama Uji Statistik]?
3. Bagaimana mengintegrasikan model [Algoritma/Arsitektur X] ke dalam aplikasi berbasis [Streamlit/Web] agar dapat digunakan secara praktis oleh [Target Pengguna]?

## 1.3 Batasan Masalah
Untuk menjaga fokus analisis dan meningkatkan efektivitas penelitian agar sesuai dengan perencanaan awal, batasan masalah dalam penelitian ini ditetapkan sebagai berikut:
1. Data yang digunakan merupakan dataset [Nama/Sumber Dataset] yang diperoleh dari [Lokasi/Platform] pada periode [Bulan/Tahun] dengan total sebanyak [Jumlah] sampel.
2. Penelitian ini berfokus pada klasifikasi/verifikasi [Jumlah Kelas/Atribut] kategori target, yaitu [Sebutkan Kelas/Atribut], serta tidak mencakup [Kategori yang Dikecualikan].
3. Data masukan berupa berkas [Format Citra/Teks/Tabel] yang melalui tahapan prapemrosesan [Sebutkan Tahapan Prapemrosesan].
4. Model kecerdasan buatan yang dibangun dan diuji dibatasi pada algoritma [Nama Algoritma/Arsitektur].
5. Implementasi antarmuka sistem dibangun menggunakan bahasa pemrograman Python dengan kerangka kerja [Streamlit/Web] dan dievaluasi menggunakan metrik [Daftar Metrik].

## 1.4 Tujuan Penelitian
Merujuk pada latar belakang dan rumusan masalah yang telah ditetapkan, tujuan yang hendak dicapai dalam penelitian ini adalah sebagai berikut:
1. Mengolah dan mempersiapkan data [Objek] serta membangun model klasifikasi/deteksi menggunakan arsitektur [Algoritma/Arsitektur X].
2. Menganalisis dan mengevaluasi performa model [Algoritma/Arsitektur X] berdasarkan metrik [Akurasi, Precision, Recall, F1-Score] dan pengujian signifikansi statistik.
3. Mengembangkan aplikasi berbasis [Streamlit/Web] yang mengintegrasikan model [Algoritma/Arsitektur X] guna menyajikan hasil identifikasi secara otomatis dan terukur.

## 1.5 Manfaat Penelitian
Sejalan dengan tujuan penelitian di atas, manfaat yang diharapkan dari penelitian ini adalah sebagai berikut:
1. Bagi [Pengguna Lapangan/Praktisi]: Menyediakan alat bantu pendukung keputusan berbasis data untuk mengidentifikasi [Objek] secara cepat, akurat, dan objektif.
2. Bagi [Institusi/Penyelenggara]: Memberikan landasan evaluasi empiris dalam pengendalian mutu dan efisiensi operasional pemeriksaan.
3. Bagi Akademisi: Menambah khazanah literatur ilmiah mengenai penerapan dan evaluasi arsitektur [Algoritma/Arsitektur X] pada domain [Bidang Ilmu] sebagai acuan penelitian selanjutnya.

## 1.6 Luaran Penelitian
Luaran yang diharapkan dari pelaksanaan penelitian ini adalah sebagai berikut:
1. Model komputasi terlatih berbasis algoritma [Algoritma/Arsitektur X] yang mampu mengklasifikasikan/memverifikasi [Objek] secara akurat.
2. Dokumen hasil analisis pengujian kuantitatif dan komparasi performa model berdasarkan metrik evaluasi standar.
3. Aplikasi purwarupa berbasis [Streamlit/Web] yang memuat fitur unggah data masukan, visualisasi distribusi fitur, serta tampilan putusan hasil prediksi.

## 1.7 Sistematika Penulisan
Sistematika penulisan skripsi ini disusun untuk memberikan gambaran menyeluruh dan sistematis mengenai alur pembahasan pada setiap bab. Adapun sistematika penulisan laporan ini diuraikan sebagai berikut:

**BAB I PENDAHULUAN**  
Bab ini menguraikan latar belakang permasalahan yang mendasari penelitian, rumusan masalah, batasan masalah atau ruang lingkup penelitian, tujuan penelitian, manfaat penelitian, luaran yang diharapkan, serta sistematika penulisan.

**BAB II TINJAUAN PUSTAKA**  
Bab ini menyajikan landasan teori yang relevan dengan objek dan metode penelitian, mencakup konsep [Teori Utama], arsitektur [Metode X], kajian penelitian terdahulu sebagai pembanding, serta kerangka pemikiran penelitian.

**BAB III METODOLOGI PENELITIAN**  
Bab ini menjelaskan tahapan pelaksanaan penelitian secara terperinci, meliputi alur kerja penelitian, teknik pengumpulan data, tahapan prapemrosesan data, perancangan arsitektur model [Metode X], implementasi antarmuka, serta skema evaluasi kinerja model.

**BAB IV HASIL DAN PEMBAHASAN**  
Bab ini memaparkan hasil implementasi model dan sistem, hasil pengujian performa kuantitatif berdasarkan metrik evaluasi, analisis signifikansi statistik, serta pembahasan terhadap temuan eksperimen guna menjawab tujuan penelitian.

**BAB V PENUTUP**  
Bab ini berisi kesimpulan akhir yang diperoleh dari keseluruhan rangkaian penelitian serta saran teknis untuk pengembangan penelitian selanjutnya.

**DAFTAR PUSTAKA**  
Bagian ini memuat sumber referensi ilmiah dari jurnal, prosiding, buku teks, dan dokumen resmi yang dijadikan acuan dalam penyusunan penelitian.

**LAMPIRAN**  
Bagian ini menyajikan data pendukung, kode program utama, serta dokumentasi pengujian yang relevan selama pelaksanaan penelitian.
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
