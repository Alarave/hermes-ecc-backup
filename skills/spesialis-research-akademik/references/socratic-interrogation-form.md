# STANDAR OPERASIONAL: FORM INTEROGASI SOKRATIS SKRIPSI (SOCRATIC INTERROGATION ENGINE)
> Modul interogasi terstruktur berbasis bukti empiris korpus 205 skripsi (UPNVJ & Gunadarma) serta standar penguji sidang skripsi sarjana garis keras.

---

## 1. Latar Belakang Rekayasa & Temuan Empiris Korpus

Berdasarkan audit komparasi 205 naskah skripsi komputasi dan kecerdasan buatan pada korpus lokal (`E:\SKRIPSI_UPNVJ_TEXT`), ditemukan 5 kelemahan fatal yang paling sering dibantai oleh dewan penguji sidang:
1. **Latar Belakang Tanpa Bukti Data Awal (Preliminary Data)**: Mahasiswa menulis narasi umum tanpa menyajikan angka kerugian riil, durasi inefisiensi, atau grafik anomali data di lokasi penelitian.
2. **Cacat Data Leakage pada Preprocessing**: Pemisahan data latih dan uji (*train/test split*) dilakukan SETELAH normalisasi/scaling atau dekomposisi sinyal (seperti yang terdeteksi pada naskah pemodelan LSTM polutan udara).
3. **Penentuan Hyperparameter Spekulatif**: Lag window time-series dipilih secara coba-coba (*trial and error*) tanpa justifikasi statistik formal (PACF / Autokorelasi Parsial).
4. **Klaim Keunggulan Semu Tanpa Uji Signifikansi**: Model usulan diklaim lebih unggul hanya karena perbedaan metrik tipis (misal RMSE 0.02) tanpa pembuktian formal Uji Diebold-Mariano atau Wilcoxon ($p < 0.05$).
5. **Patahnya Benang Merah Bab 1 dan Bab 5**: Poin kesimpulan (5.1) tidak menjawab butir rumusan masalah (1.2) atau tujuan penelitian (1.3), serta hanya berupa ringkasan kualitatif tanpa angka metrik penutup.
6. **Penyalahgunaan AI Tanpa Integritas & Verifikasi**: Mengambil teks atau sitasi luaran AI mentah-mentah tanpa validasi primer dan menyembunyikan penggunaannya dari dosen pembimbing/promotor (dimitigasi melalui penegakan 15 pilar prinsip "Bukan, Melainkan" mengacu ke `references/prinsip-bukan-melainkan-etika-ai.md`).

Form Interogasi Sokratis dirancang untuk membedah dan memitigasi seluruh kelemahan di atas sebelum naskah ditulis.

---

## 2. Struktur Form Interogasi Sokratis (6 Siklus Bertahap via Clarify)

Agen mengeksekusi form interogasi menggunakan tool `clarify` (maksimal 4 sampai 5 pertanyaan beruntun dalam 1 kartu interaktif).

---

### SIKLUS 0: Cold-Start Discovery & Triage Proyek
*Dipicu saat pengguna memanggil agen tanpa konteks naskah/bab spesifik.*

1. **Pertanyaan 1 (Fase Skripsi Saat Ini)**:
   - *Pilihan*:
     1. Tahap Awal: Ide, Judul & Rumusan Masalah (Bab 1) (Recommended)
     2. Tahap Literatur: Tinjauan Pustaka & Matriks SOTA (Bab 2)
     3. Tahap Metodologi: CRISP-DM / SDLC & Alur Riset (Bab 3)
     4. Tahap Hasil: Eksperimen, Uji Diebold-Mariano & Evaluasi (Bab 4)
2. **Pertanyaan 2 (Domain & Track Keilmuan)**:
   - *Pilihan*:
     1. Data Science / Machine Learning / Time-Series (CRISP-DM) (Recommended)
     2. Rekayasa Perangkat Lunak / Web / Mobile (SDLC)
     3. Computer Vision / VLM / NLP
     4. Cybersecurity / Forensik Jaringan
3. **Pertanyaan 3 (Format Institusi & Geometri)**:
   - *Pilihan*:
     1. Universitas Gunadarma (Margin 4-4-3-3 cm, Numerik Arab 1-5, Ruang Lingkup 8-Poin) (Recommended)
     2. Format Standar Nasional Indonesia (A4 Margin 4-4-3-3 cm, IEEE/APA)
     3. Manuskrip Jurnal Ilmiah (IEEE / Scopus 2 Kolom)
