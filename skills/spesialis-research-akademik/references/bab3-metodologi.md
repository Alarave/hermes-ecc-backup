# STANDAR OPERASIONAL & TEMPLATE: BAB III METODOLOGI PENELITIAN
> Dokumen referensi resmi penulisan Bab 3 Metodologi Penelitian (Standar CRISP-DM, SDLC Rekayasa Perangkat Lunak, Protokol Anti-Leakage AI, dan Validasi Statistik).

---

## 🏛️ PEDOMAN ARSITEKTUR BAB III (RULES & CONSTRAINTS)

### 1. Pemilihan Kerangka Kerja Metodologi Baku
Penelitian wajib menyandarkan alurnya pada metodologi ilmiah yang diakui secara global:
- **Riset AI / Data Science / Time-Series**: Wajib menggunakan **CRISP-DM (Cross-Industry Standard Process for Data Mining)**:
  1. *Business / Domain Understanding*: Pemahaman konteks masalah dan formulasi tujuan analitis.
  2. *Data Understanding*: Eksplorasi karakteristik data, distribusi, korelasi awal, dan deteksi anomali.
  3. *Data Preparation*: Pembersihan data, imputasi terukur, rekayasa fitur, dan partisi data.
  4. *Modeling*: Perancangan arsitektur, pemilihan fungsi kerugian (*loss function*), dan pelatihan model.
  5. *Evaluation*: Pengujian metrik performa multivariat dan uji signifikansi statistik.
  6. *Deployment*: Penyiapan modul inferensi atau rencana integrasi sistem.
- **Riset Rekayasa Perangkat Lunak (Software Engineering)**: Wajib menggunakan **SDLC (Waterfall / Agile Scrum)**:
  1. *Requirement Analysis*: Pengumpulan kebutuhan fungsional dan non-fungsional.
  2. *System Design*: Perancangan arsitektur sistem, diagram relasi entitas (ERD), dan antarmuka.
  3. *Implementation*: Pengkodean modul (*backend*, *frontend*, dan database).
  4. *Testing*: Pengujian *Black-Box* dan *User Acceptance Testing (UAT)*.
  5. *Maintenance*: Dokumentasi dan rencana pemeliharaan.

---

### 2. Protokol Anti-Data Leakage Mutlak (Khusus Machine Learning)
- **Partisi Data Sebelum Pemrosesan**:
  - Pemisahan data latih (*Train*) dan data uji (*Test*) **WAJIB** dilakukan sebelum operasi penskalaan (*MinMaxScaler/StandardScaler*), imputasi *missing values*, atau dekomposisi sinyal (seperti CEEMDAN/Wavelet).
  - Penskalaan hanya boleh di-*fit* pada data latih, kemudian di-*transform* ke data uji.
- **Integritas Waktu (Time-Series Guard)**:
  - Dilarang keras melakukan pengacakan data (*random shuffle*) pada data deret waktu.
  - Urutan kronologis wajib dipertahankan (*Walk-Forward Validation / Temporal Split*).
- **Penentuan Parameter Input Berbasis Statistik**:
  - Penentuan nilai *lag lookback* atau fitur input wajib dibuktikan melalui analisis statistik formal (analisis *Partial Autocorrelation Function* / PACF, korelasi Pearson/Spearman, atau *SHAP Feature Importance*). Dilarang menebak angka lag tanpa bukti empiris.

---

### 3. Prosedur Penyiapan & Pembersihan Data (Data Preparation)
- **Pembersihan Anomali**:
  - *Outlier*: Uji deteksi menggunakan metode *Interquartile Range (IQR)* atau *Z-score*. Berikan justifikasi teknis apakah outlier dipotong (*trimmed*) atau disesuaikan (*winsorized*).
  - *Missing Values*: Analisis pola kekosongan data. Terapkan interpolasi linier/spline untuk data time-series, atau imputasi berbasis median/K-NN untuk data tabular.
  - *Ketidakseimbangan Kelas*: Terapkan teknik *Synthetic Minority Over-sampling Technique (SMOTE)* atau pembobotan kelas (*class weights*) pada fungsi kerugian.

---

### 4. Diagram Alir Penelitian (Research Flowchart)
- **Standar Visualisasi Vektor (Engine FigGenie)**:
  - Diagram Alir Penelitian WAJIB digambar menggunakan engine vektor `figgenie-paper-diagram`.
  - Format keluaran: Vektor SVG cetak (240 pt untuk kolom tunggal, 504 pt untuk kolom ganda) dan PDF terpotong rapi untuk naskah skripsi.
  - Setiap blok diagram wajib mendefinisikan masukan (*input*), proses inti, dan luaran (*output*) secara transparan.

---

## 📝 TEMPLATE STRUKTUR BAB III METODOLOGI PENELITIAN

