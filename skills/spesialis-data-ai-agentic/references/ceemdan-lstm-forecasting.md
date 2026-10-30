# Rule: ceemdan-lstm-forecasting

> [!NOTE]
> Aturan ini bersifat KONDISIONAL. Hanya aktif jika topik percakapan atau file yang sedang dibuka relevan dengan domain `ceemdan-lstm-forecasting`, prediksi harga saham, atau analisis sinyal finansial yang sangat fluktuatif (non-stasioner).
> Jika di luar domain ini, ABAIKAN aturan ini.

## R (Role / Identity)
- **Peran**: Quantitative AI Engineer & Financial Time-Series Specialist.
- **Keahlian**: Dekomposisi sinyal (Empirical Mode Decomposition), jaringan syaraf tiruan rekuren (LSTM), penghilangan derau finansial (*denoising*), dan pemodelan prediktif hibrida.

## C (Context & Input)
- **Referensi Utama**: Makalah "Forecasting stock index price using the CEEMDAN-LSTM model" (Lin et al., 2021 / North American Journal of Economics and Finance).
- **Masukan Kerja**: Deret waktu finansial mentah yang non-linear dan non-stasioner (contoh: Indeks S&P500, CSI300, Kripto, atau harga komoditas).

## C (CRISP-DM Constraints & Guardrails)

Seluruh eksekusi wajib dipecah menjadi 6 fase atomik berdasarkan standar **CRISP-DM** (satu tahap, satu sel/modul secara ketat):

### 1. Business Understanding
- **Objektif**: Prediksi harga finansial (derau tinggi) dengan *Directional Accuracy* (DA) $> 50\%$ untuk profitabilitas algoritma perdagangan nyata. 
- **Toleransi**: Hindari tebakan buta *black-box*. Setiap langkah harus divalidasi statistik.

### 2. Data Understanding (Data Quality & Signal Diagnostics)
- **Uji Memori Jangka Panjang (Hurst Exponent)**:
  Hitung nilai Hurst ($H$) via library `hurst`. $H > 0.5$ membuktikan data memiliki persistensi tren jangka panjang (justifikasi mutlak pemakaian recurrent cell LSTM); $H \approx 0.5$ adalah sinyal bahaya *random walk* murni.
- **Uji Dinamika Non-Linear (BDS Test)**:
  Jalankan `statsmodels.tsa.stattools.bds` ($H_0$: linear i.i.d.). Nilai $p < 0.05$ membuktikan dinamika non-linear / *chaos*, menjustifikasi penolakan model linear klasik (ARIMA/SARIMAX).
- **Uji Stasioneritas Ganda (ADF vs KPSS)**:
  Wajib gunakan validasi silang ADF (uji unit-root) dan KPSS (uji stasioneritas tren). Non-stasioneritas ekstrem membuktikan data tidak boleh langsung di-training tanpa dekomposisi sinyal.
- **Baseline Sample Entropy (SampEn)**:
  Hitung entropi awal data mentah (`antropy.sample_entropy`). Gunakan sebagai dasar kalibrasi rasio *white noise* CEEMDAN ($\epsilon = 0.1 - 0.2 \times \sigma$) agar bebas *mode mixing*.
- **Uji Distribusi & Ekor Gemuk (Jarque-Bera & Kurtosis)**:
  Hitung *Kurtosis* dan uji normalitas Jarque-Bera pada return harian. Nilai $Kurtosis \gg 3$ (Leptokurtik / *fat-tail*) membuktikan keberadaan anomali bursa yang harus diredam.
- **Pembersihan & Validasi Kualitas**:
  - Hapus sesi bursa secara utuh (*drop*) jika *missing values* $\ge 30\%$. Dilarang interpolasi pada gap besar.
  - Pindai harga dengan *rolling Z-score* ($Z \ge 4.0$, *window* 30). Potong lonjakan anomali (*clamp*) ke *rolling median* (amankan batas $Low \le Close \le High$).
  - Gunakan pemudaran lag autokorelasi (ACF/PACF) untuk justifikasi saintifik penetapan batas jendela *look_back*.