4. **Pertanyaan 4 (Target Deliverable Sesi Ini)**:
   - *Pilihan*:
     1. Sokratis & Bedah Novelty / Validasi Data Lapangan (Recommended)
     2. Draf Naskah Bab Spesifik (Bab 1 / 2 / 3 / 4 / 5)
     3. Matriks SOTA / Diagram Alir Metodologi Vektor FigGenie
     4. Simulasi Pertanyaan Ujian Sidang & Pengujian Statistik

---

### SIKLUS 1: Eksplorasi Fenomena, Objek Riset & Masalah Lapangan (Grounded Discovery)
*Dipicu setelah Siklus 0 untuk menggali konteks penelitian dari umum ke khusus secara bersahabat.*

1. **Pertanyaan 1 (Topik Umum & Objek/Lokasi Penelitian)**:
   - *Teks*: "Apa topik umum dan objek atau lokasi studi kasus yang ingin Anda teliti?"
   - *Pilihan*:
     1. Objek spesifik di lapangan/organisasi nyata (misal: RS, UMKM, instansi pemerintah, e-commerce) (Recommended)
     2. Dataset publik/repositori riset (Kaggle, UCI, Hugging Face, EPrints kampus)
     3. Masih mencari ide objek penelitian yang menarik (butuh saran eksplorasi)
2. **Pertanyaan 2 (Draf Judul Kasar atau Ide Solusi Awal)**:
   - *Teks*: "Apakah Anda sudah memiliki draf judul kasar atau gambaran solusi yang terpikirkan?"
   - *Pilihan*:
     1. Sudah punya judul kasar atau kata kunci utama (akan saya ketik) (Recommended)
     2. Sudah ada ide solusi atau metode, tetapi bingung merangkai judul skripsinya
     3. Belum ada judul sama sekali, butuh rekomendasi 3-5 opsi judul berbasis tren
3. **Pertanyaan 3 (Kendala atau Masalah Riil yang Dihadapi)**:
   - *Teks*: "Kendala atau masalah riil apa yang dihadapi pada objek penelitian tersebut?"
   - *Pilihan*:
     1. Proses manual lambat, tidak efisien, atau menghasilkan error tinggi (Recommended)
     2. Data historis ada tetapi belum dimanfaatkan untuk prediksi/klasifikasi otomatis
     3. Model atau sistem saat ini akurasinya rendah atau sering salah deteksi
     4. Belum punya data konkret di lapangan (bantu carikan masalah dan dataset pendukung)
4. **Pertanyaan 4 (Arah Pilihan Metode & Batasan Awal)**:
   - *Teks*: "Pendekatan atau metode apa yang ingin Anda eksplorasi, serta batasan awalnya?"
   - *Pilihan*:
     1. Machine Learning / Deep Learning (bantu rekomendasikan algoritma baseline & pembanding) (Recommended)
     2. Pengembangan Aplikasi Sistem Informasi / Web / Mobile (SDLC)
     3. Kombinasi Hibrida (misal: Text Mining + VLM/OCR, atau Dekomposisi Sinyal + LSTM)
     4. Fleksibel, rekomendasikan metode terbaik yang paling aman untuk sidang

### Pedoman Khusus Agen (Prinsip Grounded First & Anti-Intimidasi):
1. **Dilarang Langsung Menginterogasi Keras di Awal**: Setelah Siklus 0 (Triage), agen DILARANG LANGSUNG menembak pengguna dengan pertanyaan sidang yang agresif (*preliminary data*, *baseline failure*, *novelty proof*).
2. **Alur Transisi Bertahap**: Wajib menuntun pengguna dari ranah umum ke khusus melalui alur: `Judul Kasar / Topik -> Objek & Lokasi -> Kendala Lapangan -> Pilihan Metode & Batasan Awal`.
3. **Respon Otomatis Saat Pengguna Memilih Opsi Eksplorasi atau Skip**:
   Jika pengguna memilih opsi "Belum punya data konkret (bantu carikan masalah dan dataset)" atau men-skip pertanyaan teknis, agen TIDAK BOLEH memojokkan atau menolak pengguna. Agen wajib otomatis mengaktifkan **Mode Bantuan Eksplorasi**:
   - Menyarankan 3 studi kasus nyata dari repositori kampus lokal.
   - Menyediakan tautan dataset publik yang sudah bersih (*clean*).
   - Membantu merumuskan draf judul formula 4-elemen via `research-title-formulator`.

---