```markdown
# 3. METODOLOGI PENELITIAN

## 3.1 Kerangka Kerja Penelitian
Penelitian ini dilaksanakan mengikuti tahapan standar *Cross-Industry Standard Process for Data Mining* (CRISP-DM) yang disesuaikan dengan kebutuhan pemodelan kecerdasan buatan, seperti divisualisasikan pada Gambar 3.1:

![Diagram Alir Metodologi Penelitian](figures/diagram_metodologi.png)  
*Gambar 3.1: Diagram Alir Tahapan Penelitian (Engine: FigGenie Vector)*

Tahapan penelitian diuraikan secara sistematis sebagai berikut:
1. **Pemahaman Domain (Domain Understanding)**: Menganalisis dinamika volatilitas [Objek Data] dan merumuskan batasan masalah prediksi.
2. **Pengumpulan dan Pemahaman Data (Data Understanding)**: Mengakuisisi dataset sekunder dari [Sumber Data] dan melakukan eksplorasi statistik deskriptif.
3. **Pra-pemrosesan Data (Data Preparation)**: Menerapkan pemisahan data latih/uji anti-leakage, pembersihan anomali, dekomposisi sinyal, dan normalisasi.
4. **Pembangunan Model (Modeling)**: Melatih arsitektur [Model Usulan] dan model baseline pembanding.
5. **Evaluasi dan Pengujian (Evaluation)**: Mengukur akurasi prediksi serta melakukan uji signifikansi statistik Diebold-Mariano.

## 3.2 Sumber dan Karakteristik Data
Dataset yang digunakan dalam penelitian ini merupakan data historis [Nama Objek] yang diperoleh dari [Sumber Resmi]:
1. **Periode Observasi**: Data harian dari tanggal [DD/MM/YYYY] hingga [DD/MM/YYYY].
2. **Jumlah Sampel**: Sebanyak [N] baris data observasi.
3. **Variabel Penelitian**: Terdiri dari variabel target [Y] dan variabel fitur pendukung [X1, X2, X3].

## 3.3 Pra-pemrosesan Data dan Protokol Anti-Leakage
Untuk menjamin integritas saintifik dan mencegah kebocoran informasi (*data leakage*), tahapan penyiapan data dirancang dengan protokol ketat:

### 3.3.1 Partisi Data Latih dan Uji
Dataset dipartisi secara kronologis (*temporal split*) tanpa pengacakan dengan rasio 80% data latih ([N_train] baris) dan 20% data uji ([N_test] baris). Partisi dilakukan pada tahap paling awal sebelum operasi normalisasi nilai.

### 3.3.2 Penentuan Lag Masukan (PACF Analysis)
Penentuan panjang jendela observasi masa lalu (*lookback lag*) didasarkan pada grafik *Partial Autocorrelation Function* (PACF). Lag yang dipilih adalah lag yang memiliki nilai signifikansi melampaui batas interval kepercayaan 95%.

### 3.3.3 Dekomposisi Sinyal dan Normalisasi
Dekomposisi sinyal dilakukan untuk mengurai derau (*noise*). Penskalaan fitur menggunakan metode *Min-Max Normalization* sesuai Persamaan 3.1:

$$ x_{\text{norm}} = \frac{x - x_{\min(\text{train})}}{x_{\max(\text{train})} - x_{\min(\text{train})}} \tag{3.1} $$

Nilai $x_{\min}$ dan $x_{\max}$ dihitung secara eksklusif dari data latih dan diterapkan pada data uji untuk mencegah bias masa depan (*look-ahead bias*).

## 3.4 Perancangan Arsitektur Model
Model yang dikembangkan mengintegrasikan modul [Komponen A] dan [Komponen B]. Konfigurasi hyperparameter ditetapkan secara terstruktur melalui pencarian sistematis:
- Ukuran *batch* (*batch size*): [Nilai]
- Laju pembelajaran (*learning rate*): [Nilai]
- Fungsi optimasi (*optimizer*): Adam dengan *weight decay*
- Fungsi kerugian (*loss function*): Huber Loss / Mean Squared Error

## 3.5 Metode Pengujian dan Evaluasi Kinerja
Kinerja sistem dievaluasi melalui dua pendekatan komplementer:

### 3.5.1 Metrik Kuantitatif
Evaluasi akurasi prediksi diukur menggunakan metrik kesalahan dan ketepatan arah tren:
1. *Root Mean Squared Error* (RMSE)
2. *Mean Absolute Error* (MAE)
3. *Mean Directional Accuracy* (MDA)

### 3.5.2 Uji Signifikansi Statistik (Diebold-Mariano Test)
Untuk membuktikan bahwa penurunan nilai kesalahan model usulan terhadap model pembanding memiliki signifikansi statistik nyata, dilakukan uji hipotesis Diebold-Mariano dengan tingkat signifikansi $\alpha = 0.05$. Hipotesis nol ($H_0$) menyatakan tidak terdapat perbedaan performa antara kedua model, sedangkan hipotesis alternatif ($H_1$) menyatakan model usulan memiliki akurasi yang lebih unggul secara signifikan.
```