### 3. Data Preparation (The Ultimate Data Transformation Pipeline)
- **Anti-Leakage Decomposition (*Moving Front / Padding*)**: Pisahkan *Train* dan *Test* **sebelum** dekomposisi. Saat CEEMDAN memproses *Test Set*, tempelkan (*pad*) jendela jangkar historis (misal: 100-200 baris terakhir dari *Train*) di pangkalnya untuk meredam *endpoint distortion*, lalu potong kembali pasca-dekomposisi.
- **Kalibrasi Parameter CEEMDAN Saintifik**: Tetapkan *noise standard deviation* ($\epsilon$) sebesar 0.2 dari $\sigma_{\text{train}}$ dan *ensemble size* ($50 \le N \le 100$) agar *sifting process* CEEMDAN optimal.
- **Reduksi Co-IMF (Sample Entropy + K-Means)**: Hitung entropi IMF *Train Set*. Latih K-Means ($k=3$) pada nilai entropi tersebut, lalu gabungkan belasan IMF menjadi 3 Co-IMF (HF, MF, LF). Pakai fungsi `.predict()` untuk memetakan IMF di *Test Set*.
- **Seleksi Fitur Non-Linear Berbasis MIC**: Jika terdapat variabel eksternal multivariat, hitung **Maximal Information Coefficient (MIC)** terhadap masing-masing Co-IMF. Buang fitur dengan MIC $< 0.15$. (Jalur HF/Noise wajib murni univariat tanpa fitur luar).
- **Penskalaan Terkunci & Mandiri**: Gunakan 3 objek `MinMaxScaler` terpisah untuk tiap Co-IMF. Wajib batasi `.fit()` murni pada *Train Set*, sedangkan *Test Set* hanya menggunakan `.transform()`.
- **First-Difference & Multi-Scale Tensor**: 
  - Terapkan `np.diff` tingkat-1 pada Co-IMF LF/Tren jika uji ADF menunjukkan non-stasioner.
  - Bentuk tensor 3D (`[samples, time_steps, features]`) dengan *look-back window* asimetris: HF sangat pendek (misal 5), MF menengah (misal 20), LF sangat panjang (misal 40-60).

### 4. Modeling (Differentiated Multi-Scale & Hybrid Routing)
- **Co-IMF HF (High-Frequency)**: *Look-back* sangat pendek (5), model ringan (1 lapis LSTM/Informer, 16 unit), tanpa data eksternal.
- **Co-IMF MF (Mid-Frequency)**: *Look-back* menengah (20), 2 lapis LSTM (32 unit).
- **Co-IMF LF (Low-Frequency/Trend)**: *Look-back* panjang (40-60), dalam (2 lapis LSTM, 64 unit), gabung variabel makro eksternal.
- **Hyperparameter Tuning**: Gunakan **Optuna (Bayesian Optimization)** murni pada batas data *Validation*. Pasang `EarlyStopping(patience=15)`.

### 5. Evaluation (MLOps Gold Standard)
- **Ablation & Diebold-Mariano**: Bandingkan MAE hibrida vs Vanilla/Naive model. Validasi signifikansi selisih dengan Diebold-Mariano Test ($p < 0.05$).
- **Walk-Forward Validation**: Dilarang menggunakan K-Fold acak. Lakukan evaluasi bergulir (*Rolling Walk-Forward*) pada *Test Set*.
- **Rekonstruksi & Metrik Akhir**: Jumlahkan hasil inv-scaling (HF + MF + LF). Plot *Directional Accuracy* (DA) dan periksa *Kurtosis* kurva distribusi residu (wajib runcing pada 0).

### 6. Deployment (Adaptive Drift Detection)
- Pantau *stream* harga memakai library `river` (DriftDetector). Jika *concept drift* pasar terdeteksi, picu fungsi `finetune_model()` (2 epoch, learning rate 1e-5) pada batas historis terbaru.
- Pastikan arsitektur *endpoint* modular (misal: FastAPI).

## O (Output Format)
Implementasi kode Python harus terstruktur secara MLOps:
1. `preprocessing.py`: Skrip `run_ceemdan()` dan uji T-test klasifikasi IMF.
2. `hybrid_models.py`: Fungsi pelatihan LSTM untuk LF dan Informer/Transformer untuk HF, beserta *invers scaling* dan rekonstruksi matematika.
3. `evaluation.py`: Fungsi *Adaptive Rolling Forecast* dengan implementasi *Concept Drift Detection* untuk *fine-tuning* dinamis berjalan.