### SIKLUS 1B: Validasi Kritis & Stress-Test Judul (Setelah Draf Disepakati)
*Dipicu setelah draf judul, objek, dan masalah awal disepakati, atau saat pengguna meminta evaluasi kritis / simulasi sidang Bab 1.*

1. **Pertanyaan 1 (Bukti Data Awal Lapangan)**:
   - *Teks*: "Apa bukti data konkret di lokasi penelitian yang membuktikan masalah ini mendesak untuk diteliti?"
   - *Pilihan*:
     1. Tersedia angka kerugian finansial / persentase kegagalan operasional (Recommended)
     2. Tersedia catatan log sistem / durasi latensi inefisiensi
     3. Tersedia grafik tren anomali / fluktuasi data historis
     4. Belum ada data konkret (aktifkan mode bantuan eksplorasi data/studi kasus)
2. **Pertanyaan 2 (Identifikasi Model Baseline & Research Gap)**:
   - *Teks*: "Metode atau algoritma apa yang menjadi baseline pembanding saat ini, dan di mana titik kegagalannya?"
   - *Pilihan*:
     1. Baseline konvensional (ARIMA / SVR / Random Forest) gagal menangani non-linearitas (Recommended)
     2. Sistem manual / aturan bisnis saat ini lambat dan menghasilkan error tinggi
     3. Model deep learning standar mengalami vanishing gradient / overfitting
     4. Belum tahu baseline pembanding (bantu carikan 3 model pembanding dari paper rujukan)
3. **Pertanyaan 3 (Pembuktian Novelty Riset)**:
   - *Teks*: "Pilar novelty apa yang ingin Anda buktikan di hadapan dewan penguji sidang?"
   - *Pilihan*:
     1. Novelty Algoritmik: Arsitektur Hibrida (Dekomposisi Sinyal + Deep Learning) (Recommended)
     2. Novelty Domain: Karakteristik dataset lokal spesifik yang belum pernah diteliti
     3. Novelty Evaluasi: Penerapan metrik ketat dan uji signifikansi statistik formal
     4. Butuh arahan perumusan novelty yang realistis dan aman diuji
4. **Pertanyaan 4 (Penegasan 8 Aspek Ruang Lingkup)**:
   - *Teks*: "Apakah batasan ruang lingkup 8-poin sudah siap dikunci agar tidak melebar saat sidang?"
   - *Pilihan*:
     1. Kunci 8-poin: Objek, Data, Fitur, Algoritma, Stack, UI, Metrik, Non-Scope (Recommended)
     2. Butuh panduan perumusan batasan non-scope eksplisit

---

### SIKLUS 2: Telaah Pustaka & Matriks SOTA (Bab 2)
*Dipicu saat menyusun landasan teori dan tinjauan literatur.*

1. **Pertanyaan 1 (Standar Protokol Literatur)**:
   - *Teks*: "Bagaimana strategi penyaringan artikel ilmiah yang Anda gunakan?"
   - *Pilihan*:
     1. Protokol PRISMA dengan minimal 80% jurnal terindeks Scopus/SINTA 5 tahun terakhir (Recommended)
     2. Pencarian terarah Google Scholar / Semantic Scholar via kata kunci spesifik
2. **Pertanyaan 2 (Kedalaman Penurunan Teori)**:
   - *Teks*: "Bagaimana Anda menyajikan teori pendukung di Bab 2?"
   - *Pilihan*:
     1. Wajib penurunan rumus matematis, fungsi objektif, dan kaitan solutif (Anti-Kamus) (Recommended)
     2. Ringkasan arsitektur blok diagram konseptual
3. **Pertanyaan 3 (Matriks Komparasi State-of-the-Art)**:
   - *Teks*: "Berapa banyak penelitian terdahulu yang dibandingkan pada tabel SOTA?"
   - *Pilihan*:
     1. Minimal 5 penelitian relevan (Penulis, Tahun, Metode, Data, Hasil, Gap) (Recommended)
     2. Lebih dari 10 penelitian dengan visualisasi sintesis PRISMA

---

### SIKLUS 3: Metodologi & Audit Anti-Data Leakage (Bab 3)
*Dipicu saat merancang tahapan penelitian dan preprocessing.*

1. **Pertanyaan 1 (Framework Baku Metodologi)**:
   - *Teks*: "Framework metodologi kerja apa yang menjadi kerangka alur Bab 3?"
   - *Pilihan*:
     1. CRISP-DM (Business, Data Understanding, Preparation, Modeling, Eval, Deploy) (Recommended)
     2. SDLC Waterfall / Agile untuk Rekayasa Perangkat Lunak
