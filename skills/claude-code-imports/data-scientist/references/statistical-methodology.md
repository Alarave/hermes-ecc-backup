# Metodologi Statistik & Desain Eksperimen (statistical-methodology)

Panduan operasional statistika terapan, desain eksperimen, dan inferensi kausal untuk perancangan eksperimen data science yang sahih secara empiris.

## 1. Pengujian Hipotesis & Statistika Inferensial
- **Uji Parametrik vs Non-Parametrik**:
  - Gunakan uji parametrik (t-test, ANOVA) hanya jika asumsi normalitas (Shapiro-Wilk) dan homoskedastisitas (Levene's test) terpenuhi.
  - Gunakan uji non-parametrik (Mann-Whitney U, Kruskal-Wallis, Wilcoxon signed-rank, McNemar test) saat distribusi data skewed atau berskala ordinal.
- **Koreksi Multi-Testing**:
  - Terapkan koreksi Bonferroni atau False Discovery Rate (Benjamini-Hochberg) saat menguji lebih dari satu hipotesis secara simultan guna mengendalikan family-wise error rate.
- **Pelaporan Statistik Lengkap**:
  - Wajib melaporkan nilai p-value bersama ukuran efek (Cohen's d, odds ratio, rank biserial correlation), interval keyakinan 95% (confidence interval), dan ukuran sampel efektif (N).

## 2. Desain Eksperimen & A/B Testing
- **Power Analysis & Penentuan Ukuran Sampel**:
  - Hitung ukuran sampel minimum sebelum eksperimen dimulai berbasis tingkat signifikansi alpha = 0.05, statistical power 1 - beta = 0.80, dan Minimum Detectable Effect (MDE).
  - Formula sampel dua kelompok proporsi: N = 2 * (Z_alpha/2 + Z_beta)^2 * p * (1 - p) / MDE^2.
- **Randomisasi & Stratifikasi**:
  - Terapkan stratified randomization untuk menyeimbangkan kovariat kritis (usia akun, histori transaksi, kategori pengguna) antar kelompok perlakuan (treatment) dan kontrol.
- **Protokol Anti-Peeking**:
  - Dilarang menghentikan eksperimen lebih awal hanya karena p-value sementara melintasi ambang batas 0.05 (peeking problem). Terapkan sequential testing (O'Brien-Fleming) atau Bayesian A/B testing jika evaluasi berkelanjutan dibutuhkan.

## 3. Inferensi Kausal & Data Observasional
- **Difference-in-Differences (DiD)**:
  - Validasi asumsi tren paralel (parallel trends assumption) pada periode sebelum intervensi (pre-treatment).
- **Propensity Score Matching (PSM)**:
  - Estimasi probabilitas menerima perlakuan berbasis regresi logistik, lakukan pencocokan 1:1 nearest neighbor dengan caliper ketat, dan uji keseimbangan kovariat pasca-matching (standardized mean difference < 0.10).
- **Variabel Instrumental (Instrumental Variables / 2SLS)**:
  - Pastikan instrumen memenuhi kondisi relevansi (F-statistic tahap pertama > 10) dan eksklusi (hanya mempengaruhi target melalui variabel endogen).

## 4. Pemodelan Bayesian & Deret Waktu
- **Bayesian Modeling (PyMC / Stan)**:
  - Formulasikan prior distribution informatif atau weakly informative; jalankan sampling MCMC (NUTS); periksa konvergensi (R-hat < 1.05 dan effective sample size > 400).
- **Analisis Deret Waktu**:
  - Uji stasioneritas (Augmented Dickey-Fuller); dekomposisi tren musiman (STL); model ARIMA / SARIMAX / Prophet dengan validasi time-series cross-validation (rolling window / expanding window tanpa lookahead bias).