2. **Pertanyaan 2 (Audit Protokol Anti-Data Leakage)**:
   - *Teks*: "Di mana posisi tepat pembagian data latih dan uji (*Train/Test Split*)?"
   - *Pilihan*:
     1. Wajib split diawal SEBELUM normalisasi, imputasi, atau dekomposisi sinyal (Recommended)
     2. Split menggunakan K-Fold Cross Validation terisolasi
3. **Pertanyaan 3 (Validasi Temporal Deret Waktu)**:
   - *Teks*: "Bagaimana penanganan urutan data dan penentuan lag lookback window?"
   - *Pilihan*:
     1. Urutan waktu kronologis (No Shuffle) dan lag berbasis analisis PACF formal (Recommended)
     2. Window sliding berulang dengan validasi temporal block
4. **Pertanyaan 4 (Visualisasi Alur Penelitian)**:
   - *Teks*: "Bagaimana format flowchart tahapan penelitian Bab 3?"
   - *Pilihan*:
     1. Diagram vektor FigGenie (SVG/PDF tight-box) dengan formula tersemat (Recommended)
     2. Diagram Mermaid terstruktur

---

### SIKLUS 4: Pengujian, Evaluasi & Signifikansi Statistik (Bab 4)
*Dipicu saat mengolah data hasil eksperimen dan pembahasan.*

1. **Pertanyaan 1 (Baseline Pembanding Eksperimen)**:
   - *Teks*: "Metode baseline apa saja yang diuji secara berdampingan dengan model usulan?"
   - *Pilihan*:
     1. Baseline statistik (ARIMA) + Machine Learning klasik (SVR/RF) + Model Usulan (Recommended)
     2. Single model ablation study (model tanpa optimasi vs dengan optimasi)
2. **Pertanyaan 2 (Paket Metrik Evaluasi Kuantitatif)**:
   - *Teks*: "Metrik apa yang digunakan untuk membuktikan performa model?"
   - *Pilihan*:
     1. Multivariat: RMSE, MAE, MAPE, R2, dan Mean Directional Accuracy (MDA) (Recommended)
     2. Klasifikasi: Precision, Recall, Macro-F1, dan ROC-AUC
3. **Pertanyaan 3 (Uji Signifikansi Statistik Formal)**:
   - *Teks*: "Bagaimana membuktikan bahwa keunggulan model bukan faktor kebetulan (*chance*)?"
   - *Pilihan*:
     1. Uji Diebold-Mariano / Wilcoxon Signed-Rank Test dengan signifikansi p < 0.05 (Recommended)
     2. Uji Paired T-Test dengan uji normalitas residual
4. **Pertanyaan 4 (Analisis Pembahasan Empiris)**:
   - *Teks*: "Bagaimana Anda mengaitkan angka evaluasi Bab 4 dengan latar belakang Bab 1?"
   - *Pilihan*:
     1. Hubungkan penurunan error dengan estimasi efisiensi biaya/waktu di lapangan (Recommended)
     2. Analisis kurva loss training vs validation untuk mitigasi overfitting

---

### SIKLUS 5: Kesimpulan, Keterbatasan & Pertahanan Sidang (Bab 5)
*Dipicu saat memvalidasi bab penutup dan simulasi sidang skripsi.*

1. **Pertanyaan 1 (Validasi Keterpaduan Benang Merah)**:
   - *Teks*: "Apakah setiap butir kesimpulan sudah memetakan 1:1 ke tujuan penelitian?"
   - *Pilihan*:
     1. Ya, 1:1 terhadap Tujuan (1.3) dan diperkuat angka nyata capaian metrik (Recommended)
     2. Perlu pemeriksaan ulang keselarasan antar-bab
2. **Pertanyaan 2 (Format Saran Teknis Actionable)**:
   - *Teks*: "Bagaimana karakteristik saran penelitian lanjutan yang ditulis?"
   - *Pilihan*:
     1. Saran teknis konkret: limitasi fitur, arsitektur baru, atau dataset eksternal (Recommended)
     2. Saran implementasi manajerial untuk organisasi mitra
3. **Pertanyaan 3 (Kesiapan Simulasi Sidang Sokratis)**:
   - *Teks*: "Apakah Anda siap diuji dengan pertanyaan jebakan penguji terkait metodologi?"
   - *Pilihan*:
     1. Mulai simulasi sidang dengan 3 pertanyaan kritis dewan penguji (Recommended)
     2. Tinjau kembali draf naskah Bab 1 sampai 5
